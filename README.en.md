<p align="right"><a href="./README.md">中文说明</a></p>

<p align="center">
  <img src="./assets/grill-loop-cover.jpg" alt="A seafoam cord threads four graphite shapes into one continuously running loop" width="100%">
</p>

<h1 align="center">loop</h1>

<p align="center"><strong>One trigger. Three deep loops. A verified result.</strong></p>

<p align="center">
  <a href="#install"><img src="https://img.shields.io/badge/install-skills.sh-111820?style=flat-square" alt="Install with skills.sh"></a>
  <a href="https://github.com/nxxxsooo/loop/releases"><img src="https://img.shields.io/github/v/release/nxxxsooo/loop?style=flat-square&color=5eead4" alt="Latest release"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-5eead4?style=flat-square" alt="MIT License"></a>
</p>

When installed, Superpowers is the default method for day-to-day execution. `loop` remains implicitly available for the complete product lifecycle without requiring an explicit invocation every time; `what` owns cross-workflow explanation and continuation controls. Neither creates duplicate durable plans.

```text
idea -> deep-grill -> Product Brief
     -> deep-design -> Build Contract
     -> deep-build -> verified result
```

## Install

Guided install is recommended. Install the complete loop bundle and the `design-taste-frontend` specialist used by `deep-design`; choose the same agents, Project or Global scope, and Symlink or Copy for both:

```bash
npx skills@latest add nxxxsooo/loop --skill '*'
npx skills@latest add Leonxlnx/taste-skill --skill design-taste-frontend
```

For a fast global install:

```bash
npx skills@latest add nxxxsooo/loop --skill '*' -g -y
npx skills@latest add Leonxlnx/taste-skill --skill design-taste-frontend -g -y
```

The fast commands skip prompts and install the complete bundle and Taste Skill globally according to the `skills` CLI agent detection.

Describe the idea directly or explicitly use `$loop` to begin the product lifecycle:

> Use $loop to take this idea through design and build.

Ordinary replies continue the active child. You may also invoke any `deep-*` skill directly for isolated work; direct use completes that work but does not automatically start the complete lifecycle.

## Migrate from grill-loop v2

The repository moved from `nxxxsooo/grill-loop` to `nxxxsooo/loop`. GitHub redirects the old repository URL, but installed snapshots keep their old skill names. Remove them once, then install v3:

```bash
npx skills@latest remove grill-loop grilling -g -y
```

Then use either installation path above.

| Skill | Owns | Ready when |
|---|---|---|
| `loop` | Implicitly available product lifecycle and artifact transitions | The requested endpoint is complete |
| `deep-grill` | Idea discovery and adversarial audit | Product Brief or audit verdict is confirmed |
| `deep-design` | Product specification and implementation design | Build Contract is confirmed |
| `deep-build` | Implementation, verification, and authorized delivery | Must-pass scenarios succeed |
| `what` | Explain the active frontier and wait for continuation | The user continues, adjusts the next action, or stops |

## `?` and `$what`: explain, then continue

During any active workflow, send exactly:

```text
?
```

or explicitly invoke `$what`. The standalone `what` skill pauses the current action and explains the last confirmed point, current workflow and step, changed artifacts, why the state matters, and the pending next action. A normal sentence that merely contains `?` does not trigger it, and `?` has no special meaning outside active work.

After explaining, `what` waits for `Continue` (recommended), `Adjust next action`, or `Stop`; it executes the pending action only after `Continue`. When `request_user_input` is callable, it uses localized native UI. Otherwise it immediately presents the same concise localized choices in the current mode. It never asks you to switch to Plan mode merely to answer or continue.

## Native questions

`deep-grill` and `deep-design` use the active client's native question interface for material user-owned decisions when it is callable. When it is unavailable in the current mode, unsupported by the client, or you explicitly choose prose, they immediately ask the same concise localized question instead. They preserve the pending decision and recommendation, then continue from an ordinary reply rather than waiting for a mode switch.

## Specification and design

`deep-design` owns the complete specification and design process. Superpowers supplies daily TDD, debugging, review, and verification methods when available, without creating a second durable plan. An active relevant OpenSpec change is the sole physical Build Contract and task state; merely having OpenSpec installed or initialized does not create one. Create or use a new change only when the user explicitly requests it or the work is durable, multi-session, cross-component, migratory, security-sensitive, architecturally consequential, high-consequence, or needs a maintained handoff record.

