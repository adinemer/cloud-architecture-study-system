# Study Tool Policy and Initial Toolset

Status: **APPROVED v1 — study start remains frozen**  
Verified: **Fedora 44 official repositories, 2026-08-09**

## Eligibility rule

A recommended software tool must satisfy:

1. **Official distribution path** acceptable to the learner:
   - official Fedora Linux package; or
   - official Flatpak published/maintained by the project/vendor; or
   - official Docker/OCI image published/maintained by the project/vendor.
2. **Cost/source condition**:
   - FOSS is preferred; or
   - a free tier is acceptable when it provides all features/options required by this study system.

Community COPRs, unofficial Flatpaks, unofficial container images, random AppImages, and third-party repackaging are not approved as core study tooling.

Tool eligibility is rechecked before adoption if distribution status can change.

## Design principle

Use the fewest tools that materially improve learning. A specialized application is not adopted merely because it has more knowledge-management features.

The authoritative system remains:

- GitHub repository for governance/state/artifacts/session history;
- Markdown/JSON for durable data;
- ChatGPT as controlled coordinator/instructor/assessor.

Personal tools are interfaces around that system, not competing authorities.

## Approved initial toolset

### 1. Ghostwriter — personal Markdown note editor

**Status: APPROVED CORE TOOL**

Verified in Fedora 44 official `updates` repository on 2026-08-09:

- package: `ghostwriter`
- version observed: `26.04.3-1.fc44`
- Fedora vendor: Fedora Project
- upstream: KDE Ghostwriter
- FOSS licensing includes GPL-3.0-or-later and compatible components.

Role:
- learner-authored personal notes;
- short mental models;
- misconception notes;
- decision explanations in learner's own words;
- links/references to controlled session/artifact IDs.

Not used for:
- authoritative study artifacts;
- session state;
- provider-source copies;
- mastery state.

Why selected:
- native Markdown;
- distraction-free;
- FOSS;
- official Fedora package;
- no proprietary database/format;
- works directly with the repository/local Markdown model.

### 2. Git — authoritative local version-control client

**Status: APPROVED CORE TOOL**

Verified in Fedora 44 official `updates` repository.

Role:
- synchronize/inspect repository state;
- version personal Markdown when stored with approved study workspace;
- review changes/diffs when useful.

Routine Git administration remains primarily coordinator/system responsibility.

### 3. ripgrep — fast local retrieval/search

**Status: APPROVED CORE TOOL**

Verified in Fedora 44 official `updates` repository.

Role:
- find session IDs, terms, misconceptions, artifact references, and personal notes quickly;
- complement GitHub search without adding an indexing/database service.

### 4. Neovim — optional power-user editor

**Status: APPROVED OPTIONAL TOOL**

Verified in Fedora 44 official `updates` repository.

Use only if the learner prefers terminal editing/search workflows. It is not required when Ghostwriter is sufficient.

### 5. Kate — optional general editor

**Status: APPROVED OPTIONAL TOOL**

Verified in Fedora 44 official `updates` repository.

Use for structured file browsing/editing when a traditional editor is preferred. It is not necessary solely for study.

## Not approved / not selected

### Anki

Fedora 44 official repositories did **not** contain a package named `anki` during the 2026-08-09 verification run.

It is therefore **not approved as a core tool under the current distribution rule** unless a future check verifies an acceptable official Flatpak or official container distribution that meets the learner's requirements.

The study system does not depend on Anki: canonical flashcards remain JSON/Markdown artifacts and ChatGPT coordinates spaced retrieval directly.

### Apostrophe

Fedora 44 official repositories did **not** contain a package named `apostrophe` during the 2026-08-09 verification run. It is not selected.

### Obsidian / Logseq / Joplin / other note applications

Not approved by default. They may be evaluated later only if:

- an acceptable official Fedora/Flatpak/container distribution is verified;
- their free/FOSS terms meet the policy;
- they solve a measured limitation of the Ghostwriter + Markdown + Git/ripgrep workflow.

Do not add them for backlinks/graph features alone.

## Personal notes storage

Recommended local layout:

```text
personal-notes/
  aws/
    sap-c02/
      Uxx/
        <topic>.md
        misconceptions/
```

Whether `personal-notes/` is committed to the public repository must be explicitly decided before real study. Personal notes can contain learner-specific mistakes/reflections and may be better stored locally or in a private repository. Do not publish personal/proprietary information accidentally.

## Spaced repetition without a dedicated SRS app

The v1 retention system uses the existing controlled flashcard artifact plus session/mastery state:

1. artifact JSON contains approved cards;
2. coordinator determines due retrieval windows under `docs/14-study-operating-routine.md`;
3. ChatGPT presents cards/architecture prompts without showing answers first;
4. response quality is recorded as evidence;
5. weak items are scheduled sooner;
6. mastered items are spaced farther apart;
7. higher-order decision/scenario retrieval is preferred over unlimited card growth.

This avoids a separate SRS database and keeps study state auditable in GitHub.

## Tool-change rule

Adding/replacing a core study tool is a governed control/toolchain change. Before adoption:

- verify eligibility;
- identify what current problem it solves;
- assess data portability;
- define authoritative vs convenience role;
- avoid duplicate state;
- update this document and change-control record when material.
