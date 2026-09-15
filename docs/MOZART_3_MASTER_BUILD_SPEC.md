# Mozart 3.0 — Master Build Specification

**Product name:** Mozart — Autonomous Software Intelligence  
**Release target:** Mozart 3.0 — Living Worker Swarm  
**Primary platform:** macOS (Apple Silicon first)  
**Core visual idea:** a premium, playful software-construction world where original tiny worker agents physically leave Mozart, perform work, return with evidence/results, and visibly carry the project forward.

> Design note: the tiny workers should capture the *comedic teamwork energy* of animated helper characters, but must be original Mozart characters rather than copies of any existing film characters.

---

## 1. Product Thesis

Mozart should make autonomous software creation understandable without requiring the user to read terminal logs.

The application exposes three truths about every project:

1. **Brain — who is thinking and working?**
2. **Build — what is physically being constructed?**
3. **Files — what source truth actually exists?**

The same runtime events drive all three views. No decorative node may exist without corresponding real state.

### Core metaphor

- **Mozart Core** = orchestrator / dispatcher / memory hub.
- **Managers** = persistent project capabilities.
- **Workers** = transient agent executions.
- **Cargo** = tasks, context, files, test results, patches, artifacts, approvals.
- **Stations** = Build-page project stages/subsystems.
- **Routes** = real dependencies / handoffs.
- **Return trip** = worker returns evidence or output.
- **Failure** = worker returns damaged/empty-handed, route blocks, or repair crew is spawned.

---

## 2. Final Navigation

Primary sidebar:

- **Overview**
- **Brain**
- **Build**
- **Objectives**
- **Agents**
- **Knowledge**
- **Files**
- **Terminal**
- **Settings**

Persistent project header:

- Project selector
- Project state
- Current model/provider
- Search
- + Objective
- Pause / Resume
- Global stop / Kill only where safe and explicit

The visual canvases should dominate the window. Inspectors are contextual and slide in only when needed.

---

## 3. Mozart Worker Character System

### 3.1 Visual identity

Workers are small original helper characters with:

- compact rounded body silhouette
- oversized expressive visor/eyes
- utility backpack / tool belt
- short legs and slightly clumsy movement
- role-specific equipment rather than role-specific body colors
- dark graphite body with Mozart cyan/amber accents
- strong readable silhouette at 24–48 px equivalent size

Avoid direct resemblance to existing licensed characters. The personality should come from animation and behavior, not copying a specific costume or anatomy.

### 3.2 Role equipment

Examples:

- **Planner:** clipboard / floating blueprint slate
- **Frontend:** UI panels / component tiles
- **Runtime:** code terminal / wrench
- **Research:** scanner / document stack
- **QA:** magnifier / test meter
- **Packaging:** crates / app bundle box
- **Knowledge:** memory capsule / books
- **Repair worker:** red toolkit / patch strip

### 3.3 Worker cargo

Workers visibly carry real data objects:

- task capsule
- file tile
- patch bundle
- test report
- green approval token
- red failure token
- artifact crate
- knowledge capsule

Cargo type is derived from actual event/output state.

---

## 4. Brain Page — The Creator

### 4.1 Purpose

The Brain answers:

> What is Mozart thinking about, who is doing the work, where is pressure building, and what is blocked?

### 4.2 Visual composition

The Brain is **not** a graph and **not** a fixed radial org chart.

Initial state for a new project:

```text
◇
```

Then Mozart forms:

```text
        ╭────────╮
        │ MOZART │
        ╰────────╯
```

As work begins, stations/capabilities appear only when real work activates them.

Workers leave the core or manager zone, travel along soft illuminated routes, perform work, then return with cargo.

### 4.3 Brain layout

The core sits near center but does not need to remain exact center.

Around it:

- persistent manager zones grow only after meaningful repeated activity
- temporary work sites can appear and disappear
- routes curve and react to traffic
- active routes glow softly
- blocked routes constrict / flash red

The scene should feel like a **living workshop**, not a network diagram.

### 4.4 Brain lifecycle mapping

