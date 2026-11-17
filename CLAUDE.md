# Vimana Grammar: notes for Claude

A browser-based 3D model of an idealized Chola temple at Thanjavur (Brihadisvara): the tower (vimana), its front halls, the court, the cloister and the two gateways. Every element and dimension is tagged with the evidence behind it. Live at https://purplefaucet.github.io/temple_project/, served by GitHub Pages from `main`.

The owner is new to GitHub and works partly from a phone. Explain git and GitHub steps in plain words, name the exact buttons, and say when a change is live. Cite claims, and say when you are less than 80% sure of one.

## Files

- `index.html`: the whole app, about 2,000 lines, with no build step. three.js r128 is loaded from cdnjs.
- `research/*.md`: research notes, one per build phase: `mandapa.md` (halls), `compound.md` (court), `measurements.md` (OpenStreetMap and satellite measurements), `gopuram.md` (gateways), `decoration.md` (carved detail: mouldings, pilasters, cornices, niches). Each build was done from these notes. Read the relevant one before changing that part.
- `sources/` and `*.pdf` are git-ignored. The Mayamata scan lives there on the owner's Mac and must never be committed, nor its OCR text copied into the repo. Notes contain summaries and short quotes only.

## The evidence model (keep it intact)

Every element is created with `mk(key, name, tier, rule, o)`:
- `tier`: `'rule'` (a documented convention puts it there, drawn solid), `'inf'` (plausible, not firmly documented, translucent amber) or `'inv'` (invented filler, hatched).
- `rule`: the explanation shown in the inspector, with citations written `[@key]`, where `key` is an entry in `SRC`.
- `o.dims`: one entry per dimension, `[label, T|B|E, text]`, for Text, Buildings (measured or described) or Estimate. These drive the "Dimensions" colouring.
- `o.src`, `o.conf` (a percentage, Claude's own estimate), `o.basis`, `o.gram` (its line in the shape grammar).

New sources go in `SRC` with `n`, `u`, `use` and `rel`. `rel` says how the source was read: directly, as excerpts from a fetch tool, or from photographs. Conflicts between sources, estimates and inferences below about 80% go in the "Not verified" list on the page. Never present an estimate as a measurement.

## Scope rules

- **Allowed:** exterior architecture, plus the halls' interiors.
- **No sanctum interior.** The walk stops at a closed sanctum door.
- **Deities only on the outside.** Deity imagery may appear on exterior decoration (gateway and wall sculpture, reliefs, stucco figures, exterior niches). None inside any building: not in the halls, the shrines or the cloister cells. This is the owner's rule.
- **How sculpture is shown now.** On the gateways, in the tower's wall niches and beside the ardhamandapa's side doors (outside) it is drawn as generic figures from `figureGeoms()`: plain standing or seated shapes with no attributes or held objects, at the recorded size where one is known. Evidence text must say their forms are invented. The tower's lower storey has closed doors at its central openings. Elsewhere (the Nandi bull, the wall-coping Nandis) it is still blank blocks. Real photographs are used on the Rajarajan's east and west faces (the "Gateway sculpture" control, default Photographs; the owner adopted them after a trial): on the east, the two guardians and the base panels; on the west, the corner and porch niche figures and the outer bays' base panels (`PHOTO_UNITS_W`, `PHOTO_WEST`), from `assets/sculpture/`, with credits in its `CREDITS.md`. More faces can be added the same way: new files in `assets/sculpture/` with credits, then entries like `PHOTO_UNITS` and `PHOTO_GUARD`. In code: `PHOTO_UNITS` and `PHOTO_GUARD` place them, `photoMat()` caches their textures, `matOf()` keeps photos as photos in every colour mode, and their elements set `noMerge` so `mergeParts()` leaves them alone. Any photograph used must be credited on the page (the sources list and the "About this page" paragraph). Some crops are CC BY-SA 3.0; whether that licence extends to the rendered model is unsettled.
- **Later additions** (Nayak, Pandya, Maratha) appear only under the court's "With later additions" period switch, labelled with their dates.

## Code map

- **Units:** model units, with the base width `W = P.base` standing for 30.18 m. `upm()` converts metres to units. Measured figures are written in metres times `s = upm()`.
- **Axes:** +z is temple east (toward the gateways), +x is temple north, the tower is centred at the origin. The real axis bearing is 70.1°: +z bears 70.1° and +x 340.1°. Only the sun uses it.
- **Build order:** `build()` makes the tower, then `buildHalls()` if `P.halls`, then `buildCourt()` if `P.court`, which uses `gopuramParts()` and the `GOP` table for the gateways. `mergeParts()` then joins each element's parts into one mesh. This is a performance fix for phones: keep new parts going through `put()` or the court's `add()`, so they merge.
- **Carved detail (the kit above `buildHalls`):** `sweep(path, profile)` runs a moulding profile along a plan outline with mitred corners; `socleProf()`, `baseProfs()` and `entProf()` are the sub-base, base and entablature profiles; `pilasterGeoms()`, `nicheGeoms()`, `kuduGeom()` and `facing()` (a wall face with recesses) make the rest; `onSide()` places a piece made in a face's own frame. New ornament goes into an existing element's geometry (`putAll(meta, list)`) or into one shared element such as `wall-niches`, never into a new element per tier, so draw calls stay flat. `HI` is the "Detail" control (`P.detail`, Standard on touch devices): same elements, finer parts.
- **Stone surface:** `stoneSurface()` adds grain and block joints to the stone and amber materials in the shader (`STONE` holds the uniforms and the noise texture). It is artistic and says so on the page. It fades out by about 90 m, so the orbit view keeps flat evidence colours. `mono(geometry)` marks a piece as one stone (figures, arches, dormers) so no joints cross it. `jala(geometry)` marks a barrel roof, and the shader draws the net pattern photographs show on the gateways' roofs.
- **Walk mode:** `WK` holds raised floors (`plats`), stair ramps (`ramps`), solid footprints (`obs`) and roofs (`roofs`, for the indoor light), all rebuilt by `build()`. A walker climbs at most 0.6 m per step. New solid things need an `obs` entry, new floors a `plat`.
- **Walk feel:** stairs are slopes and are followed exactly; any other change of floor is eased through `wk.off`. `walkFeel()` runs once a frame for the head-bob (`P.bob`, off under reduced motion) and that easing. Speed is eased in `stepWalk()`. Mouse look uses the browser's pointer lock on desktop (`P.mlook`, `locked()`): a click in walk mode locks, a click while locked inspects the middle of the view, and the first Esc only frees the mouse. Anything that moves the walker somewhere new should go through `settleWalker()`, which resets these.
- **Light:** `P.day` (day of 2026) and `P.time` (minutes, Indian Standard Time) drive `applyLight()`. `sunAt()` gives the sun's height and bearing for Thanjavur (the Astronomical Almanac's approximate formula, checked against SunCalc), turned into the model's frame with the axis bearing. Everything else is artistic and says so on the page: the sky dome (`sky`, a shader that follows the camera), the haze (`scene.fog`, lighter in orbit so the evidence colours stay readable), `glowL` (twilight and night fill) and the stars. Shadows are redrawn only when `shadowTouch()` is called, so call it after anything that changes what casts a shadow.
- **Hall lamps:** the `hall-lamps` element is Invented. Its flames are a second mesh marked `userData.night`, shown only when `lampsLit`. Real light comes from three shared point lights (`lampL`) that `updateLamps()` moves to the lamp pairs nearest the camera (`WK.lamps`). Keep the number of lights in the scene fixed: adding or hiding a light recompiles every shader.
- **Footsteps:** `footfall()` fires once a stride from `walkFeel()`. `surfaceAt()` picks stair, hall, court or earth (outside `CXT.inside`), and `footstep()` builds the sound from filtered noise with Web Audio. No sound files are loaded. If recordings are ever added, credit them like the photographs.
- **Journal:** `discover(m)` runs when an element is inspected in walk mode. Entries are per kind of element (`famOf()` folds "Tier 3 of 13" into "Tower tier"), and the text is the inspector's own, read from the current model. Only the names found are saved, in `localStorage`.
- **Map:** `miniPlan()` draws the plan from `WK` after each build, and `miniDraw()` centres it on the walker. Anything given an `obs`, `plat` or `ramp` shows up on it without more work.
- **Camera framing:** `CXT` holds the complex's extents, used for framing, shadows, the ground size and the "Go to" viewpoints (`viewSpec`).

