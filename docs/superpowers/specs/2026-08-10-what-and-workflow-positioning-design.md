# Standalone `what` and Workflow Positioning

## Context

The bundle currently embeds the bare `?` checkpoint inside `loop`. That makes a general conversation control look like a lifecycle-specific feature. It also makes `loop` appear to be the source of replay behavior even when a task actually entered through Superpowers.

The native-question failure reported in Codex comes from the child decision rules: `deep-grill` and `deep-design` currently ask the user to switch to Plan mode when `request_user_input` is unavailable. The approved automatic fallback must therefore apply to those decision rules as well as the `what` checkpoint.

The approved direction is to restore `what` as an independent skill, keep `loop` focused on its fixed product lifecycle, use Superpowers as the default day-to-day execution system when it is available, and reserve OpenSpec for durable change state rather than every initialized OpenSpec project.

## Goals

- Make `what` available from any active workflow without taking ownership of that workflow.
- Preserve the existing explain-and-resume behavior for a bare `?`.
- Prompt the user to continue the active work immediately after the explanation.
- Keep `loop` as an explicit entry point for the full Product Brief to Build Contract lifecycle.
- Document one clear collaboration model for Superpowers, `loop`, and OpenSpec.
- Avoid duplicate plans, duplicate task state, and manual Plan-mode handoffs for checkpoints or material user decisions.

## Non-goals

- Do not make Superpowers a required runtime dependency of this bundle.
- Do not make `what` answer ordinary content questions that happen to contain a question mark.
- Do not let `what` silently execute the pending action while it is explaining the current state.
- Do not remove OpenSpec support from `deep-design` or `deep-build`.
- Do not change the internal phase sequence of `loop`.

## Architecture

### Standalone `what`

Add `skills/what/` as the fifth bundled skill, with its own `SKILL.md`, `agents/openai.yaml`, and `LICENSE`. Restore the Raycast snippet named `what` with keyword `;wt` in the bundle snippet file.

The skill has two intentional entry forms:

- A user message whose entire trimmed content is `?` implicitly invokes `what`.
- An explicit `$what` invocation invokes it from any conversation or workflow.

The skill metadata must allow implicit invocation, but its description must constrain that behavior to the exact bare-message form. A question mark inside a normal sentence must not invoke the skill.

When invoked during active work, `what` freezes the current workflow frontier before the pending action. It explains, in the user's language:

1. The last confirmed point.
2. The active workflow and current step, when known.
3. What changed, including whether files or artifacts changed.
4. Why the current point matters or why progress paused.
5. The exact next action that was pending.

It must preserve defined project terms. It reads the nearest `CONTEXT.md` when one exists and otherwise keeps the terminology already established in the conversation and artifacts.

After the explanation, `what` offers continuation control:

- `Continue` is the recommended action and resumes the previously pending work.
- `Adjust next action` changes only the next action unless the adjustment invalidates an already confirmed artifact.
- `Stop` ends or pauses the active workflow without inventing further work.

Use Codex's native choice UI when `request_user_input` is callable. Otherwise, render the same three choices as concise prose in the current mode. The fallback is automatic: never ask the user to switch to Plan mode and never claim that the native tool was used when it was unavailable. The explanation must end with an explicit prompt to continue working. Both paths wait for the user's choice before executing the pending action, so explanation and execution do not become an ambiguous single step.

If no active or recoverable workflow exists, `what` states that there is no pending frontier. It must not fabricate state or offer a misleading `Continue`; it asks the user to provide the task they want to orient around.

### Native user decisions

Apply the same automatic fallback policy to `deep-grill` and `deep-design`. Before asking a material user-owned decision, they inspect the current tool metadata:

- When `request_user_input` is callable, use the native interface.
- When it is unavailable in the current mode, ask the same decision as concise prose in the current response and continue from the user's ordinary answer.

Neither skill may ask the user to switch modes merely to unlock a question UI. The fallback must preserve the pending branch or design decision, keep the existing recommended option, and use the user's language. It does not claim that a native interface was called.

### `loop`

Remove ownership of the bare `?` protocol from `loop`, including its frontmatter, workflow section, metadata, and validation assertions. `loop` remains an explicit orchestrator for this fixed lifecycle:

`deep-grill` -> confirmed Product Brief -> `deep-design` -> confirmed Build Contract -> `deep-build` -> verified result

`what` can interrupt and resume `loop` just as it can any other workflow, but `loop` does not implement a second copy of the checkpoint contract.

Documentation should stop describing `loop` as the only normal entry point. It is the deliberate choice when the user wants the complete product lifecycle in one invocation.

### Superpowers

