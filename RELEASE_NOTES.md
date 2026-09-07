# Mozart 2.1.1 — Living Matter + Tool Contract Fixes

This update keeps the full Living Swarm frontend/backend architecture and fixes the two problems exposed during the Solitaire tool-capability test.

## Living matter renderer

- Replaced clean orb-like organs with irregular, membrane-shaped viscous cells.
- Increased core and organ mass and reduced hub spacing so the organism reads as one connected body.
- Added slow internal circulation inside the membrane rather than decorative particle-only motion.
- Tendons are thicker, pressure-bearing tissue with workload-driven luminance and peristaltic bulges.
- Pinch-off now visibly forms a narrowing neck and stretched daughter cell.
- Moving work cells use deforming membrane droplets with the diamond seed retained inside.
- QA/review branches are transient buds unless they create durable project structure.
- Selection and inspector behavior remain available for core, tendons, organs, work cells, and file buds.

## Tool/QA lifecycle fixes

- Simple "can Mozart use tools?" objectives now use one bounded Tool Capability Probe instead of spawning a full build + QA topology.
- The probe executes real workspace and safe-terminal tool calls, records the observations, and completes without asking a model to invent evidence.
- Tool observations and evidence are persisted on the Job record and are visible in the work-cell inspector.
- QA treats capability probes deterministically: a real observed tool call plus an exit-0 terminal probe is sufficient evidence.
- Project stage no longer jumps to STABILIZE merely because a QA job is active early in a mission.
- Ephemeral QA organs disappear when no active/blocked QA work remains and no durable QA files were created.

## Version

`2.1.1`
