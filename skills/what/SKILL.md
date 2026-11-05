---
name: what
description: Use when the user sends a message consisting only of `?`, explicitly invokes `$what` or `@what`, sends review feedback with `what?` annotations that has this skill attached, or asks to re-orient around an active task after not understanding the current update.
---

# What

Temporarily hold the pending action, explain the active frontier, then prompt the user to resume work.

## Trigger And Scope

Treat only an entire trimmed `?` message, an explicit `$what` or `@what` invocation, and an explicit attachment of this skill as the checkpoint trigger. Do not intercept an ordinary question that merely contains `?`.

When the user instead asks to re-orient around an active task after not understanding the current update, answer in the same checkpoint style without taking ownership of ordinary prose that simply includes a question mark.

## Explain Annotated Passages

Review feedback, such as OpenCode Annotate's, may arrive with this skill attached and with annotations whose comment is `what?`. Each such annotation quotes a passage the user does not understand. Explain each quoted passage before anything else: in plain language, with more detail, a concrete example where it helps, and how it relates to the current task. Follow any instruction the feedback adds for these notes, and address its other annotations as usual.

## Explain The Frontier

State the last confirmed point, current workflow and step, changed artifacts, why the state matters, and the pending next action. Preserve project terms and read the nearest `CONTEXT.md` when it exists.

Do not advance the workflow, delegate the pending action, or invent a new route while explaining the frontier. Keep the pending action paused at its current boundary until the user explicitly resumes it.

## Prompt Continuation

When `request_user_input` is callable, invoke it with `Continue` (recommended), `Adjust next action`, and `Stop`. Otherwise, render the same localized choices in concise prose without requesting a mode switch. End every active-work explanation with that continuation prompt. Execute the pending action only after the user chooses `Continue`.

`Continue` resumes the pending next action as scoped. `Adjust next action` changes only the immediate next step unless the user's adjustment invalidates the current workflow. `Stop` ends the active run cleanly and leaves the frontier paused.

## No Active Work

When no active or resumable task frontier exists, say that no resumable frontier exists and ask what task to orient around. Do not pretend there is pending work, and do not fabricate continuation controls for a task that is not active. After explaining annotated `what?` passages, stop there instead: the passages were the task.
