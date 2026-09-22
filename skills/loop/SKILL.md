---
name: loop
description: Run a product idea through deep-grill, deep-design, and deep-build according to artifact readiness. Start when the user invokes `loop` or clearly asks to run this product lifecycle. After it starts, continue on ordinary replies until the requested endpoint is complete, the user stops, the task changes, or new authority is required.
---

# Loop

Own progression, not the child methods. Route the active product task through three artifact contracts:

```text
deep-grill -> confirmed Product Brief
deep-design -> confirmed Build Contract
deep-build -> verified result
```

## Keep The Loop Active

A fresh loop starts when the user invokes `loop` or clearly asks to run this product lifecycle. After that, treat every ordinary reply as a continuation of the same loop until the goal is achieved, the user stops, the user clearly changes tasks, or further work requires authority outside the original request. The user does not need to name `loop` or any child again.

Resume the current child while its output contract is incomplete. When its artifact is confirmed, select the next child from artifact readiness without asking the user to nominate a skill or choose a route. State the transition briefly and continue in the same response when the next action is already authorized. Artifact readiness chooses the child; it does not expand the user's authority or the requested endpoint.

## Route By Artifact Readiness

- Use `deep-grill` when no confirmed Product Brief exists, when root product intent is unresolved, or when the requested endpoint is an isolated adversarial audit. Discovery mode produces the Product Brief; audit mode may finish without advancing when an audit is the whole request.
- Use `deep-design` when the Product Brief is confirmed but no confirmed Build Contract exists.
- Use `deep-build` when the Build Contract is confirmed and implementation is authorized.
- Resume the same child when its contract is incomplete, even after a mode switch, clarification, or ordinary user answer.
- Return an invalidated artifact to the child that produces it. A root product contradiction returns to `deep-grill`; a material behavior, interface, task, or verification gap returns to `deep-design`.
- Honor a direct invocation of a child skill. Direct use does not require `loop`, but it also does not activate the persistent loop unless the user invokes `loop` or clearly asks to run this product lifecycle.

The active child selects any domain, architecture, research, interface, visual-design, testing, deployment, or other specialist it needs. The user does not manage internal routing.

## Preserve One Source Of State

Carry the goal, current child, confirmed artifacts, constraints, authority, and evidence through the conversation and artifact references. For sustained work, use the active client's native goal or plan mechanism when available. Do not create duplicate workflow state, custom gates, hooks, or background processes.

Never imitate a child contract inside `loop`. Delegate the work, accept its artifact only when its readiness rules are met, and reroute from evidence. Stop when the requested endpoint is complete, the user stops or changes tasks, progress requires new authority, or remaining work has diminishing returns.
