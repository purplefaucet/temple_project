# Thanjavur (Brihadisvara) compound: measurements from map data

Measured 29 October 2026 for the compound phase of the build. Companion to `compound.md`; the conflicts it flagged are addressed in §9.

W = 30.18 m (the tower's published base width, from `compound.md`). Ratios to W are given where useful.

## 1. Method

**Primary source: OpenStreetMap.** Overpass API query of everything within 450 m of 10.7828 N, 79.1318 E (`way(around:450,…); relation(around:450,…); out body geom;`), OSM data timestamp 2026-10-29T13:25:51Z. Coordinates were projected to local metres (WGS84 ellipsoid radii at 10.7825 N; projection error is negligible over 500 m) and then rotated into the temple's own axis frame (§2). Every OSM figure below names the way it comes from, so it can be re-derived.

**Check source: Google Maps satellite view** (built-in browser on the Mac, not desktop computer use: computer use cannot drive websites, and Google Earth was not needed). Points were read from the map's right-click coordinate readout at zoom 20 (about 0.18 m per screenshot pixel) and run through the same projection; two figures use Google's *Measure distance* tool directly and are labelled as such.

**Imagery caveat that drives most of the error estimates.** The Google (Airbus) image is strongly oblique: the camera was to the NE, so every elevated part is shifted toward the SSW (bearing about 215°). The tower's finial appears about 27 m from where its base is. Consequences:
- Distances between features at the **same height** (roof edge to roof edge, ground line to ground line) are unaffected. All Google checks below are of that kind.
- Mixing a roof point with a ground point is not safe. My first attempts at the inner (court-side) cloister corners did exactly that and disagreed with OSM by up to 6 m; they are not used.
- Tall-object footprints (the tower, gopuram bases on their SW sides) are partly hidden.
- Google imagery sits about 3–5 m east and 5 m north of the OSM geometry. That is a uniform registration offset and does not affect distances.

**What OSM mapped.** Found and used: the cloister as a ring with both faces (way 120390894), the tower as 3D building parts (889377944–889377951), the halls (889377945), both gopurams (890154570 Rajarajan, 120390895 Keralantakan, plus upper-storey parts), the Nandi pavilion (55904677), the shrine north of the tower (55904675) and the later shrines, and one enclosing wall (457131358), which is the later fort. **Not mapped:** any Chola-period outer wall separate from the fort; the gopurams' plinths; the tower's base mouldings.

## 2. Orientation: the axis is not east–west

The whole compound is rotated. Long edges of the cloister, the temple outline, the tower faces, both gopurams and the Nandi pavilion all give an axis bearing of **70.1° ± 0.3°** (they were mapped as separate ways, probably by more than one mapper, and agree to within 0.6°). The temple faces ENE, about 20° north of east. The tilt is plainly visible in the satellite view, so it is not a mapping artefact (confidence about 95%).

All figures below are in this axis frame: **u** runs along the axis toward the gateways (temple "east"), **v** runs across it toward temple "north" (bearing 340.1°). "East–west" and "north–south" in the brief are taken to mean these temple directions.

For the model: `compound.md` §6 says "long axis east–west". If the site is ever placed on a real map or given a sun direction, rotate it 19.9° anticlockwise from true east.

## 3. Results summary

| # | Measurement | Value | Method | Est. error |
|---|---|---|---|---|
| 1a | Open court, inside the cloister, along axis | **228.3 m** (7.56 W) | OSM inner ring of way 120390894 (north side 228.2, south side 228.4) | ±4 m |
| 1b | Open court, across axis | **109.0 m** (3.61 W) | Same ring (west and east sides both 109.0) | ±4 m |
| 1c | Outside of cloister walls, along axis | **241–243 m** (OSM 243.0 S side, 241.9 N side; Google roof-to-roof 238.7 S, 240.8 N) | OSM outer ring; Google coordinate readout; Google *Measure distance* gave 238.7 m for the S side | ±3 m |
| 1d | Outside of cloister walls, across axis | **120–121 m** (OSM 120.9 W, 121.4 E; Google 119.9 W, 119.5 E) | As 1c | ±2 m |
| 1e | Cloister band depth (outer face to court edge) | 6–8 m: W 6.7–7.3, E 6.2–8.0, N 6.1–6.5, S 5.9–6.3 | OSM ring | ±2 m |
| 2a | Tower centre to west wall | **60.8 m** outer face (2.01 W); 53.6 m court edge | OSM tower core/finial (889377951, 889377944) to ring | ±3 m |
| 2b | Tower centre to north wall | **62.0 m** outer; 55.7 m court edge | As 2a | ±3 m |
| 2c | Tower centre to south wall | **59.4 m** outer; 53.3 m court edge | As 2a | ±3 m |
| 3 | Rajarajan to Keralantakan, centre to centre | **71.9 m** (2.38 W) | OSM footprint centroids; Google east-face ground lines 70.9 m apart (OSM 72.5) | ±2 m |
| 4a | Rajarajan gopuram base | **25.6 m across × 16.7 m along** the axis | OSM 890154570 | ±2 m |
| 4b | Keralantakan gopuram base | **29.4 m across × 17.6 m along** | OSM 120390895; Google *Measure distance* along the east face gave 32.9 m (probably includes plinth) | ±3 m across, ±2 m along |
| 5a | Halls' front to Nandi pavilion | **45.8 m** from main east face; 39.3 m from portico front; 28.6 m from foot of front steps | OSM 120390896 / 889377952 to 55904677; Google agrees within ~2 m | ±2 m |
| 5b | Nandi pavilion footprint | **12.4 × 12.3 m** | OSM 55904677 | ±1.5 m |
| 6a | Tower centre to shrine north of tower | **29.4 m** (9.4 m along, 27.8 m across) | OSM 55904675 centroid | ±3 m |
| 6b | That shrine's footprint | **6.3 m along × 10.2 m across** | OSM 55904675 | ±2 m |
| 7 | Outer (fort) wall | 18.0 ha; irregular, about 498 m E–W × 570 m N–S on true bearings | OSM 457131358 | area ±0.5 ha |

Detail and caveats for each item follow.

## 4. Inner court and cloister (item 1)

OSM traces the cloister as a single ring (way 120390894) whose outline runs the outer face, crosses the east range at the gopuram, and returns along the court-side face. That gives both faces from one consistently drawn object.

- **Court-side ring: 228.3 × 109.0 m.** This is the open court measured to the cloister's court-side edge as seen from above, i.e. probably the eave or colonnade line, **not** the inner face of the back wall, which is under the roof and invisible in imagery. The inside face of the outer wall should lie roughly between the two rings, a wall's thickness inside the outer ring.
- **Outer ring: 243.0 × 121.4 m (OSM); 239.7 × 120.0 m mean (Google, roof edge to roof edge).** The two sources differ by 1–1.5%. Neither is ground truth; I'd use **241 × 121 m** with ±3 m.
- A separate, larger OSM outline for the temple as a place of worship (way 1564782452) measures 246.3 × 123.7 m. It looks like a looser trace of the same cloister, so it is not treated as a separate wall.
- **The ASI figure of 240.9 × 122 m matches the outside of the cloister, not the inside.** `compound.md` §4 records it as the "inner (cloistered) court" and §6 builds the court as 8 W × 4 W. The open court is about 7.6 W × 3.6 W.
- Court-side measurements are the weakest numbers here (±4 m), because the OSM mapper's choice of edge is unknown and my imagery check of them failed (§1).

## 5. Tower position (item 2)

- OSM's tower centre is consistent three ways: the 8 m core square, the finial dome and the centre of the four pyramid faces agree to 0.3 m.
- **The tower sits on the axis, centred in the western square of the cloister.** From the outer wall faces it is 60.8 m (W), 62.0 m (N) and 59.4 m (S), i.e. about half the 121 m width each way and 2.01 W from the west face. This confirms `compound.md`'s inference from Sahapedia's grid (recorded there at about 65%). Measured from the court edge instead, the figures are 53.6 / 55.7 / 53.3 m (about 1.78 W).
- The N/S asymmetry (62.0 vs 59.4) puts the mapped tower 1.3 m south of the court's centre line. The gopurams and Nandi pavilion are mapped 0.5–2 m north of the tower's line. That spread is within mapping error; I'd treat the tower as on the centre line.
- **OSM's tower footprint is 26.0 m square, not 30.18 m.** The mapper probably traced the visible pyramid rather than the base mouldings. This doesn't move the centre, but don't take a tower size from OSM.

## 6. Gateways (items 3 and 4)

- **Centre to centre: 71.9 m (OSM). Google: 70.9 m between the two east-face ground lines** (east faces, being toward the camera, are the visible ones). OSM's east faces are 72.5 m apart, so the sources agree to within about 1.5 m.
- Rajarajan base: 25.6 m across the axis × 16.7 m along it (0.85 W × 0.55 W). It straddles the cloister's east range.
- Keralantakan base: 29.4 m × 17.6 m (0.97 W × 0.58 W). Google's Measure distance along its east silhouette gave 32.9 m, which probably includes the plinth or wall junction, so treat 29.4–33 m as the range.
- **Plan ratios:** about 1.5 : 1 (Rajarajan) and 1.7 : 1 (Keralantakan), in the Manasara's 1¼–1¾ range (`compound.md` §3, MS 33.22–23).
- eSamskriti's "27 by 17.25 m" for the Rajarajan gopuram fits these dimensions better than anything else. The 17.25 m matches the along-axis depths (16.7 and 17.6 m), and 27 m sits between the two gopurams' widths.
- Both upper parts are mapped as identical 16.2 × 8.1 m rectangles, as are their tagged heights (22 m and 26 m). These look schematic and unsourced; don't use them.
- Clear space between the gopurams (Rajarajan's east face to Keralantakan's west face): 54.8 m. The Keralantakan stands 58 m beyond the cloister's outer east face.

## 7. Halls, Nandi pavilion and the shrine north of the tower (items 5 and 6)

**Halls (way 120390896, part 889377945).** The mapped halls run 54.4 m from the tower's east face to the main east face, and are 25.8 m wide. Toward the east:
- the main east face is at u = 31.0;
- a central portico 10.5 m wide projects to u = 37.5;
- the front steps (889377952) reach u = 48.2.

**"Front of the halls" depends on which line you mean:** 45.8 m from the main face to the Nandi pavilion's west face, 39.3 m from the portico, 28.6 m from the foot of the steps.

**Nandi pavilion (55904677):**
- **Footprint:** 12.4 × 12.3 m square, centred on the axis 119.2 m east of the tower centre. Google's roof centre matches OSM's position to about 1 m after the registration offset.
- **Platform:** in the imagery a larger raised platform surrounds the pavilion, about 17–18 m across. That is a rough pixel estimate (±3 m), not mapped.

**Shrine north of the tower (55904675).**
- **Identification:** OSM tags this building "Perumal temple", but its position matches what `compound.md` says of the Chandesvara shrine: north of the vimana (SP; Mayamata n. 27). Google shows a small tiered shrine at the same spot. I'm about **70% confident it is the Chandesvara shrine**. I found no source for a Perumal shrine in the inner court, and the tag may be a mislabel. Check against a site plan before building it as Buildings data.
- **Position:** 22.6 m north of the tower centre to its near face, which leaves 9.8 m clear of the tower's north face. It sits 9.4 m east of the tower centre, near the north steps of the ardhamandapa (way 890154573).
- **Footprint:** 6.3 m along × 10.2 m across the axis (0.21 W × 0.34 W). The across-axis width matches the Mayamata's ⅓ W attendant-shrine width (MM 23.35–36a), which is a coincidence worth noting rather than evidence.
- **Top:** OSM maps a dome 3.5 m in diameter on it (889563600), consistent with SP's octagonal sikhara. Its tagged height of 12 m is unsourced.

## 8. Outer wall (item 7)

The only enclosing wall in OSM (way 457131358) is the **fort**: an irregular loop of 18.0 ha that also takes in the Sivaganga tank and park to the north. That area matches IC04's "Sivaganga Little Fort" of about 18 ha, which supports the identification (about 90%). It is not the Chola outer enclosure.

- **South side:** parallel to the temple axis, 35–43 m outside the cloister's outer south face, with small projecting bastions every 40–60 m.
- **West side:** runs at bearing about 349°, nearly true north and about 21° off the temple axis, 76–100 m outside the cloister.
- **East side:** passes through the Keralantakan, so the Keralantakan sits in the fort's east line. In front of it the wall steps out into a projecting block 41.7 m wide and 23.7 m deep. Its east face is 32.6 m beyond the Keralantakan's centre. This is probably the later outermost (Maratha) entrance of `compound.md` §2.2, but that is an inference (about 60%).
- **Not found:** any separate Chola outer wall around the outer court. In the imagery a pale strip runs parallel to the cloister's east and north sides, about 5–9 m out. It could be a low wall, a plinth or paving; I couldn't tell which.

## 9. Against `compound.md`

- **Balasubrahmanyam's cloister, 152.40 × 77.20 m: contradicted.** Nothing mapped or visible has that size. The cloister is about 241 × 121 m outside and 228 × 109 m inside, i.e. 1.5–1.6 times larger each way. BS's own 240.79 × 121.92 m "complex" figure matches the cloister's outside. That suggests the 152 × 77 m figure is a slip or refers to something else; it is not the cloister.
- **"Almost a hundred metres" between the gateways: contradicted for the two Chola gopurams**, which are 72 ± 2 m apart centre to centre. A plausible reconciliation: from the Rajarajan's east face to the front of the projecting block in the fort's east wall is 96 m, and from its centre 104.5 m. If BS's "almost a hundred metres westwards" was walked from the outermost (Maratha) gate, it fits. That is my reading, not his (about 55%).
- **Court size: refined.** ASI/IC04/SP's 240 × 120 m is the outside of the cloister. The open court is 228 × 109 m. `compound.md` §6's "inner court 8 W × 4 W" should either become the outer wall rectangle (8.0 W × 4.0 W, which fits well) or be split into an outer rectangle and a court about 7.6 W × 3.6 W.
- **Tower position: confirmed.** It is centred in the western square, 2.0 W from the outer west face (§5).
- **IC87's outer boundary of 270 × 140 m: not identified.** No mapped or visible wall has those dimensions. It cannot be the fort (much larger) or the wall containing the Keralantakan (that run would need to be at least 310 m long). Still unresolved.
- **BS's "about 6.10 m" between an inner wall and an outer defensive wall:** possibly the pale strip 5–9 m outside the cloister (§8), but unconfirmed.
- **Positions of the later shrines** (the gap flagged in `compound.md` §5). OSM maps them as follows (axis frame, centroids, relative to the tower centre):

| OSM name (way) | Along axis from tower centre | Across axis from tower centre | Footprint (along × across) |
|---|---|---|---|
| Murugan Sannithi (55904676) | 18 m west | 45 m north | 41.6 × 14.3 m |
| Karuvarur Sannithi (55904674) | 36 m west | 16 m north | 7.1 × 8.6 m |
| Pillayar Sannithi (55904672) | 37 m west | 24 m south | 14.1 × 8.6 m |
| Amman Sannithi (55904669) | 102 m east | 27 m north | 17.3 × 37.1 m |
| Natarajar Mandapam (55904679) | 150 m east | 42 m north | 10.6 × 16.5 m |

These names are OSM's. They are consistent with `compound.md`'s unsourced recollection that the Subrahmanya shrine is north-west and the Amman shrine on the north side. Treat them as Buildings data from OSM, with ±2 m on positions, until checked against a published site plan.

## 10. Reproducing this

Re-run the Overpass query in §1 (POST to `overpass-api.de/api/interpreter`). Project with local WGS84 radii at 10.7825 N, 79.1315 E, then rotate by the 70.12° axis bearing (u = along bearing 70.12°, v = along 340.12°). The way IDs above identify every outline used. Google points were read at zoom 20 from the right-click coordinate readout; their coordinates are kept in the session notes, not here.
