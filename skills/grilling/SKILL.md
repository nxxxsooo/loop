---
name: grilling
description: >-
  Grill the user relentlessly about a plan, decision, or idea. Use when the
  user wants to stress-test their thinking or uses any "grill" trigger phrase.
  Also use for every reply in an active grilling session, including short
  answers, until the user confirms shared understanding, stops, or changes
  tasks; they do not need to name the skill again.
---

# Grilling

Interview the user until you reach a shared understanding. Map the work as a **design tree**: every decision branches into the decisions that depend on it.

## Keep The Session Active

A fresh grilling session starts when the user requests it. After that, treat each answer to a grilling round as a continuation of the same session. Reconstruct the current tree from the conversation, apply the answer, and continue with the next frontier. Do not ask the user to invoke `grilling` again.

The session ends when the user confirms shared understanding, asks to stop, clearly changes tasks, or authorizes a separate next phase after the interview is complete.

## Work The Frontier In Rounds

The **frontier** is every decision whose prerequisites are settled. Ask only questions that can be answered now without guessing at an answer the user has not given.

Recompute the frontier after each answer. A question that depends on another open question belongs to a later round. When the frontier is larger than the active client's question limit, ask the highest-impact questions that fit and leave the other unblocked questions for the next round. Tool capacity defines the batch size, not a new dependency between those questions.

## Use The Native Question Interface

For every round, call the active client's native question tool when it is available in the current mode. Do not merely describe the questions in prose when the tool can present them. Use one tool call for the round and include as many frontier questions as the tool supports.

For each question:

- Ask one decision with a short title and concrete wording.
- When the tool uses choices, offer two or three mutually exclusive options.
- Put the recommended option first, mark it with the client's recommendation convention when supported, and explain its main tradeoff in one sentence.
- Preserve the tool's free-form answer path so the user can reject the offered choices.
- Do not repeat the same question in Markdown after a successful tool call.

If no native question tool is available in the current mode, ask the same round in concise numbered prose. Use this fallback format for each question:

```text
Q1 - <question title>: <question body and choices>

Recommended: <recommended answer and main tradeoff>
```

Then wait for the user's answers before continuing.

## Find Facts, Ask For Decisions

Finding facts is the agent's job. Use the available environment and tools for facts instead of asking the user. Use parallel exploration only when the current host and user instructions permit it. An unresolved factual check blocks only the questions that depend on it; ask the rest of the frontier now.

The decisions are the user's. Put every material user-owned decision to them and wait.

## Finish Deliberately

The interview is ready to finish when the frontier is empty: every material branch has been visited and nothing remains silently assumed. Summarize the shared understanding and ask the user to confirm it. Do not implement or otherwise act on the result until they confirm or separately authorize that next phase.

The unmodified upstream contract that this local interaction overlay adapts is preserved in [references/upstream.md](references/upstream.md).
