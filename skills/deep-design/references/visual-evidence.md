# Visual Evidence and Feedback

Visual artifacts support the Build Contract; they are not separate workflow state or automatic permission to modify the product.

## Research board

For newly researched visual candidates, prepare a standalone HTML board, or extend an existing review artifact with equivalent capabilities, before requesting visual selection or direction approval. Already supplied references and accepted choices can be reused without recreating a board.

Each candidate needs a stable reference ID, exact source URL, evidence type, readable actual image, intended role, detail to adopt and mismatch/detail to avoid. Distinguish live-product captures, officially published screenshots, concepts and recording frames. Search thumbnails and generated approximations are not actual source evidence.

Keep images portable through embedded data or bundled relative paths. Preserve aspect ratio and provide full-size viewing. Show relevant sections of long pages legibly rather than shrinking the whole page. Capture only necessary material, excluding private account details. A blocked capture can remain a labeled research lead, but use an accessible alternative for visual approval.

Provide neutral initial per-reference selections, support multiple choices, and include labeled comments. Use stable sub-IDs for different states or screenshots from one source. Keep recommendations visually distinct from the user's choices.

Save drafts under a board-specific key when local storage is available and provide JSON or Markdown download with board/version, IDs, URLs, selections and comments. If storage fails, disclose it and preserve a working export. Explain that browser edits do not automatically reach the agent; read exported feedback or use a verified integration before interpreting it as submitted.

Open the artifact and verify image loading, normal-size readability, full-size images, multiple selection, comments, reload persistence and export. Source inspection alone cannot establish usability. State failed or unavailable checks.

Reference selection is input to the design recommendation. Follow the question precedence in SKILL.md for remaining material choices: explicit prose preference first, otherwise a callable native interface, otherwise immediate concise prose. Do not ask users to approve the same accepted reference again.

## Live visual review loop

Use a live browser review when the user would understand a question better by seeing it than reading it: UI mockups, layout or direction comparisons, diagrams of spatial relationships. A question about UI is not automatically visual — scope, wording, and tradeoff questions stay in the terminal. Get the user's approval before starting the companion; auto-open their browser only after that approval.

Start the zero-dependency Node server from this skill's `scripts/` with `--project-dir <project root>`, so screens persist under `<project>/.superpowers/brainstorm/<pid>-<ts>/`; remind the user to gitignore `.superpowers/`. Save `screen_dir` and `state_dir` from the startup JSON and give the user the complete URL including its `?key=…` session key — the key gates access, so never share a bare host:port. Run the server so it survives across turns; if the environment reaps background processes, use `--foreground` with the client's background execution mechanism. The scripts are vendored from obra/superpowers; provenance and re-sync live in `scripts/README.md`.

Per visual question:

1. Before pushing, confirm the server is alive: `$STATE_DIR/server-info` exists and `$STATE_DIR/server-stopped` does not. If it stopped, restart with the same `--project-dir` — the port is reused and the user's open tab reconnects by itself.
2. Write a new HTML file with a semantic, never-reused name (`layout.html`, `layout-v2.html`) into `screen_dir`. Write content fragments, not full documents; the server wraps them with header, theme, and interaction helper. Use the frame's `options`, `cards`, `mockup`, and `split` classes with `toggleSelect` for clickable choices (`data-multiselect` for multiple). Keep 2–4 options per screen, wireframe fidelity for structure questions, polish fidelity for polish questions, and real content when placeholders would hide design issues.
3. Summarize what is on screen in the terminal, repeat the URL as a fallback, and end the turn asking the user to look and respond.
4. On the next turn, read `$STATE_DIR/events` (JSON lines, cleared when a new screen is pushed) and merge it with the user's terminal reply. Terminal prose is primary; the event stream adds structured selections and can reveal hesitation in the click pattern. A missing events file means no browser interaction happened.
5. Iterate with a new versioned file when feedback changes the current screen; advance only when the step is validated. When the conversation returns to non-visual work, push a `waiting` screen so the browser does not keep showing a resolved choice.

A browser click records a selection; it does not by itself close a design decision. Follow the question precedence in SKILL.md for remaining material choices, and record accepted selections into the design recommendation or Build Contract like any other approved evidence. This loop is the verified integration the research board section allows; the export-based board remains the fallback when the environment cannot keep a server running. Stop the server with `stop-server.sh <session dir>` when the review ends; persisted screens remain as design evidence.

## Motion and preview evidence

Show a playable recording or live demo for motion when possible. Record what was actually triggered and observed; label unseen motion unverified. A proposed timing value is not a measured one.

An optional high-fidelity preview depicts the representative workflow with realistic content and critical states, at agreed device sizes. Keep it isolated from production behavior. Use image generation where imagery itself is the question, but do not present generated screens as real reference captures or implemented product evidence.

Explicit preview acceptance or an explicit switch to direct implementation closes that decision. Revision requests do not.

## Implementation acceptance

Deep Build checks the approved routes, data/states and viewport sizes in the running application. Actual interactions and implementation screenshots are required when runtime access is available. Record startup, authentication or data blockers and the exact unperformed checks; preview imagery cannot substitute.

A Before/After board is optional and requested explicitly. If used, match route/state, representative data, viewport and framing where practical. Label unavoidable differences and missing baseline captures honestly. No new unintended overflow, clipped or obscured controls, broken assets or related console errors should pass as accepted visual work.
