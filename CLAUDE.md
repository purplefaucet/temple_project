# Vimana Grammar: notes for Claude

A browser-based 3D model of an idealized Chola temple at Thanjavur (Brihadisvara): the tower (vimana), its front halls, the court, the cloister and the two gateways. Every element and dimension is tagged with the evidence behind it. Live at https://purplefaucet.github.io/temple_project/, served by GitHub Pages from `main`.

The owner is new to GitHub and works partly from a phone. Explain git and GitHub steps in plain words, name the exact buttons, and say when a change is live. Cite claims, and say when you are less than 80% sure of one.

## Files

- `index.html`: the whole app, about 2,000 lines, with no build step. three.js r128 is loaded from cdnjs.
- `research/*.md`: research notes, one per build phase: `mandapa.md` (halls), `compound.md` (court), `measurements.md` (OpenStreetMap and satellite measurements), `gopuram.md` (gateways). Each build was done from these notes. Read the relevant one before changing that part.
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
- **No deity imagery.** Figure sculpture (guardians, the Nandi bull, base reliefs, wall-coping Nandis) is drawn as blank blocks of its recorded size.
- **Later additions** (Nayak, Pandya, Maratha) appear only under the court's "With later additions" period switch, labelled with their dates.

## Code map

- **Units:** model units, with the base width `W = P.base` standing for 30.18 m. `upm()` converts metres to units. Measured figures are written in metres times `s = upm()`.
- **Axes:** +z is temple east (toward the gateways), +x is temple north, the tower is centred at the origin. The real axis bearing is 70.1°, not used in the model.
- **Build order:** `build()` makes the tower, then `buildHalls()` if `P.halls`, then `buildCourt()` if `P.court`, which uses `gopuramParts()` and the `GOP` table for the gateways. `mergeParts()` then joins each element's parts into one mesh. This is a performance fix for phones: keep new parts going through `put()` or the court's `add()`, so they merge.
- **Walk mode:** `WK` holds raised floors (`plats`), stair ramps (`ramps`), solid footprints (`obs`) and roofs (`roofs`, for the indoor light), all rebuilt by `build()`. A walker climbs at most 0.6 m per step. New solid things need an `obs` entry, new floors a `plat`.
- **Camera framing:** `CXT` holds the complex's extents, used for framing, shadows, the ground size and the "Go to" viewpoints (`viewSpec`).

## Testing (the cloud sandbox blocks cdnjs)

There is no test suite. Check changes in headless Chromium with Playwright:
- **Launch:** start a local server (`python3 -m http.server 8765`) and launch with `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`.
- **three.js:** cdnjs is blocked, so fetch the same version with `npm pack three@0.128.0` and serve `build/three.min.js` through `page.route('**/three.min.js', ...)`.
- **Internals:** to reach internal state, serve `index.html` through `page.route` with `'use strict';` replaced by `'use strict'; window.__t=function(){return {wk:wk, ...};};`.
- **What to check:** no console or page errors; screenshots of the views touched; walking routes (stairs, doors, walls); tapping elements; a 390 × 844 touch viewport with no horizontal scroll.
- **Performance:** `renderer.info.render.calls` is about 130 in the default view; don't let it climb back toward 1,000.

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
