# Mozart 2.1.1 — Living Swarm M4

**Mozart — Autonomous Software Intelligence** is a standalone local macOS software-building environment. This release is a full frontend reset on top of the working Mozart orchestration/runtime.

## What changed in 2.1.1

- Starts at **Project Selection / New Project** instead of a mature dashboard.
- A new project begins as a **single seed**.
- The organism grows only from real project state: agents, jobs, files, memory and events.
- Living matter now uses irregular membrane blobs, internal viscous circulation, heavier tendons, pressure bulges and visible neck/pinch-off deformation rather than clean sci-fi orbs.
- QA/review is transient biological activity unless it creates durable project structure.
- Simple tool-capability checks use one real bounded probe instead of spawning a generic runtime + QA workflow.
- Tool calls, exit codes, result previews and evidence are persisted and inspectable from moving work cells.
- Implements the Core Swarm motion language: breathing, pressure waves, pinch-off, outward travel, return/absorption, budding, amber/red rings, diamond seeds, heavy tendons and elastic settle.
- Every meaningful piece of the organism is selectable.
- **Overview** and **Canvas** share the same living world instead of being unrelated visualizations.
- Keeps first-class **Objectives, Agents, Knowledge, Files, Terminal, Settings and Source Monitor** sections.
- Adds a live backend graph endpoint: `GET /api/projects/{project_id}/graph`.
- Adds project deletion API with guarded workspace deletion.

## Run on an M4 Mac

### Fresh install

Double-click:

`FRESH_INSTALL.command`

This moves an existing Mozart app bundle to Trash and installs the new user-level application while preserving `~/Library/Application Support/Mozart` project data.

### Fully frozen ARM64 app

Double-click:

`build_m4.command`

The build script uses PyInstaller with `target_arch="arm64"`, creates `dist/Mozart.app`, and applies ad-hoc codesigning.

## Developer run

```bash
./run.command
```

or:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-desktop.txt
python desktop.py
```

## Validation

```bash
./test.sh
```

Current validation: **42 tests passed + 6 subtests passed**. The suite covers the project registry, orchestration runtime, event bus, workspace/terminal safety, live graph derivation, tool-capability probes and the Living Swarm frontend contract.
