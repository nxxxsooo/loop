---
name: deep-build
description: >-
  Implement a confirmed Build Contract through small verified slices and
  deliver the authorized result. Use when behavior, interfaces, tasks, and
  must-pass scenarios are settled and implementation authority is clear.
  Continue across ordinary replies until delivery or a contract gap requires
  deep-design.
---

# Deep Build

Turn a confirmed Build Contract into a verified result. Require both an implementation-ready contract and authority to change the scoped system. Do not infer deployment, publication, destructive migration, or external communication authority from implementation authority alone.

## Establish The Execution Path

Read the target project's instructions, current state, and Build Contract. Check that tasks trace to desired behavior and must-pass scenarios. If the contract is represented by OpenSpec artifacts, use the official installed OpenSpec apply workflow and keep task state there. Otherwise, use the active client's native plan or goal mechanism when useful; do not create duplicate workflow state.

Return to `deep-design` before editing when a material behavior, interface, data, migration, verification, release, or authority decision is missing or contradicted. Return to `deep-grill` when evidence invalidates root product intent. Small implementation details that do not alter the contract remain implementation decisions.

## Build In Verified Slices

Implement the smallest dependency-ready vertical slice that produces observable behavior. Follow the established project stack and local ownership boundaries. Use engineering, testing, security, frontend, deployment, or other specialists only within the active slice and only when their focused method is needed.

After each slice, run the narrowest credible verification and inspect the result. Fix failures before expanding scope. Reassess the remaining contract when evidence changes; do not preserve a task list that the system has disproved. Keep user changes intact and do not broaden the requested behavior through opportunistic refactors.

Verify the must-pass scenarios at real entry points when practical, then run proportionate regression checks. Record meaningful gaps and the risk they leave. For an OpenSpec-backed contract, validate and archive the change only when the official workflow calls for it and the delivered behavior is complete.

## Deliver Within Authority

Prepare commits, releases, deployment, publication, or external updates only when the user's authority covers them. Verify the actual remote or runtime result after any authorized delivery action. Stop and request new authority when completion would require a materially different external action.

Finish with exactly four concise fields, translated when appropriate to the user's language:

```text
Changes:
Verification:
Not verified:
Remaining risks:
```

Include release, deployment, or artifact links inside those fields when applicable. Mark a field `None` when it is empty. The result is complete only when the Build Contract's authorized endpoint and must-pass scenarios are satisfied, or when a clearly reported blocker prevents further progress.
