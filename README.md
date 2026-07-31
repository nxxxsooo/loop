<p align="right"><a href="./README.zh-CN.md">中文说明</a></p>

<p align="center">
  <img src="./assets/grill-loop-hero.webp" alt="A seafoam cord finds its route through four independent graphite gates" width="100%">
</p>

<h1 align="center">grill-loop</h1>

<p align="center"><strong>The loop follows the work.</strong></p>

<p align="center">
  One explicit router. One useful capability at a time.<br>
  Follow its contract, then choose again from what changed.
</p>

<p align="center">
  <a href="#install"><img src="https://img.shields.io/badge/install-skills.sh-111820?style=flat-square" alt="Install with skills.sh"></a>
  <a href="https://github.com/nxxxsooo/grill-loop/releases"><img src="https://img.shields.io/github/v/release/nxxxsooo/grill-loop?style=flat-square&color=5eead4" alt="Latest release"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-5eead4?style=flat-square" alt="MIT License"></a>
</p>

## Install

```bash
npx skills@latest add nxxxsooo/grill-loop
```

Then continue any task with:

> Use $grill-loop to continue this task.

grill-loop runs only when you name it. It does not auto-invoke or force every connected capability to run.

## Why it exists

Real work does not follow one fixed methodology. A missing product choice may need `grilling`; a formed plan may need `deep-grill`; a durable change may belong in OpenSpec; a frontend may need a taste pass.

grill-loop owns only the routing decision. It selects the smallest useful next capability, follows that capability's own contract, carries forward the relevant context, then reassesses.

## Route by where the answer lives

| The current gap | Useful next move |
|---|---|
| Intent, priorities, risk tolerance, or taste exist only with the user | `grilling` |
| A plan or decision needs autonomous investigation and adversarial review | `deep-grill` |
| Work should enter durable exploration, specification, implementation, or archival | OpenSpec |
| A frontend or brand surface needs visual direction or critique | `design-taste-frontend` |
| Another specialist better fits the current move | That Skill or tool |

These are options, not stages. Skip, repeat, reorder, return, or stop as the work changes.

<p align="center">
  <img src="./assets/grill-loop-detail.webp" alt="A seafoam braided cord passing through a precision-machined graphite gate" width="440">
</p>

## The complete contract

The installed Skill is only four paragraphs. This excerpt is kept in exact sync with [`SKILL.md`](./SKILL.md):

<!-- grill-loop-skill-body:start -->
> # Grill Loop
>
> Follow the user's goal and the latest evidence or artifacts. Choose the smallest next useful capability, load and follow its own contract, then reassess from what changed. Briefly explain each transition; the user may choose the next capability at any time.
>
> Use `grilling` when a material answer lives only in the user's intent, priorities, risk tolerance, or taste. Use `deep-grill` when a plan or decision needs autonomous investigation and adversarial review. Use OpenSpec when the work should enter or continue durable exploration, specification, implementation, or archival. Use `design-taste-frontend` when a relevant frontend or brand surface needs visual direction or critique. Use another available skill or tool when it is a better next move.
>
> Treat these as options, not stages. Skip, repeat, reorder, or return to them freely. Load only what the current move needs. Carry forward the goal, confirmed decisions, constraints, and artifact references, but impose no shared output format and maintain no duplicate workflow state.
>
> Preserve every capability's own scope, authority, and safety boundaries. Add no custom gates, hooks, background processes, or state files. Stop when the user's goal is met, a meaningful next move requires their input or authority, or further looping has diminishing returns.
<!-- grill-loop-skill-body:end -->

## Boundaries

- No mandatory order or lifecycle.
- No shared output schema or duplicate task state.
- No custom gates, hooks, background processes, or state files.
- No authority beyond the user's request and the selected capability's contract.
- No automatic invocation.

## Update

Installed copies do not follow repository changes automatically:

```bash
npx skills@latest update grill-loop -g -y
```

Use `-p` instead of `-g` for a project-scoped installation.

## Manual installation

```bash
git clone https://github.com/nxxxsooo/grill-loop ~/.claude/skills/grill-loop
```

## License

[MIT](./LICENSE)