| Runtime event | Brain behavior |
|---|---|
| objective.created | Core wakes; objective token enters Mozart |
| plan.created | Planner worker exits with blueprint cargo |
| manager.activated | Persistent work zone grows / lights up |
| job.queued | Small task capsule appears at dispatcher |
| job.started | Worker is dispatched carrying task capsule |
| model.call.started | Worker animation changes to thinking/processing |
| tool.started | Tool icon appears; worker begins tool interaction |
| file.saved | Worker picks up file tile / cargo |
| qa.rejected | Red failure token; worker returns; route pulses red |
| job.retry | Repair worker dispatched down same route |
| job.completed | Worker returns with result cargo; Mozart absorbs evidence |
| mission.completed | Core settles; successful routes remain as project history |

### 4.5 Model behavior language

- **Small local model:** quick short-stride worker motion, rapid dispatch cadence.
- **Large local model:** heavier worker/tool setup, slower but continuous activity.
- **Cloud/deep reasoning:** worker enters communication booth/uplink; route glows with deeper slow pulse.

Model type should affect movement and timing rather than making the UI a rainbow.

### 4.6 Brain failure behavior

A failure must remain readable.

Example:

1. Worker route turns red near failure point.
2. Worker returns with broken/red cargo.
3. Manager zone shows a temporary warning beacon.
4. Downstream workers visibly wait rather than pretending to work.
5. Retry spawns a repair worker or sends the same worker back out.
6. If fixed, route returns to normal and the warning fades.

### 4.7 Brain interactions

**Click Mozart Core**
- current objective
- project state
- active managers/workers
- model/provider
- queue depth
- recent decisions
- current blockers

**Click worker**
- agent name/id
- current job
- model
- progress/state
- tools used
- files touched
- evidence
- retry count
- `View in Build`

**Click manager/work zone**
- subsystem
- manager agent
- active/queued/completed jobs
- dependencies
- files owned/touched
- failure count

**Click route**
- source / destination
- jobs carried
- dependency state
- throughput
- current block reason

**Hover**
- tiny label only; no large popup.

### 4.8 Brain camera controls

- Drag empty canvas → pan
- Scroll/pinch → zoom at cursor
- Double-click empty canvas → recenter
- `F` → fit active organism/workshop
- `Space` → follow active work
- `Esc` → stop follow / close inspector

Auto-framing triggers only on major persistent growth, not every worker movement.

---

## 5. Build Page — The Creation

### 5.1 Purpose

The Build page answers:

> What is being built, what exists already, what is being tested, and exactly where did construction stop?

### 5.2 Visual composition

Build looks like a **software factory floor / assembly space** using the same Mozart worker characters.

The project grows across real stages. Recommended default stage families:

- Planning
- Design / Architecture
- Build / Implementation
- Integration
- Test / QA
- Packaging
- Complete

Stages are not hard-coded as mandatory. Only relevant stages appear based on the actual plan/job ledger.

### 5.3 Build station behavior

A station represents a real subsystem or stage.

Examples:

- Frontend
- Backend
- Runtime
- Database
- Assets
- Tests
- Packaging

Workers physically bring cargo to stations:

- plans arrive at Build
- code files stack/attach to modules
- test workers carry reports
- repair workers return failed components
- packaging workers put finished modules into app/artifact crates

### 5.4 Build growth rule

Future work is never rendered as completed structure.

States:

- **planned** → faint blueprint/ghost outline
- **queued** → blueprint + waiting task token
- **active** → station becomes solid; worker present
- **produced** → file/module physically attaches
- **verified** → green verification seal
- **failed** → damaged/red state retained in history
- **retrying** → repair route grows from failed point
- **complete** → station settles and remains as persistent project anatomy

### 5.5 Build artifacts

Only real artifacts may appear:

- workspace file exists → file tile can exist
- test report exists → test report object can exist
- app bundle exists → app bundle crate can exist
- installer exists → installer package object can exist

No inferred/fake artifact counts.

### 5.6 Build interactions

**Click station**
- stage/subsystem name
- jobs
- dependencies
- files
- tests
- completion state
- last agent to modify it

**Click file/module**
- file path
- source/owner job
- current status
- recent edits
- test coverage if known
- `Open in Files`
- `Show responsible worker`

**Click failure**
- exact failed job
- reason
- prerequisite chain
- affected downstream work
- retry history
- `Retry`
- `View worker`
- `Open logs`

