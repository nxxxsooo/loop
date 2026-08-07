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

Ask the user only for material decisions involving goals, priorities, risk tolerance, taste, or authority. Use the active client's native question interface when callable. If the interface is supported but gated behind another mode, preserve the pending decision, name the required mode when the client identifies it, ask the user to switch and continue, then wait. Use concise prose only when no native question interface exists or the user explicitly chooses prose.

## Use OpenSpec As An Adapter

Inspect the target project for its OpenSpec configuration and instructions. Use the official installed OpenSpec workflow and CLI when the project already uses it, or when the change is durable, multi-session, cross-component, high-consequence, or benefits materially from a maintained change record. Never fabricate OpenSpec setup or schema.

When OpenSpec is used, its proposal, specs, design, and tasks are the physical Build Contract. Keep them internally consistent and use their official validation flow. For a small, low-risk, single-session change, the Build Contract may instead live in the current task or the client's native plan. OpenSpec and compact contracts have the same semantic readiness requirements.

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
