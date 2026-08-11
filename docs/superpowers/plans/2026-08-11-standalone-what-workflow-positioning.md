# Standalone `what` and Workflow Positioning Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore `what` as a standalone fifth bundle skill, make a bare `?` explain and then prompt continuation in any active workflow, and make unavailable native question UI fall back automatically instead of asking for Plan mode.

**Architecture:** `what` becomes a small control-plane skill that reads the active workflow frontier but never owns its durable state. `loop` retains only the explicit Product Brief-to-verified-result lifecycle, while `deep-grill`, `deep-design`, and `deep-build` provide automatic question fallback, selective OpenSpec ownership, and Superpowers-compatible execution methods.

**Tech Stack:** Markdown Skills, YAML metadata, Python standard-library validator, JSON Raycast snippets, Git, and the shared `~/.agents/skills/` runtime snapshot.

## Global Constraints

- Keep the current in-scope working-tree edits for Codex question behavior and `design-taste-frontend`; compose with them instead of reverting them.
- A message invokes `what` implicitly only when its entire trimmed text is `?`; ordinary questions containing `?` must remain ordinary questions.
- `$what` works from any workflow. It explains the active frontier, then explicitly asks the user to continue, adjust the next action, or stop. `Continue` is the recommended option.
- Do not ask the user to switch to Plan mode merely to use `request_user_input`. Use native UI when callable and concise localized prose otherwise.
- An existing relevant OpenSpec change is the sole durable task state. Repository initialization alone never requires a new OpenSpec change.
- Do not vendor Superpowers or `design-taste-frontend`; the bundle must work when those external skills are unavailable.
- The currently published `v3.0.2` bundle has four skills and no `what`. Treat the source tree as the next release; do not claim that an already-published `npx skills@latest` install contains `what`.
- Keep every `SKILL.md` lean, under 200 lines where practical, and maintain frontmatter names that match their directory names.
- Edit source files with `apply_patch`. Synchronize installed copies only after repository validation passes.

## File Structure

| Path | Responsibility |
|---|---|
| `skills/what/SKILL.md` | Cross-workflow explain-and-continue protocol and exact trigger boundary. |
| `skills/what/agents/openai.yaml` | Discoverable metadata, explicit default prompt, and exact-`?` implicit exposure. |
| `skills/what/LICENSE` | Bundle MIT license copy. |
| `skills/loop/SKILL.md` and `agents/openai.yaml` | Explicit product lifecycle only; no duplicated `?` checkpoint. |
| `skills/deep-grill/SKILL.md` and `skills/deep-design/SKILL.md` | Native-question-first behavior with automatic prose fallback. |
| `skills/deep-design/SKILL.md` and `skills/deep-build/SKILL.md` | Selective OpenSpec ownership and Superpowers-compatible execution methods. |
| `scripts/check-bundle.py` | Five-skill structural and behavior-contract regression checks. |
| `skills/loop/assets/raycast-snippets.json` | Exact bodies for five Raycast snippets, including `what ;wt`. |
| `README.md`, `README.en.md` | Chinese and English installation, routing, and lifecycle guidance. |
| `/Users/mingjian/Documents/sync/Vault/Notes/manual/what-workflow.md` | Short human-facing manual for the independent `what` skill. |
| `/Users/mingjian/Documents/sync/Vault/Notes/manual/loop-workflow.md` | Updated role map, Raycast map, and relationship to `what`. |
| `/Users/mingjian/Documents/sync/Vault/Notes/manual/deep-grill-workflow.md` | Updated no-mode-switch decision fallback. |

---

### Task 1: Add `what` and make the bundle validator test its contract

**Files:**
- Create: `skills/what/SKILL.md`
- Create: `skills/what/agents/openai.yaml`
- Create: `skills/what/LICENSE`
- Modify: `scripts/check-bundle.py`

**Interfaces:**
- Consumes: Active conversation/workflow state, nearest `CONTEXT.md` when present, and `request_user_input` availability.
- Produces: A compact explanation followed by `Continue` (recommended), `Adjust next action`, or `Stop`.

