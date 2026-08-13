# Visual Direction Reference

Use this file when analyzing the photograph and writing the image-edit prompt. `SKILL.md` owns the workflow and hard rules; this reference owns the detailed visual decisions.

## Contents

- [Transformation map](#transformation-map)
- [Artistic proposition](#artistic-proposition)
- [Abstraction strength](#abstraction-strength)
- [Color masses and echo color](#color-masses-and-echo-color)
- [People](#people)
- [Architectural partial-sketch deconstruction](#architectural-partial-sketch-deconstruction)
- [Minor fixtures and texture](#minor-fixtures-and-texture)
- [Large regions and clouds](#large-regions-and-clouds)
- [Typography and film-title matching](#typography-and-film-title-matching)
- [Standalone processed composition](#standalone-processed-composition)
- [Prompt template](#prompt-template)
- [Targeted corrections](#targeted-corrections)

## Transformation Map

Diagnose the scene as `person`, `landmark`, `nature`, `street`, `crowd`, `minimal`, or `mixed`. Identify the primary subject, identity sensitivity, face clarity, recognition-critical evidence, dominant regions, and safe negative space before assigning treatments.

Before editing, assign every major region one treatment:

- photographic anchor;
- paper-realistic human treatment;
- illustrated replacement;
- flat semantic mass;
- paper omission or negative space;
- localized line notation;
- flat crowd silhouette.

Preserve recognition-critical silhouette, posture, perspective, horizon placement, directional mass, and one or two identifying features. Do not give every region equal visual intensity.

## Artistic Proposition

Write one sentence that interprets a visible relationship without inventing biography or events. Favor tensions such as person/scale, permanence/erosion, stillness/motion, shelter/exposure, order/interruption, distance/connection, nature/structure, or presence/absence only when supported by the image.

Use the proposition as a decision filter:

- **Preserve** the evidence that makes the relationship readable.
- **Omit** detail that competes with it.
- **Rebuild** a region when incompleteness or material contrast clarifies it.
- **Place the echo color** where it carries the visual or emotional turn, not merely where decoration is convenient.
- **Create negative space** near the proposition's quieter side or where copy can reinforce rather than explain the image.
- **Write copy** as a parallel voice; do not describe every visible object or add a story the image cannot support.

If no defensible tension is visible, use a modest proposition about spatial rhythm, light, weather, material, or scale. A quiet accurate proposition is better than a dramatic invented one.

## Abstraction Strength

Treat `light`, `medium`, and `strong` as measurable reconstruction tiers: `light` 30–40%, `medium` 45–60%, and `strong` 65–85% of visible artwork area. Default the first pass to `medium` and aim inside 45–60%, not at the old 30% floor. Lower to light only when identity/documentary sensitivity requires it.

Estimate coverage by visible area, not edit count. Before generation, name at least two major semantic regions whose combined target reaches the chosen tier and assign each a source-appropriate medium. A large sky/background field alone never satisfies coverage. After generation, count only areas where continuous photographic microdetail and internal surface structure have been replaced by unmistakable linework, drawing, abstract shapes, paper planes/omissions, oil-paint planes, watercolor, ink wash, or another chosen system. Do not count grading, blur, haze, grain, posterization, edge enhancement, paper texture, or filter-like painterly conversion. When uncertain, count an area as photographic.

Inspect continuous photographic corridors separately. Excluding exact identity-restoration zones, no connected photographic region may exceed 35% of the full artwork. If one does, split it through source-semantic reconstruction while preserving spatial function. Do not use blur or random blankness to satisfy the cap.

For the first-pass difference check, compare each claimed abstract region against the source and require visible change in at least two of: (1) outer or internal structure, (2) material/rendering language, and (3) boundary, omission, or plane organization. If only color, contrast, texture, or softness changed, record `O02 filter-look` immediately even when nominal area coverage appears sufficient.

Translate the selected strength into visible treatment rather than applying a global filter:

- **Light (30–40%):** keep primary identity evidence photographic while reconstructing at least two identity-safe regions.
- **Medium (45–60%):** retain selected photographic anchors while substantially replacing at least two major semantic regions.
- **Strong (65–85%):** preserve only the minimum evidence needed for identity and spatial recognition; use large unequal masses, open paper, broken planes, drawing/paint systems, displaced axes, and sparse photographic fragments.

Use the chosen level as a ceiling. A `light` result must not accidentally become a nearly complete redraw, and a `strong` result must not remain a lightly tinted photograph. Lower intensity around identity-sensitive faces, hands, contact points, text-bearing signs, and fragile landmark identifiers even when the rest of the image is stronger.

For a visible primary person, preserve approximately 95% perceptual facial identity while evaluating the artwork as one integrated whole. Keep pose, anatomy, gesture, and meaningful contact credible, but allow garment color, garment edges, peripheral hair, local lighting, texture, and silhouette transitions to change when they strengthen the composition.

Do not replace an artistically successful result with a coarse procedural remake in pursuit of pixel equality. Exact source pixels are unnecessary unless the user explicitly requests them. Compare source and final at matched face scale, correct only materially drifted identity carriers, and prioritize coherent palette, medium, edge behavior, and finish.

## Color Masses and Echo Color

Plan roughly 3–6 large, contiguous, unequal masses: sky/paper, vegetation, ground/water, landmark, person, and optionally one supporting plane. Merge minor color variations into the nearest semantic parent.

Treat source truth as evidence, not an obligation to preserve every visible element. If real clouds, distant houses, foliage fragments, signs, or other truthful details split a dominant mass and compete with the proposition, omit or merge them. Preserve only the horizon, depth cue, silhouette rhythm, weather logic, or other spatial function they contribute. For a secondary city behind a primary person or landmark, retain a low skyline and a few broad height changes while removing house-by-house, window, roof, and façade detail.

Build a source palette and record provenance for each hue. Keep skin natural and protect any color the user identifies as documentary evidence. Treat other material colors as a design starting point rather than an immovable endpoint.

Before choosing `factual`, `shifted`, or `expressive`, diagnose **palette separation** across at least three dominant masses: (1) the largest natural field such as sky, water, or vegetation; (2) the hero architecture or designed subject; and (3) the ground, podium, paving, wall, or other large support plane. Judge whether they separate clearly through hue, value, and temperature. If two or three masses are all pale, gray, low-chroma, or similarly warm/cool, record weak palette separation even when each local color is individually accurate.

Treat weak palette separation as a routing problem. Natural and living hue identities remain protected, so create the missing contrast through one or two human-built color levers. Compare these candidates before editing:

- shift the hero architecture while preserving landmark identity, value hierarchy, and source light;
- shift the designed ground, paving, podium, wall, seating, or fixtures as one coherent semantic mass;
- distribute a smaller coordinated shift across both hero and support surfaces when one change alone cannot separate all three dominant masses.

Choose the minimum intervention that produces a decisive hierarchy. A large gray-brown paved field may move to terracotta, muted brick, ochre, dusty rose, indigo, or another justified family; pale architecture may move toward warm ivory, mustard-cream, dusty coral, sage, or another controlled designed color. These are options, not presets. Test the changed built mass against the protected sky/water/vegetation and against adjacent built masses. Prefer a clear difference in at least one dimension and support from a second—hue plus value, hue plus temperature, or value plus saturation. Recolor the complete semantic region rather than adding small accent patches, and stop after one or two built levers so the image keeps a disciplined palette.

First divide the image into **natural/living** and **human-built/designed** regions.

- Natural/living: people and skin, animals, sky, clouds, sea/lake/river, vegetation, exposed natural soil, sand, snow, rock, and weather. Preserve their source hue identity. Permit only plausible neighboring changes in brightness, saturation, temperature, atmospheric depth, or scene-semantic value; do not turn a natural blue sky into an artificial cobalt field, recolor water to an unrelated hue, or impose expressive color on skin.
- Human-built/designed: hero and supporting architecture, podiums, paving, walls, benches, railings, lamps, roads, vehicles, signs, and manufactured objects. These may undergo substantial whole-region color displacement, including cream, ochre, terracotta, dusty rose, indigo, sage, or other propositionally justified families, while retaining material value hierarchy and semantic boundaries.
- Clothing/accessories: manufactured but identity-adjacent. Allow moderate palette integration; preserve user-specified, uniform, ceremonial, or identity-critical colors.

Choose a palette mode within that boundary:

- **Factual:** preserve source material families with restrained gray mixing. Use for documentary, identity-sensitive, or color-critical scenes.
- **Shifted:** move major non-skin regions toward adjacent designed families while retaining value and material logic—for example white stone to cream/ochre, gray paving to muted terracotta, blue water to indigo, or green foliage to olive/sage.
- **Expressive:** establish a deliberate 3–5 color system and strongly remap human-built architecture, paving, walls, fixtures, roads, vehicles, or designed background into conceptual families. Keep natural/living regions within source-faithful neighboring ranges; preserve skin, identity-critical garments, landmark silhouette, light direction, and readable separation between materials.

For `shifted` or `expressive`, write a semantic palette map before editing. Recolor whole human-built regions rather than sprinkling local tints. A floor, podium, long wall, or supporting skyline may become a clearly different color mass; a hero building may shift in body and shadow color as long as iconic geometry, internal value hierarchy, and separation from sky and ground remain legible. Keep natural and living regions source-faithful. Avoid indiscriminate hue rotation, rainbow fragmentation, artificial sky/water color, neon contamination of skin, or several unrelated accent systems.

Treat `robot-dreams-logic` as an explicit option and an automatic candidate. An explicit user request overrides the automatic gate but never overrides protected natural/living colors. Without an explicit request, mark the palette `candidate` only when all of these are true:

- the source palette hierarchy is weak, scattered, or dominated by similar gray/white/brown masses;
- human-built/designed color levers occupy roughly 25% or more of the artwork;
- the scene supports restrained everyday, travel, urban, interior, seasonal, nostalgic, or quietly emotional treatment;
- documentary, historical, ceremonial, uniform, brand, product, or other color-fidelity requirements do not dominate.

Reject automatic candidacy for primarily natural scenes without enough built color levers, already strong and coherent source palettes, or high-energy/neon intentions. For every candidate, write two semantic maps before generation: A=`shifted` and B=`robot-dreams-logic`. Compare palette hierarchy, emotional coherence, and subject/ground hierarchy. Select B only when it clearly improves at least two categories without weakening identity, landmark recognition, material logic, or protected natural hues; otherwise record `fallback` and use A.

When explicit or automatically selected, translate the reference into general relationships instead of literal imitation. Build a compact 4–6 color family: warm paper/sand or dusty cream as the quiet base; one softened cool family such as powder blue, slate blue, or muted teal; one softened warm family such as peach, terracotta, or mustard; charcoal rather than pure black; and no more than one concentrated emotional accent such as coral, tomato red, mustard, or clear blue. Use flat or semi-flat color regions with only 2–3 value steps, and let season, time of day, and emotional temperature choose which family dominates. Recolor complete semantic built regions, not scattered patches. Do not sample or reproduce an exact film frame, character design, or composition. The natural/living boundary remains binding, so skin, sky, water, vegetation, and terrain stay within plausible source-neighbor hues.

Treat echo color as optional. First ask whether a source hue can carry a necessary structural or conceptual turn. If not, record `none` and rely on value, material, omission, and scale. When justified, choose a less-dominant source hue and move it into one concentrated abstract line or structural system. Keep it on illustrated zones; do not falsely recolor photographic materials, scatter accents, or introduce conspicuous marks whose origin the viewer cannot understand.

Choose value range from scene meaning. Preserve quiet, historic, autumnal, academic, intimate, or overcast scenes at calm middle-to-lower values. Let open sunny travel, blue-sky seaside, snow, or celebration become cleaner and brighter. Avoid muddy indistinction and broad crushed blacks, but do not chase attention with universal exposure lift.

## People

Treat living-subject coherence as the first compositional boundary. Non-primary people, animals, birds, trees, and distinct connected plants remain fully photographic or fully abstract. A primary person may be identity-preserving integrated: keep facial identity at approximately 95% perceptual fidelity and anatomy coherent while allowing clothing, peripheral edges, color, light, and material transitions to participate in the artwork.

Assign the explicitly designated primary person first. Every other visible human figure is a secondary person by default, even when isolated or only loosely grouped. Render all secondary people with one shared opaque flat fill, crisp edges, no faces, clothing texture, individual shading, or photographic islands. Then detect clustered life: treat three or more same-category non-human subjects as a cluster when they are close enough to read together, overlap, occupy one shared ground/depth band, or repeat with a common direction and spacing. Force each cluster into one shared abstract language.

### Primary-face perceptual fidelity

Before editing, identify the primary face's identity carriers: overall proportions, eye spacing and gaze, brow, nose, mouth and expression, eyewear, hairline, ears, jaw, facial hair, and distinctive asymmetries. Preserve these at approximately 95% perceptual fidelity. Recognition must be immediate, but exact pixels, identical lighting, identical color, and unchanged texture are not required.

Reserve larger structural reinterpretation of the face for explicit `illustrated-portrait` or anime treatment. Ordinary poster treatment may still harmonize skin color, lighting, texture, and edges when the identity carriers remain stable.

When one identity carrier drifts, use localized generation or localized editing. Never use selective source blending, face patching, body patching, or source-person reinsertion. If a local edit cannot recover identity coherently, regenerate the person region or the complete image.

Source compositing is prohibited as an identity-preservation or repair method. Do not cut the original face, body, garment, or local photographic region out of the source and paste it into generated content. Inspect the face at matched scale and normal viewing size; protect recognizable facial identity while allowing the body, clothing, peripheral hair, and contour to be regenerated and artistically integrated.

Select treatment from subject importance, identity sensitivity, face clarity, requested abstraction strength, and user intent:

- **Fully photographic:** preserve the entire person, including face, skin, hair, anatomy, pose, hands, garments, accessories, contact points, and local light. Apply no paper, paint, hatch, geometric, or drawing treatment to any part of that person.
- **Fully abstract faceless:** use for distant, blurred, shadowed, obscured, or nonessential people. Rebuild the complete visible figure in one coherent graphic language, preserve head direction, posture, silhouette, clothing mass, and light, retain no photographic fragments, and do not guess facial anatomy.
- **Illustrated portrait:** enable only when the user explicitly requests illustration/anime treatment or accepts identity reinterpretation. Use restrained source-specific planes, exact proportions, and modest feature detail; avoid generic oversized-eye character design.

In photographic modes, retain genuine skin texture, natural tonal variation, joints, creases, highlights, and source lighting when resolvable. Restrained color unification is acceptable; paper grain, invented anatomy, plastic smoothing, and incoherent half-painted skin are not. In illustrated mode, redraw skin coherently in the chosen system.

For a primary photographic anchor, use the source only as a visual identity reference for the face, expression, gaze, hairline, and jaw. Inspect these at matched scale after every edit. The body, hands, garments, peripheral hair, and contact details may be regenerated, simplified, or integrated when anatomy and visual coherence remain credible. Correct facial drift through generation or localized editing, never by restoring source pixels.

Use an exterior isolation contour only when needed: thin, intermittent, softly broken, and low contrast. It may use a source-derived gray, umber, sage, or narrow paper-colored gap. Never cross the body or create a continuous white halo.

Make clustered people and secondary people clean solid pictograms. Across the entire image, use exactly one shared opaque flat fill color for every non-primary person; choose one restrained source-derived charcoal, deep umber, muted navy, or equivalent tone and do not vary its hue, value, opacity, or texture by depth or individual. Preserve only readable group extent, head/body proportion, pose rhythm, walking or standing direction, spacing, and necessary overlap. Use crisp hard outer edges with no feathering. When figures overlap, either merge them into one clean union silhouette or leave a narrow unpainted/paper-colored separation gap; never stack translucent shapes, blend colors, or allow neighboring figures to bleed together. Use no face, hair detail, garment detail, photographic texture, interior contour, shadow modeling, gradient, hatch, architectural line, pencil/graphite/charcoal sketch, paper pattern, grain, fuzzy edge, ink wash, watercolor, dry brush, stipple, or cast texture. Merge very dense groups into a few clean single-color masses rather than tracing every body.

Separate visual vocabularies by hierarchy: identity-sensitive primary people remain photographic; hero architecture may use sparse structural lines and broad reconstructed planes; all secondary pedestrians share one single-tone fill-only silhouette system. Never apply architectural construction lines, perspective hatching, sketch contours, ink wash, watercolor, or textured marks inside crowd figures. If buildings and people begin to merge, simplify people to cleaner fills and use a narrow exterior paper separation rather than adding lines or softening edges.

## Architectural Partial-Sketch Deconstruction

Activate architectural analysis whenever any recognizable architectural element is visible, regardless of whether it is the main subject or how small it is in the frame. Select one primary architectural hero when a dominant landmark or building exists. If no unique hero can be reliably identified, select one building or tightly related architectural group by visual weight, placement, scale, silhouette clarity, light, color relationship, depth, and eye-path contribution, and record it as a compositionally selected hero. Classify the selected hero by its own Chinese/East Asian or Western visual language. Do not apply hero-style sketch treatment to every visible building. Background buildings, distant towers, and urban skyline masses are secondary architecture and become linear colored abstraction or quiet source-derived silhouettes.

For the primary architectural hero only, use approximately 70% photographic reality and 20–35% colored hand-drawn architectural study, with 30% preferred, measured over the visible hero body. The concentrated zone must create the illusion of partial non-completion through missing planes, interrupted contours, unresolved joints/openings, construction axes, incomplete color blocks, or paper/sky intrusions. It must not be merely a complete photographic building with lines drawn on top. Keep the hero recognizable first. Deconstruction changes the construction/rendering state of the same building: preserve geometry, viewpoint, silhouette, façade, roof, openings, proportions, perspective, and structural continuity. Never replace it with another building, collage fragments, geometric blocks, invented openings, or foreign architectural components.

Use culturally matched colored sketch language to show an unfinished architectural study. Chinese/East Asian architecture may use ink-line structure, restrained pigment accents, translucent washes, intentional blank space, expressive roof-line studies, and hand-rendered detail. Western architecture may use architectural watercolor, colored pencil, ink-and-wash, graphite construction lines, perspective studies, and coherent stone, earth, brick, or aged-color notes. Do not default to monochrome blueprint treatment or surface-only line decoration.

Select exactly one concentrated contiguous zone on the hero's architectural body—such as one façade side, one connected roof section, one tower segment, or one connected area around windows and columns. Do not convert a uniform rectangular canvas slice, distribute isolated marks around the perimeter, or create several unrelated sketch islands. Preserve window placement, roof geometry, column positions, façade proportions, vanishing direction, and all decisive identity carriers. A real edge may continue as a drawn edge; a real window may become a sketched window in the same position. For secondary architecture, use sparse colored lines, simplified skyline bands, source-derived verticals/horizontals, and quiet silhouettes instead of localized hand-sketch zones.

Use organic transitions: dissolving edges, irregular pigment, unfinished drawing edges, watercolor bleed, gradually appearing construction lines, or photography fading into paper-like negative space. Avoid hard rectangular masks inside the building. Never duplicate or shift an architectural layer, offset windows, double roof outlines, paste façade fragments, or create detached pieces. If a sketch treatment cannot remain aligned, reduce it rather than altering the building.

Supporting architecture remains quieter than the hero in contrast, detail, edge sharpness, color variety, and mark density. Retain only its source location, skyline rhythm, overlap order, depth role, and enough directional silhouette for scene continuity. It may be directly abstracted into linear colored elements; it does not need to retain photographic cores or receive independent 20–35% sketch conversions. Do not replace it with unrelated structures or erase the skyline logic.

## Minor Fixtures, Ground, and Texture

Treat line density as an explicit trigger, not a stylistic preference. Before editing, scan architecture, ships, vehicles, street furniture, interior furniture, and designed ground for repeated windows, balconies, louvers, railings, grilles, tiles, brick joints, deck levels, portholes, lifeboats, cables, cushion rows, seat rows, and paving seams. Mark a region `forced abstraction` when the repetition does any of the following:

- produces high-frequency visual noise at normal viewing size;
- breaks an intended large color mass into many thin stripes or cells;
- becomes a second visual center through line count rather than conceptual importance;
- gives a supporting object equal or greater mark density than the hero;
- remains one of the most literal photographic regions after the rest of the poster is reconstructed.

For every triggered region, separate recognition-critical structure from compressible repetition. Preserve the outer silhouette, perspective, direction, contact/overlap role, and one or two decisive systems such as a ship's funnel plus deck break, a façade's bay rhythm, a bridge's primary truss, or a landmark's shell arcs. Merge everything else into 2–6 broad unequal planes or bands, allow large omissions, and retain only a few lines with clear weight hierarchy. The exact plane count may drop below two for a very small or occluded object, but it must still lose its repetitive inventory. Supporting objects must finish quieter than the hero in contrast, edge sharpness, color variety, and line count.

Do not satisfy forced abstraction with blur, haze, reduced saturation, paper texture, edge detection, uniformly tracing every source line, or replacing many literal lines with equally many sketch lines. The internal organization must visibly change from repeated units to large semantic structure.

Convert benches, ledges, steps, low walls, plinths, railings, tables, seats, lamps, signs, bins, cushions, and similar secondary objects or non-hero architectural elements into one localized notation family: parallel long/short strokes aligned to perspective, a few perpendicular ticks, and very few dots. Use fewer marks than source details.

Treat disposable support fixtures as complete mandatory abstraction targets. Preserve zero photographic material from the fixture and rebuild it with omission, sparse perspective notation, or 1–3 broad unequal structural planes. Integrate the primary person above it while preserving weight and contact; garment or body edges may harmonize with the abstract geometry.

This complete-abstraction rule overrides ordinary nonliving duality, photographic recognition-core requirements, contact-patch guidance, and the selected abstraction tier. Only explicit user designation of the fixture itself as a subject, landmark, product, artwork, or identity-bearing object unlocks photographic retention. After editing, inspect the complete connected fixture, including the area beneath the body. If any part retains photographic upholstery, masonry, wood grain, seams, repeated units, surface wear, or source microdetail, record blocking failure `D02 disposable-support-retention` and rebuild the entire fixture without altering anatomy, pose, hand/foot shape, or support logic.

Treat every visible pavement, promenade, road, platform, terrace, or designed ground plane as a mandatory mixed region: preserve its perspective, slope, edges, and spatial function, but create at least one contiguous abstract zone using broad planes, sparse perspective lines, controlled omission, or one restrained graphic medium. A photographic ground with only grading, blur, grain, texture, or a global painterly filter fails `G01 ground-abstraction-failure`.

Judge fixtures against source/result differentiation. If a long bench, cushion row, railing, or paved surface remains one of the most photographic regions after the primary transformation, abstract it more strongly than the overall level: merge repeated objects into 2–3 broad unequal planes, omit literal units, and retain sparse perspective rhythm. Do not let an unimportant fixture become a photographic corridor through an otherwise authored poster.

Ignore repeated details that do not explain recognition, depth, material, season, weather, movement, or narrative. Merge fallen leaves, grass blades, gravel, brick joints, paving seams, seat rows, ordinary windows, ripples, dense twigs, and fence units into a clean parent mass. Retain one localized rhythm only when it carries identity, such as a defining bridge truss or façade grid.

Treat ambiguous organic fragments on ground as fallen leaves for color inference, then remove literal leaves by default. Use one broad muted ground mass with at most 2–3 soft light/shadow zones; never replace nature with tiled, embossed, cellular, maze-like, or evenly repeated patterns.

## Large Regions and Clouds

If a low-variety region occupies about 30% or more, add a contained secondary rendering:

- sea/lake: 2–4 current bands, reflected-light path, sparse foam, selected photographic water islands;
- grass/meadow: broad wind, mowing, slope, or light bands without construction grids;
- sky: source-consistent gradient, vaporous transitions, and real-cloud flow;
- sand/snow/soil/mulch: broad terrain or accumulation planes and restrained grain;
- paving/wall: light/shadow planes and limited material rhythm.

Keep these effects inside the region and subordinate to the main subject. Reserve conspicuous straight construction lines for architecture and engineered structures.

Keep an abstracted sky chromatically unified at every strength level. Choose one source-derived dominant sky hue family and render the entire sky as one continuous field. A sunset or dawn may transition smoothly within its factual atmospheric sequence near the horizon, but it must not become separate hard-edged color zones. Use only soft gradients, vaporous same-family value changes, and source-grounded cloud flow. Do not use geometric wedges, overlapping cut-paper planes, torn polygons, isolated bands, or multiple competing blue fields in the sky; move structural fragmentation to architecture, ground, paths, or other designed/solid regions instead.

Keep cloud metaphor off by default. Enable it only when explicitly requested or when a real cloud formation makes the metaphor unusually natural and relevant. When enabled, reshape existing lobes and negative spaces without adding new clouds; preserve translucency, lighting, vaporous edges, and atmospheric scale. The form must read as cloud first, with no eyes, outlines, stickers, or solid body.

## Typography and Film-Title Matching

Use exact user wording first. Without fixed wording, select `descriptive`, `poetic`, `editorial`, or `none` from the proposition and available negative space. Use `cinematic` only when its optional module is enabled.

Generate original titles from concrete source evidence. Prefer 1–5 words and one strong device: a precise noun, active verb, spatial relation, time cue, material contrast, or restrained emotional tension. Reject titles that could fit almost any travel photograph, simply repeat the obvious subject, claim an unsupported memory or farewell, or rely on generic words such as dream, journey, beautiful, timeless, soul, or moment without source-specific meaning.

Film-title matching is an optional semantic editorial device, not a default naming step or a claim about provenance. Enable it only when requested or when the relationship is exceptionally strong. Select only an already released film whose narrative or emotional connection is visibly defensible. Verify exact title and release status. Do not select unreleased films, invent or loosely translate titles, or imply the photo contains actors or a filming location.

Use up to three typographic levels rather than requiring all three:

1. Main title: user wording first, otherwise a grounded original title; use a verified released-film title only when its module is enabled.
2. Subtitle: user wording first, otherwise an original image-semantic phrase; use a short verified film line only when the cinematic module is enabled. Never fabricate a quote or present generated prose as one.
3. Date: reliable embedded capture date, otherwise generation date.

Allow title only, title plus date, title plus subtitle, the full hierarchy, or no copy when typography would weaken the work. Preserve exact user-requested levels.

Use a minimalist editorial-magazine sans-serif with modern geometry and light/regular weight. Prefer PingFang SC Light/Regular, Source Han Sans/Noto Sans CJK Light/Regular, Microsoft YaHei UI Light, or another restrained neo-grotesk CJK family. Avoid STHeiti Medium as the preferred face, traditional Song/Ming newspaper styling unless requested, rounded cute fonts, brush calligraphy, condensed advertising faces, artificial italics, heavy bold, outlines, shadows, or glow.

Let the title carry the strongest scale, the subtitle sit at roughly 30–42% of title size with more breathing room, and the date sit at roughly 22–30%. Use compact title tracking, slightly expanded subtitle/date tracking when the renderer supports it, clean left alignment by default, and a single quiet color family derived from the image. Do not fill empty space with oversized typography merely because it is available.

Use embedded capture date before poster-generation date. Do not use filesystem modification time as capture date. Place type directly in negative space with no opaque text box. Use deterministic typography after image generation when exact glyphs matter.

## Standalone Processed Composition

Default to a source-derived editorial canvas containing two vertically stacked, equal-sized image panels: an upper photographic-led interwoven image with a source-semantic free edge, and a lower stronger abstraction in a strict rectangular frame. Both panels must share the same external width and height; only the upper panel's internal content contour is non-rectangular. Keep only a narrow intentional seam between them, normally 3–5% of the canvas height; do not create a large blank band. Never use fixed 3:5 or 5:3 composition geometry. Preserve source framing logic through proportional contain-style scaling, derive a quiet paper ground from the source palette, and retain meaningful negative space around the panels.

Use the source photograph only for analysis, identity, geometry, palette, and metadata. Never place it in the finished composition as a panel, inset, thumbnail, background, comparison strip, or visible fragment. The finished processed poster contains exactly two visible generated stages.

The upper processed stage is deliberately not an untouched original. Keep photographic depth, natural light, facial and landmark recognition, material evidence, and source geometry dominant while visibly simplifying at least two non-identity semantic regions through shared editorial color, reduced detail, coherent texture, restrained planes, or selective reconstruction. Generate or edit the complete upper scene coherently; never build it by pasting source people, faces, bodies, garments, or local photographic patches over generated content.

The lower stage must advance the same proposition, palette, spatial structure, and visual vocabulary into stronger abstraction. Preserve recognition-critical silhouettes and relationships while materially replacing most photographic microdetail. Reject two unrelated images, an untouched upper source, an upper stage as flat as the lower stage, or a lower stage that is only a graded version of the upper.

Plan the external contour from visible scene evidence. Choose one dominant contour family and at most one supporting family: canopy/branch/root/flower spread; roofline/façade/street perspective/arch; ridge/slope/valley/dune; coast/current/tide/wake/reflection; cloud flow; or person pose/garment/shadow/contact ground. Let dry brush, ink depletion, watercolor bloom, or paper fiber soften the semantic contour without replacing it. Reject generic ovals, rounded rectangles, capsules, centered blobs, uniform vignettes, ornamental scallops, random torn edges, and automatic cutout shapes.

The upper interwoven image may use a deliberately generated alpha edge or explicit semantic mask; background removal only implements that authored design. The lower panel is a complete rectangle and must not be treated as a cutout. Preserve source perspective and recognition-critical evidence inside both panels. Reject accidental holes, corner-connected deletions, missing architecture, or any boundary that cuts through one living subject.

Place selected copy as a small annotation in protected negative space between, beside, or below the two panels. Keep it under about 25% of paper width and 12% of paper area. Use explicit `fullbleed` mode when the user requests an edge-to-edge rectangular artwork; in that mode omit paper margins, comparison panels, and outer keylines.

## Prompt Template

```text
Use case: style-transfer
Asset type: abstract editorial photo poster
Scene diagnosis: <scene type; primary subject; identity sensitivity; face clarity; safe negative space>.
Artistic proposition: <one visible relationship or tension>; preserve <evidence>, omit <competition>, rebuild <region>, and place the echo color <where and why>.
Virtual/real thesis: <where photographic reality stays calm; where abstraction enters; how their contrast remains ordered>.
Paper field: <source-derived processed rectangular sheet; orientation; source-adjacent ground; upper photographic-led partial abstraction; lower strong semantic abstraction; coordinated progression>.
Semantic outer boundary: <dominant contour family; optional supporting family; paper-entry/exit points; dry-brush/ink/watercolor/paper behavior; no generic shape>.
Abstraction strength: <light / medium / strong and why>.
Abstract coverage: <tier target; at least two semantic regions and media; conservative counted percentages; exclude filter-only changes>.
Photographic corridor: <largest connected non-identity photographic region; target <=35%>.
Primary request: Recompose the source into 3–6 large semantic color masses while preserving recognition-critical relationships.
Preservation mode: <integrated reinterpretation or photographic fragment>
Living-subject integrity: <primary person identity-preserving integrated; all other living subjects fully photographic or fully abstract; keep anatomy coherent while allowing clothing/peripheral transitions>.
Secondary people: <every visible human other than the explicitly designated primary -> one identical opaque flat silhouette; no face, garment detail, texture, shading, gradient, wash, or photographic island>.
Living clusters: <detect close/overlapping/repetitive same-category non-human groups; force flock/herd/grove/flower bed into one shared fully abstract language; record any explicitly protected primary exception>.
Main person: <none / identity-preserving integrated / fully abstract faceless / illustrated portrait>; use identity-preserving integrated by default.
Identity fidelity: <approximately 95% perceptual facial fidelity; list identity carriers; allowed garment/color/edge/material integration; no pixel-equality requirement>.
Non-architectural duality: <for each major terrain/water/road region, identify photographic core, contiguous abstract zone, and source-grounded transition; exclude disposable support fixtures>.
Lower extreme abstraction: <85-100% non-photographic; broad robot-dreams color planes; sparse structural lines; simplified silhouettes; no faces, anatomy, clothing, or photographic material detail>.
Architectural treatment: <active whenever recognizable architecture is visible; select one identifiable hero or compositionally selected hero; apply approximately 70% photographic and 20-35% culturally matched colored sketch only in one concentrated contiguous hero zone; no scattered perimeter marks>.
Supporting architecture: <left-to-right inventory; distant/background buildings become linear colored abstraction, quiet silhouettes, or restrained line bands; preserve skyline rhythm and depth without independent hero-style sketch zones>.
Disposable support fixtures: <inventory every bench/chair/stool/seat/cushion/sofa/low seating wall/table; require complete abstraction and zero photographic texture; preserve support/contact through abstract geometry and coherently regenerated person integration; no source-person compositing>.
Ground planes: <inventory pavement/promenade/road/platform/terrace; require at least one contiguous abstract reconstruction zone with preserved perspective and spatial function>.
Line-density inventory: <complex built objects/regions; recognition-critical systems; repetitive systems that trigger mandatory abstraction>.
Forced line simplification: <for each triggered region, 2-6 replacement planes/bands, omissions, and maximum sparse line budget>.
Large region: <region over 30% and its contained tonal strategy>.
Crowd: <one identical opaque source-derived flat color for every non-primary person; hard edge; no texture, tonal steps, transparency, or bleed; overlap resolved by clean union or narrow paper gap>.
Palette: <source swatches>; Morandi relationship; scene-semantic brightness.
Palette contrast diagnosis: <dominant natural field vs hero-built mass vs ground/designed mass; sufficient or weak in hue/value/temperature>.
Protected natural hues: <regions kept source-neighbor plausible>.
Built color intervention: <none, or one/two complete built regions shifted; target families and the separation each creates>.
Robot Dreams auto assessment: <off/candidate/selected/fallback; built-area estimate; mood fit; color-truth risks; A shifted vs B robot comparison across hierarchy/coherence/subject-ground>.
Echo color: <source hue and exact one or two line systems receiving it>.
Optional modules: <cloud metaphor / cinematic title / illustrated portrait, or none>; include only enabled modules.
Architectural language classification: <each building -> chinese-east-asian / western / mixed-source; visual evidence; sketch medium; identity safeguards>.
Clouds: preserve source weather; no metaphor unless its module is enabled.
Typography: reserve a safe field for the selected copy levels, or preserve it as intentional negative space when copy mode is none; no generated text unless exact.
Constraints: preserve crop, perspective, anatomy, factual material colors, semantic boundaries; no watermark.
```

## Targeted Corrections

- **`S01 proposition-drift`:** remove interventions unrelated to the proposition; reconnect preservation, omission, reconstruction, echo color, negative space, and copy to one visible relationship.
- **`A01 insufficient-abstraction`:** expand source-semantic reconstruction until the chosen tier is met—light 30–40%, medium 45–60%, strong 65–85%—and recount conservatively without filters or overlays.
- **`A02 single-region-abstraction`:** add a second major semantic region with its own justified non-photographic treatment; do not rely on sky/background alone.
- **`A03 photographic-corridor`:** reconstruct enough of any oversized connected photographic region to bring it to 35% or less, excluding exact identity-restoration zones; preserve its spatial function and avoid blur/deletion.
- **`P01 identity-drift`:** restore source silhouette, anatomy, pose, face/skin evidence, garments, hands, contact points, and light according to the chosen mode; remove invented identity.
- **`P00 identity-fidelity-loss`:** compare source and final at matched face scale. Correct only the materially drifted identity carrier—proportion, gaze/eye spacing, brow, nose, mouth/expression, eyewear, hairline, ears, jaw, facial hair, or distinctive asymmetry. Aim for immediate recognition and approximately 95% perceptual fidelity; do not require exact pixels.
- **`Q00 artistic-quality-regression`:** keep the artistically stronger result. Remove any separately recreated, pixelated, posterized, coarsely quantized, generic-polygon, lower-resolution, pasted-person, or filter-derived fallback. Solve the specific identity issue locally without weakening the overall composition.
- **`P02 identity-integration-failure`:** remove halos, hard patches, mismatched sharpness, grain, color, or lighting. Blend or reconstruct clothing, peripheral hair, body edges, and local material transitions while preserving facial identity, anatomy, gesture, and contact.
- **`B01 biological-language-split`:** trace each affected non-human organism from contact point/root through its complete connected anatomy or botanical structure. Choose one treatment for the whole organism, then either restore all of it photographically or rebuild all of it in one abstract language. Do not correct only the visibly mismatched local patch.
- **`B02 living-subject-split`:** restore coherence to the affected living subject. Non-primary subjects remain wholly photographic or wholly abstract. For the primary person, preserve facial identity and anatomy while allowing controlled clothing, edge, color, light, and material integration.
- **`B03 living-cluster-retention`:** rescan same-category subjects by proximity, overlap, shared ground/depth band, and repeated rhythm. Convert every detected group into one shared abstract language and remove photographic microdetail from all members. For human groups, recolor every non-primary member with the same single opaque flat tone and merge dense groups into clean masses while preserving group extent and direction. Retain only an explicitly protected primary subject as a photographic exception.
- **`B04 secondary-person-retention` (blocking):** convert every visible human other than the explicitly protected primary person into the same opaque flat silhouette. Remove faces, clothing detail, individual shading, gradients, washes, texture, and photographic islands.
- **`V01 weak-virtual-real-contrast`:** strengthen upper-panel source-semantic abstract zones while retaining calm photographic evidence; reject both filter-like similarity and wholesale illustration that loses the productive contrast.
- **`X04 lower-panel-overphotographic` (blocking):** rebuild the lower panel as extreme semantic abstraction using broad planes, sparse lines, paper fields, and simplified silhouettes.
- **`X08 lower-panel-human-detail-retention` (blocking):** remove faces, skin, hands, anatomy, garment construction, folds, hair, and individual bodies from the lower panel; use flat silhouettes or grouped masses only.
- **`X09 lower-panel-robot-dreams-palette-failure` (blocking):** rebuild the lower panel with a selected 4-6 color robot-dreams palette, warm/cool hierarchy, 2-3 value steps, softened colors, charcoal/deep blue instead of pure black, and at most one concentrated accent.
- **`V02 architectural-balance-failure`:** restore approximately 70% photographic architectural reality and approximately 20-35% culturally matched colored architectural sketch, with 30% preferred.
- **`V03 transition-disorder`:** consolidate scattered virtual/real patches into a few source-grounded structural, shoreline, current, ridge, slope, shadow, or occlusion boundaries; remove extra media until one primary and at most one supporting abstract vocabulary remain.
- **`L01 landmark-generic`:** restore decisive identifiers, or replace outline tracing with a contiguous reconstruction of interior planes, openings, joints, washes, and structure.
- **`L02 hierarchy-conflict`:** select one hero building, restore its recognition core, then merge all nonessential architecture into one lower-contrast auxiliary medium; remove literal façade detail and competing landmark-like silhouettes.
- **`L03 architecture-erasure`:** compare source and result from left to right; restore every missing or blurred-away building at its original location and depth using the selected quiet supporting language. Preserve footprint, silhouette direction, overlaps, and spatial function without promoting it to hero status.
- **`H01 vocabulary-collision`:** keep structural lines on architecture only; convert crowds to clean single-tone solid fills with no internal marks and use only a narrow exterior paper separation where overlaps require it.
- **`H02 crowd-fill-contamination`:** replace every sketch, graphite, charcoal, ink-wash, watercolor, dry-brush, textured, translucent, multi-tone, depth-graded, or feathered crowd treatment with one identical opaque flat color. Rebuild every boundary as a crisp hard silhouette; resolve overlaps by a clean union or narrow paper-colored gap. Any second tone, internal mark, softened edge, blended overlap, or bleed remains a blocking failure.
- **`C01/C02 mass failure`:** merge fragmented patches into semantic parents; clip cross-boundary fields and restore readable seams.
- **`C04 sky-fragmentation`:** replace discrete sky polygons, wedges, ribbons, or cut-paper blocks with one continuous source-derived hue field; retain only smooth same-family atmospheric/value transitions and factual horizon warmth.
- **`C03 accent-scatter`:** remove unrelated spots and concentrate the echo color into one primary line or structural group.
- **`C05 weak-palette-separation`:** compare the dominant natural, hero-built, and ground/designed masses. Keep natural/living hue identities plausible, then shift one or at most two complete built regions until the hierarchy is clearly stronger in hue, value, or temperature. Prefer the smallest coherent intervention; do not scatter accent color or recolor protected natural regions.
- **`D01 detail-clutter`:** merge repetition into the parent mass and retain at most one identity-carrying rhythm; preserve only necessary contact patches on fixtures.
- **`D02 disposable-support-retention` (blocking):** identify the complete connected bench, chair, stool, seat, cushion, sofa, low seating wall, table, or comparable support. Remove every photographic fixture pixel, including beneath the body, and rebuild the entire object with omission, sparse perspective lines, or 1–3 broad unequal planes. Regenerate or locally edit the person coherently above it and preserve contact through abstract load-bearing geometry; never reinsert source-person pixels. Recheck the full fixture for upholstery, masonry, wood grain, seams, repeated units, wear, and source microdetail; any retained example still blocks delivery unless the user explicitly protected the fixture as a subject.
- **`D04 fixture-photographic-retention` (blocking):** remove every photographic pixel, texture, seam, cushion, upholstery, masonry grain, wood grain, or wear from the complete connected non-hero fixture, including beneath the body; preserve only abstract support and contact geometry.
- **`G01 ground-abstraction-failure` (blocking):** add a contiguous abstract reconstruction zone to every visible pavement, promenade, road, platform, terrace, or designed ground plane. Grading, blur, grain, texture, and global painterly treatment do not count.
- **`G02 ground-detail-overload`:** compress repeated paving units, stone texture, seams, and surface noise into broad semantic planes and sparse perspective lines so the ground does not compete with the hero.
- **`D03 high-line-density-retention`:** identify every complex built object or designed surface still dominated by repeated windows, rails, grilles, tiles, decks, portholes, cables, seats, or seams. Preserve only its silhouette, perspective, contact/overlap role, and one or two recognition-critical systems; compress the rest into 2–6 broad unequal planes or bands with far fewer lines. Recheck at normal viewing size that no supporting object competes with the hero through mark density.
- **`M01 unjustified-module`:** remove an unrequested or conceptually weak cloud, cinematic title, or illustrated portrait treatment. Architectural treatment is not optional when recognizable architecture is visible.
- **`M02 palette-reference-overreach`:** reduce a named reference to general palette relationships; remove copied frame-specific color placement, character/composition echoes, or implausible recoloring of natural/living regions.
- **`M03 architectural-language-mismatch`:** match the sketch medium to each building's own Chinese/East Asian or Western visual language; remove unjustified cross-cultural styling.
- **`M05 architectural-medium-replacement` (blocking):** restore the same building when the treatment introduces another architecture, foreign components, collage fragments, geometric mutation, invented openings, or a different style.
- **`M06 architectural-registration-failure` (blocking):** correct duplicated contours, shifted copies, detached fragments, offset windows, doubled roof outlines, hard rectangular masks, or pasted architectural layers by regenerating an aligned organic transition.
- **`M04 robot-dreams-auto-misfire`:** if automatic selection lacks roughly 25% built/design color levers, conflicts with color-fidelity needs, recolors protected nature/living regions implausibly, or fails to beat the ordinary shifted plan in at least two of palette hierarchy, emotional coherence, and subject/ground hierarchy, record `fallback` and restore plan A. Remove copied frame-specific placement, characters, composition echoes, and scattered accent colors; keep only a compact semantic 4–6 color relationship when B remains selected.
- **`T01 copy-generic`:** replace generic or unsupported wording with a concise proposition-grounded phrase; verify film titles and quotes when cinematic mode is enabled.
- **`T02 typography-failure`:** remove malformed glyphs or boxes, reduce optional text levels, and apply deterministic typography in safe negative space.
- **`O01 wrong-mode`:** rebuild the requested processed or fullbleed structure and remove elements belonging to another mode.
- **`O03 semantic-boundary-failure`:** replace a rectangular, automatic, generic, or accidental lower-artwork cutout with one source-grounded dominant contour family; for water scenes use coast/current/tide/wake or river-like arcs, for terrain use slope/ridge contours, for foliage use canopy contours, and for architecture use structural sections or perspective edges.
- **`O14 original-panel-retention`:** remove every visible use of the untouched source and restore exactly two generated stages in processed mode.
- **`O06 semantic-content-field-failure`:** rebuild default processed output on a source-derived editorial canvas; restore a source-semantic free-edged upper panel and a complete rectangular lower panel, removing generic ovals, rounded blobs, vignettes, automatic cutouts, fixed-ratio placeholders, and accidental holes.
- **`O09 source-geometry-distortion`:** restore proportional source scaling, remove independent x/y transforms, and prefer complete contain-style framing over aggressive crop.
- **`O10 fixed-canvas-forcing`:** recalculate the full canvas from original dimensions, aspect ratio, orientation profile, and relative section heights; use export sizes only as proportional caps.
- **`O02 filter-look`:** regenerate the first pass at the chosen tier and require each counted region to change at least two of structure, rendering language, and boundary/omission organization; color or texture change alone fails.
