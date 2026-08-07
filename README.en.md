<p align="right"><a href="./README.md">中文说明</a></p>

<h1 align="center">loop</h1>

<p align="center"><strong>One trigger. Three deep loops. A verified result.</strong></p>

<p align="center">
  <a href="#install"><img src="https://img.shields.io/badge/install-skills.sh-111820?style=flat-square" alt="Install with skills.sh"></a>
  <a href="https://github.com/nxxxsooo/loop/releases"><img src="https://img.shields.io/github/v/release/nxxxsooo/loop?style=flat-square&color=5eead4" alt="Latest release"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-5eead4?style=flat-square" alt="MIT License"></a>
</p>

`loop` is the only normal entry point. Invoke it once; it keeps the active product task moving by artifact readiness instead of asking you to nominate the next skill.

```text
idea -> deep-grill -> Product Brief
     -> deep-design -> Build Contract
     -> deep-build -> verified result
```

## Install

```bash
npx skills@latest add nxxxsooo/loop --skill loop deep-grill deep-design deep-build -g -y
```

Start a task with:

> Use $loop to take this idea through design and build.

Ordinary replies continue the active child. You may also invoke any `deep-*` skill directly for isolated work without activating the persistent loop.

## Migrate from grill-loop v2

The repository moved from `nxxxsooo/grill-loop` to `nxxxsooo/loop`. GitHub redirects the old repository URL, but installed snapshots keep their old skill names. Remove them once, then install v3:

```bash
npx skills@latest remove grill-loop grilling -g -y
npx skills@latest add nxxxsooo/loop --skill loop deep-grill deep-design deep-build -g -y
```

| Skill | Owns | Ready when |
|---|---|---|
| `loop` | Persistence, transitions, and `?` | The requested endpoint is complete |
| `deep-grill` | Idea discovery and adversarial audit | Product Brief or audit verdict is confirmed |
| `deep-design` | Product specification and implementation design | Build Contract is confirmed |
| `deep-build` | Implementation, verification, and authorized delivery | Must-pass scenarios succeed |

## `?` explains and reconnects

During an active loop, send exactly:

```text
?
```

`loop` freezes the current action and re-explains the last confirmed point, current child and artifact, what changed, why it matters, and the pending next action without ending the active loop.

After the explanation, OMO uses its native countdown or autoresume when available. Other clients prefer a localized native question that lets you continue, adjust the next action, or stop. When no native interface is callable, one concise prompt in your language provides the continuation. Continuing immediately resumes the pending next action without another skill invocation.

## Native questions

`deep-grill` and `deep-design` use the active client's native question interface for user-owned decisions. If the interface exists but is gated behind another mode, the child keeps the pending decision intact, asks you to switch modes, and waits. Prose is used only when no native question interface exists or you explicitly choose it.

## Specification and design

`deep-design` owns the complete specification and design process. For small work, its Build Contract may live in the current task or native plan. For durable, multi-session, cross-component, or high-consequence changes, it uses the project's official OpenSpec workflow as the physical Build Contract. `deep-build` then applies that contract through the official workflow when present.

The active child calls domain, architecture, frontend, testing, and delivery specialists as needed; the user does not manage internal routing.

## The complete loop contract

This excerpt stays in exact sync with [`skills/loop/SKILL.md`](./skills/loop/SKILL.md):

<!-- loop-skill-body:start -->
> # Loop
>
> Own progression, not the child methods. Route the active product task through three artifact contracts:
>
> ```text
> deep-grill -> confirmed Product Brief
> deep-design -> confirmed Build Contract
> deep-build -> verified result
> ```
>
> ## Keep The Loop Active
>
> A fresh loop starts only when the user explicitly invokes `loop` or clearly asks to start this workflow. After that, treat every ordinary reply as a continuation of the same loop until the goal is achieved, the user stops, the user clearly changes tasks, or further work requires authority outside the original request. The user does not need to name `loop` or any child again.
>
> Resume the current child while its output contract is incomplete. When its artifact is confirmed, select the next child from artifact readiness without asking the user to nominate a skill or choose a route. State the transition briefly and continue in the same response when the next action is already authorized. Artifact readiness chooses the child; it does not expand the user's authority or the requested endpoint.
>
> ## Handle `?` Without Breaking Flow
>
> When the user's entire trimmed message is exactly `?` during an active loop, freeze the current action at its exact frontier while keeping the loop active. Re-explain:
>
> - the last confirmed point;
> - the current child and artifact state;
> - what changed;
> - why it matters; and
> - the next action that was about to occur.
>
> Use the language of the user's latest substantive message and preserve established project terms. Do not delegate, advance an artifact, or present the child's pending domain decision while explaining.
>
> Immediately after the explanation, present the best continuation control the active host actually supports:
>
> - In OMO, use its native countdown or autoresume surface when available so the pending next action resumes automatically unless the user intervenes.
> - Otherwise, when a native question interface is callable, ask whether to `Continue` (recommended), `Adjust next action`, or `Stop`; localize every label and explanation.
> - When no native continuation interface is callable, ask one concise localized continuation question in prose. Recommend resuming the pending next action while accepting an adjustment or stop in free form.
>
> Keep the current child, artifact, frontier, and authority active while the continuation control is open. `Continue` resumes the pending next action immediately. `Adjust next action` changes only that action unless the user's instruction invalidates an artifact. `Stop` ends the loop. Never require another skill invocation to resume.
>
> ## Route By Artifact Readiness
>
> - Use `deep-grill` when no confirmed Product Brief exists, when root product intent is unresolved, or when the requested endpoint is an isolated adversarial audit. Discovery mode produces the Product Brief; audit mode may finish without advancing when an audit is the whole request.
> - Use `deep-design` when the Product Brief is confirmed but no confirmed Build Contract exists.
> - Use `deep-build` when the Build Contract is confirmed and implementation is authorized.
> - Resume the same child when its contract is incomplete, even after a mode switch, clarification, or ordinary user answer.
> - Return an invalidated artifact to the child that produces it. A root product contradiction returns to `deep-grill`; a material behavior, interface, task, or verification gap returns to `deep-design`.
> - Honor a direct invocation of a child skill. Direct use does not require `loop`, but it also does not activate the persistent loop unless the user explicitly starts one.
>
> The active child selects any domain, architecture, research, interface, visual-design, testing, deployment, or other specialist it needs. The user does not manage internal routing.
>
> ## Preserve One Source Of State
>
> Carry the goal, current child, confirmed artifacts, constraints, authority, and evidence through the conversation and artifact references. For sustained work, use the active client's native goal or plan mechanism when available. Do not create duplicate workflow state, custom gates, hooks, or background processes.
>
> Never imitate a child contract inside `loop`. Delegate the work, accept its artifact only when its readiness rules are met, and reroute from evidence. Stop when the requested endpoint is complete, the user stops or changes tasks, progress requires new authority, or remaining work has diminishing returns.
<!-- loop-skill-body:end -->

## Raycast

Import [`skills/loop/assets/raycast-snippets.json`](./skills/loop/assets/raycast-snippets.json) to use `;lp`, `;dg`, `;dd`, and `;db`. Installing the skills does not modify Raycast.

## Update

Installed copies are snapshots:

```bash
npx skills@latest update loop deep-grill deep-design deep-build -g -y
```

Reload the client or start a fresh task when it has cached skill metadata.

## License

The bundle uses the [MIT License](./LICENSE). `deep-grill` preserves its incorporated upstream source and attribution; see [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md).
