# Third-party notices

The bundled `skills/deep-design/scripts/` visual review server is vendored
unchanged from [`obra/superpowers`](https://github.com/obra/superpowers)
at revision `5bf4e78011075bcfc0dc295f0724994cd123ee71` (v6.4.1 era, retrieved
2026-09-22), from `skills/brainstorming/scripts/` (`server.cjs`, `helper.js`,
`frame-template.html`, `start-server.sh`, `stop-server.sh`), MIT licensed.
Provenance and re-sync instructions live in
`skills/deep-design/scripts/README.md`.

The bundled `skills/deep-grill` is vendored unchanged from
[`nxxxsooo/deep-grill` v3.0.1](https://github.com/nxxxsooo/deep-grill/releases/tag/v3.0.1)
at revision `9dc43b44bfe2bf9031a044f38836d6ddb0994dd0`.

Its discovery mode incorporates Matt Pocock's interactive grilling contract.
The immutable upstream source, copyright, and MIT license attribution are
preserved inside `skills/deep-grill/references/grilling-upstream.md`,
`skills/deep-grill/NOTICE`, and `skills/deep-grill/THIRD_PARTY_NOTICES.md`.

## Vendored external skills

`skills/vendor/` repackages external skills verbatim so one
`npx skills add nxxxsooo/loop --skill '*'` installs the complete set. Each
vendored directory carries the upstream `LICENSE`; byte-level provenance
(upstream repository, pinned commit, and per-file SHA-256 hashes) is recorded
in `bundle-sources.json` and validated by `scripts/check-bundle.py`.

| Skill | Upstream | Pin | License |
|---|---|---|---|
| `gsap-core` … `gsap-utils` (8) | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | `aed9cfd3277740755f6bfc1155c7aa645403b760` | MIT |
| `design-taste-frontend` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | `5217fb45be2c0b302f29c9cd31cbd3237501c684` | MIT |
| `impeccable` | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | `skill-v4.3.1` | Apache-2.0 |

The vendored `impeccable` directory also carries the upstream `NOTICE.md`
required by Apache-2.0. Upstream releases do not flow into installed copies
automatically: they arrive through loop bundle releases after re-vendoring
and re-pinning. Upgrades should be re-vendored from upstream rather than
patched in place so the hash manifest stays verifiable.

## UI workflow references

The UI workflow was informed by the installed
[`Davied-H/rebuild-ui-design`](https://github.com/Davied-H/rebuild-ui-design)
workflow, inspected on 2026-09-21. Its scope/research/preview/verification
responsibilities are re-expressed within deep-design and deep-build; its
source files are not vendored, and it is not a runtime dependency.

[`travisjneuman/.claude` ui-research](https://github.com/travisjneuman/.claude/tree/master/skills/ui-research)
is an optional independently installed research specialist. React Bits source
and assets remain governed by the [upstream license](https://github.com/DavidHDev/react-bits/blob/main/LICENSE.md).
No React Bits components or paid Agent Kit contents are bundled here.
