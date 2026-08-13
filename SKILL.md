---
name: interweave-photo-abstraction
description: "Transform user-supplied photographs into two-stage editorial posters with an upper photographic-led partial abstraction and a lower extreme semantic abstraction. Keep the original as analysis and geometry authority only; never show it as a panel. Preserve an upper primary face at about 95% perceptual fidelity without source-person compositing, while reducing the lower primary person to a readable abstract silhouette. Use for photo posterization, virtual/real contrast, colored architectural sketch deconstruction, controlled palettes, paper-field posters, and full-bleed interpretations."
---

# Interweave Photo Abstraction

> **License notice:** This skill is licensed for personal, non-commercial use only. Whenever the skill, a modified version, or work materially created with it is published or shared, credit **LeoLittleLeo** and link to the [original GitHub repository](https://github.com/LeoLittleLeo/interweave-photo-abstraction). Commercial use is prohibited. See [LICENSE](LICENSE) for the complete terms.

Create an authored poster whose central aesthetic is **ordered interweaving of reality and abstraction**. Contrast comes from photographic and non-photographic regions entering, stopping, and reappearing across the scene. Order comes from a limited palette, disciplined boundaries, restrained media, and object-level consistency: every living subject is wholly photographic or wholly abstract, while major nonliving architecture and natural scenery deliberately contain both photographic evidence and abstract reconstruction.

## Stage Contract

Treat this contract as the single source of truth for stage behavior. Preserve the same source and semantic identity across stages; never preserve one shared rendering treatment across stages.

```yaml
stage_contract:
  upper:
    purpose: photographic-led-interweaving
    abstraction: light-to-medium
    photographic_read: dominant
    source_geometry: strict
    primary_face: approximately-95-percent-perceptual-fidelity
    hero_architecture: approximately-55-percent-photographic-plus-45-percent-colored-partial-sketch
    natural_hue_policy: source-faithful-neighboring-range
    outer_boundary: non-rectangular-free-edge
  lower:
    purpose: extreme-semantic-distillation
    abstraction: 85-100-percent-non-photographic
    photographic_microdetail: nearly-none
    source_geometry: semantically-related-but-spatially-reauthorable
    primary_face: prohibited
    primary_person: readable-abstract-human-silhouette
    primary_person_palette: maximum-two-flat-colors-no-clothing-or-body-segmentation
    hero_architecture: extreme-semantic-reconstruction
    natural_hue_policy: source-derived-semantic-family
    outer_boundary: strict-rectangle
    palette: robot-dreams-logic
```

Stage-specific rules override generic rendering rules. Upper-stage fidelity requirements must never leak into the lower extreme-abstraction stage. Lower-stage spatial freedom must never leak backward into the upper source-faithful stage.

## Global Rule Priority

1. Explicit user instruction.
2. No fabrication and semantic source identity.
3. Stage Contract.
4. Stage-specific identity and architecture rules.
5. Source geometry rules.
6. Stage Treatment Matrix.
7. Abstraction coverage.
8. Palette system.
9. Boundary and material language.
10. Typography.
11. Optional modules.
12. Decorative refinement.

## Source-Faithfulness / No Fabrication Lock

Transform what exists; do not invent a different scene. Apply faithfulness in three scopes:

- **Semantic faithfulness — global:** preserve the same person identity, architecture and landmark identity, major natural-feature identity, scene semantics, object relationships needed for recognition, and absence of fabricated major subjects. Never invent people, buildings, mountains, rivers, landmarks, or major objects.
- **Geometric faithfulness — stage-dependent:** in the upper stage preserve framing, primary-subject position, perspective, pose, major silhouette, landmark geometry, and major spatial relationships. In the lower stage permit source-aware scale, crop, spacing, axis, depth-order, negative-space, perspective-emphasis, form-placement, and semantic-mass changes. Spatial re-authoring changes representation, not semantic identity.
- **Pixel/material faithfulness — stage-dependent:** keep the upper photographic-led and identity-sensitive; make the lower 85–100% non-photographic with almost no microdetail. The lower may materially reconstruct any object while retaining enough semantic anchors to remain the same scene.

- **Primary person:** globally preserve who the person is, their source-related pose/gesture/orientation, interaction, clothing category, and scene role. Apply approximately 95% facial fidelity, expression/gaze preservation, and strict source position only in the upper stage. In the lower stage prohibit realistic face/skin and preserve the person through a readable abstract silhouette and scene relationship.
- **Architecture:** globally preserve the same building identity, building count/range, landmark-defining profile, and recognition-critical relationships. Apply exact façade/perspective alignment and the 55/45 partial-sketch balance only to the upper hero. The lower may spatially re-author architecture as extreme semantic reconstruction without inventing or substituting structures.
- **Natural landscape:** globally preserve the identity and relationships of source mountains, terrain, coast, water, vegetation masses, horizon, and major weather evidence. The upper preserves source geometry closely; the lower may recompose these features into source-derived semantic masses.
- **Objects:** do not introduce people, buildings, ornaments, birds, vehicles, furniture, vegetation, boats, lamps, signs, clouds, celestial objects, or another major object merely for balance, symbolism, storytelling, or aesthetics. Construction lines, pigment, paper texture, hatch, ink traces, and abstract color fields are allowed only when they read as rendering language rather than physical objects.
- **Occlusion and ambiguity:** preserve visible evidence, simplify uncertain regions, leave incomplete sketch marks or negative space, and softly omit ambiguity. Never complete hidden, cropped, blurred, or unclear anatomy, architecture, terrain, text, signage, or objects with unsupported detail. When uncertain, simplify rather than invent.
- **Conflict resolution:** use the Global Rule Priority and Stage Contract above; do not create local priorities that override them.

Before delivery, verify that every primary person, major building, natural feature, landmark structure, and major object maps to the source or an explicit addition request. Any untraceable major element is a blocking failure and must be regenerated or locally corrected.

## Workflow

1. Inspect the source and metadata. Diagnose the scene before choosing a style: scene type, primary subject, identity sensitivity, face clarity, tall anchors, dominant regions, palette, negative space, and reliable capture date.
2. Read [references/visual-direction.md](references/visual-direction.md). When the scene contains a living cluster, an architecture-led framed view, disposable interior furniture, or a dominant botanical group, also read [references/exemplars.md](references/exemplars.md) and inspect only the routed exemplar image(s). Use exemplars as structural and quality references, never as fixed palettes or composition templates. Then state one source-grounded artistic proposition: a relationship, tension, transition, or emotional fact that the poster will clarify. Do not invent a story unsupported by the image.
3. Write a compact strategy record using the schema below. Make preservation, omission, reconstruction, echo color, negative space, and copy all serve the proposition and remain traceable to visible evidence or an explicit user request.
4. Choose `light`, `medium`, or `strong` abstraction. Respect a user-requested intensity; otherwise use `medium` with a 45–60% reconstructed-area target. Lower only for identity-sensitive documentary portraits; raise for robust silhouettes, scenery, distant figures, or explicit permission.
5. Assign each visible living subject one coherent treatment. Use `face-locked, body-flexible, no-source-composite` for the primary person by default and `fully abstract` only for distant/nonessential faceless people or explicit identity reinterpretation. Keep facial identity and semantic pose coherent while allowing the body, clothing, peripheral hair, and edges to be regenerated or integrated.
6. Assign every major nonliving built or landscape region a controlled real/abstract division. Preserve a calm photographic recognition core and reconstruct a distinct contiguous portion; avoid tiny alternating patches. Plan 3–6 large semantic masses, a limited shared palette, one concentrated echo color at most, and only justified optional modules. For the lower panel, switch from division to extreme semantic reduction and spatial re-authoring: retain only broad color planes, sparse structural lines, re-authored forms, and the minimum recognition anchors.
7. Generate or edit each stage as a coherent whole under the Stage Contract. In upper, preserve the primary face at approximately 95% perceptual fidelity without source compositing. In lower, prohibit realistic facial content and preserve the primary person through a readable abstract silhouette.
8. Let final artistic coherence take priority outside core facial identity. Permit restrained changes to garment color, garment edges, lighting, texture, peripheral hair, body contour, and local silhouette transitions when they improve palette integration, material continuity, or the real/abstract thesis. Preserve pose, anatomy, gesture, and meaningful contact relationships.
9. Compare the upper candidate with the source at matched face scale using the upper identity rubric. Review lower personhood through silhouette, pose rhythm, and scene relationship instead. Judge both stages against their own quality gates; never repair either by pasting source pixels back.
10. Before generation, assign every visible object to exactly one treatment using the Object Treatment Lock below. Do not begin generation while secondary people, seating fixtures, and ground planes remain unassigned.
11. Generate two coordinated interpretations from the same source: an upper photographic-led partial abstraction and a lower strong abstraction. Use `scripts/inspect_photo.py` for metadata when useful. Use `scripts/compose_poster.py` in default `processed` mode to assemble exactly those two generated stages, or explicit `fullbleed` mode for one edge-to-edge interpretation. The upper stage must be supplied as a free-edged authored image and the lower stage as a complete rectangular image. Never place the untouched source in the final composition.

## Strategy Record

Before editing, record the decisions in this compact form. Omit fields that do not apply; do not expose the record unless it helps the user review the direction.

```yaml
scene_type: person | landmark | nature | street | crowd | minimal | mixed
source_orientation: landscape | portrait | near-square
layout_adaptation: orientation-aware-editorial-collage
photo_section_priority: source-integrity-first
abstract_axis_bias: horizontal | vertical | balanced
section_proportions_profile: landscape-default | portrait-adapted | square-adapted
canvas_basis: source-image-dimensions
scaling_policy: proportional-only
crop_policy: minimal-and-source-aware
fixed_master_canvas: disabled
size_policy: {basis: source, export_long_edge: adaptive, preserve_source_ratio: true, allow_upscale: limited, allow_downscale: true, allow_nonuniform_scale: false}
output_mode: processed | fullbleed
layout_profile: fixed-four-band-editorial-no-date
default_poster_mode: two-image-collage
upper_stage: photographic-led-partial-abstraction
upper_abstraction_strength: light | medium
upper_photographic_read: dominant
lower_stage: extreme-source-semantic-abstraction
lower_abstraction_strength: extreme
stage_progression: partial-to-strong
stage_generation: coordinated-whole-image-edits
primary_subject: <visible subject>
artistic_proposition: <one source-grounded relationship, tension, transition, or emotional fact>
upper_architecture_hierarchy: none | identifiable-hero | selected-hero-by-compositional-harmony
architecture_stage_plan: [<hero identity -> upper 55/45 colored partial sketch; lower extreme semantic reconstruction>]
identity_sensitivity: low | medium | high
upper_person_mode: none | face-locked-body-flexible-no-source-composite | fully-abstract-faceless | illustrated-portrait
upper_identity_fidelity_target: none | approximately-95-percent-facial-perceptual
lower_primary_person: none | readable-abstract-human-silhouette-maximum-two-flat-colors
identity_core: [<facial geometry, expression, gaze, eyewear, hairline, ears, jaw, distinctive features>]
identity_integration_allowances: [<garment color/edge, peripheral hair, lighting, texture, body-edge and silhouette transitions allowed for artistic coherence>]
abstraction_strength: light | medium | strong
abstract_coverage_target: light 30-40% | medium 45-60% | strong 65-85% | extreme 85-100%
abstract_regions: [<at least two major semantic regions and their distinct media>]
upper_largest_uncontrolled_photographic_corridor: <target at most 35%; exclude primary face and upper hero architecture>
preserved_evidence: [<recognition-critical features>]
omitted_or_rebuilt: [<regions simplified, removed, or reconstructed and why>]
semantic_masses: [<3-6 major regions when useful>]
palette_mode: factual | shifted | expressive
palette_reference: none | robot-dreams-logic-explicit | robot-dreams-logic-auto | <other explicit user reference>
robot_dreams_auto_assessment: off | candidate | selected | fallback | <built-area estimate; mood fit; color-truth risks; shifted-vs-robot comparison; lower-panel palette lock>
palette_contrast_diagnosis: <dominant natural, hero-built, and ground masses; whether hue/value/temperature separation is sufficient>
upper_protected_natural_hues: [<natural/living regions kept source-neighbor plausible>]
lower_semantic_color_relationships: [<source-derived environmental associations and warm/cool roles>]
built_color_intervention: none | [<one or two human-built regions selected as color levers -> target family and contrast purpose>]
palette_map: [<semantic region -> target color family and reason>]
stage_treatment_map: [<each object -> semantic identity; upper treatment; lower treatment>]
disposable_support_fixtures: [<every bench, chair, stool, seat, cushion, sofa, low seating wall, table, or comparable non-hero support -> fully abstract; zero photographic texture unless explicitly protected>]
ground_plane_assignments: [<each ground -> upper photographic core plus contiguous abstract zone; lower broad planes plus sparse perspective cues>]
line_density_inventory: [<each complex built object/region -> recognition-critical lines vs repetitive high-frequency lines>]
forced_line_simplification: [<non-architectural triggered object/region -> preserved identifiers and sparse planes; architecture -> preserved geometry and aligned colored-sketch marks>]
stage_visual_vocabulary_limit: <per stage: one primary abstract medium plus at most one supporting medium; upper and lower treatments remain distinct>
echo_color: none | <source hue and conceptually necessary destination>
optional_modules: [<only justified modules>]
architectural_treatment: inactive | active
architectural_family: none | chinese-east-asian | western | mixed-source
architectural_recognition_skeleton: [<smallest source-derived set that preserves identity: roof/tower/façade axis/arch, column, window or eave rhythm/landmark profile>]
upper_architectural_sketch_zone: <one concentrated contiguous zone on the upper primary hero; target approximately 45% of visible hero body; no scattered edge marks>
architectural_detail_compression: [<repeated windows, columns, ornaments, seams, or trim -> fewer readable structural rhythms>]
architectural_contour_continuations: [<real source contour -> aligned colored drawn continuation across the real/sketch boundary>]
architectural_color_structure: [<source-derived roof/façade/tower/depth/light planes -> visible wash, pencil, pigment, or color block role>]
upper_secondary_architecture_treatment: linear-colored-abstraction | quiet-silhouette
lower_architecture_treatment: extreme-semantic-reconstruction
upper_architectural_medium: culturally-appropriate-colored-architectural-sketch-with-unbuilt-deconstruction
title_text: <processed default required unless copy-free or subtitle-only requested>
subtitle_text: <processed default required unless copy-free or title-only requested>
fullbleed_typography_layout: lower-left | bottom-centered | source-aware-quiet-zone
processed_typography_layout: centered-fixed-title-and-subtitle-bands
processed_band_font_size: identical-for-title-and-subtitle
typography_family: book-serif | humanist-serif | restrained-editorial-serif
processed_typography_color: warm-white-on-black
fullbleed_typography_zone: <protected source-aware negative-space region>
copy_mode: none | poetic | editorial | cinematic
content_field_boundary: <dominant semantic contour; supporting contour; paper-entry/exit points; edge material>
content_field_occupancy: <target 68-82% of paper area; justified exception>
editorial_collage_layout_landscape: {upper_board: 52%, title_band: 4%, lower_panel: 40%, subtitle_band: 4%, top_date_band: removed, panel_size_relation: upper-larger}
editorial_collage_layout_portrait: {upper_board: 52%, title_band: 4%, lower_panel: 40%, subtitle_band: 4%, top_date_band: removed, panel_size_relation: upper-larger}
editorial_collage_layout_square: {upper_board: 52%, title_band: 4%, lower_panel: 40%, subtitle_band: 4%, top_date_band: removed, panel_size_relation: upper-larger}
upper_artwork_board_occupancy: 65-85%
text_hierarchy: {date: omitted, title: upper-board-bottom-band-required, subtitle: lower-panel-bottom-band-required}
```

## Rule Priority

Typography is subordinate to the primary subject, real/abstract composition, major color masses, and negative-space structure. It completes the layout and guides the eye toward its exit point; it must never become the primary visual entry point.

### Object Identity Lock and Stage Treatment Matrix

Before generation, inventory the scene from foreground to background and left to right. Preserve each object's semantic identity across stages, but assign its rendering separately for upper and lower. Never require the same rendering treatment in both generated stages.

```yaml
object_identity_lock:
  semantic_identity: shared-across-stages
  source_relationships: shared-where-recognition-critical
  rendering_treatment: stage-specific

stage_treatment_matrix:
  primary_person:
    upper: face-locked-body-flexible-no-source-composite
    lower: readable-abstract-human-silhouette-using-one-or-two-flat-colors-without-clothing-or-body-segmentation
  secondary_people:
    upper: one-shared-opaque-flat-silhouette
    lower: simplified-grouped-semantic-masses-or-shared-flat-silhouettes
  hero_architecture:
    upper: approximately-55-percent-photographic-plus-45-percent-colored-partial-sketch
    lower: extreme-semantic-architectural-reconstruction
  secondary_architecture:
    upper: linear-colored-abstraction-or-quiet-silhouette
    lower: simplified-structural-masses-and-sparse-lines
  seating_fixtures:
    upper: fully-abstract-zero-photographic-retention
    lower: extreme-semantic-plane-or-omission
  ground:
    upper: photographic-core-plus-contiguous-abstract-zone
    lower: broad-semantic-planes-plus-sparse-perspective-lines
  sky_water_terrain:
    upper: source-faithful-controlled-abstraction
    lower: extreme-semantic-abstraction-with-source-derived-recognition-cues
```

In the upper stage, every non-primary person uses one shared opaque flat silhouette; every disposable support is fully abstract; and every designed ground plane contains a contiguous reconstruction zone. In the lower stage, apply the matrix's stronger semantic reduction while preserving only the recognition-critical identity and relationships required by the Stage Contract. If a stage-specific assignment is not visibly executed, regenerate or locally re-edit that stage.

### Non-negotiable

- Preserve user-designated unchanged regions according to their explicit scope. Apply strict anatomy, position, perspective, and landmark geometry to upper; apply semantic identity and readable source relationships to lower.
- **Ordered real/abstract thesis:** make the virtual/real relationship visible at first glance. The result must contain meaningful photographic evidence and meaningful non-photographic reconstruction; neither may collapse into a full-frame filter, an almost untouched photograph, or an almost unrelated illustration. Use a few large contiguous decisions, not confetti-like alternation.
- **Stage-scoped living-subject unity:** in upper, keep each living subject anatomically coherent and apply the face-locked mode to the primary person. In lower, preserve semantic organism/personhood and source relationships through abstract silhouettes or masses; do not require photographic anatomy or facial fidelity.
- **Stage-scoped clustered life:** detect clusters globally, then render them by stage. Upper clusters use one coherent abstract language; lower clusters become simplified grouped semantic masses or compatible shared silhouettes. The protected upper primary person may remain an exception.
- **Upper crowd single-tone lock:** every upper non-primary person uses exactly one shared opaque flat fill color with crisp edges and no internal detail.
- **Lower secondary-person treatment:** lower non-primary people become simplified grouped semantic masses or shared flat silhouettes; they do not inherit the upper single-tone rendering requirement unless that choice supports the lower composition.
- **Upper nonliving duality:** every major upper non-architectural engineered or landscape region should visibly combine one calm photographic recognition region with one contiguous abstract reconstruction region. Upper hero architecture follows its 55/45 partial-sketch rule. Lower nonliving regions follow extreme semantic reconstruction instead.
- **Boundary discipline:** for non-architectural regions, place real/abstract transitions on source-grounded seams—structural joints, perspective axes, shorelines, currents, ridges, slopes, shadow edges, or occlusion boundaries. Architectural transitions follow the dedicated organic sketch-boundary rules and must not become hard rectangular masks.
- **Stage-specific vocabulary restraint:** within each stage, use one primary abstract medium and at most one supporting medium. Keep the two stages compatible in palette and proposition but distinct in rendering treatment; do not force upper media onto lower or lower flattening onto upper.
- **High-line-density forced abstraction:** for non-architectural objects, compress repeated lines into broad unequal planes and sparse structural marks. For architecture, preserve the recognition skeleton and compress repeated windows, columns, seams, trim, ornament, and surface texture into a few readable rhythms. Do not describe every unit one by one or replace the building with generic planes. Transition the selected connected region into culturally appropriate colored architectural lines, washes, construction marks, and unfinished color while retaining the source roof geometry, façade axis, openings rhythm, column rhythm, proportions, and perspective.
- **Tiered abstract coverage:** materially reconstruct `light` at 30–40%, `medium` at 45–60% (default upper-stage target), `strong` at 65–85%, and `extreme` at 85–100% of the lower panel's visible artwork area. The extreme lower panel must use broad semantic color planes, sparse structural/contour lines, paper fields, and re-authored abstract forms, with almost no photographic microdetail. Global grading, desaturation, blur, haze, posterization, paper/canvas texture, grain, sharpening, or whole-frame painterly filters do not count.
- **Lower-panel primary-person silhouette and two-color lock:** when the source has a primary person, preserve a clearly human, immediately legible approximation of the source pose, orientation, body proportion, gesture, and dominant outer silhouette. Render the complete figure with one or at most two flat colors total. Do not use different colors to distinguish garments, garment layers, skin, limbs, torso, joints, anatomy, lighting, or body structure. If two colors are used, treat the second as one restrained compositional accent or edge/overlap aid across the figure, not as descriptive segmentation. Remove real skin, facial features, hair strands, garment folds, fabric texture, gradients, tonal modeling, and photographic shading. Personhood must come from the outer silhouette, pose, gesture, and head/torso/limb relationship—not internal color coding.
- **Lower-panel palette lock:** the lower panel must use `robot-dreams-logic` as a selected palette, not merely as an optional candidate. Use 4–6 softened colors, warm/cool opposition, 2–3 value steps per semantic mass, charcoal/deep blue instead of pure black, and at most one concentrated accent. Reject naturalistic color scattering, random neon, realistic skin tones, global grayscale, and generic painterly color treatment.
- **Multi-region transformation:** distribute counted abstraction across at least two major nonliving semantic regions—for example architecture plus ground, water plus terrain, shoreline plus supporting buildings, or road plus built fixtures. A single large flat sky or background field cannot satisfy the requirement by itself. Fully photographic living subjects are exempt from abstraction but do not reduce the coverage target for the remaining composition.
- **Upper photographic-corridor cap:** apply the <=35% cap only to uncontrolled continuous environmental photographic corridors across the upper composition. It does not override the upper primary-face identity region or the designated upper hero architecture governed by its 55/45 rule. Do not apply this cap to the lower stage, whose 85–100% non-photographic contract already controls photographic retention.
- **Upper architectural hierarchy lock:** identify one upper-stage hero building when architecture is present. Apply the approximately 55% photographic plus 45% colored partial-sketch treatment only to that upper hero, in one concentrated contiguous zone. Treat upper secondary architecture as quiet linear colored elements or simplified silhouettes. This balance must never constrain lower architecture.
- **Stage-scoped architectural identity:** in the upper stage preserve the hero's source location, footprint, silhouette, viewpoint, perspective, façade geometry, window/column rhythms, roof geometry, proportions, and recognition skeleton. In the lower stage preserve only the same architectural semantic identity, minimum recognition skeleton, and source-derived structural relationships; permit extreme reconstruction, spatial re-authoring, broad color planes, and sparse structural lines. Neither stage may replace the source architecture with unrelated structures.
- **Disposable support fixtures — zero photographic retention by default:** classify every non-hero bench, chair, stool, seat, cushion, sofa, low wall used as seating, table, or comparable furniture/support surface as disposable. Rebuild it completely in one abstract language. Integrate the person above it while preserving anatomy, weight, and contact; garment or body edges may blend into the artwork, but the fixture retains no photographic material unless explicitly protected.
- **Stage-scoped ground lock:** upper ground requires a photographic core plus one contiguous reconstruction zone with preserved perspective and spatial function. Lower ground uses broad semantic planes and sparse source-derived perspective cues.
- **Upper primary-face perceptual fidelity:** preserve approximately 95% of the upper primary face by visual comparison, not raw pixel equality. This target never applies to lower, where realistic face and skin are prohibited.
- **Face-locked, body-flexible integration:** treat the face as the protected high-fidelity region. Preserve expression, gaze, semantic pose, overall body coherence, and meaningful contact relationships, but allow clothing, hair outside the identity-critical hairline, shoulders, arms, legs, shoes, body contour, peripheral anatomy, local light, material, and color to be regenerated, stylized, simplified, or mildly deformed. The priority order is: facial identity; expression/gaze; pose and body coherence; absence of compositing artifacts; scene integration; artistic coherence; garment/body-edge fidelity; exact source pixels.
- **No Source-Person Reinsertion:** never preserve or repair a person by cutting the original person, face, body, garment, or local photographic region out of the source image and compositing it back into the generated artwork. Do not use source compositing, source-pixel restoration, cutout reinsertion, face patching, body patching, or local source patches as identity-repair methods. Identity preservation must be achieved through generation or localized editing, not source-pixel reinsertion. If the face is insufficiently recognizable, regenerate or locally re-edit the face/person region; do not paste the original face or person back. A slightly stylized or imperfect body edge is preferable to any accidental compositing artifact.
- **Intentional boundary versus compositing failure:** an intentional thin white sticker outline, paper-cut silhouette edge, graphic contour, controlled editorial halo, or cut-paper treatment is acceptable when it is uniform, deliberate, and integrated with the visual language. Misaligned cutouts, duplicated contours, shifted person layers, double edges, partial body offsets, mismatched source patches, body/background seams caused by compositing, pasted-face artifacts, pasted-person artifacts, and floating source-photo fragments are prohibited.
- **Upper 95% identity rubric:** assess only the upper face at matched scale and normal viewing size. Pass when it is immediately identifiable and no major carrier is materially wrong. Never use this rubric on lower.
- **Visual-master priority:** the strongest artistically coherent result is the delivery candidate. Never replace a successful image with a pixelated, posterized, coarsely quantized, lower-resolution, generically masked, or separately recreated fallback in pursuit of technical identity equality.
- This living-subject rule does not apply to non-individual continuous scenery such as sky, water, terrain, mountain, shore, or a grass field treated as one ground mass; these are nonliving scene structures and should carry the controlled half-real/half-abstract relationship.
- Use generation or localized editing only, according to which method best preserves facial identity without weakening the artwork. Source compositing and deterministic source-person restoration are prohibited, including as a fallback or emergency repair. Do not require deterministic full-person restoration.
- Do not invent facial anatomy, provenance, locations, quotations, or capture dates. In the upper stage keep living and natural hues within plausible source-neighbor ranges. In the lower stage preserve source-derived color relationships, warm/cool hierarchy, semantic separation, and recognizable environmental association rather than literal local color. The lower `robot-dreams-logic` contract overrides upper natural-local-color fidelity but never authorizes random unrelated color.
- **Protected-nature contrast routing:** diagnose natural, built, and ground masses together. If separation is weak, route contrast through coherent built-region color notes or the architectural sketch medium while preserving architectural identity, material logic, and light direction. Do not recolor architecture as scattered patches.
- Keep each large color field within one semantic region. Do not wash across architecture, sky, ground, water, people, or another major subject.
- **Unified-sky field:** treat the entire visible sky as one continuous natural color field. Preserve one source-derived dominant hue family across the sky; allow only smooth same-family value, temperature, or atmospheric gradients and source-grounded cloud transitions. Never split an abstracted sky into multiple discrete large polygons, cut-paper blocks, ribbons, wedges, or unrelated color fields. Reserve hard-edged plane fragmentation for built structures and designed surfaces, not open sky.
- Keep exact final lettering legible. Add it deterministically when image generation cannot render it reliably.
- **Source-derived canvas geometry:** preserve the user's original image geometry first and adapt the poster around it. Read the source width, height, and aspect ratio before allocating any band or abstract section. The source dimensions are the composition basis; fixed `1800×3000`, `3000×1800`, `3:5`, or `5:3` master canvases are disabled. Fixed export dimensions may exist only as proportional long-edge limits, bounding caps, or metadata-failure fallbacks and must never control source-image geometry.
- **Proportional scaling only:** never stretch, squeeze, widen, flatten, or independently scale the source on x and y. Preserve the full authored upper contour with assertive contain-style placement. The upper authored image must occupy approximately 65–85% of the upper board area, with 75% preferred, while retaining its irregular alpha contour. The lower rectangular stage must use aspect-ratio-preserving cover placement and may crop modestly and source-aware to fill its panel completely.
- **Default four-band editorial field:** unless the user explicitly requests `fullbleed`, derive the canvas from source geometry using `52 / 4 / 40 / 4`: upper warm-paper board, black title band, lower rectangular abstraction panel, black subtitle band. Remove the date band entirely and reassign its space to the upper board. The lower artwork fills its complete panel edge-to-edge with no internal margins or letterboxing.
- **Content-boundary semantics:** derive one dominant outer contour and at most one quieter supporting contour from visible evidence: canopy/branch fall for foliage, roofline/façade/street perspective for architecture, ridge/slope/dune for terrain, tide/current/coast/wake for water, cloud flow for sky-led scenes, or pose/gesture/shadow/contact-ground for person-led scenes. Dry brush, ink depletion, watercolor bloom, and paper-fiber disappearance may soften this structure but cannot replace it. Alpha or an explicit mask implements the design; color-based edge-keying never chooses it.
- **Upper-panel color-preservation lock:** never derive the upper panel's alpha by removing a sampled paper/ground color when that color also occurs inside the artwork. Warm ivory architecture, white clouds, pale skin, highlights, water glints, and paper-like reconstructed planes must remain fully opaque and color-identical after compositing. Prefer an authored semantic alpha mask (painted from the outer contour only) or generate the upper panel with a true transparent background. If neither is available, keep the upper panel RGB and use a conservative outer contour mask; do not use `remove_chroma_key.py`, `--background-removal edge-key`, or any flood-fill keyed by a sampled color. Always compare the isolated upper RGB against the composited upper panel at matched scale; reject any hue/value shift or pale-region deletion.

### Default strategies

- In the upper stage, apply a natural/built color boundary: keep people, animals, sky, clouds, water, vegetation, and terrain source-neighbor plausible while routing stronger shifts through built regions. In the lower stage, follow the Stage Contract's source-derived semantic color relationships and mandatory `robot-dreams-logic` palette instead of literal local-color fidelity.
- When the dominant natural, architecture, and ground colors cluster too closely, do not accept a low-impact factual palette by default. Compare at least three candidate interventions—shift the hero architecture, shift the designed ground/fixtures, or split the adjustment across both—and choose the smallest coherent built-region change that creates clear figure/ground separation. Favor complementary temperature, useful value separation, or controlled saturation contrast; avoid arbitrary neon, equal-intensity competition, and hue changes that weaken landmark identity.
- Inventory every living subject before editing. Detect clusters first and assign each cluster one shared `fully abstract` language; then assign isolated non-primary subjects `fully photographic` or `fully abstract` and the primary person `face-locked, body-flexible, no-source-composite`. Keep facial identity, semantic pose, and biological continuity coherent while allowing controlled regeneration and transitions through clothing and peripheral body edges.
- **Upper auto-candidate `robot-dreams-logic` palette:** for upper palette selection only, evaluate Robot Dreams against ordinary `shifted` color when the source has weak palette hierarchy and sufficient built/design levers. Select it only when it improves at least two of palette hierarchy, emotional coherence, and subject/ground hierarchy without weakening upper identity, landmark recognition, material logic, or protected natural hues; otherwise use `fallback`. Lower does not use this auto gate because its Robot Dreams palette is mandatory.
- **Upper monochromatic-scene palette expansion:** when upper is effectively monochromatic, compare a restrained expressive Robot Dreams plan against a conservative shifted plan. Route added color through source-supported atmosphere, reflected light, wet surfaces, clouds, architectural planes, or designed ground while preserving upper source geometry and natural/living plausibility. Lower independently follows its mandatory semantic Robot Dreams contract.
- Use scene-semantic brightness. Favor calm middle-to-lower values for quiet, historic, intimate, autumnal, or overcast scenes; allow brighter values for sunny, snowy, seaside, summer, or celebratory scenes.
- Build a few unequal semantic masses. Use an echo color only when it carries a necessary structural or conceptual turn; otherwise set it to `none`. Never add accent marks merely because a source hue is available.
- Partially deconstruct prominent tall nonliving anchors while retaining decisive silhouette, spatial role, and one or two identifying features. Make the intervention legible through one contiguous reconstructed zone, large omissions, and a few hierarchical marks; do not substitute all-over sketch texture for deconstruction.
- In the upper stage, select one hero building or coherent architectural group by dominance or compositional harmony. Apply the same-building 55/45 colored-sketch treatment only to one concentrated contiguous region of that upper hero. Deconstruct it as partially unbuilt through omissions, unfinished planes, broken structural continuations, construction axes, and paper/sky intrusions aligned to source perspective. Upper supporting architecture receives linear colored abstraction or quiet silhouettes. Lower architecture follows its extreme semantic contract instead.
- Fully abstract disposable support fixtures by default, even when their texture appears visually quiet or helps explain contact. Inventory every bench, chair, stool, seat, cushion, sofa, low seating wall, table, and comparable support before editing; assign the entire fixture a zero-photographic-retention treatment. Preserve contact logic through abstract geometry and a coherently generated or locally edited person above it, never through a photographic patch of the fixture or source-person reinsertion.
- Omit or strongly merge non-architectural source elements when they fragment the intended semantic masses without supporting recognition or the artistic proposition. Never apply this omission rule to recognizable architecture: architectural identity, geometry, and structural continuity take priority.
- Give a dominant low-variety region contained value bands or material rhythm; keep construction-line language mainly on architecture and engineered structures.
- Run the architectural hierarchy and alignment inventory before generation and again after the first pass. Select one identifiable hero or, when necessary, one compositionally selected hero by visual harmony; record its recognition skeleton, repeated-detail compression plan, contour continuations, and source-derived structural color map; define one concentrated sketch zone inside its body; and route all secondary architecture to linear colored abstraction or quiet silhouettes. Check the hero's silhouette, façade axis, roof geometry, opening/column rhythms, proportions, vanishing direction, structural continuity, and thumbnail legibility. A real edge may continue as an aligned colored drawn edge, but no duplicated, shifted, perimeter-scattered, decorative, faint monochrome, or structure-free contour is acceptable.
- Reduce clustered pedestrians and nonessential secondary pedestrians to one coherent single-tone silhouette system. Use exactly one shared opaque flat fill across all such people in the image; preserve only group range, density, proportion, pose rhythm, direction, spacing, and necessary overlap. Use crisp hard edges, merge collisions into clean union masses or open a narrow paper-colored separation gap, and allow no face, garment detail, tonal depth steps, transparency, hatch, paper grain, sketch texture, ink/watercolor wash, photographic islands, internal modeling, or edge bleed.
- Keep hierarchy classes visually distinct. Do not give secondary people the structural line language used for architecture. Assign photographic texture to identity anchors, sparse structural marks to selected built forms, and solid fill-only silhouettes to crowds.

### Architectural Partial-Sketch Deconstruction

Activate this treatment only for recognizable architecture in the **upper stage** of `processed` mode (and analogous photographic-led architecture in `fullbleed` when appropriate). The architectural 55/45 balance is an upper-stage rule only and must never constrain the lower extreme-abstraction stage. Lower architecture follows the Stage Contract and Stage Treatment Matrix.

Follow this architectural principle: **preserve the recognition skeleton, compress repeated detail into rhythms, let selected real contours continue into the abstract region, and make visible color function as architecture rather than decoration.** This refines the current partial-sketch concept; it does not authorize a Gathered Scenes layout, generic paper collage, full flat cut-paper building, contour-only conversion, torn-paper architecture, or full-building zine simplification. Keep the same source architecture mostly built in photographic reality, with approximately 30% still existing as a culturally appropriate colored architectural study.

#### Recognition Skeleton and Structural Compression

Before choosing the sketch zone, identify the hero building's **recognition skeleton**: the smallest set of source-derived structural features that makes it read as that specific architecture. Depending on the source, include the roofline; tower, spire, dome, gate, pavilion, balcony, ridge, or eave profile; façade axis; major wall planes; vertical segmentation; dominant structural diagonal; arch, column, window, lattice, or balcony rhythm; and landmark-defining silhouette. Preserve in this order: (1) recognition skeleton, (2) perspective and spatial alignment, (3) major silhouette, (4) key structural rhythms, and (5) only the secondary detail needed for recognition.

Compress detail without destroying identity. Merge repeated windows into a window rhythm, columns into a column rhythm, and trim, brick seams, carving, ornament, roof units, or repetitive façade texture into one or two legible structural cues. Do not render dense units one by one. Use fewer, clearer decisions that remain readable at thumbnail scale; never let compression become a generic abstract patch.

Before editing, classify each visible architectural element as `chinese-east-asian`, `western`, or `mixed-source`. Match both line behavior and color construction to the building itself. For Chinese/East Asian architecture, preserve eaves, tiled-roof silhouette, dougong logic when visible, gate/pavilion form, wooden-column rhythm, and lattice rhythm; simplify repeated decoration; use elegant line, wash, negative space, and restrained source-consistent mineral/pigment color to construct roof and structural planes. For Western architecture, preserve tower/dome/roof massing, façade axis, arch/window rhythm, and column grouping; simplify repeated ornament; use architectural watercolor, colored pencil, ink-and-wash, and visible stone-, earth-, brick-, or aged-color planes. If traditions coexist, treat each building in its own language. Never hybridize Chinese and Western sketch languages unless the source architecture itself is hybrid.

For the upper primary architectural hero, preserve approximately 55% photographic reality and convert approximately 45% into a colored hand-drawn architectural study. Communicate partial non-completion through structural omissions and interrupted construction, not merely surface linework. Upper secondary architecture does not receive this balance. In the lower stage, reconstruct the same architecture almost entirely non-photographically using its minimum recognition skeleton, source-derived structural relationships, broad color planes, and sparse lines; do not preserve a 55% photographic body.

#### Contour Continuation, Color as Structure, and Partial Non-Completion

Let selected source contours continue naturally across the real/sketch boundary: a photographic roofline into the same colored drawn roofline, a tower edge into its aligned sketch edge, an arch into the same colored contour, a real window row into a compressed sketched rhythm, or an eave into an unfinished study of that eave. Preserve direction, perspective, alignment, line flow, silhouette, and rhythm so the result reads as one continuous building in two rendering states—built reality crossing into drawn possibility—not a pasted drawing, detached overlay, local filter, or hard effect mask.

Use visible color as a mandatory load-bearing part of the primary hero's sketch zone. Build roof planes, façade planes, tower massing, depth steps, arch groups, eaves, and light-facing versus shadow-facing structure with watercolor washes, colored-pencil shading, gouache-like blocks, pigment accents, restrained planes, translucent fields, or architectural color notes. A few dark construction lines may support the study, but black graphite, gray tracing, monochrome outline, or technical black-and-white blueprint treatment alone fails. The viewer must immediately read a **colored architectural sketch**. Derive color direction from the source architecture, material, light, atmosphere, and surrounding palette; use color to continue actual forms and planes. Do not add bright color merely for liveliness or scatter decorative accents without structural purpose.

Use the colored sketch to depict an unfinished construction state rather than a finished building covered with lines. Select one concentrated contiguous zone based on visual logic—such as a connected façade side, roof section, tower segment, or structural bay group. Within it, use at least two deconstruction signals: incomplete color filling, open or interrupted contours, unresolved openings or joints, visible construction axes, unfinished painted edges, missing planes, paper-like gaps, transparent intrusions, soft wash transitions, or color blocks that stop before completing the form. Keep every cue aligned to the source recognition skeleton. Do not scatter marks around the perimeter, create isolated decorative patches, convert multiple unrelated zones, or turn a uniform rectangular slice of the canvas into a sketch. Secondary architecture instead becomes linear colored abstraction with sparse source-derived outlines, perspective strokes, structural rhythms, and simplified skyline bands.

Structural alignment is mandatory. Preserve perspective, recognition skeleton, silhouette, façade geometry, opening and column rhythms, roof geometry, architectural proportions, vanishing direction, and structural continuity. Never duplicate and shift an architectural layer, paste façade fragments, offset windows, double roof outlines, or create a detached overlay. Prioritize structural continuity, clean alignment, thumbnail legibility, and intentional colored abstraction over literal micro-detail reconstruction.

Use an organic transition: dissolving edges, brush-like boundaries, irregular pigment, unfinished drawing edges, watercolor bleed, sparse construction lines appearing gradually, or photography fading into paper-like negative space. Avoid hard rectangular masks inside the building unless explicitly required by the composition. Do not apply the treatment to people, faces, trees, sky, vehicles, roads, mountains, or water merely because architecture is present; non-architectural elements may interact softly with the boundary only for integration.

At reduced viewing size, require the main silhouette, dominant structure, real/sketch transition, and visible structural color to remain legible. If the study is faint, monochrome, overly detailed, fragmented, ornamental, or dependent on micro-lines, reduce the marks, enlarge meaningful color planes, and strengthen one or two defining contours.

Apply these stage-scoped priorities under the Global Rule Priority:

```yaml
upper_architecture_priority:
  1: source-architectural-identity
  2: recognition-skeleton
  3: perspective-and-structural-alignment
  4: approximately-55-percent-photographic-reality
  5: approximately-45-percent-colored-partial-sketch-deconstruction
  6: detail-compression
  7: organic-transition
lower_architecture_priority:
  1: same-architectural-semantic-identity
  2: minimum-recognition-skeleton
  3: source-derived-structural-relationship
  4: extreme-abstraction
  5: spatial-re-authoring
  6: broad-color-planes
  7: sparse-structural-lines
```

Avoid black-only pencil treatment, gray monochrome tracing, literal one-by-one detail copying, decorative crosshatching, random nonstructural color, pasted overlays, hard effect masks, generic abstract patches, lost silhouettes, misaligned continuation, Chinese-Western hybrid motifs without source justification, duplicated contours, invented structures or openings, and abstract geometry that destroys readability.
- **Cloud metaphor:** default `off`. Enable only when the user requests it or an existing cloud formation makes the metaphor unusually natural. Never add clouds merely to create a motif.
- **Cinematic title:** default `off`. Enable when requested or when a released-film connection is exceptionally strong and verifiable; otherwise use user wording or a source-grounded original title.
- **Illustrated/anime portrait:** explicit-only. Never select it solely because a face is front-facing. Enable only when the user requests illustration/anime treatment or clearly accepts identity reinterpretation.

## Abstraction Strength

Use `light`, `medium`, or `strong` for upper/fullbleed intervention planning. The default processed lower stage always uses the Stage Contract's `extreme` 85–100% non-photographic tier.

- **`light` — 30–40%:** retain most identity/documentary evidence, but reconstruct at least two identity-safe semantic regions. Prefer for sensitive portraits, complex contact points, or fragile landmarks.
- **`medium` — 45–60% (default):** retain selected photographic anchors while replacing substantial portions of at least two major regions with semantic masses, drawing, paint, ink, paper omission, or partial landmark reconstruction. The first generated pass must target this range, not the 30% floor.
- **`strong` — 65–85%:** rely on large masses, paper omissions, broken planes, displaced axes, drawing/paint systems, and sparse photographic anchors. Use for robust silhouettes, scenery, distant figures, or explicit requests.

## Person Modes

- **Upper `face-locked, body-flexible, no-source-composite`:** default for an upper primary person. Preserve approximately 95% perceptual facial identity, expression, gaze, hairline, jaw, source-related pose, and contact; allow clothing, peripheral hair, body contour, peripheral anatomy, local lighting, texture, and silhouette transitions to be regenerated or integrated. Never paste source pixels back.
- **Lower `readable-abstract-human-silhouette`:** prohibit realistic face, skin texture, facial features, hair strands, garment microdetail, gradients, anatomical color coding, and photographic shading. Preserve a clearly human silhouette, approximate source pose, orientation, gesture, head/torso/limb relationship, recognizable body rhythm, and scene relationship using one or two flat colors total. Do not assign separate colors to clothing layers or body parts. A sparse contour may support readability only when it uses one of those same two colors. The approximately 95% facial target does not apply to lower.
- **`fully-abstract-faceless`:** use only for distant, blurred, shadowed, obscured, or nonessential people. Rebuild the whole visible person in one coherent graphic language while preserving direction, posture, silhouette, clothing mass, and light; retain no photographic islands and invent no facial features.
- **`illustrated-portrait`:** this is the only mode allowed to unlock and redraw a primary face. Use only after explicit user intent for illustration/anime treatment and accepted identity reinterpretation. Preserve source-specific proportions, pose, garments, hands, light, and recognizable cues; avoid generic character design.
- Select among these modes from subject importance, identity sensitivity, face clarity, requested intensity, and user intent. Back-facing direction alone does not authorize identity reinterpretation.
- In face-locked mode, retain natural skin character and source-specific facial proportions while allowing restrained tonal and material integration. Avoid invented facial anatomy, plastic smoothing, generic facial replacement, or inconsistent rendering across facial features. The body may be simplified or regenerated when this improves visual coherence.
- Inspect the face at matched scale and normal viewing size. Correct drift in the smallest relevant identity carrier—eye/gaze, nose, mouth/expression, eyewear, hairline, jaw, or face proportion—without automatically restoring the whole person.
- Avoid accidental separation. Let garment and body edges participate in the composition through controlled blending, recoloring, texture, reconstruction, or an intentional thin sticker/paper-cut/graphic contour. A deliberate stylized edge is acceptable; a compositing artifact is never acceptable.

## Editorial Copy and Date

1. Use exact user-provided wording whenever the user supplies fixed text. In `processed` mode, omit date copy entirely: do not create a date strip, top timing area, reserved date space, or date text inside the upper board. An explicitly requested date may appear only in `fullbleed` mode as ordinary subordinate copy.
2. Otherwise derive one concise title from visible subject relationships, light, movement, distance, time-of-day impression, structural axis, spatial tension, or a meaningful source-color relationship. Prefer a restrained metaphor grounded in visible evidence. Avoid generic words such as `Memory`, `Dream`, or `Moment` unless specifically justified; avoid travel-advertising language, camera terminology, grand narratives, and arbitrary location labels.
3. In `processed` mode, default to both a 2–5 word main title and a 2–5 word subtitle. Omit both only for an explicitly copy-free result; omit one level only when the user explicitly requests one text level. In `fullbleed` mode, one main title may be the default when additional copy would weaken the artwork.
4. In the default four-band layout, center the title in the black band below the upper board and the subtitle in the black band below the lower panel. Use exactly the same font size for both lines. If either line is too long, reduce one shared size until both fit; never shrink only one line.
5. If the user requests film-title matching or the optional cinematic-title module is justified, select only a semantically fitting released film and verify its exact title and release status. Do not imply that the photo depicts the film, actors, or filming location.
6. Use an `elegant restrained editorial serif` by default. For architecture, city, and structural scenes use a composed book serif with stable proportions and restrained contrast. For nature, light, and lyrical scenes use a fine humanist serif with lighter visual weight. Do not default to bold commercial sans serif, advertising typography, cartoon fonts, exaggerated handwriting, decorative display fonts, or oversized all-caps.
7. In `processed`, use restrained warm-white serif text in the two black bands. In `fullbleed`, choose a subordinate source-derived dark or light hue with sufficient contrast.
8. In `processed`, do not reserve artwork negative space or search for text positions; the two fixed bands own typography. Reserve an artwork typography zone only in `fullbleed`.
9. Apply the following placement choices only in `fullbleed`:
   - **Lower-left editorial alignment:** use when the subject or visual weight is right-biased, the composition extends horizontally, and stable lower-left space exists. Keep the text approximately 6–9% from the left and bottom edges.
   - **Bottom-centered editorial alignment:** use when the subject is near center, the building or composition has a clear central axis, the visual relation is relatively symmetrical, and stable lower space exists. Align the title with the visual axis without placing it close to the subject or abstract motif.
   - **Source-aware quiet zone:** use another position only when it has explicit support from the visual weight, axis, motif position, or eye-path exit. Never choose a corner solely because it has the lowest edge density.
10. Keep typography clearly subordinate. At normal viewing size it must be legible but must not become the first visual entry point. Do not enlarge the title merely because the quiet area is large. Use no decorative rules, icons, fake metadata, high-contrast headline blocks, or multiple competing font families.

## Output Modes

### Two-Image Collage — Default

Unless the user explicitly requests `fullbleed` or another output mode, `processed` uses the fixed four-band editorial collage:

```text
[ upper warm-paper board containing a non-rectangular interwoven image ]
[ black main-title band ]
[ lower rectangular highly abstract image ]
[ black subtitle band ]
```

This is an integrated diptych with editorial text bands, not a before/after comparison, postcard, social-media grid, or two unrelated blocks. The upper panel is the primary authored image: photographic-led, source-semantic, richer, and bounded by a free-edged non-rectangular contour. It is never the untouched original. The lower panel is a strict rectangle and a materially stronger abstraction of the same scene, subject, structure, or proposition. It must be a deeper abstraction layer rather than a crop, duplicate, or lightly altered copy.

### Editorial Collage Hierarchy

Do not treat the stages as equally weighted stacked blocks. Use the asymmetric `52 / 4 / 40 / 4` hierarchy. Inside the 52% upper board, the authored image must occupy 65–85% of the board area, with 75% preferred. Reject timid thumbnail-like placement and edge crowding that destroys the free contour. The lower artwork must cover its complete panel edge-to-edge with preserved aspect ratio, modest source-aware cropping when needed, and no internal margins, letterboxing, stretching, or squeezing.

The panels share the same source, proposition, semantic identities, and source-derived palette relationships, but they must use different stage-specific rendering treatments: `upper = photographic-led interweaving`; `lower = extreme semantic distillation`. The upper panel carries the main identity, landmark, and scene-reading burden. The lower panel is supporting and must not dominate.

**Original-image exclusion is non-negotiable:** the uploaded photograph is an analysis, geometry, palette, identity, and metadata reference only. It must not appear as a panel, inset, thumbnail, comparison strip, background layer, or visible source fragment in the finished poster. Both visible image sections must be newly generated or coherently edited interpretations.

Before constructing this system, read `original.width` and `original.height`, compute the source aspect ratio, classify orientation, and derive the complete collage canvas from that source geometry plus relative section heights. Do not create a fixed poster canvas first and force the source into it. The upper stage preserves the source ratio, framing logic, subject placement, landmark identity, perspective, and major spatial structure through proportional contain-style scaling. The lower stage keeps the source-derived canvas ratio and semantic anchors, but may substantially recompose spatial arrangement, scale, depth, direction, negative space, and relationships between masses. Width and height parameters are export caps, not composition dimensions.

### Upper Panel — Interwoven Main Image

The upper panel is not the untouched original photograph. Generate or edit the complete scene as one coherent image with a light-to-medium intervention while keeping photography as the dominant read.

- Preserve facial identity, expression, gaze, pose, landmark identity, framing, perspective, light direction, and major object relationships.
- Permit unified editorial color, paper/gouache texture, simplified crowd language, reduced microdetail, broad designed-ground planes, and selective architectural reconstruction.
- Keep enough photographic surface, tonal depth, material evidence, and natural light that the viewer reads it first as a transformed photograph rather than a flat illustration.
- Do not create it by placing cut-out source people, faces, bodies, garments, or local source patches over generated content. Generate or locally edit the whole scene coherently.
- Apply the same palette and material family used below so the two stages feel authored together.
- When architecture is present, make its approximately 45% partial-sketch zone visibly colored at first glance through colored pencil, watercolor, gouache-like patches, washes, colored linework, and source-derived architectural study tones. Black or gray construction lines may support but must not dominate the upper-stage architectural study.
- Use a source-semantic, free-edged, non-rectangular outer contour; do not render the upper panel as a clean rectangular box.
- Preserve the main recognition anchors and allow the upper panel to carry the primary identity and landmark burden.

### Lower Panel — Rectangular Extreme Abstraction

The lower panel materially advances the same scene into **extreme semantic abstraction**. It is a strict rectangular image field and should read primarily as a composed system of broad color planes, sparse contour/structural lines, paper fields, and re-authored semantic forms. It is not required to preserve the source's original spatial pattern or literal spatial continuity. Reconstruct the space to clarify the proposition: allow changes in scale, cropping, depth ordering, axis, perspective emphasis, object spacing, form placement, negative space, and the balance between foreground, middle ground, and background. Preserve only enough source-derived semantic anchors for the lower panel to remain recognizably related to the same scene—for example, the Opera House shell rhythm or landmark mass, a water/terrain directional cue, a re-authored figure mass or grouped semantic form, a ground or horizon gesture, and one or two source-specific structural relationships. These are continuity cues, not instructions to trace or preserve the original silhouettes. Remove photographic microdetail almost completely.

The lower panel must not visibly contain human faces, realistic skin, detailed hands, garment construction, clothing folds, fabric texture, hair strands, or photographic shading. When a main person exists, preserve a clearly readable human silhouette, approximate body contour, pose, gesture, orientation, and head/torso/limb relationship using one or at most two flat colors across the complete figure. Do not use color changes to explain clothing hierarchy or anatomy. Never reduce the person to an unreadable blob or pure non-human mass. Secondary people become re-authored grouped marks or unified semantic masses. Seats, cushions, furniture, paving, windows, and repeated architectural detail become broad planes, omissions, or sparse lines.

The lower panel uses a strict `robot-dreams-logic` palette lock. Use a restrained warm/cool system with softened blue, warm ivory, muted peach/coral or tomato, dusty mauve/lilac, charcoal/deep blue, and warm off-white as appropriate to the source. Route colors through complete semantic masses, not scattered accents. Do not use naturalistic local colors, realistic skin colors, photographic shadows, global black-and-white treatment, random neon, or a generic painterly filter. The palette must feel like a deliberate robot-dreams color construction: 4–6 coherent colors, 2–3 value steps per mass, warm/cool hierarchy, charcoal instead of pure black, and at most one concentrated accent.

The lower panel normally uses the `extreme` tier, stronger than `strong`: target approximately 85–100% non-photographic semantic reconstruction. It must not merely zoom into, repeat, or remain too photographic compared with the upper panel. If a lower-panel element can be identified mainly by clothing, facial features, material texture, or photographic shading, abstract it further.

**Progression is non-negotiable:** the upper section must be visibly transformed but photographic-led; the lower section must be visibly extreme, graphic, and semantically distilled. Reject untouched-original upper sections, an upper and lower panel with similar rendering density, a lower person with photographic anatomy or clothing detail, a lower person that no longer reads as human, or two unrelated interpretations.

- **Landscape source:** keep the upper photographic region wider and shallower, permit a more horizontally extended abstract motif, and preserve horizontal movement.
- **Portrait source:** make the photographic region visibly taller, preserve portrait reading, and avoid a shallow horizontal strip. The lower abstraction may reorganize the vertical axis, headroom, footroom, and subject-to-blank-space relationship when a spatial reconstruction improves the proposition; retain only a source-derived height cue or silhouette relationship when needed for recognition.
- **Near-square source:** balance the photo and abstract sections without mechanically choosing the landscape profile; let the abstract axis follow the source's strongest relationship.

For portrait sources, prioritize source integrity in the upper stage and poster geometry over template regularity. Mild cropping is allowed in the upper stage; do not stretch, compress, severely horizontal-crop, or unnaturally truncate a person, building, tower, tree, doorway, column, mountain, or other tall subject there. The lower abstract motif may crop, reorder, resize, or reposition these semantic masses and may alter the source's vertical axis, height hierarchy, and subject-to-blank-space relationship, provided it remains a deliberate reconstruction of the same scene rather than an unrelated image.

**Orientation adaptation is non-negotiable:** keep the four-band system, but adapt panel proportions and geometry to source orientation. Portrait images must remain portrait-led compositions; landscape images may extend horizontally; near-square images should be balanced without mechanically forcing a landscape template. Never stretch or compress a panel to fit a fixed template.

### Typography in Two-Image Collage

Use the fixed four-band typography layout: upper warm-paper board, black main-title band, lower full-bleed panel, black subtitle band. Omit date entirely in `processed` mode; there is no date strip, date area, or reserved date space. Title and subtitle are required unless the user explicitly requests a copy-free result. Each text band is approximately 4% of the complete canvas height. Render title and subtitle at one identical font size selected to fit both strings. Typography must remain legible and subordinate.

**Source geometry is non-negotiable:** preserve the user's original image geometry first; adapt the poster around it. Fixed export size may exist, but fixed composition size must not control the source image.

Selectable modes:

- **`processed` — default:** orientation-adaptive photographic-led partial abstraction above and stronger abstraction below.
- **`fullbleed` — edge-to-edge treatment:** one complete rectangular interpretation.

When the user asks for a poster or processed result without specifying a mode, use `processed`.

## Identity Review

For every visible **upper-stage** primary face, inspect the final artwork beside the source at matched face scale and at normal viewing size. This review does not apply to the lower stage, where realistic facial content is prohibited. Use this order:

1. Confirm immediate recognizability.
2. Compare face shape/proportions, gaze and eye spacing, brows, nose, mouth and expression, eyewear, hairline, ears, jaw, facial hair, and distinctive asymmetries.
3. Require no major identity carrier to be materially wrong. Treat approximately 95% fidelity as a perceptual art-direction target, not a biometric calculation or pixel-difference threshold.
4. Permit neighboring changes in skin color, lighting, texture, edge softness, and material treatment when they support the final palette and do not alter identity.
5. Permit broader transformation of clothing, garment edges, fabric texture, peripheral hair, body-edge transitions, and local silhouette details when anatomy, gesture, and contact remain credible.
6. Prefer localized generation or editing when one facial feature drifts. Do not use source blending, face patches, body patches, or source-person reinsertion. Regenerate the person region or the complete image if necessary.

The bundled `verify_identity_lock.py` is not an identity-repair method. Do not use it to justify exact pixel preservation, source-person reinsertion, or compositing; facial recognizability and visual coherence take priority over exact body pixels.

### Person Conflict Priority

When person-related requirements conflict, resolve them in this order:

1. facial identity;
2. expression and gaze;
3. anatomical and visual coherence;
4. absence of compositing artifacts;
5. scene integration;
6. artistic coherence;
7. garment and body-detail fidelity;
8. exact source-pixel fidelity.

Exact source-pixel fidelity is always the lowest priority. Preserve the face, regenerate the person, and never paste the person back.

Inspect metadata:

```bash
python scripts/inspect_photo.py input.jpg
```

Compose final files with the two generated stages. Pass `--font /path/to/font.ttf` when automatic cross-platform CJK font discovery cannot find a suitable font. Use `--background-color` only when the automatically derived source-adjacent ground needs an explicit override.

In default `processed`, pass both `--title` and `--subtitle`; `--date` is unsupported. Use `--copy-free` only for an explicitly copy-free request. Use `--single-text-level title` or `--single-text-level subtitle` only when the user explicitly requests one level. `--text-position` is fullbleed-only. Long Chinese or Latin titles wrap automatically up to `--max-title-lines 3`, but keep each band one or two lines maximum.

For the lower abstract artwork, use the safest available background mode:

- `--background-removal alpha` (default): use an existing alpha channel; keep an RGB image rectangular rather than guessing.
- `--background-removal edge-key`: remove only corner-like paper connected to the image edge. Add `--mask-preview` to inspect the derived mask.
- `--background-removal mask --art-mask mask.png`: use an explicit white-foreground/black-background mask.
- `--background-removal none`: preserve the complete rectangular artwork.

For the upper artwork, treat transparency as geometry, never as color removal. The preferred order is: (1) a model-generated RGBA upper image with an authored outer contour; (2) a deterministic explicit white-foreground/black-background contour mask passed with `--background-removal mask --art-mask`; (3) an RGB upper image placed on a paper field only when the artwork itself already contains the paper field. Do not use `--background-removal edge-key` on pale, warm, white, cream, or sky-heavy upper images: it can key out the Opera House, clouds, highlights, or other legitimate interior pixels and cause the upper panel to change color after composition. If a mask is created locally, inspect its preview and verify that all interior alpha values are opaque, especially over identity-critical face/skin, architectural shells, clouds, and light ground planes.

Default fixed four-band collage output:

```bash
python scripts/compose_poster.py \
  --mode processed \
  --original input.jpg \
  --upper-poster partial-abstraction.png \
  --poster strong-abstraction.png \
  --title "Exact main title" \
  --subtitle "Short lower-band subtitle" \
  --output-dir outputs
```

In `processed` mode, `--upper-poster` supplies the complete photographic-led partial abstraction and `--poster` supplies the stronger lower abstraction. The compositor uses the asymmetric fixed four-band profile: 52% upper warm-paper board, 4% black main-title band, 40% lower panel, and 4% black subtitle band. It fits the visible alpha-shaped upper artwork toward 75% board occupancy and rejects inputs that cannot reach the required 65–85% range without clipping or distortion. The lower artwork uses aspect-ratio-preserving cover placement to fill its complete rectangular field. The untouched `--original` remains the geometry and metadata authority; it is not pasted into the upper section. Use `fullbleed` when the artwork itself must define the exact rectangular canvas.
By default, `compose_poster.py` reads the original image dimensions and derives the final canvas from them. `--width` and `--height` are optional export bounding caps only; they never define a fixed composition canvas or permit non-uniform scaling. `--export-long-edge` is an adaptive proportional output limit and defaults to `3000`; pass `--export-long-edge 0` when the uncapped source-native derived size is required.
`--text-position` applies only to `fullbleed`. Processed typography is always centered in its fixed title and subtitle bands; do not run corner search, quiet-zone placement, or artwork-negative-space placement in `processed`.

## Quality Gate

- **`S01 proposition-drift`:** every major intervention supports the source-grounded artistic proposition; no decorative motif competes with it.
- **`R01 recognition-loss`:** the source remains recognizable through large relationships and preserved evidence rather than copied microdetail.
- **`A01 insufficient-abstraction`:** upper counted reconstruction misses its chosen light/medium/strong tier, or lower misses its 85–100% non-photographic contract. Exclude filter-like tonal/texture changes.
- **`A02 single-region-abstraction`:** upper counted abstraction does not span at least two major semantic regions. Lower is instead evaluated for complete extreme semantic reconstruction across its visible field.
- **`A03 upper-photographic-corridor`:** no uncontrolled continuous upper environmental photographic corridor exceeds 35% of the full upper artwork area; exclude the primary-face identity region and upper hero architecture governed by its 55/45 rule. Do not apply this gate to lower.
- **`C01 mass-fragmentation`:** the scene reads as a few coherent semantic masses.
- **`C02 boundary-crossing`:** color fields remain inside their semantic regions.
- **`C04 sky-fragmentation`:** upper sky loses its continuous source-neighbor atmospheric field, or lower sky loses recognizable environmental association under source-derived semantic color relationships. Lower need not preserve literal same-family local color.
- **`C03 accent-scatter`:** the source-derived echo color is concentrated, visible, and subordinate.
- **`C05 weak-palette-separation`:** upper fails to improve separation through coherent built-region interventions while protecting source-neighbor natural hues, or lower fails semantic separation within its Robot Dreams hierarchy.
- **`L01 upper-landmark-generic`:** the upper hero must retain decisive identifiers while converting one concentrated approximately 45% region into a culturally appropriate colored sketch. Lower is evaluated by semantic identity and minimum recognition skeleton, not this balance.
- **`L02 hierarchy-conflict`:** one dominant hero building remains unmistakable; supporting architecture is materially quieter, simpler, lower-contrast, and does not compete through literal detail or a second incompatible style.
- **`L03 architecture-erasure`:** in upper, preserve recognizable architecture at its source location, footprint, silhouette, viewpoint, and perspective. In lower, permit spatial re-authoring but require the same architectural semantic identity, minimum recognition skeleton, and source-derived structural relationships. In either stage reject replacement by unrelated structures.
- **`L04 recognition-skeleton-loss` (blocking):** upper loses the hero's full recognition skeleton or lower loses the minimum recognition skeleton needed to identify the same architecture.
- **`L05 architectural-detail-undercompression`:** repeated windows, columns, brick seams, trim, carving, ornament, or façade texture are copied one by one and overwhelm the building's graphic read. Compress them into fewer source-aligned structural rhythms without changing architectural identity.
- **`P01 stage-person-contract-drift`:** upper fails its face/pose/contact fidelity requirements, or lower fails its readable abstract silhouette while retaining prohibited realistic face/skin/material detail.
- **`P00 upper-identity-fidelity-loss` (blocking):** the upper primary face is not immediately recognizable at approximately 95% perceptual fidelity, or a major identity carrier is materially wrong. Correct the smallest failing upper facial feature without source compositing. Never apply this gate to lower; lower realistic facial content is prohibited.
- **`Q00 artistic-quality-regression` (blocking):** a technically safer or more source-faithful revision is materially worse as an artwork through pixelation, posterization, coarse quantization, generic masking, pasted-person edges, lower resolution, weakened palette, or lost semantic structure. Keep the artistically stronger version and solve only the specific identity issue.
- **`P02 identity-integration-failure`:** an upper person appears accidentally pasted, patched, mismatched, or anatomically broken, or a lower silhouette loses coherent personhood. Regenerate the relevant stage; never repair by source compositing.
- **`P03 source-person-reinsertion` (blocking):** any original person, face, body, garment, or local photographic region is pasted into either generated stage. Preserve upper facial identity through generation or localized editing; build lower personhood through non-photographic silhouette construction.
- **`B01 biological-language-split`:** every non-human living individual or connected organism uses one coherent treatment across its complete visible body. No tree mixes photographic trunk/branches with abstract foliage; no animal or bird mixes photographic anatomy with graphic body regions. Reclassify the whole organism as photographic or abstract and restore/rebuild it consistently before delivery.
- **`B02 living-subject-split`:** within each stage, a non-primary organism uses one coherent treatment. For the upper primary person, require coherent anatomy and facial identity; for lower, require coherent abstract personhood without realistic face or material detail.
- **`B03 living-cluster-retention`:** a detected cluster retains photographic miniatures or loses its group identity. In upper, use one shared abstract language; in lower, use grouped semantic masses or compatible shared silhouettes.
- **`B04 upper-secondary-person-retention` (blocking):** an upper non-primary person retains a face, garment texture, photographic detail, individual modeling, or differs from the one shared opaque flat fill. Lower secondary people are evaluated against the lower grouped-mass treatment instead.
- **`V01 weak-virtual-real-contrast`:** both photographic evidence and authored abstraction are materially visible; the result is neither an almost unchanged photograph nor a nearly unrelated full illustration.
- **`V02 upper-architectural-balance-failure`:** the upper hero architecture does not retain approximately 55% photographic reality plus one concentrated approximately 45% colored partial-sketch zone. Never apply this gate to lower architecture, which should be extremely reconstructed.
- **`V03 transition-disorder`:** upper real/abstract boundaries ignore source structure or scatter competing media. Lower may re-author boundaries but must keep coherent semantic masses and source-derived relationships.
- **`P04 human-layer-offset` (blocking):** reject any duplicated person edge, shifted silhouette, partial body offset, non-overlapping source and generated body section, visible cutout seam, compositing offset, floating source-photo fragment, pasted face, pasted body, or mismatched resolution/noise/exposure in the human figure. Slight clothing-edge deformation, body-edge simplification, painterly body transition, white sticker outline, graphic contour, and paper-cut boundary are allowed only when deliberate and visually coherent. If this gate fails, regenerate the person region or the complete image; do not apply additional source compositing.
- **`H01 vocabulary-collision`:** architecture, identity anchors, and secondary people use distinct visual vocabularies; crowd silhouettes contain no architectural line work.
- **`H02 upper-crowd-fill-contamination` (blocking):** upper non-primary people do not use one identical opaque flat color with crisp boundaries. Correct upper overlaps by clean silhouette union or a narrow paper gap. Do not apply this identical-fill gate to lower grouped semantic masses.
- **`D01 detail-clutter`:** nonessential fixtures and repetitive textures are simplified.
- **`D02 disposable-support-retention` (blocking):** in upper, every disposable support is fully abstract with zero photographic material; in lower, reduce it further to an extreme semantic plane or omission. Preserve source-related support/contact logic in each stage.
- **`D04 fixture-photographic-retention` (blocking):** any connected portion of a non-hero seating fixture retains photographic upholstery, leather, wood grain, seams, cushion detail, masonry texture, wear, or surface microdetail. Rebuild the complete fixture in one abstract language, including the body-contact zone, while preserving only support geometry and contact logic.
- **`D03 upper-architectural-line-misalignment`:** upper sketch lines, washes, openings, roof studies, or construction marks are not aligned with source geometry and perspective. Do not apply exact registration requirements to lower spatial re-authoring.
- **`G01 ground-abstraction-failure` (blocking):** upper ground lacks its contiguous reconstruction zone, or lower ground fails to become broad semantic planes with sparse source-derived perspective cues.
- **`G02 ground-detail-overload`:** repeated paving units, stone texture, seams, or surface noise dominate the ground and compete with the hero. Compress them into broad planes, sparse perspective lines, controlled omissions, or one restrained graphic medium.
- **`M01 unjustified-module`:** optional modules appear only when enabled and propositionally relevant.
- **`M02 palette-reference-overreach`:** a named palette copies exact frames, characters, or composition. In upper, keep natural/living hues source-neighbor plausible; in lower, require source-derived semantic relationships under Robot Dreams rather than literal local fidelity.
- **`M03 upper-architectural-language-mismatch`:** the upper colored sketch language does not follow the source building's Chinese/East Asian or Western family. This partial-sketch-language gate does not apply to lower extreme reconstruction.
- **`M05 architectural-medium-replacement` (blocking):** either stage replaces source architecture with a different building or invented components. Upper changes rendering state only; lower may radically change form placement and geometry emphasis while retaining the same semantic identity and minimum recognition skeleton.
- **`M06 upper-architectural-registration-failure` (blocking):** the upper transition contains duplicated contours, shifted copies, detached fragments, offset openings, hard masking, or pasted layers. Lower spatial re-authoring is allowed but must remain semantically source-derived.
- **`M07 upper-architectural-zone-dispersion` (blocking):** the upper hero sketch treatment is scattered or split into decorative patches. Consolidate it into one contiguous zone; lower has no partial-sketch-zone requirement.
- **`M10 upper-architectural-surface-decoration` (blocking):** the upper hero region only has lines over a complete photograph and does not communicate partial non-completion. This gate does not apply to lower.
- **`M11 architectural-color-structure-failure` (blocking):** especially in the upper stage, the hero sketch zone reads primarily as black graphite, gray tracing, monochrome outline, or a faint technical drawing; or its color is decorative and unrelated to form. Rebuild clearly visible source-derived color as roof/façade/tower/depth/light structure using coherent washes, colored pencil, pigment, gouache-like patches, or restrained planes.
- **`M12 upper-contour-continuation-failure` (blocking):** upper real architectural contours stop arbitrarily, restart misaligned, or meet a detached drawing. Continue them with matching direction and alignment. Lower does not require a photographic/sketch transition.
- **`M13 upper-architectural-thumbnail-legibility`:** at reduced size the upper silhouette, real/sketch transition, or colored nature of the study is unclear. Lower is judged by minimum recognition skeleton instead.
- **`M08 upper-secondary-architecture-overprocessing`:** upper secondary architecture receives the hero's partial-sketch treatment or retains too much photographic detail. Lower secondary architecture follows simplified masses and sparse lines.
- **`M09 upper-hero-selection-failure`:** no upper hero is identified by source dominance or compositional harmony when architecture is present.
- **`M04 robot-dreams-auto-misfire`:** for upper automatic palette selection, Robot Dreams lacks sufficient built/design levers, weakens source truth, or fails its comparison against `shifted`. Lower Robot Dreams is mandatory and is instead evaluated by `X09` for coherent source-derived semantic color relationships.
- **`T01 copy-generic`:** original copy is specific to the source and proposition; quotations and cinematic references are verified.
- **`T02 typography-failure`:** in processed, title and subtitle are exact, centered, legible, refined, subordinate warm-white serif copy at exactly the same font size inside their dedicated black bands; if fitting is necessary, reduce one shared size rather than either line independently. No date or artwork-position search is permitted. In fullbleed, keep selected copy subordinate and source-aware without covering critical evidence.
- **`O01 wrong-mode`:** processed two-image collage and fullbleed deliveries follow their respective composition rules.
- **`O03 semantic-boundary-failure`:** the upper architectural sketch boundary or other authored content boundary is generic, rectangular, arbitrary, or misaligned with source geometry. The lower panel itself remains a complete rectangle; its internal abstraction must still express the scene's dominant structure.
- **`O14 original-panel-retention` (blocking):** the untouched source photograph appears anywhere in the finished composition as a panel, inset, thumbnail, comparison strip, background, or visible source fragment. Remove it and restore exactly two visible generated stages: photographic-led partial abstraction above and stronger abstraction below.
- **`X01 panel-redundancy`:** the lower panel is too similar to the upper panel in structure, abstraction depth, or visual role.
- **`X02 weak-abstraction-escalation`:** the lower rectangular panel is not materially more abstract than the upper panel.
- **`X03 upper-panel-rectangularization`:** the upper panel loses its free-edged, non-rectangular authored identity.
- **`X04 lower-panel-overphotographic` (blocking):** the lower panel retains too much photographic detail and fails to read as an extreme abstraction of broad color planes, sparse lines, paper fields, and simplified silhouettes.
- **`X08 lower-panel-human-readability-failure` (blocking):** when a primary person exists, lower reduces that person to an unreadable blob, loses personhood, or breaks the head/torso/limb relationship, orientation, pose, gesture, or approximate body contour. Rebuild a clearly human, source-related silhouette using one or at most two flat non-photographic colors.
- **`X15 lower-primary-person-color-oversegmentation` (blocking):** the lower primary person uses more than two colors, gradients or tonal modeling, or assigns different colors to clothing layers, skin, limbs, torso, joints, or anatomical structure. Collapse the complete figure to one or two flat colors and recover readability through silhouette and pose rather than internal color separation.
- **`X09 lower-panel-robot-dreams-palette-failure` (blocking):** the lower panel does not use a coherent 4–6 color `robot-dreams-logic` system with warm/cool hierarchy, softened colors, 2–3 value steps, charcoal/deep blue instead of pure black, and at most one concentrated accent. Rebuild the palette through complete semantic masses.
- **`X05 diptych-incoherence`:** the two panels do not feel like one unified poster or one shared proposition.
- **`X06 processed-copy-placement-failure`:** processed title or subtitle leaves its dedicated black band, is not centered, or is replaced by quiet-zone/corner placement. A missing level fails unless the user explicitly requested copy-free or one-level copy.
- **`X07 role-reversal`:** the lower panel dominates the composition or the upper panel fails to remain the primary visual entry point.
- **`X10 excessive-band-or-gap`:** a text strip becomes a large empty area, an unintended gap appears between a panel and its adjacent text band, or any top date/timing space remains. Keep title and subtitle bands at 4%, attach them directly to their panels, use a 52% upper board and 40% lower panel, and reject internal lower-panel margins.
- **`X11 asymmetric-panel-hierarchy-failure` (blocking):** the upper board is not 52% and visibly larger than the 40% lower panel, the removed date-band space is not absorbed into the upper board, or the composition reads as a mechanical 1:1 split. Restore the `52 / 4 / 40 / 4` hierarchy without distorting either artwork.
- **`X13 lower-panel-full-bleed-failure` (blocking):** the lower rectangular artwork does not cover its complete panel edge-to-edge, contains internal margins or letterboxing, or is stretched/squeezed. Refit it with aspect-ratio-preserving cover placement and modest source-aware cropping.
- **`X14 upper-authored-image-underoccupancy` (blocking):** the visible alpha-shaped upper artwork occupies less than 65% or more than 85% of its 52% board, feels like a timid floating insert, or is enlarged through clipping, stretching, or rectangularization. Refit toward 75% visible board occupancy while preserving the complete irregular contour and proportional geometry.
- **`X12 upper-alpha-color-shift` (blocking):** the upper panel changes hue/value after being placed in the collage, or pale interior artwork (warm ivory architecture, clouds, highlights, skin, or paper planes) becomes transparent/gray because a sampled background color was keyed out. Rebuild the alpha from the authored outer contour only, use an explicit mask or true RGBA generation, and compare isolated versus composited RGB before delivery. Never repair this by recoloring the whole upper panel.
- **`O06 semantic-content-field-failure`:** the upper panel uses a generic rectangle or arbitrary blob instead of a source-semantic free-edged contour, or the lower panel is not a strict rectangle.
- **`O07 orientation-adaptive-collage-failure` (blocking):** the two-image collage ignores source orientation, flattens portrait subjects, severely crops tall anchors, or forces either panel into a rigid template.
- **`O08 fixed-band-role-inconsistency` (blocking):** default `processed` output does not use the fixed four-band order and proportions—52% upper warm-paper board, 4% black main-title band, 40% full-bleed lower panel, and 4% black subtitle band—or retains any date band/date area, misplaces a band, or allows text to drift into an image panel.
- **`F01 major-content-fabrication` (blocking):** a person, major object, building, landmark structure, or natural feature cannot be traced to visible source evidence or an explicit user request. Remove or regenerate it; never retain invented content for composition, symbolism, or aesthetics.
- **`F02 unsupported-person-replacement` (blocking):** the primary person changes semantic identity, age/gender presentation, source-related pose/gesture/orientation, interaction, clothing category, or is replaced, multiplied, or given unsupported accessories. Enforce strict position and facial identity in upper; permit lower spatial re-authoring and facial removal under the Stage Contract.
- **`F03 unsupported-structure-completion` (blocking):** architecture, anatomy, landscape, text, signage, or objects hidden, cropped, blurred, or ambiguous are confidently completed with unsupported detail. Simplify, omit, use negative space, or leave incomplete marks instead.
- **`O09 source-geometry-distortion` (blocking):** the complete poster canvas and upper stage must preserve the original aspect ratio and source framing logic. Reject non-uniform x/y scaling, stretching, squeezing, widening, flattening, or fixed-placeholder fitting in the canvas and upper stage. The lower stage may use source-aware crop, recomposition, spatial rearrangement, scale shifts, altered depth ordering, and a different perspective emphasis when these serve the artistic proposition; it must retain semantic relation to the source rather than becoming unrelated imagery.
- **`O11 upper-stage-untouched` (blocking):** the upper section is merely the original photograph or differs only through minor grading, contrast, saturation, texture overlay, or white balance. Regenerate it as a coherent photographic-led partial abstraction.
- **`O12 stage-progression-failure` (blocking):** the lower section is not materially more abstract than upper, either stage violates its rendering contract, or semantic identity/source-derived relationships no longer connect them. Different spatial organization and rendering vocabulary are expected and must not fail by themselves.
- **`O13 upper-stage-overabstraction` (blocking):** the upper section loses photographic dominance, facial/landmark recognition, natural light logic, material depth, or source framing and reads as equally flat or abstract as the lower section.
- **`O10 fixed-canvas-forcing` (blocking):** the final canvas must be derived from original width, height, aspect ratio, orientation profile, and relative section heights. Reject any output whose composition is controlled by a hard-coded `1800×3000`, `3000×1800`, `3:5`, `5:3`, or other rigid master canvas. Export bounds may resize the complete composition proportionally but may not redefine it.
- **`O02 filter-look`:** the first pass visibly changes at least two of these three properties in each counted region—outer/inner structure, material/rendering language, or region boundary/omission pattern—and reads as authored reconstruction rather than global styling. If it remains plausible as the original photo with altered color/texture, fail immediately and regenerate at the chosen tier.

Record only the failed codes. Correct one code at a time, preserve successful regions, then re-check the full gate.
