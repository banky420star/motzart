# Mozart event contract

The living canvas is a projection of these real runtime events. Frontend motion must not invent work that is not represented here.

## Project lifecycle

- `project.created`
- `project.seeded`
- `project.stage.changed`
- `project.mission.linked`
- `project.completed`
- `project.failed`

## Mission lifecycle

- `mission.accepted`
- `mission.ready`
- `mission.progress`
- `mission.paused`
- `mission.resumed`
- `mission.cancelled`
- `loop.started`
- `loop.completed`
- `mozart.gap_detected`
- `mozart.heartbeat`

## Agent lifecycle

- `agent.spawned`
- `agent.started`
- `agent.review_started`
- `agent.review_accepted`
- `agent.review_rejected`
- `agent.result_merged`
- `agent.blocked`
- `agent.retired`

## Job lifecycle

- `job.created`
- `job.assigned`
- `job.updated`
- `job.waiting_for_dependencies`
- `job.dependencies_satisfied`
- `job.completed`
- `job.rejected`
- `job.failed`
- `job.retry_requested`
- `job.recovered_once`

## Tool lifecycle

- `tool.started`
- `tool.completed`
- `tool.failed`

Tool-completion payloads should expose the exact tool name and a bounded result preview so the UI can show real evidence without leaking hidden state.

## Workspace lifecycle

- `workspace.change_proposed`
- `workspace.change_staged`
- `workspace.change_committed`
- `workspace.change_rolled_back`
- `workspace.file_saved`

A file bud becomes persistent only after the file exists in the real workspace.