When installed and relevant, Superpowers is the default execution system for ordinary work. Its focused skills provide brainstorming, planning, test-driven development, debugging, review, and verification. This repository does not vendor or require the plugin; its bundled skills must still work without it.

Superpowers methods may operate inside a `loop` phase or an OpenSpec-backed change. They do not automatically create a second task ledger. In particular, when OpenSpec already owns the implementation state, use focused Superpowers implementation methods without creating a parallel implementation plan for the same work.

### OpenSpec

OpenSpec is the durable ledger for work that benefits from persistent, reviewable change artifacts. A relevant active OpenSpec change remains the sole task-state owner and its artifacts are the physical Build Contract.

The mere presence or initialization of OpenSpec in a repository does not require every new task to create an OpenSpec change. Create a new change when at least one of these conditions materially applies:

- The work will span sessions or handoffs.
- The work crosses components or has a migration path.
- The work has security, architectural, or other high-consequence decisions.
- The team needs a maintained, reviewable record after the current conversation.
- The user explicitly requests OpenSpec.

Small bugs, small features, and single-session changes can use Superpowers directly. If a relevant OpenSpec change already exists, continue it rather than opening a duplicate plan elsewhere.

## State and Control Flow

`what` is a control-plane adapter, not a state store. It reads the current conversation, workflow instructions, and durable artifacts to identify the frontier. It temporarily holds the pending action while explaining, then actively prompts the user to resume the work. It does not rewrite Product Briefs, Build Contracts, OpenSpec tasks, or Superpowers plans while explaining them.

On `Continue`, control returns to the workflow and pending step that existed before invocation. On `Adjust next action`, the active workflow evaluates only the requested adjustment and explicitly reports if the change invalidates prior approval. On `Stop`, no downstream phase starts.

## Files and Documentation

Implementation will update the following surfaces:

- Add the standalone `skills/what/` package.
- Remove the duplicated `?` contract from `skills/loop/`.
- Replace mode-switch waits in `deep-grill` and `deep-design` with automatic prose fallback while preserving native UI when callable.
- Refine OpenSpec ownership language in `deep-design` and `deep-build`.
- Update English and Chinese README positioning, installation commands, skill tables, examples, and the embedded `loop` body.
- Restore the `what` Raycast snippet and update bundle validation from four skills to five.
- Update installed-skill snapshots and the directly relevant workflow manuals after repository validation.

Existing unrelated working-tree changes must be preserved and incorporated rather than reverted.

## Error Handling and Edge Cases

- If the prior message is ambiguous, `what` reports the ambiguity instead of guessing a workflow state.
- If a workflow is waiting on a domain decision, `what` explains that decision boundary but does not answer the decision on the user's behalf.
- If native choice UI is unavailable, prose fallback occurs immediately in the same response without a mode-switch detour.
- If `deep-grill` or `deep-design` needs a material user decision while native UI is unavailable, it preserves that decision and asks it in concise prose instead of asking for Plan mode.
- If `$what` is invoked outside active work, it explains that no resumable action was found instead of replaying unrelated history.
- If an adjustment conflicts with a confirmed artifact, the owning workflow must return to the appropriate approval boundary before implementation continues.

## Verification

Verification must cover structure, documentation, behavior contracts, and installation:

- Run the skill validator against every modified or new skill.
- Run `scripts/check-bundle.py` and require zero errors and warnings.
- Verify README synchronization, skill count, metadata, licenses, and Raycast JSON parity.
- Assert that the exact bare `?` trigger belongs to `what` and no longer belongs to `loop`.
- Assert that ordinary question marks do not match the documented implicit trigger.
- Assert that unavailable native choice UI falls back without requesting a mode switch.
- Assert that `deep-grill` and `deep-design` no longer require a mode switch before asking a native-question fallback.
- Assert that OpenSpec initialization alone is not documented as a creation trigger.
- Assert that an active OpenSpec change remains the sole implementation state.
- Compare the installed `~/.agents/skills/` copies with the validated repository versions.
- Run the shared skill audit after installation.

## Success Criteria

- A bare `?` or explicit `$what` reliably explains and preserves any active workflow frontier.
- Every active-workflow explanation ends by prompting the user to continue, adjust the next action, or stop, with `Continue` recommended and no Plan-mode replay.
- Material decisions in `deep-grill` and `deep-design` use native UI when callable and automatic prose fallback otherwise.
- `loop` has one responsibility: the explicit fixed product lifecycle.
- Superpowers, `loop`, and OpenSpec have complementary roles and do not create duplicate task state.
- The bundle installs and validates as five skills with no documentation or snippet drift.