**Click artifact crate**
- output path
- build version
- packaging status
- test status
- reveal/download action where supported

---

## 6. Brain ↔ Build Cross-Linking

Brain and Build must use the same stable IDs.

Minimum shared keys:

- project_id
- objective_id
- manager_id
- agent_id
- job_id
- artifact_id
- file_path
- dependency_ids

Examples:

- Brain worker → `View in Build` highlights the exact module/stage being changed.
- Build file → `Show responsible worker` jumps to Brain and selects that worker.
- Build failure → Brain highlights the worker/manager/route that produced it.

---

## 7. Runtime State Contract

The UI must not derive truth from animation state.

### Canonical states

**Objective**
- pending
- planning
- active
- stabilizing
- completed
- failed
- paused

**Job**
- planned
- queued
- assigned
- running
- waiting_dependency
- reviewing
- retrying
- completed
- failed
- cancelled

**Agent**
- idle
- dispatched
- reasoning
- using_tool
- waiting
- reviewing
- returning
- blocked
- retired

**Artifact**
- planned
- creating
- present
- validating
- verified
- failed
- superseded

### Required timestamps

Every state transition should have:

- created_at
- started_at where applicable
- updated_at
- completed_at where applicable

These are required for replay and historical debugging.

---

## 8. Event Contract

Recommended normalized event envelope:

```json
{
  "event_id": "evt_...",
  "project_id": "prj_...",
  "objective_id": "obj_...",
  "type": "job.started",
  "timestamp": "2026-09-14T21:00:00Z",
  "actor": {
    "agent_id": "agt_...",
    "manager_id": "mgr_..."
  },
  "subject": {
    "job_id": "job_..."
  },
  "payload": {}
}
```

Required event families:

- project.*
- objective.*
- plan.*
- manager.*
- agent.*
- job.*
- model.*
- tool.*
- workspace.*
- qa.*
- build.*
- artifact.*
- runtime.*

The frontend should consume a normalized stream regardless of provider/model.

---

## 9. Rendering Architecture

### 9.1 Recommendation

Use a pragmatic 2.5D renderer rather than a full game engine.

Recommended stack:

- WebGL2 or Three.js scene
- orthographic camera
- instanced worker meshes/sprites
- GPU particle/route effects
- DOM overlay for inspectors/labels
- CPU state machine for worker motion targets
- optional postprocessing bloom at conservative settings

Do **not** put the source of truth inside React animation state.

### 9.2 Motion engine

Worker movement should be deterministic from event IDs and stage positions.

Use spring movement:

`F = -kx - cv`

for:

- camera easing
- worker approach/settle
- cargo lag
- station bounce/response

### 9.3 Worker animation states

- idle
- receive-task
- depart
- walk/run
- carry
- inspect
- type/code
- test
- repair
- celebrate-short
- return
- unload
- blocked

Animations should be short and readable, not constant comedy loops.

### 9.4 Performance targets

- 60 FPS target
- 30 FPS minimum graceful mode
- <= 24 fully animated workers on screen by default
- excess workers aggregate into traffic indicators or grouped crews
- LOD for labels/props
- pause/reduce motion option

---

## 10. Frontend Component Architecture

Suggested structure:

```text
frontend/
  app/
    AppShell
    ProjectContext
    Router

  brain/
    BrainPage
    BrainScene
    MozartCore
    ManagerZone
    WorkerCharacter
    WorkerCargo
    WorkRoute
    BrainInspector
    BrainCameraController

  build/
    BuildPage
    BuildScene
    BuildStation
    ArtifactObject
    FileTile
    FailureMarker
    BuildInspector
    BuildCameraController

  swarm/
    SwarmStateStore
    EventReducer
    WorkerMotionController
    CharacterAnimationController
    SceneSelection
    ReplayController

  shared/
    ProjectHeader
    Sidebar
    InspectorDrawer
    Search
    EmptyState
    StatusBadge

  api/
    websocket
    project
    jobs
    files
    artifacts
```

If Mozart remains a static HTML/JS frontend, preserve the same module boundaries using ES modules instead of one large `app.js`.

---

## 11. Backend Changes

