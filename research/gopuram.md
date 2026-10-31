# The two Chola gateways: research notes for the build

Notes for decorating the Rajarajan (inner) and Keralantakan (outer) gopurams at Thanjavur, written so a build session can work from them without the source books. They contain summaries and citations only, with quotations kept short. Compiled 31 October 2026.

Scope reminder: no sanctum interior and no deity imagery. The guardian figures, the base reliefs and the stucco figures on the tiers are figure sculpture, so they are omitted or shown as blank "Invented" blocks and panels in their places.

W means the tower's base width, 30.18 m at Thanjavur. "Long face" means the faces across the axis (east and west, 25.6 m and 29.4 m wide). "Short face" means the north and south faces, along the axis. Directions are temple directions: the real axis bearing is 70.1° (`measurements.md` §2).

## 1. Sources and how they were read

| Key | Source | How it was read | Reliability |
|---|---|---|---|
| BS-E | S. R. Balasubrahmanyam, Tanjavur page on wisdomlib, filed under [*Early Chola Temples*, ch. XIII "Prasada: component parts"](https://www.wisdomlib.org/south-asia/book/early-chola-temples/d/doc210406.html) | Through a fetch tool that returns excerpts. The gopuram paragraphs were requested verbatim and checked in a second pass. | Medium to high. This is the only source found that describes both gopurams' storeys, finials and guardians together. Its place in the book (a Middle Chola temple in an *Early Chola* volume) is odd and was not resolved. |
| BS-T | Balasubrahmanyam, *Middle Chola Temples* (1975), [Tanjavur: The Temple Complex](https://www.wisdomlib.org/south-asia/book/middle-chola-temples/d/doc210431.html) | Same tool | Medium. Short on the gopurams. |
| BS-Tv | Same book, [Tiruvarur](https://www.wisdomlib.org/hinduism/book/middle-chola-temples/d/doc211887.html) | Same tool | Medium. Comparison only: storey and finial counts of later Chola gopurams. |
| BS-G | Same book, [Gangaikondasolapuram](https://www.wisdomlib.org/south-asia/book/middle-chola-temples/d/doc211879.html) | Same tool | Medium |
| IG-I / IG-O | Indira Gandhi National Centre for the Arts, Brihadisvara pages: [Inner gopuram](https://ignca.gov.in/brhadisvaratemple/INNER_%20GOPURAM/images/Des_IG.html), [Outer gopuram](https://ignca.gov.in/brhadisvaratemple/OUTER_%20GOPURAM/images/Des_Og.html) | Same tool, as summaries (the tool would not return the text verbatim). The site's index page refused automated reading, so its other sections were not read. | Medium to high. IGNCA published Pichard's architectural study, but these pages carry no author line and no references. |
| ES | S. Nayyar, [eSamskriti, Brihadisvara Temple Thanjavur](https://www.esamskriti.com/a/TamilNadu/Brihadisvara-Temple-Thanjavur.aspx) (2016) | Same tool | Low. Photo captions by a visitor relying on a guide; the author asks to be corrected. Used for details nothing else gives. |
| TH | *The Hindu*, 29 Nov 2010 (G. Srinivasan), lightning damage to the Rajarajan gopuram, [forum repost](https://ponniyinselvan.in/forum/discussion/comment/43908) | Same tool | Low to medium (a newspaper, read secondhand) |
| IH | [indian-heritage.org, Peria Koil](https://www.indian-heritage.org/temple/peria.htm) | Same tool | Low. Unsourced. |
| IC87 / IC04 | ICOMOS evaluations for UNESCO: [1987](https://whc.unesco.org/document/153044), [2004](https://whc.unesco.org/document/153042) | Same tool | Medium |
| ASI | [ASI, Great Living Chola Temples](https://asi.nic.in/pages/WorldHeritageCholaTemples) | Same tool | Medium to high, but says almost nothing about the gopurams |
| WP | Wikipedia, [Brihadisvara Temple, Thanjavur](https://en.wikipedia.org/wiki/Brihadisvara_Temple,_Thanjavur) | Same tool | Tertiary. Cites BS for most gopuram statements. |
| MM | *Mayamata*, ed. and tr. Bruno Dagens, vol. 1 (IGNCA / Motilal Banarsidass, 1994) | Directly, from the scan in the repo (local only). Every passage cited here was read on the page image, not the OCR text. | High for what vol. 1 says. Ch. 24 (gateways) and ch. 30 are in **volume 2, not available**. |
| MS | *Manasara*, tr. P. K. Acharya (1933): [ch. 33a, gate-houses](https://www.wisdomlib.org/hinduism/book/manasara-english-translation/d/doc421080.html), [ch. 33b, windows](https://www.wisdomlib.org/hinduism/book/manasara-english-translation/d/doc421081.html) | Same tool, as summaries with verse numbers; the finial verses were requested verbatim | Low to medium. Second witness. The translation's verse numbering is garbled in places. |
| PH | Wikimedia Commons photographs, listed in §6 | Looked at in the built-in browser at full resolution, zoomed by region | Varies: see each count's error. Upper tiers are thickly covered with 17th-century stucco figures, which hides the pavilion outlines. |

## 2. Findings by question

### 2.1 Tiers: storeys and pavilion rows

**Storey counts.**
- **Rajarajan: three storeys** (BS-E: "three storeys topped by the sala type of pavilion crowned with five stupis"; IG-I: a "three-storeyed stone structure"). The photographs show what that count means: **the stone ground storey plus two tiers, then the wagon roof** on a neck. The roof is not counted as a storey. (PH1–PH4, confident about 85%.)
- **Keralantakan: five storeys** (BS-E; IG-O; ES "5 floors"). On the same counting: **the stone ground storey plus four tiers, then the neck and wagon roof** (PH5–PH7, about 80%). ES says the south face has a central niche figure "in each of its five talas", which fits a ground storey plus four tiers.
- **Consequence for the model:** it currently builds 3 tiers on the Rajarajan and 5 on the Keralantakan above the stone body. On the sources' counting those should be **2 and 4**. A model with 3 and 5 tiers would be a four- and six-storey gateway.

**Do the tiers carry pavilion rows like the tower's?** Yes. Every tier of both gateways ends in a row of aediculae, as on a vimana: square corner pavilions with domed roofs and a small finial (kutas), elongated pavilions with barrel roofs (salas), and narrow intermediate pavilions fronted by a horseshoe gable (panjaras). This is also what the Mayamata implies when it says gateways are "very similar to the temples" of the preceding chapters (MM intro p. lxx). Confidence that the same three kinds are present: about 85%. **The counts are much less certain**, because the Nayaka stucco figures (IG-I, IG-O) stand in front of the pavilions and hide their edges.

What the long faces show (PH1–PH3 for the Rajarajan, PH5–PH7 for the Keralantakan), reading from a corner to the centre:

| Gopuram, tier | Sequence per half of a long face | Per long face | Confidence |
|---|---|---|---|
| Rajarajan, tier 1 | kuta · sala fronted by a large horseshoe gable · small panjara · sala · **centre bay** | 2 kutas, 4 salas, 2 panjaras + centre | about 55% |
| Rajarajan, tier 2 | kuta · panjara · sala · **centre** | 2 kutas, 2 salas, 2 panjaras + centre | about 45% |
| Keralantakan, tier 1 | kuta · large-gabled pavilion · sala · panjara · **centre bay** | as Rajarajan tier 1 | about 50% |
| Keralantakan, tiers 2–4 | corner pavilion · one or two intermediates · **centre**, thinning upward | not counted | about 35% |

- **The centre bay** of each long face is a projecting central pavilion stacked tier on tier: a rectangular **window opening** in the lower tiers, crowned by large horseshoe gables piled one above another up into the roof's central gable. Windows are visible at the centre of tiers 1 and 2 of the Keralantakan's west face (PH6) and tiers 1–3 of its east face (PH8), and of tier 1 on both faces of the Rajarajan (PH1, PH3).
- **Which way the salas run:** on the long faces their barrel ridges run **parallel to the face**, so the side of the barrel, with its net (jala) pattern, faces outward. Some carry a horseshoe gable on that outward face (PH1, PH3, PH6; about 75%). No sala was seen turned end-on to a long face.
- **Short faces:** each tier has corner kutas and a central element with a horseshoe gable (PH4, PH8). ES places a central niche figure on each storey of the Keralantakan's south face (Dakshinamurti) and on its north face (Brahma). **Pavilion counts on the short faces were not established.**

**Step-in per tier.** No source gives this. From frontal photographs (PH2 for the Rajarajan, PH5 for the Keralantakan), measured as how far each tier's corner pavilion is set in from the edge of the main cornice. These are Estimates with about ±25% error (perspective, stucco and picking edges by eye):

| | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Roof end | Roof ridge length |
|---|---|---|---|---|---|---|
| Rajarajan (body 25.6 m) | 0.9 m | 4.9 m | — | — | 6.5 m | 13.4 m (0.52 of body width) |
| Keralantakan (body 29.4 m) | 1.3 m | 3.2 m | 5.9 m | 7.7 m | 8.6 m | 12.2 m (0.42 of body width) |

The Rajarajan steps in sharply above its first tier. The Keralantakan narrows more evenly.

### 2.2 Roof

- **Form:** both gateways end in a **wagon (barrel) roof on a neck**. The neck is a band of seated stucco figures. The barrel surface carries a net (jala) pattern. BS-E calls the Rajarajan's top "the sala type of pavilion", and WP calls the original east gopuram "barrel vaulted". Dagens says gateways are "almost always rectangular and have a wagon-roof" (MM intro p. lxx).
- **Gable ends (short faces):** a tall **horseshoe-arched gable** fills each end of the barrel. It has a scalloped flame-like frame and a lion-face (kirtimukha) crest at the top, with stucco figures inside (PH1, PH4, PH8). Below the crest, the gable's two sides curl out like horns, seen as the "ends" of the ridge in frontal views.
- **Centre of each long face:** a large horseshoe gable rises from the stacked centre bay into the roof, with a lion-face crest at its top (PH1–PH3, PH6).
- **Terms:** Dagens glosses this false dormer as *nasi* or *nasika* ("nose"), also *nida* ("nest"); Tamil *kudu* is the same element (MM 19 n. 18). The *ardhakoti*, possibly part of a wagon-roof gable, is mentioned at 24.90, 96 and 99 in vol. 2 (MM 22 n. 27).
- **Proportions:** neck plus roof is about 0.18 of the height to the ridge on the Rajarajan and 0.15 on the Keralantakan (§4). The ridge runs about half the body width (0.52, Rajarajan) or 0.42 of it (Keralantakan).
- **Finials:**
  - **Rajarajan: 5.** Supported by TH ("five kalasams") and BS-E ("five stupis"), and counted in PH3: two pots, a central pot standing behind the lion-face crest, and two more pots, evenly spaced along the ridge. From the east (PH1) the central pot is hidden by the crest, so only 4 are visible. **±0.**
  - **Keralantakan: 6 visible from the west, probably 7.** PH6 and PH7 show 6 evenly spaced pots, with a gap at the centre where the crest stands. A seventh behind the crest would fit the spacing. The oblique view PH8 seems to show seven along the ridge. **7 at about 60%, 6 otherwise.**
  - The finials are not all original. TH reports that one of the Rajarajan's brick-and-lime finials was destroyed by lightning in 2010 and was to be replaced at the 2011 consecration.

### 2.3 Base

**Rajarajan, east (outer) face**, from bottom to top (PH1; confidence about 60% on the sequence, below 50% on the moulding names):
1. A low plinth, hidden behind the railing in the photograph.
2. A tall dado with **a single row of rectangular relief panels** set between pilasters, running along both halves of the face.
3. A cornice with lion or kudu heads placed above the pilasters.
4. Two plain projecting courses.
5. The wall storey with the guardians' niches, standing on these courses.

**The panels.**
- **Subjects:** IG-I says the base's outer side is divided by pilasters into small panels of Siva's forms: Kalyanasundara (the wedding), Kirata-Arjuna and Kamantaka. It adds that they were left unfinished. BS-E names the Kiratarjuniya. ES adds Kannappa Nayanar.
- **Layout:** ES says the panel area **below each guardian** is carved in up to **four horizontal registers** (rows) of figures.
- **Number:**
  - Six panels are visible on the south half of the east face; trees hide the rest (PH1).
  - Estimate: **14–18 panels across the east face** (±4).
  - The west face has 4–5 panels in each outer bay beside its projecting porches (PH3), so about 8–10 in all (±4).
- **Short faces:** not seen.

**Keralantakan:** a tall moulded base of several plain horizontal courses. No relief panels were seen in PH5–PH7, which fits BS-T's "unpretentious". **No moulding names could be assigned from the photographs.** No text read gives either base's moulding sequence.

**Gangaikondacholapuram comparison:**
- **Condition:** only the gopuram's lower part survives (BS-G: "only the basal portion is left"). ICOMOS 2004 says the gateway and eastern prakara "have been reconstructed using the original stones".
- **What the photograph shows** (PH9, 2017): two plain stepped masonry masses with **free-standing guardians in front**. There are no panels.
- **Value:** being reconstructed, it is weak evidence for the original base. It does show that a second Chola gateway had giant guardians at its entrance.

### 2.4 The stone body

**Rajarajan, east face** (BS-E; IG-I; PH1):
- **Guardians:** "two giant dvarapalas, four armed, in the centre of the two sides of the facade adjoining the gateway on the east" (BS-E). Each stands in a tall framed niche between pilasters. BS-E calls the position "peculiar", since later gopurams put guardians in niches beside the door. They are monolithic granite and "over 16 feet" tall (IG-I); ES gives 18 ft. ICOMOS 1987 also mentions the two guardians.
- **Outer bays:** pilasters and smaller figure niches.

**Rajarajan, west (court) face** (PH2, PH3):
- **Porches:** two **projecting porch-like pavilions** flank the passage. Each is two-level, with a small door or window below, a figure niche above, and its own cornice and parapet.
- **Corner bays:** figures in niches.
- **Possible identification:** ES mentions "2 sub shrines of Indra and Nagaraja" on either side, which may be these. Unverified (below 50%).

**Keralantakan:**
- **Wall storey:** pilasters and small rectangular windows (PH5, PH6).
- **Niches:** BS-E says "The outer niches of the gopuram are empty." IG-O says the first storey's niches were meant for stone images, and that a few remain on the south and north faces (Dakshinamurti, Brahma).
- **Interior figures:** BS-E reports Brahma and Dakshinamurti inside the outer gopuram's first storey, on its inner face, as "the first instance so far known" of deities installed inside a gopuram. IG-O's wording places them on the north and south faces instead (§7).

**Passage:**
- **Keralantakan:** ES describes the central passage as having plain pilasters on plain brackets, with ganas blowing conches on its front face.
- **Rajarajan:** in PH1 and PH3 the passage opening has an **arched inner frame** inside the rectangular stone opening. No source dates it. Chola stone doorways are normally trabeate (flat-lintelled), so the arch may be later, but that is an inference (about 50%).

**Materials.** The sources disagree (§7):

| | Stone | Brick or stucco |
|---|---|---|
| Keralantakan | "first three" storeys granite (IG-O); granite "upto first floor" (ES); "a massive stone structure" (BS-T) | upper two storeys brick and mortar (IG-O); stucco above the first floor (ES); brick and lime mortar (TH) |
| Rajarajan | "three-storeyed stone structure" (IG-I); "a stone one with some modification in brick" (ES) | brick and lime mortar superstructure and finials (TH) |

**Stucco figures** on the upper parts of both are **17th-century Nayaka additions** (IG-I, IG-O). On the Rajarajan, Siva's exploits face east and Vishnu and his incarnations face west; one figure on top is a Nayaka portrait (IG-I). On the Keralantakan, Kali and Urdhva Tandava face east, Krishna and Vishnu west (IG-O). For the Chola phase, the tiers' pavilions are original but the figure crowd in front of them is not.

### 2.5 Heights

**Published:**
- **Keralantakan:**
  - 25 m (TH, from ASI sources)
  - 90 ft = 27.4 m (IH)
  - 30 m (IC87). WP also gives 30 m, citing BS 1975 pp. 16–29.
- **Rajarajan:** no figure found. TH says it is "smaller in height" than the Keralantakan, and BS-E says the outer gopuram "is taller than the inner".

**Measured from photographs** (Estimates):
- **Method:** heights were scaled from the mapped body width in frontal photographs.
- **Error:**
  - Parts set back from the face (the tiers and especially the roof) look smaller than they are, so these are underestimates by perhaps 5–15%.
  - Errors in the width each is scaled from add about ±10%.

| | Stone body (ground to main cornice) | Tiers | Neck + roof | Finials | To ridge | To finial tips |
|---|---|---|---|---|---|---|
| Rajarajan (PH2, scaled to 25.6 m + 1 m cornice overhang) | 11.9 m | 3.3 + 3.0 m | 1.8 + 2.1 m | 1.0 m | 22.1 m | 23.1 m |
| Keralantakan (PH5, scaled to 29.4 m) | 11.6 m | 3.8 + 2.8 + 2.8 + 2.3 m | 2.1 + 2.1 m | 0.5 m | 27.5 m | 28.0 m |

**Corrected for setback**, I'd put the Rajarajan at **about 22–26 m** and the Keralantakan at **about 27–31 m**. That is consistent with the published 25–30 m for the outer gateway. The model's Rajarajan at 18 m (0.6 W) looks **too low**.

Within the Rajarajan's stone body, the base zone (plinth, panel dado and the courses above it) is about 4.2 m. The wall storey is about 7.1 m (PH3, ±20%).

### 2.6 Texts

**Mayamata, vol. 1 only** (ch. 24 and ch. 30 are in vol. 2):
- **The five gateways** (intro p. lxx):
  - Size: they grow larger the farther out they stand, with up to seven storeys (24.2–36).
  - Form: they are "very similar to the temples described in the preceding chapters". They are almost always rectangular and wagon-roofed.
  - Terms: the words that normally name a temple's shrine are used for the gateway's central passage.
  - Ch. 30 treats gateways again "in a slightly different way".
- **Ch. 30 itself** (intro, in its summary of ch. 30): mostly the parts of the door. Its gateway types "merely repeat" ch. 24 with small changes.
- **Ch. 24, from the table of contents** (pp. xxviii–xxix):
  - Proportions: dimensions relative to the main temple (1–10), names (11), dimensions and proportions (12–22), doors (23–25), **bases (27–28)**, pillars (29–30) and foundation deposit (31a).
  - Fifteen types (31b–34a) and the number of storeys (34b–35).
  - Vertical proportions for gateways of 1 to 7 storeys (36–59a) and horizontal proportions (59b–77). Doors and stairways (78–80), shapes (81–84a).
  - Named types for each enclosure's gateway (84b–134), and a rule for gutters (135).
  - **The actual ratios, base mouldings and ornament rules are in vol. 2 and unread.**
- **Dating remark** (intro p. xliii): Dagens notes that the Mayamata's seven-storey maximum for gateways was not reached until the 12th-century gopurams at Chidambaram.
- **Pavilion rows** (intro p. lxvi): aediculae (*kuta, kostha, panjara*) and dwarf galleries (*hara*) belong to the storey they stand on, the top of the storey below. Aediculae project, matching projections of the face beneath. Galleries are recessed over bare wall.
- **Aedicula forms** (22.82–89, read on the page image, book p. 383):
  - **Corner aediculae:** square, octagonal, circular or sixteen-sided roofs, each with a finial.
  - **Elongated aedicula:** in the middle, with **several finials**.
  - **Intermediate aediculae:** between the two, backed like an elephant's back but fronted "like the gable frontage of a wagon-roof building".
  - The arrangement with square corners and an elongated middle is the "normal" (*jati*) mode. This matches the gateways' tiers, and the roof itself, as the topmost "elongated aedicula", would carry several finials.
- **Figures on gateway facades** (23.106, page image p. 413): ten deities (Canda, Pracanda, Rathanemi, Pancajanya, Durga, Ganesa, Ravi, Candra, Sarvesvara, Surapati) "are, all ten to be installed on the facades of the gateways of the five enclosures". This is a textual basis for niche positions, to be drawn as blank niches.

**Manasara, ch. 33a** (second witness):
- **Storeys:** gate-houses of 1 to 5 storeys from the inner court outward (vv. 94–96), with larger variants up to about 17 (v. 97).
- **Plan and height:** length exceeds breadth by ¼, ½ or ¾, preferably twice (vv. 22–23). Breadth is half the height (v. 55). Total height is about twice the breadth (vv. 208–210). The translation does not make clear which breadth is meant.
- **Base:** the division is pedestal 1 : base 1 : pillar 2 (vv. 113–115). For a five-storey gate it is plinth ½, pedestal 8¾ and base 2½ out of 48 parts (vv. 278–288).
- **Upper storeys:** each is about ¾ of the one below in pillar and entablature (vv. 167–169, 183). Five-storey pillar heights run about 5½, 5, 4, 4 parts (vv. 194–199).
- **Finials:**
  - five spires in the three-storey description (v. 174; its wording, "on the second storey", is ambiguous)
  - nine on a four-storeyed one (v. 190), or one square dome instead (v. 191)
  - "eleven spires" on a five-storeyed one (v. 202)
- **Ornament:** pinnacle-turrets (*kuta, kuta-sala*) and corner towers are added storey by storey (vv. 302–323). Corridors get cage-like windows (*panjara*, v. 307). Large, middle and small *nasi* go on the gable faces ("foreheads") and corridors (vv. 540–551). Arches decorate the corridors (v. 425).
- **Not covered:** no wagon-shaped roof is named (the roof words are *sikhara, stupi, sikha*), and no guardian figures are mentioned.

**Manasara, ch. 33b:** windows only (vv. 573–600). Gate-house windows go at the pinnacle, the neck and the solid and hollow portions (vv. 593–594). Height is "always" twice the width (vv. 599–600).

**Against the buildings:**
- The Rajarajan's **5 finials on three storeys matches the Manasara's three-storey count** (v. 174).
- The Keralantakan's 6–7 finials on five storeys is well short of the Manasara's 11.
- The Chola series at Tiruvarur gives a three-storey inner gopuram with 5 kalasas, another three-storey one with 9, and a seven-storey one with 11 (BS-Tv). So finial counts did grow with size, but not by one fixed rule.

### 2.7 Photographs

See §6 for every count with its image and error. Later work noted in the sources:
- **Stucco figures:** Nayaka, 17th century (IG-I, IG-O).
- **Finial:** replaced after lightning in 2010 (TH).
- **Passage arch** in the Rajarajan: undated (above).
- **Paint:** none visible.
- **Gangaikondacholapuram:** the base is reconstructed (IC04).

## 3. What the texts prescribe (summary)

| Topic | Mayamata vol. 1 | Manasara ch. 33a |
|---|---|---|
| Storeys | Up to 7, more the farther out the gate stands (intro p. lxx) | 1–5 by enclosure, up to about 17 at great sites (vv. 94–97) |
| Plan | Almost always rectangular (p. lxx) | Length 1¼–2 × breadth (vv. 22–23) |
| Elevation | Like a temple's (p. lxx). Rows of kuta, kostha and panjara with hara between, on each storey (p. lxvi; 22.82–89) | Kutas, corner towers, panjaras and nasis storey by storey (vv. 302–323, 540–551) |
| Roof | Wagon roof (p. lxx). The elongated aedicula has several finials (22.84–85) | Spire counts: 5 (three-storey), 9 (four-storey), 11 (five-storey) (vv. 174, 190, 202) |
| Base | Bases at 24.27–28 (vol. 2, unread) | Pedestal : base : pillar = 1 : 1 : 2 (vv. 113–115) |
| Figures | Ten deities on gateway facades (23.106) | None |

## 4. Measured data, normalised to W = 30.18 m

| Thing | Value | W | Source and note |
|---|---|---|---|
| Rajarajan base (across × along axis) | 25.6 × 16.7 m | 0.85 × 0.55 | OSM via `measurements.md` §6. ES's "27 by 17.25 m" (0.89 × 0.57) is close. |
| Keralantakan base | 29.4 × 17.6 m | 0.97 × 0.58 | OSM via `measurements.md` §6 |
| Keralantakan height | 25 / 27.4 / 30 m | 0.83 / 0.91 / 0.99 | TH / IH / IC87 and WP |
| Keralantakan height, photo | 27.5 m to ridge, 28 m to finials (uncorrected); 27–31 m corrected | 0.91–1.03 | PH5, Estimate |
| Rajarajan height, photo | 22.1 m to ridge, 23.1 m to finials (uncorrected); 22–26 m corrected | 0.73–0.86 | PH2, Estimate. No published figure. |
| Rajarajan guardians | over 16 ft (4.9 m); 18 ft (5.5 m) | 0.16 / 0.18 | IG-I / ES |
| Stone body height | Rajarajan 11.9 m; Keralantakan 11.6 m | 0.39 / 0.38 | PH2 / PH5, ±15% |
| Rajarajan base zone; wall storey | 4.2 m; 7.1 m | 0.14; 0.24 | PH3, ±20% |
| Roof ridge length | Rajarajan 13.4 m; Keralantakan 12.2 m | 0.44 / 0.40 | PH2 / PH5, ±25% |
| Finials | Rajarajan 5; Keralantakan 6–7 | — | TH, BS-E, PH3 / PH6–PH8 |

**Height fractions** (of the height to the ridge, from the photographs; ±0.03 each):

| | Stone body | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Neck | Roof | Finials above ridge |
|---|---|---|---|---|---|---|---|---|
| Rajarajan | 0.54 | 0.15 | 0.14 | — | — | 0.08 | 0.10 | 0.04 |
| Keralantakan | 0.42 | 0.14 | 0.10 | 0.10 | 0.08 | 0.075 | 0.075 | 0.02 |

Compare the model's current split (`gopuramGeoms` in `index.html`): base 0.07 + body 0.30 = 0.37 stone, tiers 0.43, roof 0.20. The photographs give **a taller stone body** (0.42–0.54) and a lower roof.

## 5. Build spec (suggested)

This uses the page's existing scheme: element evidence (Rule-derived / Inferred / Invented) and per-dimension sources (Text / Buildings / Estimate). It reuses the tower's hara code for the tier rows.

| Element | Proposal | Element tag | Dimension sources |
|---|---|---|---|
| Storey count | Rajarajan: stone body + **2 tiers** + neck + wagon roof. Keralantakan: stone body + **4 tiers** + neck + wagon roof. Change `n:3` → 2 and `n:5` → 4. | Rule-derived | Buildings (BS-E, IG-I, IG-O, ES; PH1–PH8) |
| Heights | Rajarajan about 24 m to finial tips (0.8 W); Keralantakan keep 27.4 m or raise to 28–29 m | Inferred | Rajarajan: Estimate (PH2). Keralantakan: Buildings (TH, IH, IC87) and Estimate (PH5). |
| Height split | Stone body 0.54 (Rajarajan) / 0.42 (Keralantakan) of the height to the ridge. Tiers per §4. Neck plus roof 0.15–0.18. Finials 0.02–0.04 above. | Inferred | Estimate (PH2, PH5) |
| Tier step-in | Rajarajan: tier 1 almost flush (0.9 m in), tier 2 4.9 m in, roof ends 6.5 m in. Keralantakan: 1.3, 3.2, 5.9, 7.7 m, roof ends 8.6 m in (per side, from the cornice edge). Apply the same insets on the short faces until better data exist. | Inferred | Estimate (PH2, PH5; ±25%) |
| Tier rows, long faces | Reuse `hara()`: corner kuta, salas with barrels parallel to the face, panjaras between. Tier 1: 2 kutas, 4 salas, 2 panjaras + centre bay. Upper tiers: 2 kutas, 2 salas, 2 panjaras + centre. | Rule-derived (kinds); Inferred (counts) | Kinds: Buildings (PH) and Text (MM p. lxvi, 22.82–89). Counts: Estimate (PH, about 50%). |
| Centre bay, long faces | Projecting central pavilion on every tier: window opening on tiers 1–2 (Keralantakan east face also tier 3), large horseshoe gable above, the stack rising into the roof's central gable with a lion-face crest | Rule-derived | Buildings (PH1–PH3, PH6, PH8) |
| Tier rows, short faces | Corner kutas and a central gabled pavilion with a blank niche on every tier. Fill between with hara. | Inferred | Central element: Buildings (ES: a niche figure in each storey of the south face; PH4, PH8). Counts: Estimate. |
| Neck | Band under the roof, about 0.08 of the height, with a row of blank seated-figure blocks (or plain) | Inferred | Estimate (PH). The figures are Nayaka stucco: hide them in the Chola phase. |
| Wagon roof | Barrel with jala texture. A horseshoe gable at each end with a lion-face crest and outcurled sides. A large central gable on each long face. Ridge length 0.52 (Rajarajan) / 0.42 (Keralantakan) of the body width. | Rule-derived | Form: Text (MM p. lxx; 22.84–85) and Buildings (BS-E, WP, PH). Lengths: Estimate (PH). |
| Finials | Rajarajan 5, evenly spaced, the middle one behind the central crest. Keralantakan 7 the same way (6 if the centre is left out). | Rule-derived (Rajarajan); Inferred (Keralantakan) | Rajarajan: Buildings (TH, BS-E, PH3). Keralantakan: Buildings (PH6–PH8). |
| Rajarajan base | Plinth; a dado with one row of **blank relief panels** between pilasters on both long faces (east about 16, west about 9, ±4); a cornice with blank lion-head blocks over the pilasters; two plain courses | Inferred | Panels: Buildings (BS-T, IG-I, ES, PH1, PH3). Counts and heights: Estimate. Moulding names: none (unread MM 24.27–28). |
| Keralantakan base | Tall base of plain stepped courses, no panels | Inferred | Buildings (BS-T "unpretentious"; PH5–PH7). Heights: Estimate. |
| Rajarajan guardians | Two blank blocks about 5 m high (0.17 W) in tall niches centred in each half of the **east** face, not beside the door | Rule-derived (position); Invented (figure) | Position: Buildings (BS-E, IC87, PH1). Size: Buildings (IG-I, ES). |
| Rajarajan west porches | Two projecting two-level pavilions flanking the passage on the court face, with a small door below and a blank niche above | Inferred | Buildings (PH2, PH3). Identity: unknown. |
| Wall storeys, other bays | Pilasters and blank niches. Keralantakan: small rectangular windows and empty niches on the outer faces. | Rule-derived | Buildings (BS-E, IG-O, PH). Niche positions also Text (MM 23.106). |
| Passage | Plain pilasters on plain brackets. Flat-lintelled opening in the Chola phase. Show the Rajarajan's inner arch only in "as it stands". | Inferred | Buildings (ES); the arch is an Estimate of date |
| Materials and colour | Stone body (granite) and stucco-covered upper tiers on both; same colour in the model | Inferred | Buildings (IG-I, IG-O, ES, TH, which conflict on where stone stops) |
| Stucco figures | Leave out in the Chola phase. In "as it stands", blank blocks in front of the tier pavilions. | Invented | Buildings (IG-I, IG-O: Nayaka, 17th c.) |

## 6. Photograph counts

All images are on Wikimedia Commons. Errors are my estimates of how far off each count could be.

| Key | Image | What it shows | Counts and observations | Error |
|---|---|---|---|---|
| PH1 | [Rajarajan Enterance Big Temple Thanjavur](https://commons.wikimedia.org/wiki/File:Rajarajan_Enterance_Big_Temple_Thanjavur_TamilNadu_India.jpg) (2023, 3325 × 2761) | Rajarajan, east face, frontal | Ground storey + 2 tiers + neck + wagon roof. 4 pot finials visible, with the central one hidden by the crest. Guardians in tall niches in each half. Base dado with a row of panels, 6 visible on the south half. Tier 1 sequence per half: kuta, gabled sala, panjara, sala, centre window bay. | Tiers ±0; finials ±0 (with PH3); tier elements ±1 per half; panels ±2 visible |
| PH2 | ["A beautiful stone work on Rajarajan Entrance"](https://commons.wikimedia.org/wiki/File:%22A_beautiful_stone_work_on_Rajarajan_Entrance_The_Big_Temple%22.JPG) (2012, 2256 × 1504) | Rajarajan, west face, frontal, whole | Used for heights, fractions and step-ins (§2.5, §4). Two projecting porch pavilions. Corner niche figures. | Heights ±15%; insets ±25% |
| PH3 | ["A Full Shot of Rajarajan Entrance Backside View"](https://commons.wikimedia.org/wiki/File:%22A_Full_Shot_of_Rajarajan_Entrance_Backside_View_of_The_Big_Temple%22.JPG) (2012, 1504 × 2256) | Rajarajan, west face | **5 pot finials** (the central pot is visible above the crest). Tier 1 and tier 2 sequences as in §2.1. 4–5 base panels in each outer bay. Arched inner frame in the passage. | Finials ±0; panels ±2 |
| PH4 | [Keralanthagan Thiruvasal & Rajarajan Thiruvasal](https://commons.wikimedia.org/wiki/File:Thanjavur_Big_Tempel_Keralanthagan_Thiruvasal_%26_Rajarajan_Thiruvasal.jpg) (2012, 2048 × 1536) | Rajarajan from the north-west inside the court: north short face and west face | End gable of the wagon roof: horseshoe arch with lion-face crest. Short face: corner kutas and a central gabled element on each tier. | Short-face counts not attempted |
| PH5 | ["A beautiful view of Keralantakan entrance backside"](https://commons.wikimedia.org/wiki/File:%22A_beautiful_view_of_Keralantakan_entrance_backside_The_Big_Temple%22.JPG) (2012, 1504 × 2256) | Keralantakan, west face, frontal, whole | Ground storey + 4 tiers + neck + roof. Used for heights, fractions and step-ins. Small windows in the wall storey. | Tiers ±0 (about 80%); heights ±15% |
| PH6 | [Thanjavur Brihadeeswara Entrance Gopuram-1](https://commons.wikimedia.org/wiki/File:Thanjavur_Brihadeeswara_Entrance_Gopuram-1.jpg) (2017, 4160 × 3120) | Keralantakan, west face, close | **6 pot finials** visible, evenly spaced, with the central crest between the third and fourth. Window openings at the centre of tiers 1 and 2. Tier 1 sequence: kuta, large-gabled pavilion, sala, panjara, centre. | Finials 6 visible ±0; tier elements ±1 |
| PH7 | [Thanjavur Brihadeeswara Temple Entrance Gopuram](https://commons.wikimedia.org/wiki/File:Thanjavur_Brihadeeswara_Temple_Entrance_Gopuram.JPG) (2014, 2592 × 1728) | Keralantakan, west face | 6 pot finials plus the central crest (confirms PH6) | ±0 |
| PH8 | [Gopuram of the Brihadisvara Temple … 203](https://commons.wikimedia.org/wiki/File:Gopuram_of_the_Brihadisvara_Temple,_Thanjavur,_Tamil_Nadu,_India_203.jpg) (2016, 5184 × 3456) | Keralantakan from outside, oblique: east face and one short face | Ridge seems to carry 7 pots. End gable with lion-face crest over the short face. Windows at the centre of tiers 1–3 on the east face. | Finials ±1 |
| PH9 | [Gangaikonda Cholapuram Temple entrance](https://commons.wikimedia.org/wiki/File:Gangaikonda_Cholapuram_Temple_entrance.jpg) (2017) | Gangaikondacholapuram east gopuram, surviving lower part | Two plain stepped masses; guardians stand in front. No panels. Reconstructed (IC04). | — |

Several other Commons photographs were looked at and gave nothing new (the 2016 "Gopuram of the Brihadisvara Temple" 202–224 series, mostly the Keralantakan from outside at dusk). One file titled "Gangaikonda Gopuram" shows that temple's vimana, not a gopuram.

## 7. Conflicts to flag on the page

- **Where the stone stops:**
  - Keralantakan: three storeys of granite (IG-O), against granite up to the first floor (ES), against a brick-and-lime gopuram (TH).
  - Rajarajan: a stone structure (IG-I), against stone with some brick (ES), against a brick-and-lime superstructure (TH).
  - A plausible reading is a granite ground storey (perhaps with a granite core in the lowest tiers) under brick and stucco tiers, but nothing read settles it.
- **Keralantakan height:** 25, 27.4 or 30 m. The photograph estimate (27–31 m) cannot separate them.
- **Rajarajan height:** no published figure. The model's 18 m is lower than the photograph estimate of 22–26 m.
- **Storey counts in the model:** 3 and 5 tiers, against 2 and 4 on the sources' counting (§2.1).
- **Keralantakan finials:** 6 or 7. There is no text source, and the model's estimate of 5 is probably low.
- **Interior figures of the outer gopuram:** BS-E puts Brahma and Dakshinamurti inside the first storey, on its inner face. IG-O puts the surviving first-storey sculptures (Dakshinamurti, Brahma) on the south and north faces, and ES puts them in each storey's central niche on those faces. These may describe different things (interior images against stucco niche figures).
- **Guardians:** BS-E calls their position in the middle of each half-facade unusual for gopurams. It is what the photographs show, and it differs from the side-of-door position later gopurams use.
- **Guardian names:** ES gives Indra and Rahu, and asks to be corrected. IG-I identifies the Rajarajan's pair as Nandi and Mahakala.
- **Finial rules:** the Rajarajan's 5 on three storeys matches the Manasara (v. 174). The Keralantakan's 6–7 on five storeys does not match its 11 (v. 202).
- **"Almost a hundred metres" between the gateways** (BS-T; WP's 100 m): contradicted by the mapped 72 m (`measurements.md` §9).

## 8. Not read or still needed

- **Mayamata vol. 2, ch. 24 and ch. 30.** These hold the gateway proportions, the bases (24.27–28), the storey heights for 1 to 7 storeys, and the wagon-roof details (24.90–99). This is the main textual gap.
- **Pichard, *Tanjavur Brhadisvara: An Architectural Study* (1995).** It should have measured elevations of both gopurams, which would replace every photograph estimate here.
- **J. C. Harle, *Temple Gateways in South India* (1963).** The standard study of the early gopura. Dagens cites it twice in vol. 1 (notes on book pp. 175 and 219). Not found online.
- **Crispin Branfoot, "The Tamil gopura: from temple gateway to global icon", *Ars Orientalis* 45 (2015).** Its [repository record](https://eprints.soas.ac.uk/21449) lists a PDF, but neither the fetch tool nor the browser could open it.
- **IGNCA's other Brihadisvara sections** (architecture, iconography) and the [Amrit Kaal "Outer Gopura" PDF](https://amritkaal.nic.in/writereaddata/Portal/images/pdf/011_Outer%20Gopura.pdf). Both refused automated reading; they could be opened by hand.
- **Short faces:** pavilion counts on the north and south faces of both gopurams. Side-on photographs were not found on Commons.
- **Base mouldings by name** for both gopurams, and the Rajarajan's short-face panels.
- **The Rajarajan's passage arch:** when it was inserted.
- **Gangaikondacholapuram's gopuram base:** a description from before its reconstruction.
