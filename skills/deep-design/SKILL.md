---
name: deep-design
description: Turn confirmed product intent into an implementation-ready Build Contract. Use for behavior, interfaces, architecture, new UI, partial or complete UI rebuilds, reference research, visual direction, and preview decisions. Continue across ordinary replies until the contract is confirmed; production implementation belongs to deep-build.
---

# Deep Design

Design the implementation contract, not the production implementation. Start from a confirmed Product Brief and finish with a confirmed Build Contract that another agent can execute without inventing material product or design decisions. Isolated visual previews may supply design evidence when requested and permitted by the environment; they are not production edits.

## Verify The Input

Locate the Product Brief and the target project's sources of truth. Confirm that the brief states the target user, desired outcome, constraints, non-goals, decisions, success scenarios, and material assumptions. Inspect the existing system before proposing changes.

The brief can be confirmed in conversation; do not require a separate document or repeat settled questions just to satisfy a template. For an existing UI, distinguish required behavior from replaceable presentation. For new UI, use confirmed tasks and states rather than inventing a legacy baseline.

If root product intent is missing or contradicted, return the specific gap to `deep-grill`. Do not hide a product decision inside architecture, interface, or task design.

## Resolve The Design

Trace desired behavior through the relevant system boundaries. Resolve only what the change needs: public behavior, data and state, interfaces, errors, migration and compatibility, accessibility, security, observability, rollout, and rollback. Preserve existing project patterns unless the Product Brief requires changing them.

Use domain, architecture, research, frontend, prototype, visual-design, or other specialists only for a material unresolved design question. Feed their accepted decisions back into the Build Contract. They do not own progression or create parallel workflow state.

When UI structure, visual direction, or interaction design is material, use the conditional UI branch below. Backend-only work skips it. For landing pages, portfolios, or editorial interfaces, `design-taste-frontend` remains the default aesthetic specialist when available; dashboards, tables, and multi-step product UI need task-appropriate methods. Specialists inform this contract rather than starting another lifecycle or implementing production UI.

Ask the user only for material decisions involving goals, priorities, risk tolerance, taste, or authority. Honor an explicit user preference for prose first. Otherwise use the active client's callable native question interface: `request_user_input` in Codex or its available equivalent in another client. If no native question interface is callable now, immediately ask the same localized concise prose question. Preserve the pending branch or design decision, recommend the same option, and continue from the ordinary reply. Do not repeat a successful native question call in Markdown.

Do not require a particular client's planning mode solely to ask a question. Respect actual read/write restrictions; request narrowly scoped artifact permission only when needed. Reuse prior approvals and reopen only the decision invalidated by new evidence. This question precedence also governs reference, preview, and contract approval.

## UI Design Branch

Read [UI design workflow](references/ui-design-workflow.md) for new interfaces or partial/full rebuilds, and [visual evidence](references/visual-evidence.md) when presenting researched references or a preview. For visual choices or mockup approval, use the live visual review loop in visual evidence when the environment can keep its server running. These methods are integrated here; do not invoke the retired `rebuild-ui-design` skill.

For approved motion research, consult [motion reference sources](references/motion-references.md): MotionSites AI, 21st, React Bits, and Godly / Recent, with source roles and access notes.

When used as a standalone pasted prompt, resolve references from the installed `deep-design` directory or the repository's `skills/deep-design/`. If neither is accessible, use this minimum contract and state the evidence gap rather than inventing a reference file:

1. Inspect tasks, affected states, technical contracts, and shared consumers. Confirm the change boundary and supported viewports. A bounded page/component can combine scope and direction approval; a full rebuild requires scope approval and a representative workflow before wider migration.
2. Reuse or ask the research choice: product behavior, UI appearance, both, or no external research. `ui-research`, when available, supplies search and analysis methods only within that choice. No fixed reference quota or mandatory search overrides an explicit opt-out.
3. Use actual readable images with source IDs and adopt/avoid notes for newly researched visual candidates. Provide per-reference selection/comments with saved drafts and exportable feedback; links or invented mockups are not source evidence. Inspect motion live or label recordings and unverified candidates. A missing capture blocks that candidate's visual approval, not unrelated work.
4. Resolve one coherent direction for layout, hierarchy, density, typography, components and relevant states. Use `react-bits` for free motion/component discovery only when it addresses the design question; verify official source/variant/dependencies and record fallbacks. Do not install into the product during design.
5. Ask whether to preview first or proceed to implementation after contract approval. A requested isolated preview needs explicit approval; revision feedback leaves it pending. Existing explicit choices are reused.
6. Put direction, evidence links, preview status, behavior checklist, target routes/states/viewports, motion constraints and rollout milestones into the same Build Contract. For broad redesigns, require review of the first implemented core workflow before remaining-page migration. `deep-build` owns production changes, browser interactions and actual implementation screenshots.

Use available search/browser tools directly if a specialist is absent. Stop dependent work for unavailable evidence, not for a missing optional skill. Keep the user's domain content and realistic information density central to the design.

## Use OpenSpec As An Adapter

Inspect the target project for its OpenSpec configuration and instructions. Never fabricate OpenSpec setup or schema.

If a relevant OpenSpec change is already active, continue its official workflow and treat its artifacts as the sole physical Build Contract. Do not open a second plan.

If no relevant change is active, do not create one merely because OpenSpec is installed or initialized. Create a new change only when the user explicitly requests it or the work is durable, multi-session, cross-component, migratory, security-sensitive, architecturally consequential, or needs a maintained handoff record.

## Produce The Build Contract

Record the applicable fields:

```text
Project and sources of truth:
Desired behavior:
Must preserve:
Non-goals:
Interfaces, data, state, and errors:
Accessibility and security:
UI scope, approved direction, evidence, and preview status (when applicable):
Motion/component choices, target viewports, and staged review (when applicable):
Must-pass scenarios:
Implementation slices and tasks:
Verification and release plan:
Residual risks:
```

Make tasks vertically executable, dependency-aware, and traceable to the desired behavior and must-pass scenarios. Distinguish assumptions from confirmed facts. Include enough detail to reveal material omissions, not speculative detail that implementation can decide safely.

Present the completed Build Contract for confirmation through the same native-question rules. It is ready for `deep-build` only when no material behavior, interface, task, verification, release, or authority question remains open, including approval of any requested preview. Do not implement production changes. Record a future representative-slice review as a known execution milestone, not an unresolved design decision.