### 11.1 Stable IDs

Guarantee stable project/objective/manager/agent/job/artifact IDs across restarts.

### 11.2 Event persistence

Persist normalized lifecycle events so Brain/Build can replay prior runs.

### 11.3 Dependency truth

Jobs must explicitly expose:

- depends_on
- blocked_by
- retry_of
- supersedes
- produced_files
- produced_artifacts
- evidence
- tool_events

### 11.4 Recovery logic

Required:

- bounded retry count
- prerequisite recovery
- stale-job detection
- completion-gate reason surfaced to UI
- no infinite recursive restart
- user-visible manual retry

### 11.5 Progress calculation

Progress must be derived from real weighted jobs/stages.

Never infer `42%` solely from UI animation or number of nodes.

---

## 12. Overview Page

Overview is intentionally simple.

Show:

- current project
- objective
- overall build progress
- active workers
- blockers
- latest artifacts
- current model/provider
- runtime health
- buttons: Brain / Build / Files / Terminal

No duplicate visualization.

---

## 13. Agents Page

Textual operational view for exact inspection.

Groups:

- Mozart orchestrator
- Managers
- Active workers
- Waiting workers
- Reviewers
- Historical/retired workers

Each row links to the corresponding Brain character.

---

## 14. Files Page

Files is source truth.

Required:

- tree
- file preview/editor where supported
- generated-by metadata
- last modified by job/agent
- test/evidence references
- diff/history if available
- open/reveal action

Never show a file in Build unless it exists here.

---

## 15. Source Monitor

Source Monitor should answer:

> Is Mozart actually doing anything, and what source/runtime is changing?

Show:

- backend health
- event stream health
- model health
- workspace watcher
- active writes
- current branch/worktree if available
- last successful heartbeat
- current errors

---

## 16. Settings

Required settings:

- model/provider selection
- local vs cloud routing
- worker concurrency
- retry limits
- completion gate/tool-turn budget
- motion: full / reduced / off
- rendering quality: auto / high / balanced / low
- auto-follow behavior
- sound effects toggle (optional)
- workspace permissions
- tool safety policy

---

## 17. CLI + CI Review Gate

GitHub Actions must run for every PR and main push.

Required checks:

1. Python syntax / compileall
2. JavaScript syntax / frontend build
3. unit tests
4. runtime tests
5. event contract tests
6. dependency/retry tests
7. CLI smoke test
8. API startup smoke test
9. static asset existence checks
10. version consistency check

For macOS-specific packaging, add a macOS runner when practical:

- create app bundle
- launch backend process
- verify health endpoint
- validate required resources
- optional pywebview/native smoke test

PR should not be merged while required CI is failing.

---

## 18. Replay / Review Mode

After core 3.0 is stable, add replay.

Timeline:

```text
12:03 ──────────●──────────── 12:48
                ↑
              selected
```

Replay must reconstruct from persisted events:

- worker dispatch
- cargo movement
- failures
- retries
- file creation
- test passes
- packaging

This turns Mozart into a visual execution record, not just a live dashboard.

---

## 19. Accessibility / Reduced Motion

Workers must remain understandable with motion reduced or disabled.

Reduced-motion mode:

- no bouncing
- no long travel animation
- workers teleport between meaningful states with short fades
- active routes pulse minimally
- all information remains available in inspectors

Status must never be represented by color alone.

---

## 20. Release Acceptance Criteria

Mozart 3.0 is not considered complete until all conditions below pass.

### Runtime

- [ ] New project can be created/opened.
- [ ] Objective can be submitted.
- [ ] Managers/workers spawn from real jobs.
- [ ] Tools execute with recorded evidence.
- [ ] Files are written to the real workspace.
- [ ] Failed prerequisites block downstream work correctly.
- [ ] Retry/recovery works without loops.
- [ ] Project can reach completed state.

### Brain

- [ ] No fixed radial graph.
- [ ] Workers visually dispatch only when jobs start.
- [ ] Workers return when jobs finish/fail.
- [ ] Cargo corresponds to real outputs/evidence.
- [ ] Managers appear only from real subsystem activity.
- [ ] Click/hover/selection works.
- [ ] Brain ↔ Build linking works.

### Build

