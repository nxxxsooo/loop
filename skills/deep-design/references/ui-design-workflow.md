# UI Design Workflow

Use only when interface decisions are material. Deep Design owns design progression; research and aesthetic specialists supply methods. Their search quotas, mandatory execution steps, or client-specific modes do not replace this contract.

## Inspect and establish the boundary

For an existing interface, inspect relevant code and the running product when accessible. Treat it as evidence of behavior, not a requirement to retain the current composition. Record affected routes, deep links, actions, validation, permissions, data/API contracts, side effects, and default/loading/empty/error/success/disabled states. Link each important preserved behavior to existing evidence and its verification method. Mark unknowns rather than guessing.

Preserve authentication, authorization, analytics hooks, localization, accessibility, performance/browser requirements, required platform behavior, brand assets/constraints, legal copy, product terminology and reliable behavioral primitives unless the brief explicitly changes them. Redesigning presentation does not authorize new business rules, feature removal, or a framework migration. Note existing defects separately.

For a new interface, map confirmed user tasks into routes, states, actions and acceptance scenarios. Ask only about missing product decisions that affect design. Do not impose old-product inspection requirements on a greenfield project.

Scope is one of:

- **Bounded change:** a page/component with no material shared-navigation, token, or cross-page impact. Present scope and direction together when this avoids unnecessary approval rounds.
- **Broad change:** the shell, information architecture, shared design foundation, cross-page flows, or uncertain shared impact. Approve scope first; select a representative end-to-end workflow for initial implementation and review before migration.

A complete rebuild uses the broad route. A partial redesign may too. Inspect shared component consumers so a local-looking change does not silently alter other pages. Reopen scope only when the impact expands.

Summarize the user job, usability problems, and regions to keep/rebuild/add/remove. Do not require current-app screenshot boards for scope; use them only if requested or necessary evidence. Old screenshots are not prerequisites for later acceptance.

## Select research once

Before external inspiration research, reuse an explicit research preference or ask whether to study product behavior, UI appearance, both, or neither. If the native tool has fewer than four choices, ask two yes/no decisions together. Existing references focus research but do not cancel requested searching.

When research is selected, load `ui-research` if available for its source selection and analysis structure. Apply only the selected research types; its fixed example counts and mandatory-research language are not progression requirements here. Without it, perform the same focused research with available tools.

- **Product:** investigate comparable tasks, capabilities, permissions and recovery through official documentation or visible flows. A marketing claim is not observed product behavior.
- **UI:** investigate structure, density, core controls, states and visual tone. Behance, Dribbble and Pinterest are valid concept/style sources; real product interfaces help validate practical fit. Follow original sources and label concepts accurately.
- **Both:** report behavioral findings and appearance findings distinctly, then synthesize a coherent recommendation.
- **Neither:** work from supplied references, current product and confirmed requirements; do not add an inspiration search. Necessary technical API/source verification is distinct from visual research; honor any broader no-network restriction too.

Search for the task, category, device and unsettled question rather than visiting a fixed site list. Public official demos, case studies, independent sites and design systems are all eligible. There is no source quota. Stop when the design questions have enough evidence.

Default to no-payment access. Distinguish public content, free-login content, paid/trial-only content and unknown access. Use existing authorized access or accessible alternatives; do not require a subscription or trial to finish research. Do not treat a paid site's free thumbnail as access to its full flow. Respect an explicit authorization to use existing paid material without assuming authority to purchase.

Keep private project data, credentials and internal URLs out of public search queries. Browsing access does not grant reuse rights for images, fonts, branded assets or code; check the original source's terms before incorporating material into the deliverable.

## Translate evidence into a direction

For each retained reference identify its source, evidence type, role, specific detail to adopt, mismatch and detail to avoid. Roles include structure, density, core component, state behavior, typography/color and motion. Newly researched visual candidates use the board defined in [visual evidence](visual-evidence.md).

When motion matters, inspect the actual trigger and sequence on a live demo or a clearly labeled recording. A still image or component source does not prove how it looks. Avoid inventing exact timing/easing from observation; implementation values can be explicit proposals.

Use [motion reference sources](motion-references.md) to route between MotionSites AI for animated page ideas, 21st for component-level patterns, React Bits for free implementable effects, and Godly / Recent for curated interaction inspiration. The catalog is optional and does not override the selected research scope.

Use `react-bits` when a free animated component can answer the design question. Inspect the current official catalog, chosen variant, source, dependencies, rendered semantics and customization options. Record mobile, keyboard and reduced-motion behavior to implement or verify. Prefer existing CSS or the project's existing motion library when it is sufficient. No animation is also a valid decision.

Do not assume React Bits is installed, that its Pro templates are free, or that every suggested effect has acceptable performance. If this optional local skill is absent, use official free documentation directly. Component installation belongs to deep-build; a separately requested isolated preview can have its own bounded dependencies.

Resolve conflicts among references in the order of user task, structure, density, state/interaction behavior and visual tone. Propose a usable target layout with realistic content, primary action, navigation, main components and critical states. Offer alternatives only when they represent meaningful choices; users can select different details from multiple references.

Fit composition to the product: compact and scannable working surfaces for business tools, visible work areas for AI tools, platform-appropriate flows for mobile, offer-specific imagery for marketing. Avoid automatic giant headings, nested cards, decorative glow or excessive whitespace as universal personality. Treat aesthetic preferences as contextual judgments, not a ban on styles across all products.

## Approval, preview and handoff

Confirm the proposed direction and preview preference together if unresolved. Options are an isolated high-fidelity preview of the first core workflow, or direct implementation after Build Contract approval. Preview approval and implementation authority are separate. Read feedback, revise, and keep approval pending until the user accepts or explicitly changes the preview choice.

Artifacts obey actual environment permissions. Use existing project artifact conventions; do not create another plan or app runtime merely for process. If required artifact creation is unavailable, explain the specific missing evidence and request bounded permission instead of claiming it exists.

The one Build Contract captures:

- Approved scope and must-preserve behavior, including adjacent shared consumers.
- Reference IDs, observed facts, accepted/rejected details and reconciled design decisions.
- Layout, tokens, hierarchy, density, control/state behavior and responsive targets.
- Requested preview location/version and approval status, or the confirmed direct route.
- Motion purpose, trigger/sequence, verified component source/variant/dependencies, proposed timing, and fallbacks when applicable.
- Exact representative routes, important states/data and viewport sizes for acceptance.
- Implementation slices: layout/reflow, hierarchy, shared components, states/content, visual finish and purposeful motion.
- For broad scope, review of the first implemented end-to-end workflow before remaining-page migration.
- Browser interaction and actual screenshot checks, behavior regression checks, and honest handling of unavailable startup/auth/data.

Keep small visual adjustments within the current accepted direction. New navigation, scope or layout principles reopen only the affected design decisions. The existing loop resumes deep-build when the revised contract is ready and authorized.
