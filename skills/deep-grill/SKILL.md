---
name: deep-grill
description: >-
  Deeply grill an idea, decision, design, plan, or implied approach through
  evidence, failure modes, and user-owned decisions. Use discovery mode for raw
  ideas, clarification, "grill me", or an unfinished Product Brief; use audit
  mode for a formed target that needs a verdict or revision. Continue every
  reply in an active deep-grill session until its Product Brief or verdict is
  confirmed, without requiring the user to name the skill again.
---

# Deep Grill

Run one evidence-driven branch loop in either **discovery mode** or **audit mode**. Facts belong to the agent; goals, priorities, risk tolerance, taste, and authority belong to the user.

## Select The Mode

Use discovery mode when the input is a raw idea, the user asks to be interviewed or clarified, `loop` supplies work without a ready Product Brief, or materially different approaches depend on a user-owned decision tree. Its output is a confirmed Product Brief.

Use audit mode when the user supplies a formed plan, design, decision, or implied approach and wants autonomous pressure-testing, a verdict, or revisions. Its output is an audit verdict.

If the mode is initially unclear, state and audit the smallest plausible approach. Switch to discovery mode only when continuing would invent a material user-owned decision. Discovery mode may use audit passes between question rounds; the modes share one tree rather than handing work to another grilling skill.

## Keep The Session Active

After deep-grill starts, treat each answer to its question round as a continuation of the same session. Reconstruct the current branch tree from the conversation and artifacts, apply the answer, and continue. The user does not need to invoke `deep-grill` or `loop` again.

End the session when the user confirms the Product Brief or audit verdict, asks to stop, clearly changes tasks, or authorizes a separate next phase after deep-grill is complete.

## Work The Branches

Map material branches in dependency order. The **frontier** is every branch whose prerequisites are settled.

Investigate factual branches with the available environment, sources, tests, and bounded experiments. For each provisional answer, use the strongest objection and a concrete failure scenario to keep, revise, or reject it. Mark insufficient evidence and provide a validation path instead of inventing facts. An unresolved factual check blocks only dependent branches.

Ask the user only about frontier decisions that the agent cannot own. Recompute the frontier after every answer or evidence change. Prioritize impact, uncertainty, and reversibility; stop at diminishing returns.

## Use Native Questions

Before presenting the first user decision, determine from the active client's tool metadata whether its native question interface is callable now, supported but gated behind another mode, or unsupported.

- If callable, use one native question call for the round and include as many frontier decisions as the tool supports.
- If mode-gated, do not present the decision in prose. Name the question-capable mode when the client identifies it, ask the user to switch and continue, then wait with the pending frontier intact.
- Use concise numbered prose only when the client has no native question interface or the user explicitly chooses prose.

Each native question asks one decision, offers two or three mutually exclusive options, puts and marks the recommended option first, explains its main tradeoff in one sentence, and preserves free-form input. Do not repeat a successful native question call in Markdown.

## Discovery Output

When every material user-owned branch is settled, produce a concise Product Brief with the applicable fields:

```text
Product / offer:
Target user and context:
Problem and desired outcome:
Constraints and must-preserve behavior:
Non-goals:
Confirmed decisions:
Evidence and assumptions:
Success scenarios:
Residual risks:
```

Ask the user to confirm the brief through the native question interface under the same mode rules. The brief is ready for `deep-design` only after confirmation and when no root product decision remains open.

## Audit Output

Report the target, verdict, recommended revisions, supporting evidence, strongest objections, failure scenarios, evidence limits, residual risks, unresolved items, and unexamined scope. Keep one or two bounded user choices inside the audit using the same native question rules. If a decision tree emerges, continue in discovery mode instead of recommending another grilling skill.

Do not implement or otherwise act on a Product Brief or verdict until the user confirms it or separately authorizes the next phase.

The upstream interactive-grilling contract incorporated into discovery mode is preserved in [references/grilling-upstream.md](references/grilling-upstream.md).
