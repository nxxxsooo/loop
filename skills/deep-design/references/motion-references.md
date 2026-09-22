# Motion Reference Sources

Use when motion or animated UI is part of the approved research scope. These are starting points, not a mandatory itinerary or source quota. Continue to honor no-external-research choices. Entry pages and access notes were checked on 2026-09-21; the GSAP entry was checked on 2026-09-22. Individual animations were not visually evaluated during that catalog check.

## Choose the source by the question

| Source | Entry | Best use | Access and evidence limits |
|---|---|---|---|
| **MotionSites AI** | https://motionsites.ai/ | Animated landing-page composition, hero sequences, background treatments and prompt-based design examples | Public page exposes previews and video links; complete prompts/library access can be gated. Use visible evidence and existing authorized access; a preview does not establish code availability or reuse rights. |
| **21st** | https://21st.dev/community/components | Component-level interactions, animated heroes, shaders, backgrounds and reusable React/Tailwind UI patterns | Community registry with live previews; copying and premium templates have access limits. Check the specific author, source, dependencies and license. Do not treat the whole catalog as an unlimited free component library. |
| **React Bits** | https://reactbits.dev/ | Concrete free text animations, backgrounds, scroll reveals and interactive React components | Use the current official demo and registry, then the `react-bits` skill for variant/source/dependency checks. Pro blocks and Agent Kit are separate paid products. |
| **Godly / Recent** | https://recent.design/ | Curated motion and interaction inspiration, visual rhythm, transitions and linked designers/products | https://godly.website/ redirected to Recent when checked. Entries may be concepts or recordings rather than live shipped interfaces; follow original sources and label the evidence type. It is not automatically a source-code library. |
| **GSAP** | https://gsap.com/ | Production motion implementation library (not a gallery): timelines and sequencing, ScrollTrigger scroll scenes, SplitText text animation, Flip layout transitions, MorphSVG; the docs, demos and showcase also serve as motion reference material | Framework-agnostic JS, npm `gsap` (current v3.15). 100% free for commercial use since v3.13 (April 2025) under Webflow ownership, including former Club plugins (SplitText, MorphSVG, ScrollSmoother). License is GreenSock's standard "no charge" license (https://gsap.com/standard-license), not OSI open source — read it before redistributing or bundling. In React use the `useGSAP` hook (@gsap/react) and `gsap.matchMedia()` for responsive and reduced-motion handling. The official `gsap-*` skills (github.com/greensock/gsap-skills) are the preferred implementation guidance when installed; absent them, use the official documentation directly. |

### MotionSite naming ambiguity

The user's screenshot was labeled “motionsite.” MotionSites AI at `motionsites.ai` uses “Unlock your AI Design” wording, making it the closer candidate to the screenshot, but the exact identity is not conclusively established by the image.

`https://www.motionsite.ai/` is a separate similarly named site advertising animation website prompts/templates, sections and backgrounds. Its homepage says “One Prompt. Zero Coding. Stunning Motionsites.” Keep the two domains distinct; do not transfer accounts, access assumptions, or attribution between them. Use the user's exact link if later supplied.

## Turn a reference into a design decision

1. Identify the job: feedback, state change, hierarchy, entrance sequence, navigation, or atmosphere. Search for that effect and the relevant device rather than collecting unrelated impressive examples.
2. Open the actual item. Trigger scroll, hover, click or navigation when possible. Watch available recordings and label them as recordings. A poster image, search snippet, or text extractor's “Video” link alone is not observed motion.
3. Record the concrete source/item URL, original author, evidence type, trigger, animated properties, visible sequence, what to adopt and what to avoid. Treat timing/easing inferred from appearance as proposals, not measurements.
4. Map the idea to the current stack: existing CSS/motion library, GSAP when a timeline, scroll-triggered or text-splitting implementation is chosen, a verified React Bits item, or a verified 21st component. Record dependency cost, customization, touch/keyboard behavior, reduced-motion fallback and performance questions.
5. Put the chosen reference ID, rationale and implementation/verification constraints into the existing Build Contract. Include live or playable motion evidence alongside readable images on the reference board where available.

No new MCP server, account, paid plan, template purchase, or production dependency is required merely to browse these references. If content is gated, choose an accessible example or disclose the missing evidence. Check code, image, font and video rights separately before reuse; public viewing does not authorize redistribution.

Prefer a coherent motion language and a clear user purpose over effect quantity. Component examples do not replace full product-flow research, and absence of animation is a valid outcome.
