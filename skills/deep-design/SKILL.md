---
name: deep-design
description: >-
  Turn a confirmed Product Brief into a confirmed, implementation-ready Build
  Contract. Use when product intent is settled but behavior, interfaces, tasks,
  verification, or release design remains unresolved. Continue an active design
  session across ordinary user replies without requiring another invocation.
---

# Deep Design

Design the implementation contract, not the implementation. Start from a confirmed Product Brief and finish with a confirmed Build Contract that another agent can execute without inventing material product or design decisions.

## Verify The Input

Locate the Product Brief and the target project's sources of truth. Confirm that the brief states the target user, desired outcome, constraints, non-goals, decisions, success scenarios, and material assumptions. Inspect the existing system before proposing changes.

If root product intent is missing or contradicted, return the specific gap to `deep-grill`. Do not hide a product decision inside architecture, interface, or task design.

## Resolve The Design

Trace desired behavior through the relevant system boundaries. Resolve only what the change needs: public behavior, data and state, interfaces, errors, migration and compatibility, accessibility, security, observability, rollout, and rollback. Preserve existing project patterns unless the Product Brief requires changing them.

Use domain, architecture, research, frontend, prototype, visual-design, or other specialists only for a material unresolved design question. Feed their accepted decisions back into the Build Contract. They do not own progression or create parallel workflow state.

When `design-taste-frontend` is available and the material question concerns a landing page, portfolio, editorial page, or visual redesign, load it as the default visual-design specialist. During `deep-design`, use it to resolve and record visual direction, not to implement. It does not apply to dashboards, data tables, or multi-step product UI; choose a specialist suited to those interfaces.

Ask the user only for material decisions involving goals, priorities, risk tolerance, taste, or authority. If `request_user_input` is callable now, use it for the pending material decision. If it is unavailable in the current mode, present the same localized concise prose question now. Preserve the pending branch or design decision, recommend the same option, and continue from the ordinary reply. Use concise prose only when the active client has no native question interface or the user explicitly chooses prose. Do not repeat a successful native question call in Markdown.

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
Must-pass scenarios:
Implementation slices and tasks:
Verification and release plan:
Residual risks:
```

Make tasks vertically executable, dependency-aware, and traceable to the desired behavior and must-pass scenarios. Distinguish assumptions from confirmed facts. Include enough detail to reveal material omissions, not speculative detail that implementation can decide safely.

Present the completed Build Contract for confirmation through the same native-question rules. It is ready for `deep-build` only when no material behavior, interface, task, verification, release, or authority question remains open. Do not implement.
