---
name: grill-loop
description: Adaptively chain grilling, deep-grill, OpenSpec, and related skills. Use only when explicitly invoked.
---

# Grill Loop

Follow the user's goal and the latest evidence or artifacts. Choose the smallest next useful capability, load and follow its own contract, then reassess from what changed. Treat a capability's suggested next command as evidence, not as the loop's decision; reassess before relaying or acting on it. Briefly explain each transition; the user may choose the next capability at any time.

Use `grilling` when a material answer lives only in the user's intent, priorities, risk tolerance, or taste. Use `deep-grill` when a plan or decision needs autonomous investigation and adversarial review. Use OpenSpec when the work should enter or continue durable exploration, specification, implementation, or archival. When an apply-ready change still has unresolved user-facing design, use Open Design or another prototyping capability to make it reviewable, then use `design-taste-frontend` where its scope fits or another design specialist. Feed accepted decisions back into the OpenSpec design and tasks before implementation; skip this route when no material design decision remains. Use another available skill or tool when it is a better next move.

Treat these as options, not stages. Skip, repeat, reorder, or return to them freely. Load only what the current move needs. Carry forward the goal, confirmed decisions, constraints, and artifact references, but impose no shared output format and maintain no duplicate workflow state.

Preserve every capability's scope, authority, and safety boundaries. Add no custom gates, hooks, background processes, or state files. When sustained work needs a goal, propose this adaptable card in the current transition: `Goal`, `Project / sources of truth`, `Boundaries (may change / must preserve)`, `Done when`, and `Must-pass real scenarios`; omit irrelevant fields. After user approval, register it with the active client's native goal mechanism when available and keep routing until it is met; pause only for new user input or authority. Keep no goal state of your own. Otherwise, stop when the request is fulfilled or returns diminish.
