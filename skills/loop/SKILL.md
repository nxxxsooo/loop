---
name: loop
description: Take product work from idea to verified result through deep-grill, deep-design, and deep-build, or pause to explain an active task. Use for end-to-end build requests ("build me…", "从想法到上线"), loop invocation, a message consisting only of `?`, explicit `$what` or `@what` reorientation, attached `what?` review annotations, or requests to explain the current frontier. Build mode continues on ordinary replies; reorientation pauses until explicit continuation. Single-stage requests and small fixes do not start build mode.
---

# Loop

## Select The Mode

Use **build mode** for end-to-end product work as defined below. Use **reorientation mode** for an entire trimmed `?` message, explicit `$what` or `@what` invocation, an explicit request for loop's reorientation mode, attached reorientation instructions, or a request to re-orient after not understanding the current update. An ordinary question merely containing `?` does not trigger it.

Reorientation takes precedence over automatic progression, including inside an active child or a non-product workflow. Read [Reorientation and continuation](references/reorientation.md) before responding, especially for attached review feedback with `what?` annotations. Explain those passages first, pause the pending action, and wait for an explicit continuation choice. This mode neither starts a product build loop nor replaces the current workflow or its state.

## Build Mode

Own progression, not the child methods. Route the active product task through three artifact contracts:

```text
deep-grill -> confirmed Product Brief
deep-design -> confirmed Build Contract
deep-build -> verified result
```

## Keep The Loop Active

A fresh build loop starts when the user invokes `loop` for product progression or wants a product idea, feature, app, or tool built end to end across more than one stage. Single-stage requests and small fixes stay with the matching child or ordinary work. After that, treat every ordinary reply as a continuation of the same loop until the goal is achieved, the user stops, the user clearly changes tasks, or further work requires authority outside the original request. A reorientation trigger pauses this progression until the user explicitly resumes it. The user does not need to name `loop` or any child again.

Resume the current child while its output contract is incomplete. When its artifact is confirmed, select the next child from artifact readiness without asking the user to nominate a skill or choose a route. State the transition briefly and continue in the same response when the next action is already authorized. Artifact readiness chooses the child; it does not expand the user's authority or the requested endpoint.

## Route By Artifact Readiness

- Use `deep-grill` when no confirmed Product Brief exists, when root product intent is unresolved, or when the requested endpoint is an isolated adversarial audit. Discovery mode produces the Product Brief; audit mode may finish without advancing when an audit is the whole request.
- Use `deep-design` when the Product Brief is confirmed but no confirmed Build Contract exists.
- Use `deep-build` when the Build Contract is confirmed and implementation is authorized.
- Resume the same child when its contract is incomplete, even after a mode switch, clarification, or ordinary user answer.
- Return an invalidated artifact to the child that produces it. A root product contradiction returns to `deep-grill`; a material behavior, interface, task, or verification gap returns to `deep-design`.
- Honor a direct invocation of a child skill. Direct use does not require `loop`, but it also does not activate the persistent loop unless the user invokes `loop` or asks for end-to-end work as defined above.

The active child selects any domain, architecture, research, interface, visual-design, testing, deployment, or other specialist it needs. The user does not manage internal routing.

## Preserve One Source Of State

Carry the goal, current child, confirmed artifacts, constraints, authority, and evidence through the conversation and artifact references. For sustained work, use the active client's native goal or plan mechanism when available. Do not create duplicate workflow state, custom gates, hooks, or background processes.

## Set The Native Goal

When a build loop starts, register its requested endpoint as the client's native goal without asking, and state the goal in one line. The goal holds the endpoint, never the child route or artifact state. In OpenCode, set it on the current session from the shell:

```sh
opencode api post "/api/session/$OPENCODE_SESSION_ID/command" -d '{"name":"goal","text":"<objective>","delivery":"steer"}'
```

Write the objective in the user's language, under 4000 characters: the endpoint, the project, authority limits (for example no deploy or publish), and observable done-when evidence. The same call with `text` set to `pause`, `resume`, or `clear` controls the goal; an empty `text` returns its status inside a `CommandExecutionError`, which is a status report rather than a session failure. OpenCode's reviewer judges completion from visible evidence after each turn and keeps the session going until then, so show verification output.

- Check status first and skip setting a goal when one is already active for this endpoint. Single-stage work and reorientation mode set no goal.
- Ask user decisions through the native question tool inside the turn. Ending a turn to wait for a prose answer lets the reviewer pause the goal as blocked; when the user's next ordinary reply continues the loop, resume it.
- Pause the goal before a reorientation explanation and resume it only when the user chooses Continue.
- Clear the goal when the user stops, changes tasks, or changes the endpoint; set a new one if the new endpoint still spans stages.

Never imitate a child contract inside `loop`. Delegate the work, accept its artifact only when its readiness rules are met, and reroute from evidence. Stop when the requested endpoint is complete, the user stops or changes tasks, progress requires new authority, or remaining work has diminishing returns.
