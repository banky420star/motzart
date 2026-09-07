# Fresh Living Project Lifecycle

The animation is a projection of runtime state, not a substitute for runtime state.

| Product event/state | Visual behavior |
|---|---|
| Project created | One embryonic Mozart core; no subsystem lobes |
| `project.seeded` | Core pressure pulse |
| `mission.accepted` / planning | Thin exploratory tendrils; Connect stage |
| `agent.spawned` | A piece buds from the core and grows toward its branch |
| `job.created` / `job.assigned` | Outward directional transfer through the branch |
| Running job | Peristaltic flow packets travel outward |
| `workspace.change_committed` / `workspace.file_saved` | Persistent file bud appears on the responsible branch |
| Review / QA | Flow concentrates toward QA and Stabilize |
| Failure / rejection | Red constriction/turbulence around the real affected branch |
| Retry / recovery | Flow resumes on the branch; no fake reroute if no event exists |
| Completion | Inward return/absorption pulse; created files remain as project structure |

## Canvas semantics

- **Overview / Organism** answers: *Who/what is working right now?*
- **Canvas** answers: *What has actually become part of the project?*
- **Files** is the literal workspace source of truth.
- **Agents/Jobs** are the orchestration source of truth.

The core starts small. Branches are not visible until a branch has real agents, jobs, or files.