- [ ] **Step 1: Record the current validator baseline**

Run:

```bash
python3 scripts/check-bundle.py
```

Expected: the current four-skill bundle passes before the new contract is introduced.

- [ ] **Step 2: Write the failing five-skill validator expectations**

In `scripts/check-bundle.py`, replace the shared implicit-policy assertion with per-skill expectations and add `what` to both expected registries:

```python
EXPECTED = {"loop", "deep-grill", "deep-design", "deep-build", "what"}
EXPECTED_IMPLICIT_INVOCATION = {
    "loop": False,
    "deep-grill": True,
    "deep-design": True,
    "deep-build": True,
    "what": True,
}
EXPECTED_RAYCAST_SNIPPETS["what"] = {"keyword": ";wt", "skill": "what"}
```

Require `what` fragments for the exact bare-message trigger, `$what`, the five explanation fields, automatic native/prose continuation fallback, and `Continue` as recommended. Reject the retired `loop` `?` heading and trigger wording. Require the same repository `LICENSE` digest for `what` as for the local skills.

- [ ] **Step 3: Verify the red state**

Run:

```bash
python3 scripts/check-bundle.py
```

Expected: failure that reports the missing `skills/what/` package and the missing `what` Raycast snippet. Do not change unrelated validation rules to hide this failure.

- [ ] **Step 4: Create the minimal standalone `what` skill**

Add this frontmatter and triggering boundary to `skills/what/SKILL.md`:

```markdown
---
name: what
description: Use when the user sends a message consisting only of `?`, explicitly invokes `$what`, or asks to re-orient around an active task after not understanding the current update.
---
```

The body must implement this exact shape:

```markdown
# What

Temporarily hold the pending action, explain the active frontier, then prompt the user to resume work.

## Trigger And Scope

Treat only an entire trimmed `?` message and an explicit `$what` invocation as the checkpoint trigger. Do not intercept an ordinary question that merely contains `?`.

## Explain The Frontier

State the last confirmed point, current workflow and step, changed artifacts, why the state matters, and the pending next action. Preserve project terms and read the nearest `CONTEXT.md` when it exists.

## Prompt Continuation

When `request_user_input` is callable, invoke it with `Continue` (recommended), `Adjust next action`, and `Stop`. Otherwise, render the same localized choices in concise prose without requesting a mode switch. End every active-work explanation with that continuation prompt. Execute the pending action only after the user chooses `Continue`.
```

Add a no-active-work branch that says no resumable frontier exists and asks what task to orient around. Add `agents/openai.yaml` with `display_name: "What"`, short description, a `$what` default prompt, and `allow_implicit_invocation: true`. Copy the repository `LICENSE` byte-for-byte.

- [ ] **Step 5: Verify the green state for the standalone package**

Run:

```bash
python3 scripts/check-bundle.py
```

Expected: the only remaining failure, if any, concerns stale `loop` ownership or Raycast/documentation work that later tasks intentionally fix. Confirm that `skills/what/` itself has no missing-file, metadata, license, or contract failure.

- [ ] **Step 6: Commit the standalone skill slice**

Run:

```bash
git add skills/what scripts/check-bundle.py
git commit -m "feat: restore standalone what skill"
```

Expected: one focused commit; do not stage unrelated worktree files.

### Task 2: Decouple `loop` from the checkpoint protocol

**Files:**
- Modify: `skills/loop/SKILL.md`
- Modify: `skills/loop/agents/openai.yaml`
- Modify: `scripts/check-bundle.py`
- Modify: `README.md`
- Modify: `README.en.md`

**Interfaces:**
- Consumes: An explicit `$loop` invocation and artifact readiness.
- Produces: The fixed `deep-grill -> deep-design -> deep-build` lifecycle without owning a general explanation control.

- [ ] **Step 1: Make the no-duplicate-protocol assertions fail first**

Extend `scripts/check-bundle.py` so `loop` must not contain these retired fragments:

