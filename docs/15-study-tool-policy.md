# Study Tool Policy and Initial Toolset

Status: **APPROVED v1.1 — study start remains frozen**  
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

Not used for authoritative artifacts, session state, provider-source copies, or mastery state.

### 2. Git — authoritative local version-control client

**Status: APPROVED CORE TOOL**

Verified in Fedora 44 official `updates` repository.

Role: synchronize/inspect repository state and review diffs when useful. Routine Git administration remains primarily coordinator/system responsibility.

### 3. ripgrep — fast local retrieval/search

**Status: APPROVED CORE TOOL**

Verified in Fedora 44 official `updates` repository.

Role: find session IDs, terms, misconceptions, artifact references, and personal notes without adding an indexing/database service.

### 4. Neovim — optional power-user editor

**Status: APPROVED OPTIONAL TOOL**

Verified in Fedora 44 official `updates` repository. Use only if preferred; not required when Ghostwriter is sufficient.

### 5. Kate — optional general editor

**Status: APPROVED OPTIONAL TOOL**

Verified in Fedora 44 official `updates` repository. Optional traditional editor/file browser.

## Not approved / not selected

### Anki

Fedora 44 official repositories did not contain a package named `anki` during the 2026-08-09 verification. It is not a core dependency unless a future check verifies an acceptable official Flatpak/container distribution meeting the policy.

The system does not depend on Anki: canonical flashcards remain JSON/Markdown artifacts and ChatGPT coordinates spaced retrieval.

### Apostrophe

Fedora 44 official repositories did not contain a package named `apostrophe` during verification. It is not selected.

### Obsidian / Logseq / Joplin / other note applications

Not approved by default. Evaluate only if an acceptable official distribution/free-or-FOSS condition is verified and the candidate solves a measured limitation of the Ghostwriter + Markdown + Git/ripgrep workflow.

## Personal notes storage — resolved default

Personal notes are **local-only by default and are not committed to the public study-system repository**.

Recommended local layout outside the public repository:

```text
~/Documents/cloud-study-notes/
  aws/
    sap-c02/
      Uxx/
        <topic>.md
        misconceptions/
```

Reason:
- notes may contain learner-specific mistakes/reflections;
- they are not authoritative study state;
- public publication adds no learning value and creates unnecessary privacy/noise risk.

A private Git repository may be adopted later for backup/versioning if desired, but that is optional and does not block study. Controlled artifact/session IDs can be linked from personal notes without copying authoritative content.

## Spaced repetition without a dedicated SRS app

The v1 retention system uses controlled flashcard artifacts plus session/mastery state:

1. approved artifact JSON contains cards;
2. coordinator determines due retrieval windows under `docs/14-study-operating-routine.md`;
3. ChatGPT presents cards/architecture prompts without revealing answers first;
4. response quality is recorded as evidence;
5. weak items are scheduled sooner;
6. strong items are spaced farther apart;
7. higher-order decision/scenario retrieval is preferred over unlimited card growth.

This avoids duplicate SRS state.

## Tool-change rule

Adding/replacing a core study tool is governed. Before adoption:

- consult current repository state first;
- verify eligibility;
- identify the measured problem it solves;
- assess data portability;
- define authoritative vs convenience role;
- avoid duplicate state;
- update this policy/change record when material.
