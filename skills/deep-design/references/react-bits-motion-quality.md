# Motion quality and verification

## Select for a purpose

Name the role of each effect: draw attention, establish sequence, confirm interaction, or create atmosphere. Prefer one clear focal effect over unrelated animation layers. Match its speed, easing, contrast, and visual weight to the page and reference.

Compare a lightweight CSS or existing-library option against a component that introduces a new runtime. Choose according to the effect and measured constraints, not an arbitrary fixed animation count.

## Integration checks

- Use real content and a stable container size to reveal wrapping and layout shifts.
- Check text semantics and accessibility output. Preserve readable text when effects are disabled; avoid announcing individual letters or duplicating visible and screen-reader text.
- Implement `prefers-reduced-motion` with a static or substantially reduced alternative. Important content must remain present.
- Treat hover-only visuals as enhancement; keyboard and touch users still need the action and visible focus.
- Inspect expensive blur, particles, WebGL, and continuous loops. Reduce or suspend work when offscreen and clean up observers, listeners, and animation loops on unmount.
- Do not equate reduced-motion preference with low-power hardware. Both may justify adaptation, but they are different signals.
- Preserve contrast over moving backgrounds and keep decorative layers from intercepting input.

## Verification evidence

Use the project's existing type/lint/build checks plus a real page inspection. Verify first load and re-entry, scroll triggers, narrow screens, reduced motion, and keyboard operation where applicable.

For performance, inspect a browser trace, main-thread activity, frames, or relevant Web Vitals in the real page. Report the viewport and method. Avoid unsupported promises such as universal 60fps, fixed component byte sizes, or automatic accessibility.

## Reusable feedback

Capture: reference URL, selected component/variant, purpose, configuration, why it was accepted or rejected, actual verification, and conditions where the pattern should be reused. Mark taste preferences separately from measured limitations.