```text
Handle `?` Without Breaking Flow
When the user's entire trimmed message is exactly `?`
`request_user_input` is callable in the active mode
```

Also require `loop` metadata to set `allow_implicit_invocation: false` so it starts only when explicitly requested.

- [ ] **Step 2: Run the loop contract test in red**

Run:

```bash
python3 scripts/check-bundle.py
```

Expected: failure identifying the existing checkpoint section and implicit `loop` policy.

- [ ] **Step 3: Remove checkpoint ownership from `loop`**

Update `skills/loop/SKILL.md` so its description and body cover only the three artifact contracts, active-session continuation, artifact-readiness routing, and one source of state. Remove the whole `## Handle ? Without Breaking Flow` section. Do not copy `what` instructions into `loop`.

Set `skills/loop/agents/openai.yaml` to this policy:

```yaml
policy:
  allow_implicit_invocation: false
```

Shorten its default prompt to the explicit lifecycle request and remove `?`, `request_user_input`, and continuation-UI wording.

- [ ] **Step 4: Keep README excerpts byte-equivalent to the shortened loop body**

Update only the content between each `loop-skill-body` marker pair in `README.md` and `README.en.md` using the final `skills/loop/SKILL.md` body. Preserve the blockquote format required by `scripts/check-readme-sync.py`.

- [ ] **Step 5: Verify loop no longer owns `?`**

Run:

```bash
python3 scripts/check-bundle.py
python3 scripts/check-readme-sync.py
```

Expected: no failure says that `loop` owns, triggers, or explains a bare `?`; both README excerpts exactly match the final body.

- [ ] **Step 6: Commit the lifecycle-only loop slice**

Run:

```bash
git add skills/loop scripts/check-bundle.py README.md README.en.md
git commit -m "refactor: keep checkpoint control outside loop"
```

Expected: lifecycle removal is reviewable independently from child-rule changes.

### Task 3: Make question fallback automatic and clarify OpenSpec/Superpowers ownership

**Files:**
- Modify: `skills/deep-grill/SKILL.md`
- Modify: `skills/deep-design/SKILL.md`
- Modify: `skills/deep-build/SKILL.md`
- Modify: `scripts/check-bundle.py`

**Interfaces:**
- Consumes: Native `request_user_input` availability, active product/design decision state, and any relevant active OpenSpec change.
- Produces: Native questions when callable, prose questions otherwise; one durable implementation state; focused Superpowers execution methods when available.

- [ ] **Step 1: Add regression checks for the reported Codex failure**

Require both `deep-grill` and `deep-design` to contain automatic fallback wording and reject these phrases:

```text
ask the user to switch
switch to Plan mode
wait with the pending frontier intact
```

Require `deep-design` to state that an active relevant OpenSpec change is the Build Contract and that project initialization alone is not a creation trigger. Require `deep-build` to state that OpenSpec remains the sole task state and focused Superpowers methods do not create a parallel plan.

- [ ] **Step 2: Verify the red state**

Run:

```bash
python3 scripts/check-bundle.py
```

Expected: failures identify the current mode-switch waits and old OpenSpec wording before those instructions are edited.

- [ ] **Step 3: Replace child mode-switch waits with automatic fallback**

In both `deep-grill` and `deep-design`, use this decision rule:

```markdown
- If `request_user_input` is callable now, use it for the pending material decision.
- If it is unavailable in the current mode, present the same localized concise prose question now. Preserve the pending branch or design decision, recommend the same option, and continue from the ordinary reply.
```

Remove every instruction that asks the user to change modes to unlock the UI. Keep the rule that a successful native call is not duplicated in Markdown.

- [ ] **Step 4: Make OpenSpec a selected ledger, not an initialization side effect**

Replace the `deep-design` OpenSpec section with a conditional contract:

```markdown
If a relevant OpenSpec change is already active, continue its official workflow and treat its artifacts as the sole physical Build Contract. Do not open a second plan.

If no relevant change is active, do not create one merely because OpenSpec is installed or initialized. Create a new change only when the user explicitly requests it or the work is durable, multi-session, cross-component, migratory, security-sensitive, architecturally consequential, or needs a maintained handoff record.
```

