---
name: react-bits
description: Find, compare, and integrate free React Bits animated components in React projects. Use for React Bits/reactbits requests, reference-to-motion matching, animated typography, backgrounds, scroll reveals, and creative UI effects. Verify official source, dependencies, and variants before implementation; pair with deep-design when the visual direction is unsettled.
---

# React Bits — Free Component Workflow

Mingjian-maintained integration guidance for the free library at https://reactbits.dev. This is a local skill, not the official paid React Bits Pro Skill. No license key or MCP server is needed for the free registry.

## 1. Establish the task

- Read project instructions and inspect the framework, package manager, React version, styling, existing motion libraries, and component conventions.
- Determine whether the user wants discovery, comparison, or implementation. Discovery alone does not authorize changes to the app.
- If design direction is unclear, use `deep-design` to settle it first, with `impeccable` for frontend craft when needed. Research only within the user's chosen scope. Convert selected references into concrete effects: entrance sequence, hover feedback, text reveal, ambient background, or navigation behavior.
- Prefer an existing lightweight implementation for routine interactions. Use React Bits where the selected effect adds clear value.

## 2. Discover from current official evidence

Use `agent-reach` for web/GitHub access and the available browser for visual inspection. Read [official sources and retrieval](react-bits-official-sources.md).

1. Read the live free registry index; search names and descriptions instead of inventing component names.
2. Retrieve the exact component variant JSON. Verify its name, dependencies, files, and source before recommending an install command.
3. Inspect the official demo and usage where available. Source inspection establishes implementation facts; it does not prove what an animation looks like. State when visual inspection was unavailable.
4. Offer a small shortlist with official links, purpose, fit to the reference, dependencies, and mobile/reduced-motion considerations. Recommend one with reasons.

Do not claim generic component names, prop names, installed MCP tools, frame rates, or bundle sizes without evidence. Registry metadata and current source take precedence over examples in older third-party skills.

## 3. Integrate only the chosen effect

- Match the existing stack: `JS-CSS`, `JS-TW`, `TS-CSS`, or `TS-TW`. Do not migrate styling solely for a component.
- In projects already using shadcn, use its add command for the verified item. Read the [shadcn workflow](shadcn.md) when working with its CLI or configuration. Run commands inside the target project using its package manager.
- Otherwise follow the official manual-copy method: copy the verified source and any companion styles/assets into the project's existing structure, then install only required missing dependencies. Do not initialize a design system as a side effect.
- Preserve local files. Inspect destinations before copying and review changes after a CLI install.
- For Next.js, inspect hooks, browser globals, and imports. Add an appropriate client boundary; use client-only loading only if the actual component requires it. Do not assume downloaded files contain `use client`.
- Read actual prop types and examples. Check duration units and rendered HTML semantics; do not assume a text animation renders an `h1`.
- Keep source URL, variant, retrieval date, and local modifications in a brief project note. Retain upstream copyright/license notices.

## 4. Verify the integrated behavior

Read [motion quality and verification](react-bits-motion-quality.md). Run existing project checks and inspect the changed page in a browser: initial load, trigger behavior, mobile layout, reduced motion, keyboard behavior for interactive elements, and console errors.

Measure animation performance with a browser trace or frame observation on the target viewport. A successful build or a timed DOM query is not evidence of smooth animation. Report untested dimensions accurately.

## 5. Deliver and improve

For discovery, return the shortlist and recommended mapping to the reference. For implementation, report changed files, chosen variant/dependencies, meaningful verification, and remaining gaps.

When asked to retain feedback, record adopted/rejected choices with context and reasons in the owning project or knowledge document. Distinguish user taste from validated technical constraints; update this local skill only when explicitly requested.

## Scope

- The free library provides components; do not promise Pro page templates, blocks, or Agent Kit contents.
- If a requested item is paid, identify that boundary and find a free alternative when appropriate. Do not silently use a paid registry.
- Upstream uses MIT + Commons Clause, not plain MIT. Consult its current license for redistribution of component collections; normal application integration follows the upstream terms.
