---
title: "HELIX hero — planning and execution as a double helix"
component: "hero illustration"
generator: nano-banana-pro-openrouter
model: gemini-3-pro-image-preview
aspect_ratio: "9:16"
size: "2K"
output: helix-hero.png
depends_on:
  - .stitch/DESIGN.md
  - website/content/docs/background.md
---

# Prompt

A tall, portrait-oriented editorial illustration of two intertwining ribbon strands forming a double helix, running vertically through the full height of the canvas. This is not a biology diagram — it is a metaphor for two co-dependent processes that feed back into each other continuously.

**The coral strand** (warm terracotta, #C44B2F) represents the planning loop: review, validate, govern. It flows smoothly, with confident intentionality — this is the strand that shapes what happens next.

**The indigo strand** (cool blue-indigo, #3B6BA8) represents the execution loop: build, measure, record. It is continuous and persistent — this is the strand that makes things real.

Neither strand leads. They are equal in visual weight, intertwined by design, each one informing the other as they wind together from top to bottom. The two strands cross each other at regular intervals — at each crossing, the front strand is clearly in front of the back strand, with proper occlusion. The z-ordering alternates: coral in front for one half-turn, indigo in front for the next.

**Between the strands**, at each crossing point, there are short connecting bridges — transverse rungs rendered in violet (#6842A8), each one a gradient from coral on one end to indigo on the other. These are the feedback moments: where execution surfaces something that changes the plan, or where planning adjusts what gets built next. The rungs are substantial and confident, not decorative — they carry the meaning of the image.

**Form:** Each strand is a smooth, flowing ribbon — slightly faceted to convey gentle volume, with a soft gradient shading from a lighter leading edge (#E07A5F for coral, #6B9FD4 for indigo) to a slightly deeper receding face (#C44B2F for coral, #3B6BA8 for indigo). No harsh shadows. No reflective or metallic surfaces. No CGI specularity or glossy highlights. The depth comes from careful tonal modulation, not from dramatic lighting.

**Atmosphere:** The background is pure white or the faintest warm off-white (#F9F8F6), with a barely perceptible radial glow centered behind the helix — the softest possible halo of coral-to-indigo at no more than 5% opacity, suggesting that the helix generates its own quiet energy. The helix itself has very soft, warm drop shadows beneath each strand to anchor it in space — extremely subtle, not dramatic.

**Composition:** The helix runs from near the top edge to near the bottom edge of the tall canvas, centered horizontally. Approximately 2.5 full turns are visible. The strands occupy roughly the center 55% of the canvas width, with generous breathing room on either side. The helix is the only subject — no background elements, no additional shapes, no decorative frames.

**Style reference:** The feeling of a Stripe or Linear hero illustration — expressive and precise, with atmospheric depth, not a flat icon and not a CGI render. Rendered with care: the kind of illustration that looks hand-considered even though it is digital. Clean enough to read at a glance, rich enough to reward a second look.

**Portrait orientation is required.** The canvas must be taller than it is wide. The helix flows vertically.

# Style constraints (.stitch/DESIGN.md)

- Coral strand: #C44B2F body, #E07A5F highlight edge
- Indigo strand: #3B6BA8 body, #6B9FD4 highlight edge
- Rungs: gradient #C44B2F → #6842A8 → #3B6BA8
- Background: pure white or #F9F8F6. No dark backgrounds.
- Surfaces: matte with subtle tonal gradient for volume. No gloss, no specularity, no metallics.
- Atmosphere: faint radial glow behind the helix only, ≤5% opacity, coral-to-indigo.
- Z-ordering: alternating per half-turn — front strand clearly occludes back strand.
- Register: expressive editorial illustration. Atmospheric, precise, not clinical.

# Negative prompt

DNA molecule, biology textbook, double helix laboratory diagram, anatomical illustration, CGI 3D render, photorealistic lighting, specular highlights, metallic surfaces, glass surfaces, glossy reflections, neon colors, dark background, black background, gradient background, glowing strands, particle effects, sparkles, lens flares, motion blur, circuit board, neural network sphere, abstract nodes, network graph, robot imagery, human figures, hands, faces, brain imagery, watercolor, hand-drawn sketch, flat vector icon, pixel art, anime style, cartoon shading, cel shading, isometric 3D, landscape orientation, horizontal composition, wide canvas, text, labels, watermarks, logos, decorative borders, vignette.

# Acceptance criteria

- Canvas is portrait orientation (taller than wide).
- Two distinct strands clearly visible throughout — coral and indigo, equal visual weight.
- Z-ordering correct and apparent: strands alternate in front across crossings.
- Violet rung connections visible at each crossing, with coral-to-indigo gradient.
- Matte surfaces — no CGI specularity, no gloss.
- Background is white or near-white; helix is the only subject.
- Expressive illustration register — not a biology diagram, not a CGI render.
- Approximately 2–3 full turns of the helix visible from top to bottom of frame.
- File ≤ 500KB after WebP conversion at quality 85.