In `deep-build`, preserve an active OpenSpec change as the only task state. Add one sentence that Superpowers TDD, debugging, review, and verification skills may be used as focused implementation methods when available, but they must not create a duplicate plan or replace OpenSpec task state.

- [ ] **Step 5: Verify automatic fallback and durable-state boundaries**

Run:

```bash
python3 scripts/check-bundle.py
rg -n "switch to Plan mode|ask the user to switch|mode-gated" skills/deep-grill/SKILL.md skills/deep-design/SKILL.md
```

Expected: the validator passes; the `rg` command returns no mode-switch instruction in the two child skills.

- [ ] **Step 6: Commit the child-contract slice**

Run:

```bash
git add skills/deep-grill/SKILL.md skills/deep-design/SKILL.md skills/deep-build/SKILL.md scripts/check-bundle.py
git commit -m "fix: fall back when native questions are unavailable"
```

Expected: the original failed-question behavior and OpenSpec role changes remain together in one focused commit.

### Task 4: Update Raycast, bilingual documentation, and user manuals

**Files:**
- Modify: `skills/loop/assets/raycast-snippets.json`
- Modify: `README.md`
- Modify: `README.en.md`
- Create: `/Users/mingjian/Documents/sync/Vault/Notes/manual/what-workflow.md`
- Modify: `/Users/mingjian/Documents/sync/Vault/Notes/manual/loop-workflow.md`
- Modify: `/Users/mingjian/Documents/sync/Vault/Notes/manual/deep-grill-workflow.md`

**Interfaces:**
- Consumes: Final bodies of the five bundled skills and the selected collaboration model.
- Produces: Correct install/update guidance and Raycast expansion for `what ;wt` without drifting from source skill bodies.

- [ ] **Step 1: Write the failing snippet expectation**

Run the bundle checker after adding `what` to `EXPECTED_RAYCAST_SNIPPETS` but before inserting its JSON entry.

```bash
python3 scripts/check-bundle.py
```

Expected: it identifies that the Raycast JSON has four entries or lacks `what ;wt`.

- [ ] **Step 2: Synchronize Raycast bodies exactly**

Update the `loop` JSON `text` to the final `loop` skill body with no `?` section. Add:

```json
{
  "name": "what",
  "keyword": ";wt",
  "text": "<exact body of skills/what/SKILL.md, excluding frontmatter>"
}
```

Keep the other three bodies byte-for-byte equivalent to their source skills. Do not change existing Raycast keywords `;lp`, `;dg`, `;dd`, or `;db`.

- [ ] **Step 3: Reposition the bilingual README guidance**

In both README files:

- Replace the claim that `loop` is the only normal entry point with the approved roles: Superpowers is the default execution system when available; `loop` is the explicit fixed product lifecycle; `what` is a cross-workflow explanation-and-continue control; OpenSpec is a selective durable ledger.
- Expand the skill table to five skills and move `?` ownership from `loop` to `what`.
- State that `?` and `$what` explain the frontier and then prompt `Continue` (recommended), `Adjust next action`, or `Stop`.
- State that native question UI is used when callable and concise prose is automatic otherwise; remove all Plan-mode-switch instructions.
- Preserve the existing Taste Skill installation, specialist boundaries, and license attribution.
- Add `what` to the explicit update command only in the next-release guidance. State that current published `v3.0.2` users must wait for that release or synchronize from the checked-out source; do not present the command as a fix for a package that has not been published.
- Add `;wt` to the Raycast list and state that an already imported Raycast library needs a manual update after the next release or local source synchronization.
- Keep the embedded loop-body excerpt synchronized through `scripts/check-readme-sync.py`.

- [ ] **Step 4: Write concise user manuals**

Create `what-workflow.md` with frontmatter, a one-line purpose, a short use/avoid decision table, examples for `?` and `$what`, the three continuation outcomes, and the relationship to Superpowers, `loop`, and OpenSpec.

