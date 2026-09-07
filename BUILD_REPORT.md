# Mozart 2.1.1 Build Report

## Scope

This revision updates the real full-stack Mozart 2.1.0 source rather than the visual mockup bundle.

### Frontend / living organism

- Replaced circular/orb-like organs with irregular membrane blobs generated from smooth multi-lobed paths.
- Added internal viscous circulation within each membrane.
- Increased core/organ mass and pulled branch targets inward for a denser single-body silhouette.
- Increased tendon thickness and pressure response; active work adds moving peristaltic bulges.
- Reworked pinch-off into visible bulge/neck/daughter-cell separation.
- Moving work cells are deforming droplets with the diamond seed retained inside.
- QA is represented as an ephemeral bud unless it creates durable project structure.
- Core, tendon, organ, moving work cell, and file bud remain hit-tested/selectable.
- Work-cell inspector now shows persisted tool calls, exit codes, result previews, evidence, output, failures, and files.

### Backend / orchestration

- Added a dedicated tool-capability objective fast path.
- `check if you can use tools` now creates one Tools manager + one atomic probe job, not a generic runtime + QA decomposition.
- Capability probe performs real `list_files` and safe-terminal `pwd` calls and records the observations.
- Job records persist `evidence` and `tool_events`.
- QA deterministically accepts a capability probe only when at least one observed tool call exists and the terminal probe exits 0.
- Project stage no longer jumps to STABILIZE merely because QA is active early in a mission.
- Completed transient QA branches without durable files are omitted from the living graph.

## Verification

Executed from repository root with `PYTHONPATH=.`:

```text
42 passed, 6 subtests passed
```

Additional checks:

```text
node --check backend/static/app.js       PASS
python -m compileall -q backend          PASS
```

Version: `2.1.1`
