---
name: dreamwoven-reality
description: "Transform user-supplied photographs into one default processed 53/2/43/2 editorial artwork: a 53% upper paper board containing a 75–85% occupied photographic-led partial abstraction, a 2% black title band, a 43% full-width lower extreme semantic abstraction, and a 2% black subtitle band. Preserve upper facial identity without source-person compositing and reduce lower people to readable abstract silhouettes. Use for photo posterization, virtual/real contrast, architecture reconstruction, and editorial two-stage artworks."
---

# Dreamwoven Reality

> **License notice:** This skill is licensed for personal, non-commercial use only. Whenever the skill, a modified version, or work materially created with it is published or shared, credit **LeoLittleLeo** and link to the [original GitHub repository](https://github.com/LeoLittleLeo/dreamwoven-reality). Commercial use is prohibited. See [LICENSE](LICENSE) for the complete terms.

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
    hero_architecture: approximately-55-percent-photographic-plus-45-percent-materially-replaced-reconstruction-constrained-by-recognition-skeleton
    natural_hue_policy: source-faithful-neighboring-range
    board_base_color: source-semantic-robot-dreams-pale-counterpoint
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

## Canonical Abstraction Vocabulary

Treat this section as the single source of truth for what abstraction means, which operations are available, and how many may be combined. Other sections may assign an operation to an object or stage, but must not introduce additional abstraction methods.

Abstraction counts only when visible source material is replaced through at least one of these four operations:

```yaml
canonical_abstraction_vocabulary:
  planar-replacement:
    action: replace photographic material with broad coherent color or value planes
    primary_stage: upper-and-lower
  silhouette-merging:
    action: merge repeated, secondary, or living subjects into one or a few readable flat masses
    primary_stage: upper-and-lower
  semantic-omission:
    action: remove nonessential detail or material and replace it with controlled negative space or a quiet field
    primary_stage: upper-and-lower
  spatial-reauthoring:
    action: change scale, crop, spacing, axis, depth order, perspective emphasis, or mass placement while preserving semantic identity
    primary_stage: lower-only

stage_limits:
  upper:
    role: photographic-led-partial-abstraction
    source_geometry: strongly-preserved
    default_material_reconstruction: 45-60-percent
    allowed_operations: [planar-replacement, silhouette-merging, semantic-omission]
    operation_limit: one-primary-plus-at-most-one-supporting
    execution: few-large-contiguous-regions
  lower:
    role: extreme-semantic-abstraction
    source_geometry: spatial-reauthoring-allowed
    non-photographic_target: 85-100-percent
    allowed_operations: [planar-replacement, silhouette-merging, semantic-omission, spatial-reauthoring]
    operation_limit: one-primary-plus-at-most-one-supporting
    execution: few-large-semantic-masses
```

An operation is not a visual medium. Colored linework, flat paint, charcoal, ink, pencil, watercolor, gouache, paper, or digital shape language may realize an allowed operation, but naming or layering a medium does not create another abstraction method. Choose one consistent material voice for the primary operation and, only when necessary, one quieter supporting voice. Do not stack multiple textures or mark-making systems to increase apparent abstraction.

`recognition skeleton` is an identity and geometry constraint, not a countable abstraction operation. Use it to decide which silhouette, axis, joint, opening rhythm, overlap, support, and proportion must survive material replacement. Lines that merely describe this skeleton over intact photography never count toward reconstruction coverage.

For the upper stage, cleanliness is a hard requirement: make 2–4 large reconstruction decisions across at least two major nonliving semantic regions; keep transitions source-grounded; leave photographic areas calm; and avoid small alternating patches, scattered strokes, repeated edge effects, or all-over surface treatment. When the upper looks busy, remove the supporting operation first, enlarge the remaining regions, and reduce internal marks before changing coverage.

The following do **not** count as abstraction by themselves:

- color grading, desaturation, hue shift, exposure, contrast, or white-balance change;
- blur, haze, glow, grain, noise, sharpening, posterization, or pixelation;
- paper, canvas, paint, film, dust, scratch, or other texture overlays;
- an all-over painterly, illustrated, or stylized filter;
- decorative lines, hatch, washes, brush marks, or collage fragments placed over intact photographic material;
- masking, cropping, background removal, torn edges, alpha contours, typography, or layout changes without material reconstruction;
- merely simplifying detail while leaving the same photographic surface visible.

To count an upper region toward the 45–60% target, the original photographic material in that region must be visibly replaced by one of the four upper-allowed operations. To count a lower region, it must be non-photographically reconstructed through the vocabulary; spatial re-authoring alone does not excuse retained photographic microdetail.

## Upper Boundary Contract

Treat this contract as the single source of truth for the upper outer contour in `processed` mode. Other boundary instructions may explain implementation or review, but must not redefine its geometry.

```yaml
upper_boundary_contract:
  stage: upper
  mode: processed
  boundary_type: source-semantic-free-edge
  geometry_source: source-image
  output: authored-alpha-contour
  target_character: [calm, intentional, structurally-derived, visually-simple, non-rectangular]
  contour_model:
    dominant_semantic_contour: exactly-one
    supporting_contours: zero-or-one
    major_direction_changes: 3-7
    micro-object-tracing: prohibited
    rectangular_edge_retention: maximum-two-partial-sides
  prohibited:
    - random-blob
    - generic-torn-paper-shape
    - full-object-cutout
    - noisy-micro-contour
    - color-key-derived-alpha
    - arbitrary-rectangular-crop
    - rectangle-with-damaged-edges
```

Derive the contour in this order:

1. Identify the scene's dominant structural flow from the source: roofline or façade axis; ridge, slope, or dune; shoreline, current, coast, or wake; canopy fall or branch spread; cloud-bank flow; road or ground perspective; or a primary pose plus contact-ground relationship.
2. Choose exactly one dominant semantic contour that carries most of the outer edge. Add at most one supporting contour only when it clarifies a second major source relationship.
3. Simplify both into broad segments. Preserve only 3–7 major directional changes across the complete boundary. Ignore leaves, hair strands, windows, railings, sheep, pedestrians, furniture, ornaments, and other small-object silhouettes.
4. Let the artwork enter and leave the board through source-grounded continuations. A contour may dissolve into paper where source evidence becomes weak, low-priority, cropped, atmospherically soft, or compositionally quiet. Do not trace every visible object to keep it inside.
5. Preserve a substantial calm interior field. The boundary shapes the scene as one authored field, not as a union of object cutouts. It may retain no more than two partial source-image sides; never keep a near-complete rectangle and distress its perimeter.
6. Implement the final geometry as true RGBA alpha or an explicit outer-contour mask. Keep all pixels inside the chosen field opaque unless transparency is intentionally part of the outer dissolution. Never infer alpha from color.

Use edge material only as a subordinate finish after geometry is locked. Dry brush, watercolor bloom, pigment depletion, soft atmospheric fade, or paper-fiber disappearance may soften limited boundary segments, but must not create the contour, add extra lobes, or simulate generic torn paper.

At thumbnail size, the viewer should be able to describe the boundary with one short source-grounded phrase, such as “roofline into harbor horizon,” “canopy falling into the slope,” or “cloud bank into field.” If it reads only as “an irregular shape,” simplify and rebuild it.

## Global Rule Priority

1. Explicit user instruction.
2. No fabrication and semantic source identity.
3. Stage Contract.
4. Stage-specific identity and architecture rules.
5. Source geometry rules.
6. Stage Treatment Matrix.
7. Canonical Abstraction Vocabulary and coverage.
8. Palette system.
9. Upper Boundary Contract, then other boundary and material language.
10. Typography.
11. Optional modules.
12. Decorative refinement.

## Output Mode Contract

Treat this contract as the single source of truth for output mode and layout. No alternate output mode exists.

```yaml
output_mode:
  only_mode: processed
  layout: source-derived-53/2/43/2-editorial-collage
  upper_board: 53-percent
  title_band: 2-percent
  lower_panel: 43-percent
  subtitle_band: 2-percent
  upper_artwork_occupancy_within_board: 75-85-percent
  alternate_modes: prohibited
```

Always use `processed`. Compose exactly `53 / 2 / 43 / 2`: upper paper board, black centered-title band, full-width lower extreme-abstraction panel, and black centered-subtitle band. Omit dates, postcard fields, postal-code cells, postmarks, stamps, stickers, and alternate full-bleed layouts.

## Source-Faithfulness / No Fabrication Lock

Transform what exists; do not invent a different scene. Apply faithfulness in three scopes:

- **Semantic faithfulness — global:** preserve the same person identity, architecture and landmark identity, major natural-feature identity, scene semantics, object relationships needed for recognition, and absence of fabricated major subjects. Never invent people, buildings, mountains, rivers, landmarks, or major objects.
- **Geometric faithfulness — stage-dependent:** in the upper stage preserve framing, primary-subject position, perspective, pose, major silhouette, landmark geometry, and major spatial relationships. In the lower stage permit source-aware scale, crop, spacing, axis, depth-order, negative-space, perspective-emphasis, form-placement, and semantic-mass changes. Spatial re-authoring changes representation, not semantic identity.
- **Pixel/material faithfulness — stage-dependent:** keep the upper photographic-led and identity-sensitive; make the lower 85–100% non-photographic with almost no microdetail. The lower may materially reconstruct any object while retaining enough semantic anchors to remain the same scene.

- **Primary person:** globally preserve who the person is, their source-related pose/gesture/orientation, interaction, clothing category, and scene role. Apply approximately 95% facial fidelity, expression/gaze preservation, and strict source position only in the upper stage. In the lower stage prohibit realistic face/skin and preserve the person through a readable abstract silhouette and scene relationship.
- **Architecture:** globally preserve the same building identity, building count/range, landmark-defining profile, and recognition-critical relationships. In the upper hero, retain approximately 55% photographic reality and materially replace approximately 45% primarily through contiguous planar replacement, optionally supported by semantic omission; use the recognition skeleton only to constrain identity and geometry. The lower may spatially re-author architecture as extreme semantic reconstruction without inventing or substituting structures.
- **Natural landscape:** globally preserve the identity and relationships of source mountains, terrain, coast, water, vegetation masses, horizon, and major weather evidence. The upper preserves source geometry closely; the lower may recompose these features into source-derived semantic masses.
- **Objects:** do not introduce people, buildings, ornaments, birds, vehicles, furniture, vegetation, boats, lamps, signs, clouds, celestial objects, or another major object merely for balance, symbolism, storytelling, or aesthetics. Construction lines, pigment, paper texture, hatch, ink traces, and abstract color fields are allowed only when they read as rendering language rather than physical objects.
- **Occlusion and ambiguity:** preserve visible evidence, simplify uncertain regions, leave incomplete sketch marks or negative space, and softly omit ambiguity. Never complete hidden, cropped, blurred, or unclear anatomy, architecture, terrain, text, signage, or objects with unsupported detail. When uncertain, simplify rather than invent.
- **Conflict resolution:** use the Global Rule Priority and Stage Contract above; do not create local priorities that override them.

Before delivery, verify that every primary person, major building, natural feature, landmark structure, and major object maps to the source or an explicit addition request. Any untraceable major element is a blocking failure and must be regenerated or locally corrected.

## Workflow

1. Inspect the source and metadata. Diagnose the scene before choosing a style: scene type, primary subject, identity sensitivity, face clarity, tall anchors, dominant regions, palette, negative space, and reliable capture date.
2. Read [references/visual-direction.md](references/visual-direction.md). When the scene contains a living cluster, an architecture-led framed view, disposable interior furniture, or a dominant botanical group, also read [references/exemplars.md](references/exemplars.md) and inspect only the routed exemplar image(s). Use exemplars as structural and quality references, never as fixed palettes or composition templates. Then state one source-grounded artistic proposition: a relationship, tension, transition, or emotional fact that the poster will clarify. Do not invent a story unsupported by the image.
3. Write a compact strategy record using the schema below. Make preservation, omission, reconstruction, echo color, negative space, and copy all serve the proposition and remain traceable to visible evidence or an explicit user request.
4. Choose `light`, `medium`, or `strong` upper abstraction. Respect a user-requested intensity; otherwise use `medium` with a 45–60% materially reconstructed-area target. Select one primary Canonical Abstraction Vocabulary operation and at most one supporting operation. Lower only for identity-sensitive documentary portraits; raise for robust silhouettes, scenery, distant figures, or explicit permission.
5. Assign each visible living subject one coherent treatment. Use `face-locked, body-flexible, no-source-composite` for the primary person by default and `fully abstract` only for distant/nonessential faceless people or explicit identity reinterpretation. Keep facial identity and semantic pose coherent while allowing the body, clothing, peripheral hair, and edges to be regenerated or integrated.
6. Assign every major nonliving built or landscape region a controlled real/abstract division using only the Canonical Abstraction Vocabulary. Preserve a calm photographic recognition core and make 2–4 large contiguous reconstruction decisions; avoid tiny alternating patches. For the lower panel, use a few large semantic masses and the same vocabulary, with `spatial-reauthoring` additionally available.
7. Generate or edit each stage as a coherent whole under the Stage Contract. In upper, preserve the primary face at approximately 95% perceptual fidelity without source compositing. In lower, prohibit realistic facial content and preserve the primary person through a readable abstract silhouette.
8. Let final artistic coherence take priority outside core facial identity. Permit restrained changes to garment color, garment edges, lighting, texture, peripheral hair, body contour, and local silhouette transitions when they improve palette integration, material continuity, or the real/abstract thesis. Preserve pose, anatomy, gesture, and meaningful contact relationships.
9. Compare the upper candidate with the source at matched face scale using the upper identity rubric. Review lower personhood through silhouette, pose rhythm, and scene relationship instead. Judge both stages against their own quality gates; never repair either by pasting source pixels back.
10. Before generation, assign every visible object to exactly one treatment using the Object Treatment Lock below. Do not begin generation while secondary people, seating fixtures, ground planes, hero-architecture photographic core, hero-architecture reconstruction zone, or secondary architecture remain unassigned.
11. Generate two coordinated interpretations from the same source: a dominant photographic-led partial abstraction and an extreme semantic abstraction. Use `scripts/inspect_photo.py` for metadata when useful. Before composition, run the Upper Architecture Execution Lock below; do not assemble a candidate that fails it. Use `scripts/compose_poster.py` in the only mode, `processed`, to assemble the `53 / 2 / 43 / 2` full-width artwork. Never place the untouched source in the final composition.

## Strategy Record

Before editing, record the decisions in this compact form. Omit fields that do not apply; do not expose the record unless it helps the user review the direction.

```yaml
scene_type: person | landmark | nature | street | crowd | minimal | mixed
source_orientation: landscape | portrait | near-square
layout_adaptation: source-derived-processed-collage
photo_section_priority: source-integrity-first
abstract_axis_bias: horizontal | vertical | balanced
section_proportions_profile: landscape-default | portrait-adapted | square-adapted
canvas_basis: source-image-dimensions
scaling_policy: proportional-only
crop_policy: minimal-and-source-aware
fixed_master_canvas: disabled
size_policy: {basis: source, export_long_edge: adaptive, preserve_source_ratio: true, allow_upscale: limited, allow_downscale: true, allow_nonuniform_scale: false}
output_mode: processed
layout_profile: 53-upper-board/2-title-band/43-lower-panel/2-subtitle-band
default_poster_mode: processed
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
architecture_stage_plan: [<hero identity -> upper 55% photographic plus 45% contiguous material replacement constrained by recognition skeleton; lower extreme semantic reconstruction>]
identity_sensitivity: low | medium | high
upper_person_mode: none | face-locked-body-flexible-no-source-composite | fully-abstract-faceless | illustrated-portrait
upper_identity_fidelity_target: none | approximately-95-percent-facial-perceptual
lower_primary_person: none | readable-abstract-human-silhouette-maximum-two-flat-colors
identity_core: [<facial geometry, expression, gaze, eyewear, hairline, ears, jaw, distinctive features>]
identity_integration_allowances: [<garment color/edge, peripheral hair, lighting, texture, body-edge and silhouette transitions allowed for artistic coherence>]
abstraction_strength: light | medium | strong
abstract_coverage_target: light 30-40% | medium 45-60% | strong 65-85% | extreme 85-100%
abstract_regions: [<at least two major semantic regions and their assigned canonical operations>]
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
upper_architecture_reconstruction_color_separation: <reconstruction family versus retained photographic building tone; record the strong hue, value, or temperature contrast used to distinguish them>
palette_map: [<semantic region -> target color family and reason>]
stage_treatment_map: [<each object -> semantic identity; upper treatment; lower treatment>]
disposable_support_fixtures: [<every bench, chair, stool, seat, cushion, sofa, low seating wall, table, or comparable non-hero support -> fully abstract; zero photographic texture unless explicitly protected>]
ground_plane_assignments: [<each ground -> upper photographic core plus contiguous abstract zone; lower broad planes plus sparse perspective cues>]
line_density_inventory: [<each complex built object/region -> recognition-critical lines vs repetitive high-frequency lines>]
forced_line_simplification: [<non-architectural triggered object/region -> preserved identifiers and sparse planes; architecture -> recognition skeleton plus compressed structural rhythms>]
stage_visual_vocabulary_limit: <per stage: one primary canonical operation plus at most one supporting operation; one material voice per operation>
echo_color: none | <source hue and conceptually necessary destination>
optional_modules: [<only justified modules>]
architectural_treatment: inactive | active
architectural_recognition_skeleton: [<smallest source-derived set that preserves identity: roof/tower/façade axis/arch, column, window or eave rhythm/landmark profile>]
upper_architectural_reconstruction_zone: <one coherent region or structurally connected set covering approximately 45% of the upper hero>
architectural_detail_compression: [<repeated windows, columns, ornaments, seams, or trim -> fewer readable structural rhythms>]
architectural_structural_connections: [<photographic structure -> credible reconstructed continuation, joint, support, or deliberate open termination>]
upper_reconstruction_language: colored-line-study | exposed-frame | scaffolded-skeleton | structural-color-planes | transparent-construction | paper-omission | mixed-source-grounded
upper_secondary_architecture_treatment: simplified-structural-abstraction | quiet-silhouette
lower_architecture_treatment: extreme-semantic-reconstruction
title_text: <short centered title-band copy; optional when copy-free>
subtitle_text: <short centered subtitle-band copy; optional when copy-free>
date_text: omitted
processed_typography_layout: centered-black-bands
typography_family: book-serif | humanist-serif | restrained-editorial-serif
processed_typography_color: source-derived-dark-ink-on-paper
upper_board_base_color: <source-semantic Robot Dreams pale base; record source mood, dominant temperature, selected family, and contrast purpose>
copy_mode: none | poetic | editorial | cinematic
content_field_boundary: <one dominant source-semantic contour; optional one supporting contour; 3-7 major direction changes; paper-entry/exit points; subordinate edge material>
content_field_occupancy: <target 68-82% of paper area; justified exception>
processed_layout: {upper_board: 53%, title_band: 2%, lower_panel: 43%, subtitle_band: 2%}
upper_artwork_board_occupancy: 75-85%
text_hierarchy: {title: centered-first-band, subtitle: centered-second-band, date: omitted}
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
    upper: approximately-55-percent-photographic-plus-45-percent-contiguous-planar-replacement-optionally-supported-by-semantic-omission
    lower: extreme-semantic-architectural-reconstruction
  secondary_architecture:
    upper: simplified-structural-abstraction-or-quiet-silhouette
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

### Upper Architecture Execution Lock

Apply this lock before generating any upper stage that contains recognizable architecture. It converts the architectural ratio and hierarchy requirements into explicit, inspectable regions.

```yaml
upper_architecture_execution_lock:
  hero_photographic_core:
    required: true
    target: 50-60-percent-of-visible-hero
    geometry: one-contiguous-or-structurally-connected-region
    must_retain: [photographic-material-depth, source-light, recognition-critical-geometry]
  hero_reconstruction_zone:
    required: true
    target: 40-50-percent-of-visible-hero
    geometry: one-contiguous-or-structurally-connected-region
    must_replace_photographic_material: true
    must_follow: [recognition-skeleton, source-perspective, credible-structural-connections]
    surface-decoration-only: prohibited
  real_abstract_partition:
    required_before-generation: true
    record_as: [photographic-core-location, reconstruction-zone-location, connecting-structure]
    ambiguous-or-global-estimate-only: prohibited
  secondary_architecture:
    allowed: [quiet-silhouette, simplified-structural-abstraction]
    photographic-windows: prohibited
    photographic-facade-texture: prohibited
    photographic-roof-or-masonry-microdetail: prohibited
    individually-readable-repetitive-detail: prohibited
    maximum-contrast: materially-below-hero
  precomposition_gate:
    blocking: true
    fail_if:
      - hero-photographic-core-is-not-locatable
      - hero-reconstruction-zone-is-not-locatable
      - hero-real-abstract-boundary-is-unclear
      - reconstruction-does-not-replace-photographic-material
      - secondary-architecture-remains-photographic
      - secondary-architecture-competes-with-hero
```

Do not judge the 55/45 balance from a vague whole-image impression. Point to the photographic core and reconstruction zone before generation, then point to both again in the generated candidate. Treat an intact photographic building with lines drawn over it as fully photographic, not reconstructed. Treat background or supporting buildings with visible photographic windows, façade texture, roof detail, or masonry microdetail as a blocking failure even when they are small, distant, blurred, or low contrast. Regenerate or locally edit the upper stage before composition; grading, blur, or reduced saturation does not satisfy the secondary-architecture treatment.

In the upper stage, every non-primary person uses one shared opaque flat silhouette; every disposable support is fully abstract; and every designed ground plane contains a contiguous reconstruction zone. In the lower stage, apply the matrix's stronger semantic reduction while preserving only the recognition-critical identity and relationships required by the Stage Contract. If a stage-specific assignment is not visibly executed, regenerate or locally re-edit that stage.

### Non-negotiable

- Preserve user-designated unchanged regions according to their explicit scope. Apply strict anatomy, position, perspective, and landmark geometry to upper; apply semantic identity and readable source relationships to lower.
- **Ordered real/abstract thesis:** make the virtual/real relationship visible at first glance. The result must contain meaningful photographic evidence and meaningful non-photographic reconstruction; neither may collapse into a full-frame filter, an almost untouched photograph, or an almost unrelated illustration. Use a few large contiguous decisions, not confetti-like alternation.
- **Stage-scoped living-subject unity:** in upper, keep each living subject anatomically coherent and apply the face-locked mode to the primary person. In lower, preserve semantic organism/personhood and source relationships through abstract silhouettes or masses; do not require photographic anatomy or facial fidelity.
- **Stage-scoped clustered life:** detect clusters globally, then render them by stage. Upper clusters use one coherent abstract language; lower clusters become simplified grouped semantic masses or compatible shared silhouettes. The protected upper primary person may remain an exception.
- **Upper crowd single-tone lock:** every upper non-primary person uses exactly one shared opaque flat fill color with crisp edges and no internal detail.
- **Lower secondary-person treatment:** lower non-primary people become simplified grouped semantic masses or shared flat silhouettes; they do not inherit the upper single-tone rendering requirement unless that choice supports the lower composition.
- **Upper nonliving duality:** every major upper non-architectural engineered or landscape region should visibly combine one calm photographic recognition region with one contiguous abstract reconstruction region. Upper hero architecture follows its 55/45 contiguous planar material-replacement rule, with the recognition skeleton acting only as a geometry constraint. Lower nonliving regions follow extreme semantic reconstruction instead.
- **Boundary discipline:** for non-architectural regions, place real/abstract transitions on source-grounded seams—structural joints, perspective axes, shorelines, currents, ridges, slopes, shadow edges, or occlusion boundaries. Architectural transitions follow the recognition skeleton and credible structural connections; they need not use one fixed edge style.
- **Stage-specific vocabulary restraint:** follow the Canonical Abstraction Vocabulary: one primary operation plus at most one supporting operation per stage, with one coherent material voice per operation. Keep the two stages compatible in palette and proposition but distinct in rendering density.
- **High-line-density forced abstraction:** for non-architectural objects, compress repeated lines into broad unequal planes and sparse structural marks. For architecture, preserve the recognition skeleton and compress repeated windows, columns, seams, trim, ornament, and surface texture into a few readable rhythms. Do not describe every unit one by one or replace the building with generic planes.
- **Tiered abstract coverage:** count only material replacement through the Canonical Abstraction Vocabulary. Reconstruct upper `light` at 30–40%, `medium` at 45–60% (default), or `strong` at 65–85%; reconstruct lower `extreme` at 85–100% non-photographic. The vocabulary's non-counting list overrides any implication elsewhere that grading, texture, marks, masking, or filtering contributes coverage.
- **Lower-panel primary-person silhouette and two-color lock:** when the source has a primary person, preserve a clearly human, immediately legible approximation of the source pose, orientation, body proportion, gesture, and dominant outer silhouette. Render the complete figure with one or at most two flat colors total. Do not use different colors to distinguish garments, garment layers, skin, limbs, torso, joints, anatomy, lighting, or body structure. If two colors are used, treat the second as one restrained compositional accent or edge/overlap aid across the figure, not as descriptive segmentation. Remove real skin, facial features, hair strands, garment folds, fabric texture, gradients, tonal modeling, and photographic shading. Personhood must come from the outer silhouette, pose, gesture, and head/torso/limb relationship—not internal color coding.
- **Lower-panel palette lock:** the lower panel must use `robot-dreams-logic` as a selected palette, not merely as an optional candidate. Use 4–6 softened colors, warm/cool opposition, 2–3 value steps per semantic mass, charcoal/deep blue instead of pure black, and at most one concentrated accent. Reject naturalistic color scattering, random neon, realistic skin tones, global grayscale, and generic painterly color treatment.
- **Multi-region transformation:** distribute counted abstraction across at least two major nonliving semantic regions—for example architecture plus ground, water plus terrain, shoreline plus supporting buildings, or road plus built fixtures. A single large flat sky or background field cannot satisfy the requirement by itself. Fully photographic living subjects are exempt from abstraction but do not reduce the coverage target for the remaining composition.
- **Upper photographic-corridor cap:** apply the <=35% cap only to uncontrolled continuous environmental photographic corridors across the upper composition. It does not override the upper primary-face identity region or the designated upper hero architecture governed by its 55/45 rule. Do not apply this cap to the lower stage, whose 85–100% non-photographic contract already controls photographic retention.
- **Upper architectural hierarchy lock:** identify one upper-stage hero building when architecture is present. Retain approximately 55% of that hero as photographic reality and materially replace approximately 45% primarily through `planar-replacement`, optionally supported by `semantic-omission`. Use the recognition skeleton only as an identity and geometry constraint; it contributes zero coverage by itself. Treat secondary architecture more quietly. This balance must never constrain lower architecture.
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
- **Protected-nature contrast routing:** diagnose natural, built, and ground masses together. If separation is weak, route contrast through coherent built-region color notes or the chosen architectural reconstruction language while preserving architectural identity, material logic, and light direction. Do not recolor architecture as scattered patches.
- **Upper architectural reconstruction color separation:** color the reconstructed portion of the upper hero architecture with a family that is clearly separated from the retained photographic building tone. Require a strong, immediately visible difference in hue, value, temperature, or a controlled combination of them; near-matching local color that makes the real/abstract partition difficult to see is prohibited. Apply the contrast to the complete reconstruction zone rather than scattered accents. Preserve landmark identity, credible material relationships, source light direction, and protected natural/living hues; distinction does not authorize random neon or unrelated color.
- Keep each large color field within one semantic region. Do not wash across architecture, sky, ground, water, people, or another major subject.
- **Unified-sky field:** treat the entire visible sky as one continuous natural color field. Preserve one source-derived dominant hue family across the sky; allow only smooth same-family value, temperature, or atmospheric gradients and source-grounded cloud transitions. Never split an abstracted sky into multiple discrete large polygons, cut-paper blocks, ribbons, wedges, or unrelated color fields. Reserve hard-edged plane fragmentation for built structures and designed surfaces, not open sky.
- Keep exact final lettering legible. Add it deterministically when image generation cannot render it reliably.
- **Processed canvas geometry:** derive the canvas width from the source width and the canvas height from the source height divided by the 53% upper-board fraction. Use exactly `53 / 2 / 43 / 2`; export caps may resize only the complete composition proportionally.
- **Proportional scaling only:** never stretch, squeeze, widen, flatten, or independently scale either generated stage. Preserve the full authored upper contour with contain-style placement and require 75–85% visible occupancy inside the 53% board. Fit the lower abstraction edge-to-edge by proportional cover; modest source-aware crop is allowed.
- **Single processed hierarchy:** the upper board is visibly larger than the lower panel; the lower abstraction remains a full-width strict rectangle. No postcard message field, stamp, postmark, date band, fullbleed variant, or alternate arrangement is permitted.
- **Postcard paper base:** choose the full card's base color from scene meaning and source palette relationships. Diagnose scene atmosphere, dominant temperature, natural/built balance, light level, season/weather impression, and the hero artwork's largest color masses. Select one visibly tinted low-chroma Robot Dreams family—warm ivory, dusty peach, powder blue, soft lilac, or mineral sage—that supports the proposition and creates calm figure/ground separation. Pure white, off-white that reads as white, and neutral near-white gray are prohibited unless the user explicitly requests a white card. Prefer a restrained temperature counterpoint: cool/blue scenes may receive dusty peach; warm scenes may receive powder blue; dark or neutral structural scenes may receive warm ivory; quiet pale neutrals may receive soft lilac; bright vegetation-led scenes may receive mineral sage when it remains distinct from the artwork. This is semantic art direction, not literal average-color sampling.
- Keep the 53% upper board visually quiet, visibly colored, materially paper-like, and intentionally structured rather than vacant. It must not compete with the upper authored image, repeat its dominant hue so closely that the free edge disappears, introduce random accent color, or collapse toward white. Preserve a subtle source echo while using Robot Dreams warm/cool logic. An explicit non-white user color overrides automatic selection; otherwise record the chosen family and contrast purpose in the strategy record.
- **Upper outer boundary:** follow the Upper Boundary Contract. Do not improvise another contour system elsewhere in the workflow.
- **Upper-panel color-preservation lock:** implement the Upper Boundary Contract with authored RGBA or an explicit outer-contour mask. Never derive alpha from sampled color. Keep pale architecture, clouds, skin, highlights, water glints, and paper-like reconstructed planes opaque and color-identical after compositing. Compare isolated and composited RGB at matched scale; reject hue/value shift or interior deletion.

### Default strategies

- In the upper stage, apply a natural/built color boundary: keep people, animals, sky, clouds, water, vegetation, and terrain source-neighbor plausible while routing stronger shifts through built regions. In the lower stage, follow the Stage Contract's source-derived semantic color relationships and mandatory `robot-dreams-logic` palette instead of literal local-color fidelity.
- When the dominant natural, architecture, and ground colors cluster too closely, do not accept a low-impact factual palette by default. Compare at least three candidate interventions—shift the hero architecture, shift the designed ground/fixtures, or split the adjustment across both—and choose the smallest coherent built-region change that creates clear figure/ground separation. Favor complementary temperature, useful value separation, or controlled saturation contrast; avoid arbitrary neon, equal-intensity competition, and hue changes that weaken landmark identity.
- Inventory every living subject before editing. Detect clusters first and assign each cluster one shared `fully abstract` language; then assign isolated non-primary subjects `fully photographic` or `fully abstract` and the primary person `face-locked, body-flexible, no-source-composite`. Keep facial identity, semantic pose, and biological continuity coherent while allowing controlled regeneration and transitions through clothing and peripheral body edges.
- **Upper auto-candidate `robot-dreams-logic` palette:** for upper palette selection only, evaluate Robot Dreams against ordinary `shifted` color when the source has weak palette hierarchy and sufficient built/design levers. Select it only when it improves at least two of palette hierarchy, emotional coherence, and subject/ground hierarchy without weakening upper identity, landmark recognition, material logic, or protected natural hues; otherwise use `fallback`. Lower does not use this auto gate because its Robot Dreams palette is mandatory.
- **Upper monochromatic-scene palette expansion:** when upper is effectively monochromatic, compare a restrained expressive Robot Dreams plan against a conservative shifted plan. Route added color through source-supported atmosphere, reflected light, wet surfaces, clouds, architectural planes, or designed ground while preserving upper source geometry and natural/living plausibility. Lower independently follows its mandatory semantic Robot Dreams contract.
- Use scene-semantic brightness. Favor calm middle-to-lower values for quiet, historic, intimate, autumnal, or overcast scenes; allow brighter values for sunny, snowy, seaside, summer, or celebratory scenes.
- Build a few unequal semantic masses. Use an echo color only when it carries a necessary structural or conceptual turn; otherwise set it to `none`. Never add accent marks merely because a source hue is available.
- Partially deconstruct prominent tall nonliving anchors while retaining decisive silhouette, spatial role, and one or two identifying features. Make the intervention legible through one contiguous reconstructed zone, large omissions, and a few hierarchical marks; do not substitute all-over sketch texture for deconstruction.
- In the upper stage, select one hero building or coherent architectural group by dominance or compositional harmony. Keep approximately 55% photographic and materially replace approximately 45% with one contiguous region or structurally connected set of broad source-aligned planes. Optionally omit secondary material inside that zone. Use the smallest source-derived recognition skeleton only to preserve identity, alignment, joints, overlaps, and proportions. Sparse structural lines may clarify the replaced planes but never count as reconstruction. Upper supporting architecture remains quieter. Lower architecture follows its extreme semantic contract instead.
- Fully abstract disposable support fixtures by default, even when their texture appears visually quiet or helps explain contact. Inventory every bench, chair, stool, seat, cushion, sofa, low seating wall, table, and comparable support before editing; assign the entire fixture a zero-photographic-retention treatment. Preserve contact logic through abstract geometry and a coherently generated or locally edited person above it, never through a photographic patch of the fixture or source-person reinsertion.
- Omit or strongly merge non-architectural source elements when they fragment the intended semantic masses without supporting recognition or the artistic proposition. Never apply this omission rule to recognizable architecture: architectural identity, geometry, and structural continuity take priority.
- Give a dominant low-variety region contained value bands or material rhythm; keep construction-line language mainly on architecture and engineered structures.
- Run the architectural hierarchy and alignment inventory before generation and after the first pass. Record the hero's recognition skeleton, the 55/45 division, the chosen reconstruction language, repeated-detail compression, and the structural connections between photographic and rebuilt regions. Check identity, silhouette, perspective, proportions, key rhythms, structural continuity, and thumbnail legibility. Reject duplicated or shifted layers, decorative surface tracing, unsupported components, and reconstruction that no longer reads as the same building.
- Reduce clustered pedestrians and nonessential secondary pedestrians to one coherent single-tone silhouette system. Use exactly one shared opaque flat fill across all such people in the image; preserve only group range, density, proportion, pose rhythm, direction, spacing, and necessary overlap. Use crisp hard edges, merge collisions into clean union masses or open a narrow paper-colored separation gap, and allow no face, garment detail, tonal depth steps, transparency, hatch, paper grain, sketch texture, ink/watercolor wash, photographic islands, internal modeling, or edge bleed.
- Keep hierarchy classes visually distinct. Do not give secondary people the structural line language used for architecture. Assign photographic texture to identity anchors, sparse structural marks to selected built forms, and solid fill-only silhouettes to crowds.

### Architectural Hierarchy and Hero Selection

Define architectural roles by scene function rather than by size, distance, or whether a structure is a famous landmark.

```yaml
architecture_hierarchy:
  hero_architecture:
    definition: >
      The single identifiable building or coherent building group that contributes most to
      scene recognition, visual center of gravity, and compositional relationships.
    selection_priority:
      1: explicit-user-designation
      2: scene-recognition-contribution
      3: visual-center-of-gravity
      4: compositional-relationship
      5: landmark-distinctiveness
    constraints:
      - may-be-a-single-building-or-a-coherent-structural-group
      - do-not-select-only-by-largest-area-or-nearest-distance
    upper_treatment: approximately-55-percent-photographic-plus-45-percent-contiguous-planar-replacement-constrained-by-recognition-skeleton
    lower_treatment: extreme-semantic-reconstruction
  secondary_architecture:
    definition: >
      Every identifiable artificial structure other than hero_architecture, including
      background city skylines, distant building groups, port structures, bridges, roofs,
      façades, and other built forms.
    upper_treatment: quiet-silhouette-or-simplified-structural-abstraction
    lower_treatment: broad-semantic-planes-plus-sparse-structural-cues
    photographic_detail: prohibited
```

A background city skyline remains `secondary_architecture` even when it is small, distant,
low-contrast, partially cropped, or visually subordinate. It must not be classified as ordinary
environmental background and must not retain photographic windows, façade texture, masonry,
roof detail, or individually readable repeated structures. Compress it into a quiet silhouette,
low-contrast geometric mass, or sparse structural rhythm while preserving only the source-derived
skyline direction and scene relationship.

Before generation, record the role of every visible built region:

```yaml
architecture_role_inventory:
  - region: <source-grounded region>
    role: hero_architecture | secondary_architecture
    reason: <scene recognition, visual weight, compositional relationship, or explicit designation>
    upper_treatment: <stage-specific treatment>
    lower_treatment: <stage-specific treatment>
```

If any identifiable background building remains photographic in the upper stage, fail the
secondary-architecture gate and regenerate or locally re-edit the upper stage before composition.

### Upper Architectural Reconstruction

Apply this treatment to one recognizable hero building in the **upper stage**. Keep approximately 55% as photographic reality and materially replace approximately 45% through contiguous `planar-replacement`, optionally supported by `semantic-omission`. The building's recognition skeleton constrains the replacement but is not itself an abstraction method and contributes no coverage. This balance is an upper-stage rule only; lower architecture follows the extreme semantic reconstruction contract.

Identify the smallest source-derived skeleton that preserves the building's identity: landmark silhouette, roofline or crown, façade axis, major wall planes, tower, dome, gate, arch, column grouping, structural diagonal, opening rhythm, and other decisive relationships actually visible in the source. Compress repeated windows, columns, seams, trim, ornament, and surface texture into a few readable rhythms.

Choose one planar material language according to the scene and proposition. Valid directions include:

- structural color planes or simplified volumes;
- broad opaque paper planes aligned to shells, walls, roofs, or façades;
- planar construction fields with sparse skeleton lines used only as identifiers;
- planar replacement supported by deliberate paper omission or interrupted material.

These are options, not a checklist. Use `planar-replacement` as the primary operation and at most `semantic-omission` as support. A line-only frame, colored study, transparent drawing, or intact photograph beneath structural marks is insufficient even when structurally intentional.

Make the reconstruction replace photographic material rather than decorate a complete photograph. It may occupy one connected region or several structurally connected components when the building's skeleton supports that choice. Maintain credible perspective, proportions, silhouette, supports, joints, and recognition-critical relationships between the photographic and rebuilt portions. A real contour must continue into a source-aligned color plane, planar joint, or deliberate omission; a drawn line alone cannot carry the transition.

Make that partition legible through color as well as material. The reconstruction zone must differ strongly from the retained photographic building tone through hue, value, temperature, or a controlled combination of them. Do not sample or closely imitate the building's local color when that would visually collapse the reconstruction back into the photographic core. Use one coherent contrasting family across the reconstructed zone, while preserving source light direction, structural credibility, and architectural identity.

Do not paste, duplicate, or offset architectural fragments. Do not invent unsupported wings, towers, openings, roofs, or structural systems. At thumbnail scale, the result must still read as the same building, with the 55% photographic reality and 45% authored reconstruction both clearly visible.

Apply these stage-scoped priorities under the Global Rule Priority:

```yaml
upper_architecture_priority:
  1: source-architectural-identity
  2: recognition-skeleton
  3: perspective-and-structural-alignment
  4: approximately-55-percent-photographic-reality
  5: approximately-45-percent-contiguous-planar-material-replacement
  6: detail-compression
  7: coherent-reconstruction-language
lower_architecture_priority:
  1: same-architectural-semantic-identity
  2: minimum-recognition-skeleton
  3: source-derived-structural-relationship
  4: extreme-abstraction
  5: spatial-re-authoring
  6: broad-color-planes
  7: sparse-structural-lines
```

Avoid literal one-by-one detail copying, decorative surface tracing, random nonstructural marks, pasted overlays, generic abstract patches, lost silhouettes, broken perspective, unsupported structural additions, duplicated contours, and abstract geometry that destroys readability.
- **Cloud metaphor:** default `off`. Enable only when the user requests it or an existing cloud formation makes the metaphor unusually natural. Never add clouds merely to create a motif.
- **Cinematic title:** default `off`. Enable when requested or when a released-film connection is exceptionally strong and verifiable; otherwise use user wording or a source-grounded original title.
- **Illustrated/anime portrait:** explicit-only. Never select it solely because a face is front-facing. Enable only when the user requests illustration/anime treatment or clearly accepts identity reinterpretation.

## Abstraction Strength

Use `light`, `medium`, or `strong` for upper-stage intervention planning. The processed lower stage always uses the Stage Contract's `extreme` 85–100% non-photographic tier.

- **`light` — 30–40%:** retain most identity/documentary evidence, but reconstruct at least two identity-safe semantic regions. Prefer for sensitive portraits, complex contact points, or fragile landmarks.
- **`medium` — 45–60% (default):** retain selected photographic anchors while replacing substantial portions of at least two major regions through the Canonical Abstraction Vocabulary. The first generated pass must target this range, not the 30% floor.
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

## Editorial Copy

1. Use exact user-provided wording whenever supplied. Never add a date or date band.
2. Otherwise derive one concise title and one concise subtitle from visible subject relationships, light, movement, distance, structural axis, spatial tension, or a meaningful source-color relationship. Avoid generic travel language, unsupported narratives, and fabricated locations.
3. A single text level or copy-free result is allowed when it better serves the artwork.
4. Center title and subtitle in their respective 2% charcoal-black bands using identical-sized warm-ivory type.
5. Use an elegant restrained editorial serif. Typography must remain legible and subordinate; do not place it inside either image panel.
6. If a cinematic-title module is explicitly requested or justified, verify the exact released-film title and never imply unsupported provenance.

## Output Mode — Processed Only

Always compose one source-derived vertical two-stage artwork:

```text
[ 53% upper paper board: free-edged photographic-led partial abstraction ]
[  2% charcoal-black centered-title band ]
[ 43% full-width lower: extreme semantic abstraction ]
[  2% charcoal-black centered-subtitle band ]
```

Derive the canvas width from the source width and the canvas height from the source height divided by `0.53`. Fixed export dimensions are proportional bounding caps only. Never use a fixed master canvas, stretch either stage, or independently scale x and y.

The upper artwork must occupy 75–85% of the 53% board, measured from its visible authored alpha area relative to the board area. Preserve the complete source-semantic free edge; do not reach the occupancy target through clipping, stretching, or rectangularization. The lower panel is a strict full-width rectangle fitted edge-to-edge with aspect-ratio-preserving cover and modest source-aware cropping. It has no margin or letterboxing.

No alternate mode exists. Do not output a postcard, stamp, postmark, message field, postal-code cells, date band, fullbleed image, equal split, comparison grid, or any layout other than `53 / 2 / 43 / 2`.

**Original-image exclusion is non-negotiable:** the uploaded photograph is an analysis, geometry, palette, identity, and metadata reference only. It must not appear as a panel, inset, thumbnail, comparison strip, background layer, or visible source fragment. Both visible image sections must be newly generated or coherently edited interpretations.

### Upper Panel — Interwoven Main Image

Generate or edit the complete scene as one coherent photographic-led image with light-to-medium intervention.

- Preserve facial identity, expression, gaze, pose, landmark identity, framing, perspective, light direction, and major object relationships.
- Keep enough photographic surface, tonal depth, material evidence, and natural light to remain photography-dominant.
- Apply counted abstraction through the Canonical Abstraction Vocabulary, not through filtering or surface effects.
- Never construct it by compositing source people, faces, bodies, garments, or local source patches.
- Apply the Upper Architecture Execution Lock when architecture is present.
- Build the outer contour exactly through the Upper Boundary Contract.
- Carry the primary identity, landmark, and scene-reading burden.

### Lower Panel — Rectangular Extreme Abstraction

Advance the same scene into full-width extreme semantic abstraction. Use the Canonical Abstraction Vocabulary with `spatial-reauthoring` available, preserve source-derived semantic anchors, remove photographic microdetail almost completely, and keep the field a strict rectangle.

The lower panel must not contain realistic faces, skin, detailed hands, garment construction, clothing folds, fabric texture, hair strands, or photographic shading. When a primary person exists, preserve a readable human silhouette, approximate body contour, pose, gesture, orientation, and head/torso/limb relationship using one or at most two flat colors across the complete figure.

Use the mandatory `robot-dreams-logic` palette: 4–6 coherent softened colors, warm/cool hierarchy, 2–3 value steps per semantic mass, charcoal/deep blue instead of pure black, and at most one concentrated accent.

Target 85–100% non-photographic semantic reconstruction. The lower must not merely zoom, crop, duplicate, or retain similar rendering density to the upper.

**Progression is non-negotiable:**

```text
upper = photographic-led partial abstraction
lower = extreme semantic abstraction
```

Preserve source orientation and tall anchors in the upper. The lower may crop, reorder, resize, or reposition semantic masses when it remains a deliberate reconstruction of the same scene.

**Source geometry is non-negotiable:** preserve the user's source dimensions and aspect ratio as composition authority. Export bounds may resize the complete result proportionally but may not redefine its geometry.

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

Compose final files with the two generated stages. Pass `--font /path/to/font.ttf` when automatic cross-platform CJK font discovery cannot find a suitable font. Use `--background-color` to apply the strategy record's semantically selected Robot Dreams board base. If omitted, the compositor performs a deterministic source-palette fallback: cool-dominant -> dusty peach, warm-dominant -> powder blue, green-dominant -> warm ivory or mineral sage by light level, neutral-dark -> warm ivory, and neutral-light -> soft lilac, each with a subtle source echo.

In `processed`, pass a short `--title` and compact `--subtitle` for the two centered bands. Either text level may be omitted; use `--copy-free` only for an explicitly copy-free request. Do not pass a date or alternate text position.

For the lower abstract artwork, use the safest available background mode:

- `--background-removal alpha` (default): use an existing alpha channel; keep an RGB image rectangular rather than guessing.
- `--background-removal edge-key`: remove only corner-like paper connected to the image edge. Add `--mask-preview` to inspect the derived mask.
- `--background-removal mask --art-mask mask.png`: use an explicit white-foreground/black-background mask.
- `--background-removal none`: preserve the complete rectangular artwork.

For the upper artwork, treat transparency as the implementation of the Upper Boundary Contract, never as color removal. Use either (1) model-generated RGBA with the authored semantic contour or (2) a deterministic white-foreground/black-background outer-contour mask passed with `--background-removal mask --art-mask`. Do not use `--background-removal edge-key`. Inspect the mask preview and verify that the interior is opaque, especially over identity-critical face/skin, architectural shells, clouds, and light ground planes.

Default and only output:

```bash
python scripts/compose_poster.py \
  --mode processed \
  --original input.jpg \
  --upper-poster partial-abstraction.png \
  --poster strong-abstraction.png \
  --title "Exact main title" \
  --subtitle "Exact short subtitle" \
  --output-dir outputs
```

In `processed`, `--upper-poster` supplies the photographic-led partial abstraction and `--poster` supplies the full-width extreme abstraction. The compositor derives the canvas from the source, uses `53 / 2 / 43 / 2`, and rejects upper occupancy outside 75–85%. The untouched `--original` remains the geometry and metadata authority and is never pasted into the artwork. `--width` and `--height` are proportional export caps only; `--export-long-edge` defaults to `3000`, and `0` disables the cap.

## Failure Modes and Quality Gate

### Gate Semantics

Treat this section as the validation layer, not as a second behavior specification. The Stage Contract, Canonical Abstraction Vocabulary, Upper Boundary Contract, Source-Faithfulness / No Fabrication Lock, stage-treatment rules, execution locks, palette rules, geometry rules, and layout rules remain the sole sources of behavior.

```yaml
gate_semantics:
  blocking:
    result: reject-current-candidate
    composition_allowed: false
    delivery_allowed: false
    action: regenerate-or-locally-correct-then-recheck
  non_blocking:
    result: correction-required
    composition_allowed: conditional
    delivery_allowed: false-until-resolved-when-visually-material
    action: correct-smallest-relevant-region-then-recheck
  rule_source:
    behavior_definition: existing-contracts-and-locks
    failure_detection: this-quality-gate
```

Any blocking failure immediately rejects the current candidate. Do not pass it into final composition or delivery.

### Blocking Reject Gate

#### A. Abstraction execution

- `A04`
  - name: `upper-vocabulary-overload`
  - trigger: upper uses more than one primary plus one supporting canonical operation, mixes more than one material voice per operation, or accumulates scattered textures and marks.
  - reject: `true`
  - repair: Remove the supporting operation first, enlarge the primary reconstructed regions, and simplify internal marks.
- `A05`
  - name: `non-counting-effect-substitution`
  - trigger: claimed abstraction consists mainly of grading, blur, haze, grain, texture, filtering, decorative marks, masking, edge treatment, or intact photography under a stylized surface.
  - reject: `true`
  - repair: Replace photographic material through a canonical operation.

#### F. Source faithfulness and fabrication

- `F01`
  - name: `major-content-fabrication`
  - trigger: a person, major object, building, landmark structure, or natural feature cannot be traced to visible source evidence or an explicit user request.
  - reject: `true`
  - repair: Remove or regenerate it; never retain invented content for composition, symbolism, or aesthetics.
- `F02`
  - name: `unsupported-person-replacement`
  - trigger: the primary person changes semantic identity, age/gender presentation, source-related pose/gesture/orientation, interaction, clothing category, or is replaced, multiplied, or given unsupported accessories.
  - reject: `true`
  - repair: Enforce strict position and facial identity in upper; permit lower spatial re-authoring and facial removal under the Stage Contract.
- `F03`
  - name: `unsupported-structure-completion`
  - trigger: architecture, anatomy, landscape, text, signage, or objects hidden, cropped, blurred, or ambiguous are confidently completed with unsupported detail.
  - reject: `true`
  - repair: Simplify, omit, use negative space, or leave incomplete marks instead.

#### P. Primary person and compositing

- `P00`
  - name: `upper-identity-fidelity-loss`
  - trigger: the upper primary face is not immediately recognizable at approximately 95% perceptual fidelity, or a major identity carrier is materially wrong.
  - reject: `true`
  - repair: Correct the smallest failing upper facial feature through regeneration or localized editing; never apply this gate to lower or use source compositing.
- `P03`
  - name: `source-person-reinsertion`
  - trigger: any original person, face, body, garment, or local photographic region is pasted into either generated stage.
  - reject: `true`
  - repair: Preserve upper facial identity through generation or localized editing; build lower personhood through non-photographic silhouette construction.
- `P04`
  - name: `human-layer-offset`
  - trigger: any duplicated person edge, shifted silhouette, partial body offset, non-overlapping body section, visible cutout seam, compositing offset, floating source fragment, pasted face/body, or mismatched resolution, noise, or exposure; exclude deliberate coherent sticker, paper-cut, or graphic edges.
  - reject: `true`
  - repair: Regenerate or locally edit the person region; never add source compositing.

#### B/H. Secondary living subjects

- `B04`
  - name: `upper-secondary-person-retention`
  - trigger: an upper non-primary person retains a face, garment texture, photographic detail, individual modeling, or differs from the one shared opaque flat fill.
  - reject: `true`
  - repair: Rebuild all upper non-primary people with the shared opaque flat silhouette treatment; evaluate lower separately.
- `H02`
  - name: `upper-crowd-fill-contamination`
  - trigger: upper non-primary people do not use one identical opaque flat color with crisp boundaries.
  - reject: `true`
  - repair: Correct upper overlaps by clean silhouette union or a narrow paper gap; do not apply this identical-fill gate to lower.

#### L/M. Architecture

- `L02`
  - name: `hierarchy-conflict`
  - trigger: no unmistakable hero remains, or upper supporting architecture retains photographic windows, façade texture, roof/masonry microdetail, or individually readable repetition; blur, grading, desaturation, distance, or small scale do not excuse retention.
  - reject: `true`
  - repair: Collapse supporting architecture to a quieter silhouette or simplified structural abstraction below the hero's contrast.
- `L04`
  - name: `recognition-skeleton-loss`
  - trigger: upper loses the hero's full recognition skeleton or lower loses the minimum recognition skeleton needed to identify the same architecture.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `M05`
  - name: `architectural-medium-replacement`
  - trigger: either stage replaces source architecture with a different building or invented components. Upper changes rendering state only; lower may radically change form placement and geometry emphasis while retaining the same semantic identity and minimum recognition skeleton.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `M06`
  - name: `upper-architectural-registration-failure`
  - trigger: the upper transition contains duplicated contours, shifted copies, detached fragments, offset openings, hard masking, or pasted layers. Lower spatial re-authoring is allowed but must remain semantically source-derived.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `M07`
  - name: `upper-architectural-reconstruction-dispersion`
  - trigger: the upper reconstruction is scattered as unrelated decorative patches rather than a coherent region or structurally connected system.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `M10`
  - name: `upper-architectural-surface-decoration`
  - trigger: the upper hero remains fully photographic beneath superficial lines or effects.
  - reject: `true`
  - repair: Replace photographic material with contiguous opaque or deliberately omitted planes; skeleton lines alone never pass.
- `M11`
  - name: `architectural-reconstruction-language-failure`
  - trigger: the upper reconstructed portion lacks one coherent planar material language, or its planes do not follow the building's frame, joints, massing, proportions, and recognition skeleton.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `M12`
  - name: `upper-structural-connection-failure`
  - trigger: photographic and reconstructed portions meet through arbitrary breaks, impossible joints, detached fragments, or unsupported transitions.
  - reject: `true`
  - repair: Reconnect them through credible structure or a deliberate source-grounded omission.
- `M08`
  - name: `upper-secondary-architecture-treatment-failure`
  - trigger: upper secondary architecture retains photographic detail or competes with the hero through elaborate reconstruction.
  - reject: `true`
  - repair: Collapse it to a quiet silhouette or simplified structural abstraction before composition; treat lower with simplified masses and sparse lines.

#### G/D. Ground and disposable supports

- `D02`
  - name: `disposable-support-retention`
  - trigger: an upper disposable support retains photographic material, or a lower support remains more detailed than an extreme semantic plane or omission.
  - reject: `true`
  - repair: Rebuild the support at the stage-required abstraction while preserving source-related support/contact logic.
- `D04`
  - name: `fixture-photographic-retention`
  - trigger: any connected portion of a non-hero seating fixture retains photographic upholstery, leather, wood grain, seams, cushion detail, masonry texture, wear, or surface microdetail.
  - reject: `true`
  - repair: Rebuild the complete fixture in one abstract language, including the body-contact zone, while preserving only support geometry and contact logic.
- `G01`
  - name: `ground-abstraction-failure`
  - trigger: upper ground lacks its contiguous reconstruction zone, or lower ground fails to become broad semantic planes with sparse source-derived perspective cues.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.

#### C. Palette and semantic masses

- `C06`
  - name: `upper-board-base-misfire`
  - trigger: the upper board base ignores scene semantics, lacks a source-derived relationship, competes with the authored image, collapses the free-edge contrast, reads as pure/near white without an explicit user request, or uses a saturated/random color outside the restrained Robot Dreams pale families. Re-select a visibly tinted warm ivory, dusty peach, powder blue, soft lilac, or mineral sage base with a documented semantic and contrast purpose.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `C07`
  - name: `upper-architecture-reconstruction-color-collapse`
  - trigger: the upper hero reconstruction uses a color too close to the retained photographic building tone, so the real/abstract partition is not immediately legible.
  - reject: `true`
  - repair: Recolor the complete reconstruction zone with a coherent family that creates strong hue, value, or temperature separation without introducing random neon, breaking source light direction, weakening architectural identity, or contaminating protected natural/living hues.

#### O. Boundary, geometry, and output

- `O14`
  - name: `original-panel-retention`
  - trigger: the untouched source photograph appears anywhere in the finished composition as a panel, inset, thumbnail, comparison strip, background, or visible source fragment.
  - reject: `true`
  - repair: Remove it and restore exactly two visible generated stages: photographic-led partial abstraction above and stronger abstraction below.
- `O06`
  - name: `upper-boundary-contract-failure`
  - trigger: the upper contour is a random blob, generic torn-paper shape, full-object cutout, noisy micro-contour, arbitrary crop, or color-key-derived alpha; or it cannot be explained by one dominant and at most one supporting source-semantic contour with 3–7 major directional changes. Rebuild only the boundary from source geometry without redesigning the upper composition. The lower panel remains a strict rectangle.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `O15`
  - name: `upper-boundary-overtracing`
  - trigger: the upper alpha follows leaves, hair, windows, railings, pedestrians, animals, furniture, ornaments, or other small-object silhouettes.
  - reject: `true`
  - repair: Remove micro-contours and restore one calm scene-level field.
- `O16`
  - name: `upper-boundary-source-disconnection`
  - trigger: the contour's entry, exit, dissolution, or major turns cannot be traced to roofline/façade, ridge/slope, shoreline/current, canopy/branch fall, cloud-bank flow, road/ground perspective, or primary pose/contact-ground evidence in the source.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `O07`
  - name: `source-orientation-failure`
  - trigger: the processed composition ignores source orientation, flattens portrait subjects, severely crops tall anchors, or ceases to derive its geometry from the source dimensions.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `O08`
  - name: `processed-layout-inconsistency`
  - trigger: processed output deviates from `53 / 2 / 43 / 2`, adds an alternate field or band, or places title/subtitle inside an image panel.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `O09`
  - name: `source-geometry-distortion`
  - trigger: either stage uses non-uniform x/y scaling, stretching, squeezing, widening, or flattening; or the upper no longer preserves source framing logic and proportional geometry.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `O11`
  - name: `upper-stage-untouched`
  - trigger: the upper section is merely the original photograph or differs only through minor grading, contrast, saturation, texture overlay, or white balance.
  - reject: `true`
  - repair: Regenerate it as a coherent photographic-led partial abstraction.
- `O12`
  - name: `stage-progression-failure`
  - trigger: the lower section is not materially more abstract than upper, either stage violates its rendering contract, or semantic identity/source-derived relationships no longer connect them. Different spatial organization and rendering vocabulary are expected and must not fail by themselves.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `O13`
  - name: `upper-stage-overabstraction`
  - trigger: the upper section loses photographic dominance, facial/landmark recognition, natural light logic, material depth, or source framing and reads as equally flat or abstract as the lower section.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `O10`
  - name: `fixed-canvas-forcing`
  - trigger: the final canvas must be derived from original width, height, aspect ratio, orientation profile, and relative section heights. Reject any output whose composition is controlled by a hard-coded `1800×3000`, `3000×1800`, `3:5`, `5:3`, or other rigid master canvas. Export bounds may resize the complete composition proportionally but may not redefine it.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.

#### X. Upper–lower progression and collage

- `X03`
  - name: `upper-panel-rectangularization`
  - trigger: the upper panel is a rectangle, arbitrary rectangular crop, or near-complete rectangle with slightly damaged edges.
  - reject: `true`
  - repair: Rebuild it from the Upper Boundary Contract.
- `X04`
  - name: `lower-panel-overphotographic`
  - trigger: the lower panel retains too much photographic detail and fails to reach 85–100% non-photographic reconstruction through the Canonical Abstraction Vocabulary.
  - reject: `true`
  - repair: Correct the smallest relevant region under the cited contract or lock, then recheck.
- `X08`
  - name: `lower-panel-human-readability-failure`
  - trigger: when a primary person exists, lower reduces that person to an unreadable blob, loses personhood, or breaks the head/torso/limb relationship, orientation, pose, gesture, or approximate body contour.
  - reject: `true`
  - repair: Rebuild a clearly human, source-related silhouette using one or at most two flat non-photographic colors.
- `X15`
  - name: `lower-primary-person-color-oversegmentation`
  - trigger: the lower primary person uses more than two colors, gradients or tonal modeling, or assigns different colors to clothing layers, skin, limbs, torso, joints, or anatomical structure.
  - reject: `true`
  - repair: Collapse the complete figure to one or two flat colors and recover readability through silhouette and pose rather than internal color separation.
- `X09`
  - name: `lower-panel-robot-dreams-palette-failure`
  - trigger: the lower panel does not use a coherent 4–6 color `robot-dreams-logic` system with warm/cool hierarchy, softened colors, 2–3 value steps, charcoal/deep blue instead of pure black, and at most one concentrated accent.
  - reject: `true`
  - repair: Rebuild the palette through complete semantic masses.
- `X11`
  - name: `processed-hierarchy-failure`
  - trigger: the upper board is not 53%, either black band is not 2%, the lower full-width panel is not 43%, or the upper board no longer reads as the dominant section.
  - reject: `true`
  - repair: Restore the exact `53 / 2 / 43 / 2` hierarchy.
- `X13`
  - name: `lower-panel-fit-failure`
  - trigger: the lower abstraction is stretched, squeezed, letterboxed, margined, or fails to cover the complete 43% full-width rectangle.
  - reject: `true`
  - repair: Refit it edge-to-edge with aspect-ratio-preserving cover and modest source-aware cropping.
- `X14`
  - name: `upper-authored-image-occupancy-failure`
  - trigger: the visible alpha-shaped upper artwork occupies less than 75% or more than 85% of the 53% board, or reaches that range through clipping, stretching, or rectangularization.
  - reject: `true`
  - repair: Refit within 75–85% while preserving the complete irregular contour and proportional geometry.
- `X12`
  - name: `upper-alpha-color-shift`
  - trigger: the upper panel changes hue/value after being placed in the collage, or pale interior artwork (warm ivory architecture, clouds, highlights, skin, or paper planes) becomes transparent/gray because a sampled background color was keyed out. Rebuild the alpha from the authored outer contour only, use an explicit mask or true RGBA generation, and compare isolated versus composited RGB before delivery.
  - reject: `true`
  - repair: Never repair this by recoloring the whole upper panel.

#### Q. Artistic quality regression

- `Q00`
  - name: `artistic-quality-regression`
  - trigger: a technically safer or more source-faithful revision is materially worse as an artwork through pixelation, posterization, coarse quantization, generic masking, pasted-person edges, lower resolution, weakened palette, or lost semantic structure.
  - reject: `true`
  - repair: Keep the artistically stronger version and solve only the specific identity issue.

### Non-Blocking Quality Corrections

- **`S01 proposition-drift`:** every major intervention supports the source-grounded artistic proposition; no decorative motif competes with it.
- **`R01 recognition-loss`:** the source remains recognizable through large relationships and preserved evidence rather than copied microdetail.
- **`A01 insufficient-abstraction`:** upper counted reconstruction misses its chosen light/medium/strong tier, or lower misses its 85–100% non-photographic contract. Count only Canonical Abstraction Vocabulary operations.
- **`A02 single-region-abstraction`:** upper counted abstraction does not span at least two major semantic regions. Lower is instead evaluated for complete extreme semantic reconstruction across its visible field.
- **`A03 upper-photographic-corridor`:** no uncontrolled continuous upper environmental photographic corridor exceeds 35% of the full upper artwork area; exclude the primary-face identity region and upper hero architecture governed by its 55/45 rule. Do not apply this gate to lower.
- **`C01 mass-fragmentation`:** the scene reads as a few coherent semantic masses.
- **`C02 boundary-crossing`:** color fields remain inside their semantic regions.
- **`C04 sky-fragmentation`:** upper sky loses its continuous source-neighbor atmospheric field, or lower sky loses recognizable environmental association under source-derived semantic color relationships. Lower need not preserve literal same-family local color.
- **`C03 accent-scatter`:** the source-derived echo color is concentrated, visible, and subordinate.
- **`C05 weak-palette-separation`:** upper fails to improve separation through coherent built-region interventions while protecting source-neighbor natural hues, or lower fails semantic separation within its Robot Dreams hierarchy.
- **`L01 upper-landmark-generic`:** the upper hero loses decisive identifiers or its reconstructed portion no longer derives from the source recognition skeleton. Lower is evaluated by semantic identity and minimum recognition skeleton, not the upper 55/45 balance.
- **`L03 architecture-erasure`:** in upper, preserve recognizable architecture at its source location, footprint, silhouette, viewpoint, and perspective. In lower, permit spatial re-authoring but require the same architectural semantic identity, minimum recognition skeleton, and source-derived structural relationships. In either stage reject replacement by unrelated structures.
- **`L05 architectural-detail-undercompression`:** repeated windows, columns, brick seams, trim, carving, ornament, or façade texture are copied one by one and overwhelm the building's graphic read. Compress them into fewer source-aligned structural rhythms without changing architectural identity.
- **`P01 stage-person-contract-drift`:** upper fails its face/pose/contact fidelity requirements, or lower fails its readable abstract silhouette while retaining prohibited realistic face/skin/material detail.
- **`P02 identity-integration-failure`:** an upper person appears accidentally pasted, patched, mismatched, or anatomically broken, or a lower silhouette loses coherent personhood. Regenerate the relevant stage; never repair by source compositing.
- **`B01 biological-language-split`:** every non-human living individual or connected organism uses one coherent treatment across its complete visible body. No tree mixes photographic trunk/branches with abstract foliage; no animal or bird mixes photographic anatomy with graphic body regions. Reclassify the whole organism as photographic or abstract and restore/rebuild it consistently before delivery.
- **`B02 living-subject-split`:** within each stage, a non-primary organism uses one coherent treatment. For the upper primary person, require coherent anatomy and facial identity; for lower, require coherent abstract personhood without realistic face or material detail.
- **`B03 living-cluster-retention`:** a detected cluster retains photographic miniatures or loses its group identity. In upper, use one shared abstract language; in lower, use grouped semantic masses or compatible shared silhouettes.
- **`V01 weak-virtual-real-contrast`:** both photographic evidence and authored abstraction are materially visible; the result is neither an almost unchanged photograph nor a nearly unrelated full illustration.
- **`V02 upper-architectural-balance-failure`:** the upper hero does not retain approximately 55% photographic reality plus approximately 45% visible contiguous planar material replacement, optionally supported by semantic omission. Recognition-skeleton lines contribute zero coverage. Never apply this gate to lower architecture, which should be extremely reconstructed.
- **`V03 transition-disorder`:** upper real/abstract boundaries ignore source structure or scatter competing media. Lower may re-author boundaries but must keep coherent semantic masses and source-derived relationships.
- **`H01 vocabulary-collision`:** architecture, identity anchors, and secondary people use distinct visual vocabularies; crowd silhouettes contain no architectural line work.
- **`D01 detail-clutter`:** nonessential fixtures and repetitive textures are simplified.
- **`D03 upper-architectural-structural-misalignment`:** reconstructed supports, joints, axes, planes, openings, or frames break the source building's perspective, proportions, or recognition-critical structural relationships. Do not apply exact registration requirements to lower spatial re-authoring.
- **`G02 ground-detail-overload`:** repeated paving units, stone texture, seams, or surface noise dominate the ground and compete with the hero. Compress them into broad planes, sparse perspective lines, controlled omissions, or one restrained graphic medium.
- **`M01 unjustified-module`:** optional modules appear only when enabled and propositionally relevant.
- **`M02 palette-reference-overreach`:** a named palette copies exact frames, characters, or composition. In upper, keep natural/living hues source-neighbor plausible; in lower, require source-derived semantic relationships under Robot Dreams rather than literal local fidelity.
- **`M13 upper-architectural-thumbnail-legibility`:** at reduced size the hero silhouette, 55/45 contrast, recognition skeleton, or reconstructed structure is unclear. Lower is judged by minimum recognition skeleton instead.
- **`M09 upper-hero-selection-failure`:** no upper hero is identified by source dominance or compositional harmony when architecture is present.
- **`M04 robot-dreams-auto-misfire`:** for upper automatic palette selection, Robot Dreams lacks sufficient built/design levers, weakens source truth, or fails its comparison against `shifted`. Lower Robot Dreams is mandatory and is instead evaluated by `X09` for coherent source-derived semantic color relationships.
- **`T01 copy-generic`:** original copy is specific to the source and proposition; quotations and cinematic references are verified.
- **`T02 typography-failure`:** processed title or subtitle is illegible, not centered in its 2% black band, visually dominant, inconsistent in size/color, or placed inside an image panel.
- **`O01 wrong-mode`:** delivery uses any mode or layout other than processed `53 / 2 / 43 / 2`.
- **`O03 semantic-boundary-failure`:** the upper architectural reconstruction boundary or other authored content boundary is generic, arbitrary, or unrelated to source geometry and structure. The lower panel itself remains a complete rectangle; its internal abstraction must still express the scene's dominant structure.
- **`X01 panel-redundancy`:** the lower panel is too similar to the upper panel in structure, abstraction depth, or visual role.
- **`X02 weak-abstraction-escalation`:** the lower rectangular panel is not materially more abstract than the upper panel.
- **`X05 processed-incoherence`:** the upper and lower panels do not feel like one unified artwork or one shared proposition.
- **`X06 processed-copy-placement-failure`:** title or subtitle leaves its centered black band, enters an image panel, or introduces a fabricated date.
- **`X07 role-reversal`:** the lower panel or typography dominates while the upper fails to remain the primary visual entry point.
- **`X10 processed-spacing-failure`:** either 2% band becomes visually heavy, inconsistent, or disrupts the exact `53 / 2 / 43 / 2` rhythm.
- **`O02 filter-look`:** the first pass visibly changes at least two of these three properties in each counted region—outer/inner structure, material/rendering language, or region boundary/omission pattern—and reads as authored reconstruction rather than global styling. If it remains plausible as the original photo with altered color/texture, fail immediately and regenerate at the chosen tier.

### Repair and Recheck Protocol

1. Record only the failed codes.
2. Stop composition or delivery whenever any blocking code is present.
3. Correct one code at a time in the smallest relevant region. Preserve successful regions and the visual master; never degrade the complete artwork to satisfy a local metric.
4. Use regeneration or localized generative editing for person/compositing failures. Never add source compositing.
5. Re-run the relevant stage contract and execution lock after each correction, then recheck the complete Failure Modes and Quality Gate.
6. Continue to composition or delivery only when no blocking code remains and every visually material non-blocking correction is resolved.
