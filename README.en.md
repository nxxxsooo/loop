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

`loop` is a persistent product-work orchestrator: one trigger starts a run where ordinary replies continue the active child, and artifact readiness moves the task from idea to verified result. When Superpowers is installed, it is the default method for day-to-day execution; `loop` implicitly takes the complete lifecycle without being named. Its reorientation mode explains active work and controls continuation across workflows, without creating a second durable plan.

In OpenCode, a loop build registers its endpoint as the built-in `/goal`. OpenCode's reviewer keeps the session going until visible evidence shows the endpoint is met. Reorientation pauses the goal; stopping or changing tasks clears it.

```text
idea -> deep-grill -> Product Brief
     -> deep-design -> Build Contract
     -> deep-build -> verified result
```

## Install

**Use this repository for the complete lifecycle. For idea discovery and adversarial review alone, use the [standalone deep-grill repository](https://github.com/nxxxsooo/deep-grill).** Both use the same DG source; the standalone distribution can be released and updated independently.

One command installs all five skills: the four Loop-maintained skills plus `impeccable`, vendored from a pinned upstream commit:

```bash
npx skills@latest add nxxxsooo/loop --skill '*'
```

For a fast global install:

```bash
npx skills@latest add nxxxsooo/loop --skill '*' -g -y
```

For a partial install, select skills by name (for example `--skill loop --skill deep-grill`). GSAP, React Bits, and shadcn guidance comes with `deep-design`; it does not appear as standalone skills in the install list.

Install standalone DG only:

```bash
npx skills@latest add nxxxsooo/deep-grill --skill deep-grill -g -y
```

Describe the idea directly or explicitly use `$loop` to begin the product lifecycle:

> Use $loop to take this idea through design and build.

Ordinary replies continue the active child. You may also invoke any `deep-*` skill directly for isolated work; direct use completes that work but does not automatically start the complete lifecycle.

## What's in the bundle

Loop-owned skills (maintained here, under `skills/`):

| Skill | Owns | Ready when |
|---|---|---|
| `loop` | Product lifecycle, artifact transitions, and reorientation | The endpoint is complete, or the user chooses how to continue |
| [`deep-grill`](https://github.com/nxxxsooo/deep-grill) | Idea discovery and adversarial audit; independently installable and updatable | Product Brief or audit verdict is confirmed |
| `deep-design` | Product specification and implementation design | Build Contract is confirmed |
| `deep-build` | Implementation, verification, and authorized delivery | Must-pass scenarios succeed |

Vendored external skill (`skills/vendor/`, verbatim upstream):

| Skill | Upstream | Role |
|---|---|---|
| `impeccable` | `pbakaus/impeccable` | Interface design, redesign, review, and polish |

The [deep-design reference index](./skills/deep-design/SKILL.md#on-demand-component-and-motion-guidance) includes eight official GSAP topics from `greensock/gsap-skills` plus React Bits and shadcn guidance. Upstream commits and file hashes for `impeccable` and the GSAP references and licenses are recorded in [`bundle-sources.json`](./bundle-sources.json) and checked by `scripts/check-bundle.py`.

## `?` and `$what`: explain, then continue

During any active workflow, send exactly:

```text
?
```

or explicitly invoke `$what` (`@what` in OpenCode). These select loop's reorientation mode, which pauses the current action and explains the last confirmed point, current workflow and step, changed artifacts, why the state matters, and the pending next action. A normal sentence that merely contains `?` does not trigger it. With no resumable task, it asks which task to orient around.

In [OpenCode Annotate](https://github.com/nxxxsooo/opencode-annotate), select a passage and press **what?** to mark it. Attached reorientation instructions select the same loop mode: it explains each marked passage in plain language, with an example where it helps, before any pending work continues.

After explaining active work, loop waits for `Continue` (recommended), `Adjust next action`, or `Stop`; it executes the pending action only after `Continue`. When the client's native question interface is callable, it uses localized native UI. Otherwise it immediately presents the same concise localized choices in the current mode. It never asks you to switch to Plan mode merely to answer or continue.

## Native questions

`deep-grill` and `deep-design` use the active client's native question interface for material user-owned decisions when it is callable. When it is unavailable in the current mode, unsupported by the client, or you explicitly choose prose, they immediately ask the same concise localized question instead. They preserve the pending decision and recommendation, then continue from an ordinary reply rather than waiting for a mode switch.

## Specification and design

`deep-design` owns the complete specification and design process. Superpowers supplies daily TDD, debugging, review, and verification methods when available, without creating a second durable plan. An active relevant OpenSpec change is the sole physical Build Contract and task state; merely having OpenSpec installed or initialized does not create one. Create or use a new change only when the user explicitly requests it or the work is durable, multi-session, cross-component, migratory, security-sensitive, architecturally consequential, or needs a maintained handoff record.

The active child calls domain, architecture, frontend, testing, and delivery specialists as needed; the user does not manage internal routing.

`deep-design` orchestrates the design process and produces the Build Contract. `impeccable` supplies interface design, review, and polish, feeding decisions into that same contract. `design-taste-frontend` is retired: it is no longer a default specialist, dependency, or bundled skill.

### UI design and rebuilds

`deep-design` covers new UI, partial redesigns, and complete rebuilds: confirm scope and preserved behavior, choose product/UI/both/no external research, review actual visual evidence with per-reference feedback, run visual choices through a local browser live review loop when the environment permits, settle direction, and choose whether to preview first. Existing approvals are reused; backend-only tasks skip this branch.

Use independently installed `ui-research` when available for research methods. Read the bundled React Bits references for free motion discovery, the shadcn references for shadcn/ui projects, and the relevant GSAP topics when the Build Contract selects GSAP. Reference quotas, paid pages, and client-specific modes are not extra gates. The former `rebuild-ui-design` workflow is integrated. `impeccable` supplies methods for new interface design and improvements; `deep-build` owns production implementation.

All decisions feed one Build Contract. `deep-build` owns real pages, browser interactions, and screenshot verification; broad rebuilds review a representative end-to-end slice before migrating the rest. Preview revisions do not count as approval, and component research does not authorize installation.

See the [UI workflow](skills/deep-design/references/ui-design-workflow.md) and [visual evidence](skills/deep-design/references/visual-evidence.md) methods.

## The complete loop contract

This excerpt stays in exact sync with [`skills/loop/SKILL.md`](./skills/loop/SKILL.md):

<!-- loop-skill-body:start -->
> # Loop
>
> ## Select The Mode
>
> Use **build mode** for end-to-end product work as defined below. Use **reorientation mode** for an entire trimmed `?` message, explicit `$what` or `@what` invocation, an explicit request for loop's reorientation mode, attached reorientation instructions, or a request to re-orient after not understanding the current update. An ordinary question merely containing `?` does not trigger it.
>
> Reorientation takes precedence over automatic progression, including inside an active child or a non-product workflow. Read [Reorientation and continuation](references/reorientation.md) before responding, especially for attached review feedback with `what?` annotations. Explain those passages first, pause the pending action, and wait for an explicit continuation choice. This mode neither starts a product build loop nor replaces the current workflow or its state.
>
> ## Build Mode
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
> A fresh build loop starts when the user invokes `loop` for product progression or wants a product idea, feature, app, or tool built end to end across more than one stage. Single-stage requests and small fixes stay with the matching child or ordinary work. After that, treat every ordinary reply as a continuation of the same loop until the goal is achieved, the user stops, the user clearly changes tasks, or further work requires authority outside the original request. A reorientation trigger pauses this progression until the user explicitly resumes it. The user does not need to name `loop` or any child again.
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
> - Honor a direct invocation of a child skill. Direct use does not require `loop`, but it also does not activate the persistent loop unless the user invokes `loop` or asks for end-to-end work as defined above.
>
> The active child selects any domain, architecture, research, interface, visual-design, testing, deployment, or other specialist it needs. The user does not manage internal routing.
>
> ## Preserve One Source Of State
>
> Carry the goal, current child, confirmed artifacts, constraints, authority, and evidence through the conversation and artifact references. For sustained work, use the active client's native goal or plan mechanism when available. Do not create duplicate workflow state, custom gates, hooks, or background processes.
>
> ## Set The Native Goal
>
> When a build loop starts, register its requested endpoint as the client's native goal without asking, and state the goal in one line. The goal holds the endpoint, never the child route or artifact state. In OpenCode, set it on the current session from the shell:
>
> ```sh
> opencode api post "/api/session/$OPENCODE_SESSION_ID/command" -d '{"name":"goal","text":"<objective>","delivery":"steer"}'
> ```
>
> Write the objective in the user's language, under 4000 characters: the endpoint, the project, authority limits (for example no deploy or publish), and observable done-when evidence. The same call with `text` set to `pause`, `resume`, or `clear` controls the goal; an empty `text` returns its status inside a `CommandExecutionError`, which is a status report rather than a session failure. OpenCode's reviewer judges completion from visible evidence after each turn and keeps the session going until then, so show verification output.
>
> - Check status first and skip setting a goal when one is already active for this endpoint. Single-stage work and reorientation mode set no goal.
> - Ask user decisions through the native question tool inside the turn. Ending a turn to wait for a prose answer lets the reviewer pause the goal as blocked; when the user's next ordinary reply continues the loop, resume it.
> - Pause the goal before a reorientation explanation and resume it only when the user chooses Continue.
> - Clear the goal when the user stops, changes tasks, or changes the endpoint; set a new one if the new endpoint still spans stages.
>
> Never imitate a child contract inside `loop`. Delegate the work, accept its artifact only when its readiness rules are met, and reroute from evidence. Stop when the requested endpoint is complete, the user stops or changes tasks, progress requires new authority, or remaining work has diminishing returns.
<!-- loop-skill-body:end -->

## Raycast

Import [`skills/loop/assets/raycast-snippets.json`](./skills/loop/assets/raycast-snippets.json) to use `loop ;lp`, `deep grill ;dg`, `deep design ;dd`, `deep build ;db`, and `loop reorient ;wt`. The bundle-refresh command below updates installed skills and this JSON file, not entries already imported into Raycast; update those five entries in place, replacing the former standalone reorientation entry to avoid duplicates.

## Update

Installed copies are snapshots: refresh the bundle to pick up changes to the skills, bundled references, and vendored `impeccable`:

```bash
# After each release, refresh the whole bundle
npx skills@latest add nxxxsooo/loop --skill '*' -g -y
```

`update loop` follows only the existing lock record for `loop`; it does not refresh sibling bundle skills. Use the bundle `add` command after every release instead. It does not remove old entries: after confirming the replacement references are present, remove old standalone `gsap-*`, `react-bits`, and `shadcn` entries if you no longer want to expose them. Reorientation now lives in `loop`; the old standalone `what` entry can also be removed.

Reload the client or start a fresh task when it has cached skill metadata.

## Maintenance and independent releases

The sole maintained DG source is [`skills/deep-grill/`](./skills/deep-grill/), including its standalone READMEs, images, and checker. The standalone repository is a distribution entry point, no longer an upstream source for loop. See the [maintenance guide](./docs/standalone-deep-grill.md) for exports and independent releases. Updating DG does not require a loop release; installed snapshots still need refreshing from their chosen source. Avoid mixing both installation sources for the same skill.

## License

Loop uses the [MIT License](./LICENSE). `deep-grill` carries its own MIT license. The GSAP and shadcn references retain their upstream MIT terms; `impeccable` ships under Apache-2.0 with its upstream `NOTICE.md`. See [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md).