The active child calls domain, architecture, frontend, testing, and delivery specialists as needed; the user does not manage internal routing.

For material visual-design questions involving landing pages, portfolios, editorial pages, or visual redesigns, `deep-design` loads `design-taste-frontend` by default when available. Dashboards, data tables, and multi-step product UI use a more suitable specialist.

### UI design and rebuilds

`deep-design` covers new UI, partial redesigns, and complete rebuilds: confirm scope and preserved behavior, choose product/UI/both/no external research, review actual visual evidence with per-reference feedback, settle direction, and choose whether to preview first. Existing approvals are reused; backend-only tasks skip this branch.

Use independently installed `ui-research` for research methods and an available `react-bits` integration for free motion discovery. Neither is a hard bundle dependency; official sources work directly when they are absent. Reference quotas, paid pages, and client-specific modes do not become extra gates. The former `rebuild-ui-design` workflow is integrated and no longer needs a separate installation.

All decisions feed one Build Contract. `deep-build` owns real pages, browser interactions, and screenshot verification; broad rebuilds review a representative end-to-end slice before migrating the rest. Preview revisions do not count as approval, and component research does not authorize installation.

See the [UI workflow](skills/deep-design/references/ui-design-workflow.md) and [visual evidence](skills/deep-design/references/visual-evidence.md) methods.

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
> A fresh loop starts when the user invokes `loop` or clearly asks to run this product lifecycle. After that, treat every ordinary reply as a continuation of the same loop until the goal is achieved, the user stops, the user clearly changes tasks, or further work requires authority outside the original request. The user does not need to name `loop` or any child again.
>
> Resume the current child while its output contract is incomplete. When its artifact is confirmed, select the next child from artifact readiness without asking the user to nominate a skill or choose a route. State the transition briefly and continue in the same response when the next action is already authorized. Artifact readiness chooses the child; it does not expand the user's authority or the requested endpoint.
>
> ## Route By Artifact Readiness
>
> - Use `deep-grill` when no confirmed Product Brief exists, when root product intent is unresolved, or when the requested endpoint is an isolated adversarial audit. Discovery mode produces the Product Brief; audit mode may finish without advancing when an audit is the whole request.
> - Use `deep-design` when the Product Brief is confirmed but no confirmed Build Contract exists.
> - Use `deep-build` when the Build Contract is confirmed and implementation is authorized.
> - Resume the same child when its contract is incomplete, even after a mode switch, clarification, or ordinary user answer.
> - Return an invalidated artifact to the child that produces it. A root product contradiction returns to `deep-grill`; a material behavior, interface, task, or verification gap returns to `deep-design`.
> - Honor a direct invocation of a child skill. Direct use does not require `loop`, but it also does not activate the persistent loop unless the user invokes `loop` or clearly asks to run this product lifecycle.
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

Import [`skills/loop/assets/raycast-snippets.json`](./skills/loop/assets/raycast-snippets.json) to use `loop ;lp`, `deep grill ;dg`, `deep design ;dd`, `deep build ;db`, and `what ;wt`. The bundle-refresh command below updates installed skills and this JSON file, not entries already imported into Raycast; update those five entries in place after importing so retired loop-owned `?` text and duplicate entries do not remain.

## Update

Installed copies are snapshots:

```bash
# After each release, idempotently refresh the whole bundle and discover new bundled skills
npx skills@latest add nxxxsooo/loop --skill '*' -g -y

# Taste is an independently installed upstream skill
npx skills@latest update design-taste-frontend -g -y
```

`update loop` follows only the existing lock record for `loop`: it cannot discover `what` in an older installation or refresh sibling bundle skills. Use the bundle `add` command after every release instead; it is safe to repeat and synchronizes the complete bundle.

Reload the client or start a fresh task when it has cached skill metadata.

## License

The bundle uses the [MIT License](./LICENSE). `deep-grill` preserves its incorporated upstream source and attribution; see [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md). `design-taste-frontend` is installed separately from [`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill), is not part of this bundle, and remains under its upstream license and update path.
