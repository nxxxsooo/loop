# Component and motion guidance provenance

These references replace the standalone global `gsap-*`, `react-bits` and `shadcn` entries. Read them on demand through deep-design's index, including during deep-build. Former skill names in vendor prose mean the matching sibling reference, not a skill invocation. Original frontmatter is retained as source metadata only; no migrated file is named `SKILL.md`.

## Source and relocation map

| Original global location | Current location relative to deep-design | Source |
|---|---|---|
| `gsap-<topic>/SKILL.md` | `references/gsap-<topic>.md` | Installed from `nxxxsooo/loop`, `skills/vendor/gsap-<topic>/SKILL.md`; upstream guidance: https://github.com/greensock/gsap-skills |
| `gsap-<topic>/LICENSE` | `assets/gsap-<topic>.LICENSE` | Original MIT notices, retained separately for all eight topics |
| `react-bits/SKILL.md` | `references/react-bits.md` | Mingjian-maintained free-library integration guidance; no standalone lock record was present |
| `react-bits/references/*.md` | `references/react-bits-*.md` | Original official-sources and motion-quality references |
| `react-bits/agents/openai.yaml` | `assets/react-bits-openai.yaml` | Retired UI metadata, retained as provenance, not discovery configuration |
| `shadcn/SKILL.md` | `references/shadcn.md` | https://github.com/shadcn/ui.git, `skills/shadcn/SKILL.md` |
| `shadcn/{cli,customization,mcp,registry}.md` | `references/shadcn-<name>.md` | Installed vendor guidance |
| `shadcn/rules/*.md` | `references/shadcn-<name>.md` | Installed vendor rules, flattened with rebased links |
| `shadcn/assets/*.png` | `assets/*.png` | Both original icons |
| `shadcn/agents/openai.yml` | `assets/shadcn-openai.yml` | Retired UI metadata; icon paths rebased to retained icons |
| `shadcn/evals/evals.json` | `assets/shadcn-evals.json` | Original evaluation prompts and expectations |

No scripts or other assets existed in the relocated entries. Guidance bodies are preserved except relocation links and explicit routing to references. Retired UI metadata is historical, not an instruction to expose another skill. Deep-design's own `agents/openai.yaml` remains its active UI metadata.

## Source records and update boundaries

The nine retired installation records are preserved in [component-motion-installation-records.json](../assets/component-motion-installation-records.json). They record source paths, folder hashes and install/update times, not a verified upstream commit SHA. Loop's separate `bundle-sources.json` pins the eight unchanged GSAP documents and licenses. The shadcn guidance revision remains unverified; its [MIT license](../assets/shadcn.LICENSE) was retrieved separately from [upstream license history](https://github.com/shadcn-ui/ui/blob/6ea6856f5a1082d4d9c231559b6bc3ee73827493/LICENSE.md). React Bits' live library sources and license remain in [its sources reference](react-bits-official-sources.md).

Refresh the bundled guidance deliberately from the recorded sources, preserving local routing and flat relative links. The references now ship with `deep-design` in the Loop bundle. Do not reinstall the retired standalone entries to refresh them.

## Runtime adaptations and inherited gaps

- shadcn's original entry used command-output injection for `npx shadcn@latest info --json`. A reference read cannot execute it. Run that read-only context command explicitly inside the target project with its package runner before using the guide; do not assume context was injected. Installation, preset changes and component writes still require implementation authority.
- shadcn's MCP reference documents optional tools; it does not install or authorize an MCP server.
- GSAP frameworks mentions upstream `examples/vue/` and `examples/nuxt/`. Neither example directory was present in the installed copy. They remain upstream pointers, not bundled runnable projects; consult the recorded upstream repository if examples are needed. This migration does not fabricate or fetch missing resources.
- Vendor API examples and performance claims are retained, not newly runtime-verified. Verify current APIs and actual animation behavior in the target application.
