# Standalone deep-grill maintenance

## One source, two distribution entry points

- Maintain DG only in [`skills/deep-grill/`](../skills/deep-grill/), including
  its bilingual READMEs, images, license, and checker.
- [loop](https://github.com/nxxxsooo/loop) ships the complete lifecycle.
- [deep-grill](https://github.com/nxxxsooo/deep-grill) ships DG alone and
  retains its own release cadence and existing Git history.
- [`distributions/deep-grill.json`](../distributions/deep-grill.json) is an
  explicit export allowlist. Add new distribution files there; do not copy
  private workspaces or unrelated loop skills into DG.
- `bundle-sources.json` now covers external vendors only. Do not re-import DG
  from its distribution repository or pin owned source to its previous release.

The migration baseline is DG v3.0.2,
`dd2ce0e743aa0d2370db64edd5882d4d3ccda4b8`. Any existing local DG checkout and
worktrees are kept under `.local/distributions/deep-grill/` as distribution
and history workspaces, not a second maintained source. `.local/` stays ignored.

## Verify and export

From the loop root:

```bash
python3 scripts/sync-skill-artifacts.py --write
python3 scripts/check-bundle.py
python3 scripts/check-readme-sync.py
python3 skills/deep-grill/scripts/check-readme-sync.py
python3 -m unittest discover -s tests
python3 scripts/export-deep-grill.py
python3 scripts/export-deep-grill.py --check
python3 .local/exports/deep-grill/scripts/check-readme-sync.py
```

The default export is `.local/exports/deep-grill/`. It contains the standalone
package plus `loop-source.json`, which records canonical source and per-file
SHA-256 hashes and modes, without private paths or machine state. Exports are
deterministic; unrelated loop changes do not change a DG export.

To refresh an unchanged export after editing canonical DG:

```bash
python3 scripts/export-deep-grill.py --update
```

The exporter refuses unknown directories, changed exports, symlinks, and dirty
Git checkouts. It never commits, tags, fetches, pushes, or publishes. `--check`
never writes. Run `python3 scripts/sync-skill-artifacts.py --write` whenever
SKILL.md changes to refresh README excerpts and Raycast snippet text. Running
the same command without `--write` checks for stale generated text only.

## Prepare an independent DG release

When publication is separately authorized:

1. Commit and verify the canonical DG source in loop. Push that source commit
   when authorized so public source links resolve. A **loop release is not
   required** to release DG.
2. Use the preserved distribution checkout or a clean checkout of the DG
   distribution's main branch. For the preserved checkout:

   ```bash
   python3 scripts/export-deep-grill.py --output .local/distributions/deep-grill --update
   python3 scripts/export-deep-grill.py --output .local/distributions/deep-grill --check
   python3 .local/distributions/deep-grill/scripts/check-readme-sync.py
   git -C .local/distributions/deep-grill diff --stat
   ```

3. Review and commit only the generated distribution changes, including
   `loop-source.json`. Tag and publish a **DG** version in that repository,
   preserving its existing history; never force-push a subtree over it.
4. Refresh standalone consumers with:

   ```bash
   npx skills@latest add nxxxsooo/deep-grill --skill deep-grill -g -y
   ```

The initial checkout must match the pristine migration baseline. Later updates
require a clean checkout whose files still match its committed `loop-source.json`.
Unique distribution-side edits are refused, not overwritten; port legitimate
changes into canonical loop source before exporting again. A newly generated
dirty checkout must be reviewed and committed before another update.

Users who installed DG from loop should either refresh the loop bundle or
explicitly switch the DG installation source. Both sources install the same
skill identifier, not two cooperating copies. A standalone update does not
retroactively modify an already-installed loop snapshot.

## Current skill boundaries

- DG is self-contained; no separate grilling skill or bundled upstream prompt
  is loaded. The rewritten package carries its own MIT LICENSE; previous
  versions and their notices remain available in Git history.
- Deep-design orchestrates design and produces the Build Contract.
- Impeccable supplies interface design, review, and polish within that contract.
- Design-taste-frontend is retired and no longer bundled or routed by deep-design.
- Deep-build implements and verifies the approved contract.
