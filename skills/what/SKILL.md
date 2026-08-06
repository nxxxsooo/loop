---
name: what
description: Pause the current work and re-explain the last message when the user did not understand it. Use only when the user explicitly invokes this skill to request more context, a clearer explanation, or a new pitch of the current state.
---

# What

Stop the current progression. Re-explain the most recent update. Do not continue the task in the same response.

Use the language of the user's latest message. Give only enough context to make the update understandable:

- State the last confirmed point.
- State the current position.
- State what changed.
- State why it matters.
- State the proposed next action.

Then explain the conclusion or proposal again in a clearer way. Keep the response compact.

Read the nearest `CONTEXT.md` when it exists. Use its ubiquitous language exactly. Do not replace defined project terms with synonyms. If no `CONTEXT.md` exists, preserve the established terms from the conversation and current artifacts. Do not claim that a context file exists when it does not.

For English, use ASD-STE100 Simplified Technical English. Use short sentences, explicit subjects, active voice, and one main idea per sentence. Define an abbreviation before using it.

For Chinese, use clear technical Chinese. Use short sentences and explicit subjects. Put one main idea in each sentence. Avoid metaphors, wordplay, and vague pronouns. Define an abbreviation before using it. Keep identifiers, commands, paths, and defined project terms unchanged.
