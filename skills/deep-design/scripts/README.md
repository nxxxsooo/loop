# Scripts

Vendored from [obra/superpowers](https://github.com/obra/superpowers) `skills/brainstorming/scripts/` — the visual review companion server (MIT license).

- Upstream commit: `5bf4e78011075bcfc0dc295f0724994cd123ee71` (v6.4.1 era, 2026-09)
- Files are byte-identical to upstream. Do not edit them locally; record needed changes here or fix upstream.
- Re-sync: `gh api "repos/obra/superpowers/contents/skills/brainstorming/scripts/<file>" --jq '.content' | base64 -d > <file>`

## Usage in this skill

`start-server.sh --project-dir <project> [--open]` starts a zero-dependency Node server that serves the newest HTML file in the session's `screen_dir` and records the user's browser clicks to `state_dir/events`. `stop-server.sh <session-dir>` stops it. The full workflow is documented in `references/visual-evidence.md` ("Live visual review loop").

Known surfaces:

- Session files persist under `<project>/.superpowers/brainstorm/<pid>-<ts>/`; remind the user to gitignore `.superpowers/`.
- Requires Node.js; no npm dependencies.
- The URL embeds a session key (`?key=…`) — always share the complete URL.
