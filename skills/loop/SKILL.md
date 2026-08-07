---
name: loop
description: >-
  Run a product idea through deep-grill, deep-design, and deep-build according
  to artifact readiness. Start only when the user explicitly invokes loop.
  After it starts, continue on ordinary replies without another invocation;
  treat a message containing only ? as a request to pause and re-explain the
  current state without advancing.
---

# Loop

Own progression, not the child methods. Route the active product task through three artifact contracts:

```text
deep-grill -> confirmed Product Brief
deep-design -> confirmed Build Contract
deep-build -> verified result
```

## Keep The Loop Active

A fresh loop starts only when the user explicitly invokes `loop` or clearly asks to start this workflow. After that, treat every ordinary reply as a continuation of the same loop until the goal is achieved, the user stops, the user clearly changes tasks, or further work requires authority outside the original request. The user does not need to name `loop` or any child again.

Resume the current child while its output contract is incomplete. When its artifact is confirmed, select the next child from artifact readiness without asking the user to nominate a skill or choose a route. State the transition briefly and continue in the same response when the next action is already authorized. Artifact readiness chooses the child; it does not expand the user's authority or the requested endpoint.

## Handle `?`

When the user's entire trimmed message is exactly `?` during an active loop, pause the current child. Re-explain:

- the last confirmed point;
- the current child and artifact state;
- what changed;
- why it matters; and
- the next action that was about to occur.

Use the language of the user's latest substantive message and preserve established project terms. Do not delegate, advance an artifact, ask the pending decision, or continue the task in the same response. Wait for the next user reply. `?` is a loop protocol, not a skill and not a request to explain an arbitrary topic.

## Route By Artifact Readiness

- Use `deep-grill` when no confirmed Product Brief exists, when root product intent is unresolved, or when the requested endpoint is an isolated adversarial audit. Discovery mode produces the Product Brief; audit mode may finish without advancing when an audit is the whole request.
- Use `deep-design` when the Product Brief is confirmed but no confirmed Build Contract exists.
- Use `deep-build` when the Build Contract is confirmed and implementation is authorized.
- Resume the same child when its contract is incomplete, even after a mode switch, clarification, or ordinary user answer.
- Return an invalidated artifact to the child that produces it. A root product contradiction returns to `deep-grill`; a material behavior, interface, task, or verification gap returns to `deep-design`.
- Honor a direct invocation of a child skill. Direct use does not require `loop`, but it also does not activate the persistent loop unless the user explicitly starts one.

Domain, architecture, research, interface, visual-design, testing, deployment, and other specialists are internal resources selected by the active child. They are not sibling routes that the user must manage. OpenSpec is an internal adapter owned by `deep-design` and `deep-build`; Wayfinder is not part of this workflow.

## Preserve One Source Of State

Carry the goal, current child, confirmed artifacts, constraints, authority, and evidence through the conversation and artifact references. For sustained work, use the active client's native goal or plan mechanism when available. Do not create duplicate workflow state, custom gates, hooks, or background processes.

Never imitate a child contract inside `loop`. Delegate the work, accept its artifact only when its readiness rules are met, and reroute from evidence. Stop when the requested endpoint is complete, the user stops or changes tasks, progress requires new authority, or remaining work has diminishing returns.