## Testing (the cloud sandbox blocks cdnjs)

There is no test suite. Check changes in headless Chromium with Playwright:
- **Launch:** start a local server (`python3 -m http.server 8765`) and launch with `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`.
- **three.js:** cdnjs is blocked, so fetch the same version with `npm pack three@0.128.0` and serve `build/three.min.js` through `page.route('**/three.min.js', ...)`.
- **Internals:** to reach internal state, serve `index.html` through `page.route` with `'use strict';` replaced by `'use strict'; window.__t=function(){return {wk:wk, ...};};`.
- **Sound:** nothing can be heard in headless tests. Render `footstep()` into an `OfflineAudioContext` and check the result is neither silent nor NaN.
- **Pointer lock:** headless Chromium refuses it. Test mouse look by replacing `document.pointerLockElement` and the canvas's `requestPointerLock` with stand-ins and sending `pointermove` events that carry `movementX`.
- **What to check:** no console or page errors; screenshots of the views touched; walking routes (stairs, doors, walls); tapping elements; a 390 × 844 touch viewport with no horizontal scroll.
- **Performance:** `renderer.info.render.calls` is about 124 in the default view; don't let it climb back toward 1,000. The model is about 250,000 triangles at High detail and 200,000 at Standard. That figure leaves out the shadow pass, which three.js does not count. The shadow pass costs about as much again, and now runs only when the light or the model changes.
- **Light:** check noon, a low sun, dusk and night. A colour or intensity that becomes NaN turns the whole model black with no error.

Run a syntax check after edits:
`node -e "new Function(require('fs').readFileSync('index.html','utf8').split('<script>')[1].split('</script>')[0])"`

## Git and publishing

- Work on a branch, open a pull request, and merge only when the owner says so. Merging to `main` publishes the site within a minute or two. Check the "pages build and deployment" run or the repo's Deployments.
- **Commit messages:** do not add `Co-Authored-By` or session-link lines. The owner removed them from this repo.
- The owner pushes research notes from a Mac with GitHub Desktop, so `main` may move between sessions. Fetch and branch from the latest `main` before starting.

## How a phase is done

1. Research happens in a desktop Claude chat on the owner's Mac, which can read the Mayamata scan and reach wisdomlib, OpenStreetMap and Google Maps. Cloud sessions cannot reach those sites. The chat writes `research/<topic>.md` in the format of the existing notes (sources table, findings, measurements normalised to W, a build spec with evidence tags, conflicts, what is unread) and pushes it.
2. A Claude Code session builds from the notes, tests, and opens a pull request with screenshots.
3. The owner merges, then pulls in GitHub Desktop.

## Known gaps

- Mayamata volume 2 (gateways, chapter 24; pavilions and halls, chapter 25) has not been read.
- Pichard, *Tanjavur Brhadisvara: An Architectural Study* (1995), has not been read. It would replace many estimates.
- Hall heights, gateway heights and pavilion counts are estimates from photographs.
- Whether the hall roofs carry pavilions was not checked.