- [ ] Planned work is visually distinct from real output.
- [ ] Only real files/artifacts appear as completed objects.
- [ ] Dependencies are understandable.
- [ ] Failures remain visible.
- [ ] Retry history is inspectable.
- [ ] Build stage progress matches backend truth.

### Packaging

- [ ] macOS M-series launch works from double-click.
- [ ] First-run dependency/bootstrap path succeeds or native build contains dependencies.
- [ ] App does not silently quit.
- [ ] Health/startup failures produce readable diagnostics.
- [ ] Clean install and upgrade paths are tested.

### CI

- [ ] Required GitHub checks pass.
- [ ] CLI smoke test passes.
- [ ] API smoke test passes.
- [ ] frontend syntax/build passes.
- [ ] full automated test suite passes.

---

## 21. Implementation Phases

### Phase A — Runtime truth first

1. Normalize event contract.
2. Persist lifecycle events.
3. Fix dependency/retry/completion-gate behavior.
4. Guarantee stable IDs.
5. Add tests around all above.

**Exit gate:** backend can build a small sample project end-to-end without visual UI.

### Phase B — Brain worker swarm

1. Remove old radial renderer.
2. Build original worker character system.
3. Implement deterministic dispatch/return motion.
4. Implement cargo mapping.
5. Implement manager/work zones.
6. Implement selection/inspector.

**Exit gate:** every visible worker corresponds to a real running/returning job.

### Phase C — Build factory

1. Derive Build stations from real jobs/subsystems.
2. Implement blueprint/planned state.
3. Implement real file/module/artifact objects.
4. Implement failure/repair visuals.
5. Implement Build inspector.
6. Link Brain ↔ Build.

**Exit gate:** user can visually identify exactly what exists and what is blocked.

### Phase D — Production UX

1. Overview cleanup.
2. Search.
3. keyboard shortcuts.
4. reduced motion.
5. performance/LOD.
6. startup/loading polish.

### Phase E — macOS + CI hardening

1. Native startup regression.
2. packaging validation.
3. GitHub Actions review gate.
4. release ZIP/app artifact.
5. clean-machine test.

---

## 22. Migration from 2.2.x

Keep:

- backend project model
- job ledger
- agents/managers
- tools
- workspace/files
- Objectives/Agents/Knowledge/Files/Terminal/Settings
- Source Monitor
- existing macOS bootstrap/diagnostics where stable

Replace/refactor:

- Brain renderer
- Build renderer
- scene interaction system
- frontend event reducer
- progress truth if currently inferred incorrectly
- any duplicate GPU + canvas renderer path

Do not rewrite the whole backend unless a specific contract requires it.

---

## 23. Coding-Agent Handoff Prompt

Use the following instruction for the coding agent responsible for implementation:

> Implement **Mozart 3.0 — Living Worker Swarm** against the actual repository, not as a mockup. Preserve the existing functional backend and only replace/refactor subsystems required by the master build specification. The Brain page must show original tiny worker characters leaving Mozart to perform real jobs and returning with real evidence/results; no worker may exist without corresponding runtime state. The Build page must show the real project assembling from planned blueprint states into real modules/files/tests/artifacts. Remove the old radial graph renderer completely. Brain and Build must share stable job/agent/file identifiers and cross-link selection. Fix backend lifecycle/retry/dependency issues before hiding them with visuals. Add/extend automated tests for every state transition, and add GitHub CI checks for Python, JavaScript, runtime, API, event-contract and CLI smoke tests. Run the complete test suite after every repair cycle. Do not mark work complete while tests are failing or while a visible artifact has no backing runtime/file state. Preserve macOS M-series launch and packaging behavior. Produce a release report listing exact changed files, tests executed, failures repaired, remaining risks and the final build artifact.

---

## 24. Final Product Definition

Mozart 3.0 should feel like this:

> Give Mozart an objective. The core wakes. Tiny workers receive tasks and physically leave to research, design, code, test and package. They carry real project objects with them. When they succeed, they return and the project visibly grows. When something breaks, the worker returns with the failure and the exact construction point becomes visibly blocked. The user can click anything to see the real agent, job, file, evidence or error behind it.

That is the defining interaction for Mozart 3.0.
