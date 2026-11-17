# Carved detail: research notes for the build

Notes for adding surface detail (mouldings, pilasters, cornices, niches) to the tower, the halls, the court and the gateways. Summaries and citations only, with quotations kept short. Compiled 16 November 2026, in the build session itself, not in a separate research chat.

Scope reminder: no sanctum interior. Deity imagery only on exteriors, drawn as generic figures that depict no one.

## 1. Sources and how they were read

| Key | Source | How it was read | Reliability |
|---|---|---|---|
| MM | *Mayamata*, ed. and tr. Bruno Dagens, vol. 1 (1994) | Chapters 13 to 16 and passages of 19 to 22, from the **machine-read (OCR) text** of the scan in `sources/` (local only). The page images were not checked this time. Verse numbers below are the ones Dagens's own introduction and notes give; where the OCR alone gave a number it is marked "about". | High for the sense of the text. Medium for verse numbers marked "about". |
| BS-C | S. R. Balasubrahmanyam, *Middle Chola Temples* (1975), [Tanjavur: The Central Shrine](https://www.wisdomlib.org/south-asia/book/middle-chola-temples/d/doc210432.html) | Through a fetch tool that returns a summary with short quotes, on 16 November 2026 | Medium. The counts of wall sculptures are the tool's summary of his lists. |

The gateways' detail rests on `gopuram.md`, the halls' on `mandapa.md` and the court's on `compound.md`.

## 2. What the Mayamata prescribes

**Sub-base (ch. 13).** Several socles are listed by their mouldings. The simplest, *vedibhadra*, has eight mouldings, or six without its two doucines (curved mouldings): a plinth, a tall dado between fillets (the dado is 5 parts), and an upper string-course with its fillet. The start of the verse is garbled in the OCR, so the plinth's share (taken as 2 of 12 parts) is my reading. The face of the string-course is to be carved with lions, elephants, sea-monsters and the like (13.19b–20).

**Base (ch. 14).**
- *Padabandha* base, 24 parts: plinth 8, torus 7, fillet 1, dado (neck) 3, fillet 1, upper string-course (band) 3, its fillets 1 (14.19–20).
- Projections: the torus and the string-course project as far as the plinth, and the dado is recessed by the same amount (14.17–18). A string-course projects by its height or three quarters of it; a doucine by its height (14.41–44).
- Any base "may be provided with small pillars and false dormer-windows" (about 14.38). Dagens's note: the small pillars stand on the dado, the dormers (*kudu*) on a dripstone.
- Other bases have a "well rounded" torus, or an octagonal one. The padabandha's torus is not described further.

**Pillars and pilasters (ch. 15).**
- The level of pillars may be a colonnade, a wall with pilasters, or a plain wall (Dagens, introduction).
- A square pillar with bell capital and abacus is *brahmakanta*; octagonal *visnukanta*; circular *rudrakanta* (15.13–16).
- Every pillar has a bracket capital (15.28a). From the top: bracket capital (*potika*), a dye, abacus, bell capital (*kumbha*), support, lotus, garland band (about 15.31). The bell and the abacus are about twice the pillar's width.
- The module is the width of the top of the pillar (15.28b–29a).
- A pilaster is half, two thirds or three quarters as wide as the pillar (about 15.8–9), and a square one stands a quarter of its width proud of the wall (15.51).
- The spacing chosen is to be used for all pillars of a building (15.52–54).
- A ground-floor pillar of a twelve-storey building is a sixth of its height in diameter (about 15.11–12).

**Entablature (ch. 16).** From the bottom: architrave (*uttara*) as wide as the pillar, with an upper fascia a third or a quarter of its height (16.2–7); optionally a frieze of dwarves or geese over the fascia; a rounded cornice (*kapota*) with false dormer windows (*nasika*) rising from its rim, one and a quarter to two modules wide and high, set one above another from storey to storey (16.18b–24a and following); then a fillet and a groove; then the upper frieze (*prati*), carved with lions, elephants or mythical beasts "or it may be bare", topped by a fillet (16.28–35). Beams rest on the fascia (16.36 on).

**Doors (19.20–22).** Seven eighths to nine tenths of the pillar height, and half as wide. Jambs as wide as a pillar or a quarter more.

**Gargoyle (ch. 19, about 19.26–29).** A water-spout in the middle of the left (normally north) face, ending in a lion's mouth. Not built.

**Roof dormers (19.18–19a) and octagonal roofs (ch. 21).** Large false dormers (*mahanasi*) set in the roof project by their width or less. Types with an octagonal roof have "eight niches (on the roof)".

**Niches and arches (20.36–39; 21.29–35; 22.70–79).** An arcature (*torana*) is two colonnettes under a curved "fish-like" lintel. Colonnettes are seven tenths, six ninths or five eighths of the storey's pillar height (ch. 20), or the pillar height is cut into 5, 6 or 7 parts with 2 for the arch (ch. 22). The arch is half as wide as the colonnettes are high. Colonnettes are three quarters of a pillar's width, with bell capital and abacus but no bracket. Arcatures go round or beside the door, in the middle of facades, and on the pavilions and dwarf galleries of the storeys above. "In the niches (under the arcatures) there are statues." Three kinds are named by their carving: foliage, sea-monsters (*makara*), and a mixed kind.

**Pavilions on the storeys (22.82–89, already in `gopuram.md`).** Corner pavilions have square, octagonal, round or sixteen-sided roofs, each with one finial. The elongated one has several finials. Intermediate ones are fronted like the gable of a wagon roof.

## 3. What Balasubrahmanyam records of Thanjavur's tower (BS-C)

- Each storey of the wall is marked by "a massive overhanging cornice".
- Lower storey, outer walls: sculptures of forms of Siva. The tool's summary lists seven entries on the south wall, six on the west and six on the north, each including "a pair of dvarapalas" at a central opening, and three on the east: the entrance with one figure each side. I read that as **four or five figures a face plus two guardians (about 70%)**.
- Upper storey: niches above the lower ones, with Siva as Tripurantaka.
- "Each storey is adorned with ornamental salas and kutas."
- At the top, "Nandis in pairs adorning the four corners" of a granite block 7.77 m square. Each Nandi is 1.98 by 1.68 m.
- A "cupola-shaped sikhara". Stupi 3.35 m (older figures 3.66 and 3.81 m).
- **Not mentioned:** pilasters, the shape of the base's mouldings, friezes, dormers.

## 4. Build spec

| Element | Proposal | Element tag | Dimension sources |
|---|---|---|---|
| Sub-base | Vedibhadra mouldings swept round the tower and halls. String-course bare. | Rule-derived | Height: Buildings. Mouldings: Text (ch. 13). Which socle Thanjavur has: not found. |
| Base | Padabandha with real profiles: plinth, rounded torus, recessed neck between fillets, band. | Rule-derived | Shares and projection rule: Text (14.17–20). Amount of projection, rounded torus: Estimate. |
| Small pillars on the neck | Optional in the text | Inferred (about 60%) | Presence: Text. Spacing: Estimate. |
| Wall pilasters | Square, with bell capital, abacus and bracket; fourteen a face | Part of the wall storey (Rule-derived) | Form: Text (ch. 15). Count and size: Estimate. |
| Wall entablature | Architrave, fascia, frieze, kapota with dormers, groove, upper frieze | Rule-derived | Parts: Text (ch. 16). Shares, overhang, dormer count: Estimate. |
| Wall niches | Four a face on each storey, two guardian niches at each central opening | Rule-derived | Count: Buildings (BS-C, about 70%). Proportions: Text. Bays: Estimate. |
| Niche figures | Generic standing figures | Rule-derived (presence); form invented | Presence: Buildings. Form: Estimate. |
| Central openings | South, west and north, **drawn closed** | Rule-derived | Position: Buildings. Size: Text (19.20–22). |
| Stone surface | Grain and block joints in the shader | Artistic, stated on the page | None |
| Tier walls | The wall steps forward under each pavilion of the row it carries (Dagens, introduction p. lxvi: pavilions project to match projections of the face beneath), with a pilaster at each edge | Part of each tier (Rule-derived) | Arrangement: Text. Depth and pilaster size: Estimate. |
| Tier entablatures | Same parts as the wall's, one dormer to each part of the side | Rule-derived | Parts: Text (ch. 16). Shares and counts: Estimate. |
| Kutas | Square roof curving in to one pot finial, replacing the pyramid and the invented ball finial | Rule-derived | Roof and finial: Text (22.82–89). Curve: Estimate. BS-C: "ornamental salas and kutas". |
| Salas | Three finials on the ridge, a dormer on the front | Rule-derived | Several finials: Text (22.82–89). Arch on pavilions: Text (20.38). Count: Estimate. |
| Nandis at the top | A pair at each corner of the platform under the neck, blank blocks 1.98 by 1.68 m | Rule-derived | Count, place, size: Buildings (BS-C). Breadth and facing: Estimate. |
| Sikhara dormers | Eight plain horseshoe dormers, one a face | Part of the sikhara (Rule-derived) | Presence: Text (19.18–19a; ch. 21). Size: Estimate. Thanjavur's own not described in BS-C. |
| Hall walls | Pilasters at the tower's spacing on every outside face; a pilaster each side of a door as its jamb, with a lintel band | Part of each hall (Rule-derived) | Form: Text (ch. 15; 19.20–22 for jambs). Count and size: Estimate. |
| Hall entablature | The tower wall's cornice and dormers round all three halls; ceiling beams over each row of pillars | Rule-derived | Parts: Text (ch. 16; MS 34.70–72). Beams: Text (16.36 on). Sizes: Estimate. |
| Hall pillars | Square shaft, abacus and a cross-shaped bracket capital | Rule-derived | "Plain, square and heavy": Buildings (BS-G). Bracket on every pillar: Text (15.28a). |
| Guardians at the side doors | Generic standing figures either side of each ardhamandapa door, outside | Rule-derived (presence); form invented | Presence: Buildings (BS-T, `mandapa.md` §2). Size, place: Estimate. |
| Stair balustrades | A wavy band ending in a curl at the foot | Rule-derived | "Sinuous" (BS-T) and "elephant's trunk" (MM 19.6–7): Text and Buildings. Curve: Estimate. |
| Court wall | Coping of architrave, fascia, doucine and cap-stone at 3 : 3 : 2 : 3, as high as the wall is thick, on the outer face | Part of the wall (Rule-derived) | Text (MM 23.23–25). |
| Cloister | Moulded base, a cornice with dormers on the ground storey and a cornice on the upper; pillars with abacus and bracket | Rule-derived | Base, pillars, entablature: Text (MM 23.30–31, 23.67b–69; MS 31.61–62). Shapes: Estimate. |
| Shrines | Stepped base, pilasters, three-step entablature with a dormer a face, pot finial | As each shrine | Shrines may look like temples: Text (MM 23.57b–58a). Shapes: Estimate. |
| Nandi pavilion (later) | Moulded platform, twelve pillars round the edge, beams, cornice | Inferred | All Estimate. Not the Nayak building as it stands. |
| Gateway bases | Rajarajan: chamfered plinth, a rounded cornice over the dado, two chamfered courses. Keralantakan: four plain courses with chamfered tops. | Inferred (as before) | Sequence: Buildings (`gopuram.md` §2.3). Profiles: Estimate (MM 24.27–28 unread). |
| Gateway main cornice | The tower's entablature profile with a dormer over each bay | Part of the stone storey (Rule-derived) | Parts: Text (ch. 16, with p. lxx "very similar to the temples"). Profile and count: Estimate. |
| Gateway pilasters | Bell capital, abacus and bracket | Rule-derived | Text (ch. 15). Not checked in the photographs. |
| Passages | Four plain pilasters on plain brackets each side, a beam across at each pair | Part of the stone storey | Keralantakan: Buildings (ES, `gopuram.md` §2.4). Rajarajan: assumed from it. Count: Estimate. |
| Gateway tier pavilions | Corner pavilions domed with a small finial; barrels with a net pattern and two finials | Rule-derived | Domes, finial and net: Buildings (PH, `gopuram.md` §2.1–2.2). Barrel finials: Text (22.82–89). |
| Wagon roofs | Net (jala) pattern drawn in the surface by the shader; end gables with an inner step and two horn discs at High detail | Rule-derived | Net and horns: Buildings (PH). Mesh size: Estimate. Lion-face crests stay plain blocks. |

## 5. Not read or still needed

- The page images for the verses marked "about".
- Mayamata ch. 17 (joinery) and ch. 18 beyond the finial.
- Pichard (1995) for Thanjavur's actual mouldings, pilasters and bay counts.
- Whether Thanjavur's base torus is rounded or faceted, and what its friezes carry.
