#!/usr/bin/env python3
"""Minimal source ingestion for the cloud architecture study system.

AWS priority:
1) provider-native Markdown (.md companion for docs.aws.com HTML pages)
2) HTML -> Markdown with trafilatura if available, else pandoc
3) PDF -> Markdown/text with pymupdf4llm if available, else pdftotext -layout

Writes normalized content plus a provenance sidecar JSON. No LLM calls.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import mimetypes
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

UA = "cloud-architecture-study-system/0.1 (+source-ingestion)"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run(cmd: list[str], *, input_bytes: bytes | None = None) -> bytes:
    p = subprocess.run(cmd, input=input_bytes, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode:
        raise RuntimeError(f"command failed: {' '.join(cmd)}\n{p.stderr.decode(errors='replace')}")
    return p.stdout


def fetch(url: str) -> tuple[bytes, str]:
    req = Request(url, headers={"User-Agent": UA, "Accept": "text/markdown,text/html,application/pdf;q=0.9,*/*;q=0.1"})
    with urlopen(req, timeout=30) as r:
        return r.read(), (r.headers.get_content_type() or "application/octet-stream")


def aws_markdown_url(url: str) -> str | None:
    p = urlparse(url)
    if p.netloc == "docs.aws.amazon.com" and p.path.endswith(".html"):
        return url[:-5] + ".md"
    return None


def html_to_markdown(data: bytes) -> tuple[bytes, str]:
    trafilatura = shutil.which("trafilatura")
    if trafilatura:
        return run([trafilatura, "--markdown", "--no-comments", "--recall"], input_bytes=data), "trafilatura"
    pandoc = shutil.which("pandoc")
    if pandoc:
        return run([pandoc, "--from=html", "--to=gfm", "--wrap=none"], input_bytes=data), "pandoc-fallback"
    raise RuntimeError("HTML normalization needs trafilatura (preferred) or pandoc")


def pdf_to_text(data: bytes) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory() as td:
        pdf = Path(td) / "source.pdf"
        pdf.write_bytes(data)
        try:
            import pymupdf4llm  # type: ignore
            out = pymupdf4llm.to_markdown(str(pdf), header=False, footer=False)
            return out.encode(), "pymupdf4llm"
        except Exception:
            pdftotext = shutil.which("pdftotext")
            if not pdftotext:
                raise RuntimeError("PDF normalization needs pymupdf4llm or pdftotext")
            return run([pdftotext, "-layout", str(pdf), "-"]), "pdftotext-fallback"


def normalize(data: bytes, content_type: str, name: str) -> tuple[bytes, str]:
    ext = Path(name).suffix.lower()
    if content_type in {"text/markdown", "text/plain"} or ext in {".md", ".markdown", ".txt"}:
        return data, "native-text"
    if content_type == "application/pdf" or ext == ".pdf":
        return pdf_to_text(data)
    if content_type in {"text/html", "application/xhtml+xml"} or ext in {".html", ".htm"}:
        return html_to_markdown(data)
    raise RuntimeError(f"unsupported content type: {content_type} ({ext})")


def main() -> int:
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--url")
    src.add_argument("--file", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    requested = args.url or str(args.file)
    retrieved = requested
    if args.url:
        md_url = aws_markdown_url(args.url)
        if md_url:
            try:
                data, ctype = fetch(md_url)
                retrieved = md_url
            except Exception:
                data, ctype = fetch(args.url)
        else:
            data, ctype = fetch(args.url)
        name = urlparse(retrieved).path
    else:
        data = args.file.read_bytes()
        ctype = mimetypes.guess_type(args.file.name)[0] or "application/octet-stream"
        name = args.file.name

    normalized, method = normalize(data, ctype, name)
    text = normalized.decode("utf-8", errors="replace").replace("\r\n", "\n")
    text = "\n".join(line.rstrip() for line in text.splitlines()).strip() + "\n"
    out_bytes = text.encode()

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(out_bytes)
    meta = {
        "source": requested,
        "retrieved_from": retrieved,
        "retrieved_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "content_type": ctype,
        "normalizer": method,
        "source_sha256": sha256(data),
        "normalized_sha256": sha256(out_bytes),
        "normalized_bytes": len(out_bytes),
    }
    args.out.with_suffix(args.out.suffix + ".source.json").write_text(json.dumps(meta, indent=2) + "\n")
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