Update `loop-workflow.md` to describe `loop` as an explicit lifecycle rather than the default entry point, list five Raycast mappings, and route the checkpoint protocol to `what`. Update `deep-grill-workflow.md` so an unavailable native UI produces concise prose immediately, not a Plan-mode request. Preserve the existing Taste and source links unless the changed role text requires an update.

- [ ] **Step 5: Verify documentation and snippet parity**

Run:

```bash
python3 scripts/check-bundle.py
python3 scripts/check-readme-sync.py
python3 -m json.tool skills/loop/assets/raycast-snippets.json
```

Expected: all checks pass, the JSON parses, five expected snippets exist, and both languages describe the same routing model.

- [ ] **Step 6: Commit the user-facing documentation slice**

Run:

```bash
git add README.md README.en.md skills/loop/assets/raycast-snippets.json
git commit -m "docs: explain what and workflow roles"
```

Expected: Vault manuals remain in their owning workspace; only repository files enter this commit.

### Task 5: Validate, synchronize installed copies, and audit the active runtime

**Files:**
- Synchronize: `/Users/mingjian/.agents/skills/{what,loop,deep-grill,deep-design,deep-build}/`
- Verify exposure: `/Users/mingjian/.config/opencode/skills/`

**Interfaces:**
- Consumes: Fully validated repository source.
- Produces: Matching cross-runtime skill snapshots and an audit record with no unreported errors.

- [ ] **Step 1: Run repository checks before installation**

Run:

```bash
git diff --check
python3 scripts/check-bundle.py
python3 scripts/check-readme-sync.py
```

Expected: no whitespace errors, no bundle contract failures, and no README-body drift.

- [ ] **Step 2: Synchronize only the five scoped installed skills**

Copy the complete validated `skills/what` directory into `/Users/mingjian/.agents/skills/`. Copy the modified `SKILL.md`, metadata, license, and Raycast asset from the four existing scoped skill directories without deleting unrelated installed skills or directories.

- [ ] **Step 3: Compare source and installed entry files**

Run one comparison for each scoped entry point:

```bash
cmp skills/what/SKILL.md /Users/mingjian/.agents/skills/what/SKILL.md
cmp skills/loop/SKILL.md /Users/mingjian/.agents/skills/loop/SKILL.md
cmp skills/deep-grill/SKILL.md /Users/mingjian/.agents/skills/deep-grill/SKILL.md
cmp skills/deep-design/SKILL.md /Users/mingjian/.agents/skills/deep-design/SKILL.md
cmp skills/deep-build/SKILL.md /Users/mingjian/.agents/skills/deep-build/SKILL.md
```

Expected: every command exits `0`. Also confirm the OpenCode skill exposure resolves under `/Users/mingjian/.agents/skills/` without replacing working symlinks.

- [ ] **Step 4: Run the shared skill audit**

Run:

```bash
/Users/mingjian/.agents/skills/mj-maintenance/scripts/oscripts/audit-skills.sh
```

Expected: report every hard error or warning. Fix only errors attributable to these five skills; leave unrelated audit findings visible and untouched.

- [ ] **Step 5: Perform final scope and behavior review**

Run:

```bash
git status --short
git diff --check HEAD
```

Manually review these scenarios against the installed `SKILL.md` files:

1. A bare `?` during a Superpowers task explains the frontier and ends with a recommended continuation prompt.
2. `$what` during an active `loop` does the same without restarting the lifecycle.
3. A normal sentence containing `?` does not activate `what`.
4. A `deep-grill` decision in a mode without native question UI is asked in concise prose without a Plan-mode detour.
5. An initialized OpenSpec repository with a small one-session task does not create a change; an existing relevant change remains the sole task state.

- [ ] **Step 6: Report and restart guidance**

Report the source and manual paths, validator/audit results, any unrelated dirty state, and the need to reload the affected client or start a fresh task because skill metadata changed.
