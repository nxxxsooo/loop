<p align="right"><a href="./README.md">中文说明</a></p>

<p align="center">
  <img src="./assets/grill-loop-social-poster.png" alt="grill-loop — the loop follows the work" width="100%">
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

One install includes `grill-loop`, `grilling`, and `deep-grill`:

```bash
npx skills@latest add nxxxsooo/grill-loop --skill '*' -g -y
```

| Skill | Purpose | Source |
|---|---|---|
| `grill-loop` | Choose the next capability from the current goal and artifacts | This repository |
| `grilling` | Interview user-owned decisions one question at a time | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) |
| `deep-grill` | Investigate, challenge, and revise plans autonomously | [nxxxsooo/deep-grill](https://github.com/nxxxsooo/deep-grill) |

OpenSpec, Open Design, taste, and other specialists remain optional integrations supplied by the current environment.

When grill-loop selects OpenSpec, it checks whether the target project is initialized for the active client. Missing setup is generated only through `openspec init <project-root> --tools <active-client>`; the router does not fabricate OpenSpec files. The CLI remains an environmental prerequisite, and its reload or restart instruction applies before the generated entry point is used.

Here `--skill '*'` installs all three skills in this repository. `--all` would also target every supported agent, which is a different operation.

Then continue any task with:

> Use $grill-loop to continue this task.

grill-loop runs only when you name it. It does not auto-invoke or force every connected capability to run.

### Optional: Raycast snippets

Raycast users can import [the bundled snippets](./skills/grill-loop/assets/raycast-snippets.json) with Raycast's **Import Snippets** command:

| Skill | Keyword |
|---|---|
| `grilling` | `;gr` |
| `deep-grill` | `;dg` |
| `grill-loop` | `;lp` |

The snippets paste the full prompts into any text field. Importing is opt-in; installing the skills never modifies a user's Raycast data. Raycast skips duplicates during import as described in its [official import documentation](https://manual.raycast.com/import-export).

## Why it exists

Real work does not follow one fixed methodology. A missing product choice may need `grilling`; a formed plan may need `deep-grill`; a durable change may belong in OpenSpec; an apply-ready interface may still need an Open Design prototype and a taste pass.

grill-loop owns only the routing decision. It selects the smallest useful next capability, follows that capability's own contract, carries forward the relevant context, then reassesses.

## Route by where the answer lives

| The current gap | Useful next move |
|---|---|
| Intent, priorities, risk tolerance, or taste exist only with the user | `grilling` |
| A plan or decision needs autonomous investigation and adversarial review | `deep-grill` |
| Work should enter durable exploration, specification, implementation, or archival | OpenSpec |
| The spec is implementable, but interface structure or visual direction remains unresolved | Open Design or another prototyping capability |
| A reviewable frontend or brand prototype needs visual direction or critique | `design-taste-frontend` or the relevant design specialist |
| Another specialist better fits the current move | That Skill or tool |

These are options, not stages. Skip, repeat, reorder, return, or stop as the work changes.

An OpenSpec message saying “ready for `/opsx-apply`” is new evidence, not the Loop's terminal decision. If implementation still depends on unresolved interface design, give the spec to Open Design for a reviewable prototype, then route it through taste or another design specialist as their scope fits. Carry accepted structure, state, and visual decisions back into the OpenSpec design and tasks, confirm apply-readiness again, then implement. Backend-only changes, resolved designs, and work without a material design surface skip this branch.

When continued work would benefit from a persistent goal, grill-loop naturally proposes a compact, adaptable goal card in the current transition:

```text
Goal:
Project / sources of truth:
Boundaries (may change / must preserve):
Done when:
Must-pass real scenarios:
```

Fields that do not materially apply may be omitted. After the user agrees to the card, grill-loop uses the current client's native goal mechanism and keeps choosing the next useful capability until the goal is met. It pauses only when progress needs new user input or authority, and keeps no goal state of its own. Otherwise, it stops when the request is fulfilled or further looping has diminishing returns.

<p align="center">
  <img src="./assets/grill-loop-detail.webp" alt="A seafoam braided cord passing through a precision-machined graphite gate" width="440">
</p>

## The complete contract

The router itself is only four paragraphs. This excerpt is kept in exact sync with [`skills/grill-loop/SKILL.md`](./skills/grill-loop/SKILL.md):

<!-- grill-loop-skill-body:start -->
> # Grill Loop
>
> Follow the user's goal and the latest evidence or artifacts. Choose the smallest next useful capability, load and follow its own contract, then reassess from what changed. Treat a capability's suggested next command as evidence, not as the loop's decision; reassess before relaying or acting on it. Briefly explain each transition; the user may choose the next capability at any time.
>
> Use `grilling` when a material answer lives only in the user's intent, priorities, risk tolerance, or taste. Use `deep-grill` when a plan or decision needs autonomous investigation and adversarial review. Use OpenSpec when the work should enter or continue durable exploration, specification, implementation, or archival. Before the first OpenSpec move, resolve the intended project root and verify both its OpenSpec project state and active-client integration. If either is missing, initialize or add the client only through `openspec init <project-root> --tools <active-client>`; name all intended clients in the comma-separated `--tools` value when appropriate. Never hand-create or copy generated OpenSpec commands, skills, or bootstrap state. Follow the CLI's reload or restart instruction before invoking the generated entry point. If the CLI is unavailable, explain the prerequisite and request installation authority instead of simulating OpenSpec. When an apply-ready change still has unresolved user-facing design, use Open Design or another prototyping capability to make it reviewable, then use `design-taste-frontend` where its scope fits or another design specialist. Feed accepted decisions back into the OpenSpec design and tasks before implementation; skip this route when no material design decision remains. Use another available skill or tool when it is a better next move.
>
> Treat these as options, not stages. Skip, repeat, reorder, or return to them freely. Load only what the current move needs. Carry forward the goal, confirmed decisions, constraints, and artifact references, but impose no shared output format and maintain no duplicate workflow state.
>
> Preserve every capability's scope, authority, and safety boundaries. Add no custom gates, hooks, background processes, or state files. When sustained work needs a goal, propose this adaptable card in the current transition: `Goal`, `Project / sources of truth`, `Boundaries (may change / must preserve)`, `Done when`, and `Must-pass real scenarios`; omit irrelevant fields. After user approval, register it with the active client's native goal mechanism when available and keep routing until it is met; pause only for new user input or authority. Keep no goal state of your own. Otherwise, stop when the request is fulfilled or returns diminish.
<!-- grill-loop-skill-body:end -->

## Boundaries

- No mandatory order or lifecycle.
- No shared output schema or duplicate task state.
- No custom gates, hooks, background processes, or state files.
- After the user accepts a proposed goal, native clients may persist it; grill-loop never duplicates that goal state.
- No authority beyond the user's request and the selected capability's contract.
- No automatic invocation.

## Update

Installed copies do not follow repository changes automatically:

If the existing copy came from `v1.2.0` or an earlier single-skill layout, its lock still points to the repository-root `SKILL.md`. Rebind the source once when migrating to the three-skill bundle:

```bash
npx skills@latest add nxxxsooo/grill-loop --skill '*' -g -y
```

After migration, use the normal update command:

```bash
npx skills@latest update grill-loop grilling deep-grill -g -y
```

Use `-p` instead of `-g` for a project-scoped installation.

## License

This repository and `deep-grill` use the [MIT License](./LICENSE). The bundled `grilling` skill retains Matt Pocock's MIT license and source attribution; see [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md).
