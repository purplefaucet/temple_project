# The compound: research notes for the build

Notes for adding the court around the tower and halls: the enclosure wall and cloister, the gateways, the Nandi pavilion and the other buildings in the court. The model is Thanjavur (Brihadisvara), with Gangaikondacholapuram as a comparison. The notes are written so a build session can work from them without the source books. They contain summaries and citations only, with quotations kept short. Compiled 18 October 2026.

Scope reminder: no sanctum interior and no deity imagery. The subshrines therefore need only their outer form; their images are never drawn. The Nandi bull, the guardian figures and the stucco figures on the gateways are figure sculpture, so they are omitted or shown as blank "Invented" blocks.

W means the tower's base width: 30.18 m at Thanjavur and 30.48 m at Gangaikondacholapuram (GKC).

## 1. Sources and how they were read

| Key | Source | How it was read | Reliability |
|---|---|---|---|
| MM | *Mayamata*, ed. and tr. Bruno Dagens, vol. 1 (IGNCA / Motilal Banarsidass, 1994) | Directly, from the scan in `sources/` (local only, not in the repo). Chapter 23 (book pp. 387 ff.) and the introduction (pp. lxviii–lxx) were read on the OCR text and checked against the page image where the OCR was garbled. | High for what the text says. Ch. 24 (the five gateways), ch. 25 (pavilions, including cloister galleries) and ch. 30 (gateways again) are in **volume 2, not available**. They are known only from the analytical table of contents and Dagens's introduction in vol. 1. |
| BS-T | S. R. Balasubrahmanyam, *Middle Chola Temples* (1975), Thanjavur sections on wisdomlib: [The Temple Complex](https://www.wisdomlib.org/south-asia/book/middle-chola-temples/d/doc210431.html), [Composite Plan](https://www.wisdomlib.org/south-asia/book/middle-chola-temples/d/doc210435.html), [Sabhapati-mandapa](https://www.wisdomlib.org/south-asia/book/middle-chola-temples/d/doc210436.html), [Amman Shrine](https://www.wisdomlib.org/south-asia/book/middle-chola-temples/d/doc210437.html), [Parivaralayattu Pillaiyar](https://www.wisdomlib.org/south-asia/book/middle-chola-temples/d/doc210438.html), [Later History](https://www.wisdomlib.org/south-asia/book/middle-chola-temples/d/doc210450.html) | Through a fetch tool that returns excerpts, with quotes capped at about 120 characters. The numbers in §4 were requested verbatim. | Medium. It is the standard survey, but it was read only in excerpts, and one of its figures conflicts with every other source (§4). |
| BS-G | Same book, [Gangaikondasolapuram](https://www.wisdomlib.org/south-asia/book/middle-chola-temples/d/doc211879.html) | Same tool | Medium |
| ASI | Archaeological Survey of India, [Great Living Chola Temples](https://asi.nic.in/pages/WorldHeritageCholaTemples) | Same tool | Medium to high. This is the site's custodian, but the page is a short summary. |
| IC87 / IC04 | ICOMOS advisory evaluations for UNESCO: [1987](https://whc.unesco.org/document/153044) and [2004](https://whc.unesco.org/document/153042) | Same tool | Medium. They summarise the nomination files. |
| SP | Sahapedia, [Notes on Certain Aspects of Brihadisvara Temple](http://www.sahapedia.org/notes-certain-aspects-of-brihadisvara-temple) (no byline) | Same tool | Medium to low. Detailed, but unsigned and without references in the excerpt. |
| FH | Friends of Heritage Sites, Tamil Nadu (text by V. Selvakumar and S. Devadoss), [Google Arts & Culture story](https://artsandculture.google.com/story/brihadeesvara-temple-thanjavur-friends-of-heritage-sites/HgWhnVO44mWnIw) | Same tool | Medium |
| ES | S. Nayyar, [eSamskriti, Brihadisvara Temple Thanjavur](https://www.esamskriti.com/a/TamilNadu/Brihadisvara-Temple-Thanjavur.aspx) (2016). Sources: the site guide, temple boards and an ASI booklet. | Same tool | Low. Travel write-up, used only for dates where nothing better was found. |
| TH | *The Hindu*, 29 Nov 2010 (G. Srinivasan), on lightning damage to the Rajarajan gopuram, [reposted here](https://ponniyinselvan.in/forum/discussion/comment/43908) | Same tool, via a forum repost | Low to medium (a newspaper, read secondhand) |
| WP | Wikipedia, [Brihadisvara Temple, Thanjavur](https://en.wikipedia.org/wiki/Brihadisvara_Temple,_Thanjavur) | Same tool | Tertiary. Mostly cites BS and Michell 2008, and in places is internally inconsistent. |
| MS | *Manasara*, tr. P. K. Acharya (1933): [ch. 31, Courts](https://www.wisdomlib.org/hinduism/book/manasara-english-translation/d/doc421078.html), [ch. 32, Attendant deities](https://www.wisdomlib.org/hinduism/book/manasara-english-translation/d/doc421079.html), [ch. 33a, Gate-houses](https://www.wisdomlib.org/hinduism/book/manasara-english-translation/d/doc421080.html) | Same tool, as summaries with verse numbers | Low to medium. Second witness only. |

## 2. Layout: what is where (Thanjavur)

Reading from east to west along the axis:

1. **Moat and fort wall.** BS-T describes a deep moat, filled at the entrance, and a fortification wall with bastions along it. There are two further walls outside it, the outer one with gun-holes. These are later than the temple: WP says "added after the 16th century" (citing Michell 2008), FH says the Nayakas built them, and IC04 calls the enclosure the "Sivaganga Little Fort" of about 18 ha. **Out of scope for the Chola phase.**
2. **Outermost entrance.** This is a Maratha-period gate. SP describes a brick-and-mortar arch "at the easternmost entrance" with stucco figures it dates to the Maratha period, and FH says the first gateway "was built by the Marathas". BS-T describes a gateway in this wall "whose upper inner surface is semi-circular and top flat". IC04 counts **three** eastern gateways in all, which fits this gate plus the two Chola gopurams.
3. **Keralantakan tiruvasal (outer gopuram).** It is in the outer enclosure wall, on the axis (BS-T, BS Composite Plan). The name comes from a surname of Rajaraja I (BS-T, WP).
4. **The outer court.** BS-T: "we traverse almost a hundred metres westwards" before reaching the inner gopuram. That is about 3.3 W. See §6 for why this is doubtful.
5. **Rajarajan tiruvasal (inner gopuram).** It stands in the east wall of the inner enclosure (BS-T, SP, BS Composite Plan), and the inner court starts behind it.
6. **Inner court.** The court is cloistered and about 240 × 120 m (§4). It holds, from east to west, the Nandi pavilion, the three halls and the tower. ASI: the court is 240.9 m east–west by 122 m north–south, entered by one gopura on the east and "three ordinary torana entrances" on the sides and rear. BS Composite Plan: the cloister wall has three entrances, "two of which are now closed", and the northern one was "perhaps used solely by royalty", being nearest the palace. (ASI's count is four entrances including the gopura; BS's is three. That is unresolved.)

**Where the tower sits in the court.** No measured offset was found. SP describes the court as twice as long as it is wide and the original layout as a grid of 60 × 60 squares, with the vimana taking 225 squares (15 × 15). If that 60 × 60 grid covers the **western square** of the court (120 × 120 m), each square is 2 m and the vimana is 30 m wide, which matches W = 30.18 m. On that reading the tower is centred in the western half of the court, about 2 W from the west wall. **This is my inference from SP's grid, about 65% confident.** SP does not say which part of the court the grid covers.

**Nandi pavilion.** It stands on the axis, in front of the mukhamandapa (BS-T, WP). No distance from the halls was found.

## 3. What the texts prescribe

### Mayamata, ch. 23 "Enclosures and Attendants' shrines" (read directly)
- **Purpose:** enclosures protect and adorn the temple and hold the Attendants' shrines (23.1). There are up to five concentric enclosures, laid out on nested square grids (23.2–5). Dagens: *prakara* means both the wall and the court it encloses (n. 2).
- **Size of enclosures:** the front length of an enclosure is 1½, 1¾, 2, 2½, 3 or 4 times the temple's width (23.6–7). Dagens: enclosures are square or oblong, and the temple's width is the reference unit (n. 4). For small temples, the spacings between successive walls are also given in cubits (23.8–16). These do not scale to Thanjavur.
- **Reference line:** dimensions are taken from the inner face of the wall, or from its middle or outer face (23.17).
- **Walls:** the first wall is 1½ cubits thick, and each further enclosure adds 3 digits, up to 2 cubits. Height is 3 or 4 times the thickness, and the top is ⅞ as thick as the bottom (23.18–20a). Walls rise to the level of the architrave, bell-capital or abacus of the main temple's pillars (23.20b–21). The wall may be treated like a small building, with a base, a pillar level and an entablature (n. 8). It may be plain or have flanking structures, and its top may have rounded merlons (23.20b–21).
- **Coping:** an architrave, fascia, doucine and cap-stone. Its height equals the wall's width, or that plus ¼ or ½, divided 3 : 3 : 2 : 3 (23.23–25).
- **Cloister gallery:** a cloister-like gallery of one, two or three storeys may stand against the **inner** face of the wall, with the outer face left bare. Its top storey is ⅔, ¾ or ⅞ the height of its ground floor, or the gallery is as high as the wall (23.26–28a). The exterior walls may reach at most the main temple's bottom-storey floor, its architrave, its engaged structures or its roof (23.28b–29). Dagens infers the wall must stay lower than the temple (n. 13). A gallery of one or two storeys may run all round, with its base equal to the wall's base or ¾ or 6/8 of it, and pillars twice the base height or slightly less (23.30–31).
- **Coping figures:** bulls and dwarves are set on the wall coping for Siva's temples (23.32a, n. 14). **Thanjavur matches this:** SP notes "a row of Nandis seated on top" of the prakara's outer wall.
- **Attendants' shrines:**
  - **Size:** the shrine's sanctum is half its width, and its width is ⅓, ½ or ¾ of the main temple's (23.35–36a).
  - **Number:** 8, 12, 16 or 32 attendants, each tied to a square of the site grid (23.36b–52; Fig. 17).
  - **Placement:** shrines either stand against the wall or are free-standing in their squares (23.53a). When they stand against the wall, they are housed in the cloister or treated like the wall's flanking structures (n. 24).
  - **Candesa:** Dagens notes that Candesa's chapel "is always located at the north of the sanctum" (n. 27). The verse says Candesa faces south (23.56b–57a).
  - **Form:** shrines may look like temples, pavilions, halls or houses (23.57b–58a). Dagens glosses these as a six-level elevation, a three-level elevation with a terrace roof, a four-level elevation with a hipped roof, or a four-level elevation with a wagon roof (n. 28).
- **Storeyed galleries (*malika*):** rows of galleries of one to five storeys in the second and third enclosures (23.58b–59a). Wall goes over wall and pillar over pillar, never wall over pillar (23.59b–60a).
- **Gallery proportions:**
  - Take the height from the top of the main temple's base to its architrave and divide it into 7: the gallery's base is 2 parts and its pillars 5 (23.61b–67a). Pillar diameter equals the wall thickness.
  - Alternatively, the gallery's base is ½, ⅓ or ¼ of its pillar height, and its entablature is a quarter less than its base (23.67b–69).
- **In front of the shrines:** the pavilions for dance and ablutions and the altars (23.72b–73).
- **Altars and flagstaff:**
  - **Altar size:** the two altars are each half the sanctum's width in height and width (23.74–76).
  - **Altar positions:** the outer altar (*paisacapitha*) stands outside the gopura, at half the temple's width from it. The *balivistara* stands between it and the temple (23.74–76).
  - **Flagstaff:** it stands in front of the bull (Vrsabha), halfway from the temple (23.82–83a).
- **Other buildings:** service buildings are placed in named squares, for example the ablution pavilion and the pavilion for flowers on the south side (23.83b–88).

### Mayamata, gateways: vol. 2, known only from vol. 1
- **Introduction (p. lxx, read on the page image):**
  - The five gateways correspond to the five enclosures and grow larger the farther they are from the temple.
  - They may have up to seven storeys (24.2–36).
  - Dagens: they are "almost always rectangular and have a wagon-roof".
  - Gateways are also treated in ch. 30.
- **Table of contents for ch. 24:**
  - Dimensions are related to the main temple's (24.1–10), with proportions for one-, two-, three- and seven-storeyed gateways.
  - Each enclosure's gateway has its own name: *dvarasobha* (1st), *dvarasala* (2nd), *dvaraprasada* (3rd), *dvaraharmya* (4th) and *dvaragopura* (5th).
  - **The actual ratios are in vol. 2 and unread.**

### Manasara (second witness, via excerpts)
- **Ch. 31, Courts:**
  - **Number:** five courts, with mentions of a sixth and seventh.
  - **Walls:** height equal to the wall's width or ¼ more (31.51–55).
  - **Galleries:** a gallery runs along the wall, with base, pillar and entablature (31.61–62), and a parapet above it (31.65–66).
  - **Attendant shrines:** in the courts, at the main building's height or ¾ or ½ of it (31.74–75). The extract's statements on court extent (31.40–48) were too garbled to use.
- **Ch. 32, Attendant deities:**
  - **Groups:** eight attendants in the first court, sixteen in the second and third, thirty-two in the third.
  - **The bull:** its shrine is in the east (32.10, 32.33) and is "made like a pavilion" (32.118–119).
  - **Altars:** the bali-altar stands one, two or three rods from the main edifice, toward the gateway (32.101–102).
- **Ch. 33a, Gate-houses:**
  - **Names:** five names, one per court, matching the Mayamata's (33.8–11).
  - **Storeys:** 1, 2, 3, 4 and 5 storeys from the inner court outward (33.94–96), and up to about 17 for great sites (33.97).
  - **Plan:** length is 1¼, 1½ or 1¾ times the width, preferably twice (33.22–23).
  - **Size relative to the temple:** breadth equals the main building's or exceeds it by ¼ up to double (33.85–87).
  - **Storeys relative to the temple:** for temples, a gateway may have more storeys than the main building (33.107–110).

## 4. Measured data

| Thing | Value | W | Source and note |
|---|---|---|---|
| Inner (cloistered) court | 240.9 × 122 m | 7.98 × 4.04 | ASI. IC04 gives "ca 240 m east-west and 120 m north-south". SP and FH give 240 × 120. **Recommended.** |
| BS's "temple complex" | 240.79 × 121.92 m (= 790 × 400 ft) | 7.98 × 4.04 | BS-T. Same figure as ASI, but BS applies it to the whole complex. |
| BS's cloister (*tiruch-churru-maligai*) | 152.40 × 77.20 m | 5.05 × 2.56 | BS-T, quoted verbatim. 152.40 m = 500 ft, and 77.20 m ≈ 253 ft (probably 250 ft = 76.20 m, misprinted). **Conflicts with all other sources** (§6). |
| Outer boundary wall | 270 × 140 m | 8.95 × 4.64 | IC87. Which wall this is was not established. |
| Inner wall to outer defensive wall | about 6.10 m | 0.20 | BS-T, "removed about 6.10 ms from it". Which pair of walls is meant is unclear. |
| Keralantakan to Rajarajan gopuram | "almost a hundred metres" | ≈ 3.3 | BS-T |
| Keralantakan gopuram height | 25 m / 27.4 m / 30 m | 0.83 / 0.91 / 0.99 | TH (25 m) / an [indian-heritage.org](https://www.indian-heritage.org/temple/peria.htm) page (90 ft) / IC87 and WP (30 m) |
| Nandi bull | 3.65 m high, 5.94 m long, 2.59 m broad | 0.12 × 0.20 × 0.09 | BS p. 22 via WP. WP's own text gives other figures. |
| Vimana for reference | about 60–65 m high | ≈ 2.0–2.2 | IC87 60.95 m; IC04 65 m |

The ASI figure also fits IC04's area for the "temple complex", 2.85 ha: 240 × 120 m = 2.88 ha.

**Gangaikondacholapuram** (W = 30.48 m):
- **Court:** "172.82 ms (567') long and 96.93 ms (318') wide" (BS-G), which is 5.67 W × 3.18 W, a ratio of about 1.78 : 1 rather than 2 : 1.
- **Wall:** only "a vestigial wall of enclosure" survives. BS-G says the wall was almost wholly destroyed for materials for a dam.
- **Gopuram:** the east gopuram's "superstructure ... has fallen, and only the basal portion is left" (BS-G). IC04 reports that the eastern gateway and prakara have been reconstructed.
- **Tower and subshrines:**
  - The tower stands in the middle of the court (BS-G).
  - Two subsidiary temples flank it, the Ten Kailasam (south) and Vada Kailasam (north). The Vada Kailasam was later converted to an Amman shrine.
  - There is a Chandesvara shrine.
  - A large stucco Nandi stands to the east, with a bali-pitha east of it.
  - A lion-well (step-well) lies near the north-east (BS-G).

## 5. Gateways, cloister and other buildings (answers to the brief)

### Gopurams at Thanjavur
Your reading is confirmed: there are **two Chola gopurams on the east**, the outer Keralantakan and the inner Rajarajan (BS-T, SP, FH, WP). East of them is a third, Maratha-period outer gate (§2.2).

| | Keralantakan tiruvasal (outer) | Rajarajan tiruvasal (inner) |
|---|---|---|
| Storeys | 5 (ES; WP gives "five-story" for the main entrance gopuram, citing BS) | **Not found.** Often said to be three; I could not verify this (below 70%). |
| Height | 25–30 m (§4) | Lower than the Keralantakan (TH). No figure found. |
| Plan | Not found | ES gives "27 by 17.25 m" for the Rajarajan gopuram without saying what is measured. That would be 0.89 W × 0.57 W if it is the base. Low confidence. |
| Materials | Granite up to the first storey, stucco above (ES). BS-T: "a massive stone structure". | Stone with brick (ES). TH: the superstructure is "brick and lime mortar". |
| Form | BS-T: "the entablature is ... unpretentious, the superstructure being stocky and short" | More ornate: "attractive panels on the adhishthanam" (BS-T), with Puranic reliefs on the base (WP) |
| Top | Wagon (barrel) roof: WP says the original east gopuram is "barrel vaulted". The general type is confirmed by Dagens (p. lxx). | Wagon roof with **five finials** (TH: one of its five kalasas was struck by lightning) |
| Date | Chola, Rajaraja I (FH; the name refers to his Kerala campaign). Exact year not found. | Chola, Rajaraja I (FH, TH). Exact year not found. |

**Do the two differ in form?** Yes, on what was found. The outer gate is taller and has more storeys, but it is plainer and "stocky". The inner gate is lower, with a richly sculpted base. That matches the Mayamata's rule that gateways grow larger outward (p. lxx) and the Manasara's rule of more storeys in the outer courts (MS 33.94–96). Both are far lower than the vimana: WP says "less than half the height". That is the reverse of later Nayak temples, where the gopurams dominate.

### Enclosure wall and cloister
- **Storeys:** the cloister has two (SP: "The two-storeyed, cloistered prakara ... The upper storey has almost disappeared"; ASI: a "double-storeyed malika"; IC04: "a low, two-storied cloistered prakara").
- **Builder:** Rajaraja's commander Krishnan Raman. It was complete by about 1010 (SP), and BS names it the "Krishnan Raman tiruch-churru-maligai".
- **Lingas:** ES says the 108 lingas now in the cloister were installed by the Maratha ruler Serfoji. Not verified elsewhere.
- **Wall coping:** a row of Nandis along the top of the outer wall (SP).
- **Not found:** wall height, wall thickness, cloister depth and the number of pillar rows.
- **Subshrines in or along the cloister:**
  - **SP:** 36 subshrines, "some of which no longer exist". 27 are square with octagonal *sikharas* and 9 are rectangular.
  - **BS Composite Plan:** the original plan had "the eight shrines for the parivaradevatas, the eight shrines for the dikpalas".
  - **WP:** the original Chola set of eight is "now missing" (citing BS pp. 22–25).
  - **The western cloister:** an inscription on a pillar of the western wing records a Ganapati image ("Parivaralayattu Pillaiyar") set up by Rajaraja I (BS).
  - Their positions were not found beyond this.

### Nandi pavilion
- **Date:** the present Nandi and its pavilion are Nayak, 16th–17th century (WP citing Michell 2008; ES; *The News Minute* 2015 says the bull "was added in the 16th century"). The pavilion's ceiling paintings are Maratha (ES).
- **Your conflict:** WP's statement that the bull was made under Rajaraja I was not supported by anything I read. BS gives the bull's size without a date. I have seen it said that an earlier, smaller Chola Nandi now stands in the cloister, but **I could not find a source for that, so treat it as unverified (below 60%).**
- **Size:** bull 3.65 × 5.94 × 2.59 m (BS via WP). Pavilion dimensions were not found.
- **Distance from the halls:** not found.

### Other buildings in the court

| Building | Date and builder | Position | Size and form | Phase |
|---|---|---|---|---|
| Chandesvara shrine | Chola, "part of the original master plan", built before Rajaraja's conquest of "the 12,000 islands" (BS Composite Plan). IC04: contemporary with the main temple. | North of the vimana (SP; consistent with Mayamata n. 27) | Three storeys including the *sikhara*, with an octagonal *sikhara* (SP). "Perhaps the biggest surviving Candesa temple" (SP). Dimensions not found. | **Chola** |
| Parivara and dikpala shrines | Chola plan (BS) | Cloister (SP, BS) | Small. Square ones have octagonal tops (SP). | **Chola** (most lost) |
| Amman (Brihannayaki) shrine | Pandya, 13th c., "Konerinmaikondan" (BS; IC87). SP says about 1400. Front hall Nayak or Maratha (ES). | Not found in the sources read | Not found | Later |
| Subrahmanya (Murugan) shrine | Nayak, 16th–17th c. (WP citing Michell; IC87 "a Nayak king"; ES). Hall by Serfoji II (ES). | Not found | Not found | Later |
| Sabhapati (Nataraja) mandapa | Not dated by BS. IC87 lists it among later additions. | East of the Amman shrine (BS) | Not found | Later |
| Ganesha shrine | Rebuilt by the Maratha Serfoji II, late 18th c. (ES; ASI; BS records repairs dated 1801) | Not found | Small | Later |
| Karuvur Devar shrine | Maratha, 19th c. (ES) | Not found | Small | Later |
| Dakshinamurti shrine | "Of different later dates" (BS) | Not found | Not found | Later |
| Varahi shrine | Modern brick building (WP) | South side of the court (WP) | Small | Later |
| Mandapa in the north-east corner | "A later" mandapa (BS-T) | North-east corner of the court | Not found | Later |
| Fort walls, moat | Post-16th c., Nayak (WP, FH). WP says (uncited) the French used the temple as an arsenal in 1777. | Around everything | — | Later |

**Positions are the big gap.** None of the sources read places the Amman, Subrahmanya or Nataraja buildings within the court. I believe the Subrahmanya shrine is north-west of the vimana and the Amman shrine on the north side, but **that is from memory and below 70%**. Do not build those positions as Buildings data.

## 6. Build spec (suggested)

This uses the page's existing scheme: element evidence (Rule-derived / Inferred / Invented) and per-dimension sources (Text / Buildings / Estimate). It also proposes a **phase toggle**: "Chola, about 1010" against "As it stands", so later additions can be hidden.

| Element | Proposal | Element tag | Dimension sources |
|---|---|---|---|
| Inner court | Rectangle 8 W × 4 W (240 × 120 m), long axis east–west | Rule-derived | Buildings (ASI, IC04). Text: 4 W is one of the Mayamata's front lengths (23.6–7). |
| Tower position | Tower centred in the western square, about 2 W from the west wall, on the centre line | Inferred | Estimate (inferred from SP's grid, about 65%) |
| Enclosure wall | Plain outer face, Nandi figures on the coping drawn as blank blocks | Rule-derived | Text: wall rules (MM 23.18–25). Buildings: coping Nandis (SP). Height and thickness: Estimate (suggest wall top at the tower's first-storey architrave, per MM 23.20b–21). |
| Cloister | Two-storey pillared gallery along the inside of all four walls. Ground floor: base 2/7 and pillars 5/7 of the height from the tower's base top to its first architrave. Upper storey ¾ of the ground floor. | Rule-derived | Storeys: Buildings (ASI, SP, IC04). Proportions: Text (MM 23.26–28a, 23.61b–67a). Depth and bays: Estimate. |
| Cloister subshrines | Small cells or aediculae along the cloister. Either 16 (BS's 8 + 8) or 36 (SP), as a choice. | Inferred (existence); Invented (positions) | Count: Buildings (BS, SP). Positions: Estimate. |
| Rajarajan gopuram | On the axis in the east wall. Stone base with sculpted panels (plain bands, no figures), brick superstructure, 3 storeys, wagon roof with 5 finials. | Rule-derived (existence, roof); Inferred (storeys) | Finials and materials: Buildings (TH). Wagon roof: Text (Dagens p. lxx) and Buildings (WP). Storeys: Estimate. Plan: Estimate (ES 27 × 17.25 m as a starting point, low confidence). Height: Estimate, below the Keralantakan. |
| Keralantakan gopuram | On the axis, about 3.3 W east of the Rajarajan gopuram, in an outer wall. 5 storeys, about 0.9 W high (27 m), plainer, wagon roof. | Rule-derived | Storeys: Buildings (ES, WP). Height: Buildings (range 25–30 m). Distance: Buildings (BS-T, doubtful, §7). Plan: Estimate. |
| Outer wall | Plain wall linking the Keralantakan to an outer rectangle | Inferred | Estimate (IC87's 270 × 140 m is a candidate, but its identity is unclear) |
| Inner side entrances | Small plain openings in the north, south and west walls (ASI: torana entrances on the sides and rear) | Inferred | Count: Buildings (ASI; BS says three in all). Size: Estimate. |
| Chandesvara shrine | North of the tower, facing south toward the tower's north side. Small three-level shrine with an octagonal top. Width about ⅓ W. | Rule-derived (position, form); Inferred (size) | Position: Buildings (SP) and Text (Dagens n. 27; facing south, 23.56b–57a). Form: Buildings (SP). Width: Text (MM 23.35–36a gives ⅓–¾) and Estimate. |
| Altars and flagstaff | One bali altar on the axis inside the Rajarajan gopuram. Optional flagstaff between the Nandi and the halls. | Rule-derived (text only) | Text (MM 23.74–76, 23.82–83a). No Thanjavur positions found: Estimate. |
| Nandi pavilion | On the axis, east of the mukhamandapa. Four-pillar pavilion with a flat roof. The bull is a blank block 0.20 W long. **Later phase only.** | Inferred | Bull size: Buildings (BS via WP). Pavilion and distance: Estimate. Date: Buildings (WP/Michell, ES). |
| Later shrines (Amman, Subrahmanya, Nataraja, Ganesha and others) | Simple massing, **later phase only**, positions marked Invented | Invented | Estimate |
| Fort, moat, Maratha gate | Leave out, or show only in an "as it stands" view | — | — |

## 7. Conflicts to flag on the page

- **Court size:** BS's cloister figure of 152.40 × 77.20 m (5 W × 2.5 W) against ASI, IC04, SP and FH at about 240 × 120 m (8 W × 4 W). ASI is the custodian, and its figure matches IC04's area for the complex, so **use 240 × 120 (about 85%)**. BS gives 240.79 × 121.92 for the "complex", so its smaller figure may be a slip or refer to something else. Both sizes happen to be Mayamata ratios (2½ W and 4 W). Do not cite that coincidence as support for either.
- **Outer court depth:** BS-T's "almost a hundred metres" between the gopurams cannot be squared with IC87's 270 m outer wall around a 240 m court. That would leave about 15 m at each end. Either the Keralantakan stands outside IC87's wall, or one figure is wrong. **Unresolved.**
- **Which wall is 6.10 m from which** (BS-T): unclear.
- **Entrances to the inner court:** ASI says one gopura plus three toranas, while BS says three entrances, two now closed.
- **Keralantakan height:** 25, 27.4 or 30 m.
- **Rajarajan storeys:** not established.
- **Amman shrine date:** 13th-century Pandya (BS, IC87) or about 1400 (SP).
- **Nandi date:** Nayak (most sources) against WP's stray Rajaraja attribution. The claim of a surviving earlier Chola Nandi is unverified.
- **Consecration year:** BS puts the final consecration in Rajaraja's 25th regnal year. The ASI page says the temple was inaugurated in his "19th regnal year (AD 1009–10)". This does not affect the build.
- **Subshrine count:** BS's 8 + 8 in the original plan against SP's 36.

## 8. Not read or still needed

- **Pichard, *Tanjavur Brhadisvara: An Architectural Study* (1995).** This should settle the court size, wall and cloister dimensions, gopuram plans and heights, entrance count and shrine positions. It is the most useful single source for this phase.
- **Mayamata vol. 2:** ch. 24 (the five gateways: proportions, storeys, wagon roof), ch. 25 (cloister galleries, 25.188–97) and ch. 30 (gateways).
- **Michell (2008)**, cited by WP for the Nayak dates of the Nandi, Subrahmanya shrine and fort walls. Not read directly.
- **A measured site plan.** A satellite measurement of the court would settle 240 × 120 m against 152 × 77 m in a minute. One way is the distance tool in Google Maps or Google Earth. The two gopurams' distance and the Nandi pavilion's position can be measured the same way. I could not reach map services from here.
- **Manasara chs. 31–33** were read only as summaries. Ch. 33b (doc421081) was not read.
- **GKC:** BS-G gives the court and the shrine positions in outline only. No dimensions were found for the Kailasam shrines or the gopuram base.
