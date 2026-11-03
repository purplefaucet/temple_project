# Sculpture images: sources, licences and edits

Images of the sculpture on the **Rajarajan gopuram** at Thanjavur, for use as textures in the 3D model: the **east (outer) face**, gathered 1 November 2026, and the **west (court) face** (files named `west-…`), gathered 3 November 2026 and described in the [West face](#west-face-court-side) section at the end. Every file here is a crop of a photograph on Wikimedia Commons. None of the photographs is mine.

The sections up to "Not done" cover the east face.

## Licences in short

| Photographer | Licence | Files | What it requires |
|---|---|---|---|
| Richard Mortel ("Richard Mortel from Riyadh, Saudi Arabia", via Flickr) | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) | `guardian-north.png`, `guardian-south.png`, `panel-S4.jpg`, `panel-S7-detail.jpg`, `panel-N4-row2-detail.jpg`, `panel-N4-row3-detail.jpg` | Credit the photographer, link the licence, and say that the image was changed. **No share-alike.** |
| Thamizhpparithi Maari | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) | every other `panel-*.jpg` (14 files) | Credit, link the licence, and say what changed. **Share-alike:** these cropped files are adaptations, so they must themselves be offered under CC BY-SA 3.0 or a compatible licence (CC BY-SA 4.0 is allowed as a later version). |

**Using the images in the model.** Keep this file in the repo and show a credits line for both photographers on the page. Whether a rendered 3D scene that uses a BY-SA image as a texture counts as an "adaptation" (and so must itself be BY-SA) is not clear-cut. The cautious reading is that the textured model or its screenshots would carry the share-alike condition. Using only the six Mortel files avoids the question. This is my reading of the licence texts, not legal advice.

## How panel positions are named

Each half of the east face's base has nine vertical units, counted **from the passage outward**:

| Unit | What it is |
|---|---|
| 1 | narrow strip of small figures |
| 2 | panel of stacked scenes |
| 3 | narrow strip |
| 4 | the large panel directly **below the guardian**, four rows of scenes |
| 5 | narrow strip |
| 6, 7, 8 | panels of stacked scenes, widening outward |
| 9 | narrow strip at the outer end of the face |

`S` means the south half (to the left as you face the gateway from the east), and `N` the north half.

- **Basis for the layout:** a frontal view of the whole face ([Sri Brihadisvara Temple … (2002) 1](https://commons.wikimedia.org/wiki/File:Sri_Brihadisvara_Temple,_Thanjavur,_Tamil_Nadu,_India_(2002)_1.jpg), by G41rn8, CC BY-SA 4.0; used for reference only, not cropped) and the order and timestamps of Thamizhpparithi Maari's photographs, which run along the face.
- **Confidence:** the nine-unit layout and the assignments below are about 75% reliable; individual assignments carry their own figure.
- **Missing units:** S1, S2 and N5 are not here. None of the photographs found shows them frontally and unobstructed: a bush hides S1–S2 in the 2023 frontal view, and the only close views of them are steep wide-angle shots.

## Guardians (transparent PNG)

Which guardian is which was checked against two independent frontal views of the face, from [2002](https://commons.wikimedia.org/wiki/File:Sri_Brihadisvara_Temple,_Thanjavur,_Tamil_Nadu,_India_(2002)_1.jpg) and [2023](https://commons.wikimedia.org/wiki/File:Rajarajan_Enterance_Big_Temple_Thanjavur_TamilNadu_India.jpg). The south guardian's raised foot points toward the passage (north), with his club upright beside it. The north guardian's foot points the other way. Mortel's photograph (29), taken seconds earlier with the passage visible to the figure's right, confirms the south one. About 90% confident.

**Edits made to both guardian files:**
1. Cropped from the 3840-px-wide Commons rendering of the original.
2. Scaled to 1400 px tall.
3. Background (the niche behind the figure) removed with the BiRefNet-general-lite segmentation model, run locally through `rembg`'s model file. macOS Preview's Remove Background could not be used: it stayed disabled with Preview in the background.
4. Trimmed to the figure.
5. Scaled to 1000 px tall.
6. Reduced to a 256-colour palette PNG (alpha kept) to stay under 400 KB.

The base of each figure is cut off by the niche floor at the bottom edge. The cutouts include the relief's own projecting parts (raised hand, club). The mask edges are good but not hand-checked pixel by pixel.

| File | Shows | Original | Photographer, date | Licence | Crop (x, y, w, h) in the 3840-px rendering |
|---|---|---|---|---|---|
| `guardian-south.png` (556 × 1000) | South guardian, frontal, evenly lit (face in shade, late afternoon) | [Commons page](https://commons.wikimedia.org/wiki/File:Brihadishwara_Temple,_Dedicated_to_Shiva,_built_by_Rajaraja_I,_completed_in_1010,_Thanjavur_(31)_(37237881240).jpg) · [original file](https://upload.wikimedia.org/wikipedia/commons/9/9a/Brihadishwara_Temple%2C_Dedicated_to_Shiva%2C_built_by_Rajaraja_I%2C_completed_in_1010%2C_Thanjavur_%2831%29_%2837237881240%29.jpg) (4000 × 6000) | Richard Mortel, 1 Sep 2017 | CC BY 2.0 | 269, 346, 3226, 5126 of 3840 × 5760 |
| `guardian-north.png` (565 × 1000) | North guardian, frontal, same light | [Commons page](https://commons.wikimedia.org/wiki/File:Brihadishwara_Temple,_Dedicated_to_Shiva,_built_by_Rajaraja_I,_completed_in_1010,_Thanjavur_(23)_(36786184134).jpg) · [original file](https://upload.wikimedia.org/wikipedia/commons/d/df/Brihadishwara_Temple%2C_Dedicated_to_Shiva%2C_built_by_Rajaraja_I%2C_completed_in_1010%2C_Thanjavur_%2823%29_%2836786184134%29.jpg) (4000 × 6000) | Richard Mortel, 1 Sep 2017 | CC BY 2.0 | 768, 576, 2803, 4838 of 3840 × 5760 |

Suggested credit line: *Guardian figures: photos by Richard Mortel (CC BY 2.0), cropped and background removed.*

## Base panels (JPG)

**Edits made to every panel file:** cropped to the panel's frame, scaled down (never up) to at most 1000 px on the long side, and saved as JPEG at quality 90. Nothing else was changed (no colour, perspective or retouching).

**Quality caveats:**
- Thamizhpparithi Maari's photographs are 2256 px wide and each covers about a third of a half-face. So his single panels come out only 130–550 px wide, and the narrow strips are very low resolution.
- His shots are slightly oblique, so panel edges are not perfectly rectangular.

### High-resolution panels (Richard Mortel, CC BY 2.0)

| File | Position | Shows | Original | Crop (x, y, w, h) in the 3840-px rendering | Position confidence |
|---|---|---|---|---|---|
| `panel-S4.jpg` (1000 × 659) | S4, the whole large panel under the south guardian | Four rows of scenes | [Commons page](https://commons.wikimedia.org/wiki/File:Brihadishwara_Temple,_Dedicated_to_Shiva,_built_by_Rajaraja_I,_completed_in_1010,_Thanjavur_(30)_(36786088694).jpg) · [original](https://upload.wikimedia.org/wikipedia/commons/a/a6/Brihadishwara_Temple%2C_Dedicated_to_Shiva%2C_built_by_Rajaraja_I%2C_completed_in_1010%2C_Thanjavur_%2830%29_%2836786088694%29.jpg) | 134, 410, 3245, 2138 of 3840 × 2560 | about 85% (layout matches S4 in Thamizhpparithi Maari's frontal view, and the photo was taken between two shots of the south guardian) |
| `panel-S7-detail.jpg` (1000 × 632) | S7, middle register | Standing group around a tall central pair, possibly the wedding of Siva (Kalyanasundara), which the IGNCA lists among the base subjects. The subject is unverified. | [Commons page](https://commons.wikimedia.org/wiki/File:Brihadishwara_Temple,_Dedicated_to_Shiva,_built_by_Rajaraja_I,_completed_in_1010,_Thanjavur_(33)_(37237843780).jpg) · [original](https://upload.wikimedia.org/wikipedia/commons/0/07/Brihadishwara_Temple%2C_Dedicated_to_Shiva%2C_built_by_Rajaraja_I%2C_completed_in_1010%2C_Thanjavur_%2833%29_%2837237843780%29.jpg) | 384, 512, 2995, 1893 of 3840 × 2558 | about 65% |
| `panel-N4-row2-detail.jpg` (1000 × 515) | N4, second row from the top, the scene nearest the passage | A seated couple (Siva and Parvati?) with attendants | [Commons page](https://commons.wikimedia.org/wiki/File:Brihadishwara_Temple,_Dedicated_to_Shiva,_built_by_Rajaraja_I,_completed_in_1010,_Thanjavur_(25)_(37448298766).jpg) · [original](https://upload.wikimedia.org/wikipedia/commons/0/07/Brihadishwara_Temple%2C_Dedicated_to_Shiva%2C_built_by_Rajaraja_I%2C_completed_in_1010%2C_Thanjavur_%2825%29_%2837448298766%29.jpg) | 77, 399, 3533, 1820 of 3840 × 2493 | about 85% |
| `panel-N4-row3-detail.jpg` (1000 × 625) | N4, third row, the scene nearest the passage, after a single standing figure | An archer drawing a bow against a second figure: consistent with Kirata-Arjuna, which Balasubrahmanyam and the IGNCA name among the base panels. The Commons title calls it a "dancers relief", which is wrong. | [Commons page](https://commons.wikimedia.org/wiki/File:Brihadishwara_Temple,_dancers_relief,_built_by_Rajaraja_I,_completed_in_1010,_Thanjavur_(26)_(37237944520).jpg) · [original](https://upload.wikimedia.org/wikipedia/commons/b/b2/Brihadishwara_Temple%2C_dancers_relief%2C_built_by_Rajaraja_I%2C_completed_in_1010%2C_Thanjavur_%2826%29_%2837237944520%29.jpg) | 326, 400, 2957, 1849 of 3840 × 2499 | about 85% |

Suggested credit line: *Panel details: photos by Richard Mortel (CC BY 2.0), cropped.*

### Whole panel columns (Thamizhpparithi Maari, CC BY-SA 3.0, all taken 22 September 2012)

Sources, each 2256 × 1504 px:
- **A** (14:08:48): [Commons page](https://commons.wikimedia.org/wiki/File:%22A_collection_of_details_on_the_Rajarajan_Entrance_of_The_Big_Temple%22.JPG) · [original](https://upload.wikimedia.org/wikipedia/commons/2/20/%22A_collection_of_details_on_the_Rajarajan_Entrance_of_The_Big_Temple%22.JPG). South half, centred on S4.
- **B** (14:09:00): [Commons page](https://commons.wikimedia.org/wiki/File:%22A_beautiful_collection_of_details_on_the_Rajarajan_Entrance_of_The_Big_Temple%22.JPG) · [original](https://upload.wikimedia.org/wikipedia/commons/3/36/%22A_beautiful_collection_of_details_on_the_Rajarajan_Entrance_of_The_Big_Temple%22.JPG). South half, outer part, S5–S9.
- **C** (14:09:45): [Commons page](https://commons.wikimedia.org/wiki/File:%22An_image_of_collection_of_details_on_the_Rajarajan_Entrance_of_The_Big_Temple%22.JPG) · [original](https://upload.wikimedia.org/wikipedia/commons/8/8c/%22An_image_of_collection_of_details_on_the_Rajarajan_Entrance_of_The_Big_Temple%22.JPG). North half, outer part, N6–N9.
- **D** (14:10:01): [Commons page](https://commons.wikimedia.org/wiki/File:%22A_view_of_collection_of_details_on_the_Rajarajan_Entrance_of_The_Big_Temple%22.JPG) · [original](https://upload.wikimedia.org/wikipedia/commons/7/7a/%22A_view_of_collection_of_details_on_the_Rajarajan_Entrance_of_The_Big_Temple%22.JPG). North half from the passage, N1–N4.

| File | Position | Source | Crop (x, y, w, h) in the 2256 × 1504 original | Output size |
|---|---|---|---|---|
| `panel-S3.jpg` | S3, narrow strip | A | 1805, 466, 147, 737 | 147 × 737 |
| `panel-S5.jpg` | S5, narrow strip | B | 2008, 587, 135, 669 | 135 × 669 |
| `panel-S6.jpg` | S6 | B | 1566, 587, 329, 684 | 329 × 684 |
| `panel-S7.jpg` | S7 | B | 1015, 602, 442, 677 | 442 × 677 |
| `panel-S8.jpg` | S8 | B | 381, 617, 535, 662 | 535 × 662 |
| `panel-S9.jpg` | S9, narrow strip at the outer end | B | 156, 722, 140, 534 | 140 × 534 |
| `panel-N1.jpg` | N1, narrow strip by the passage | D | 107, 579, 132, 677 | 132 × 677 |
| `panel-N2.jpg` | N2 | D | 404, 579, 316, 692 | 316 × 692 |
| `panel-N3.jpg` | N3, narrow strip | D | 803, 579, 142, 692 | 142 × 692 |
| `panel-N4.jpg` | N4, the whole large panel under the north guardian | D | 1015, 564, 1085, 714 | 1000 × 658 (scaled from 1085 px) |
| `panel-N6.jpg` | N6 | C | 226, 579, 395, 699 | 395 × 699 |
| `panel-N7.jpg` | N7 | C | 733, 579, 438, 699 | 438 × 699 |
| `panel-N8.jpg` | N8 | C | 1254, 579, 550, 699 | 550 × 699 |
| `panel-N9.jpg` | N9, narrow strip at the outer end | C | 1875, 722, 162, 534 | 162 × 534 |

Suggested credit line: *Base panels: photos by Thamizhpparithi Maari (CC BY-SA 3.0), cropped; these crops are shared under CC BY-SA 3.0.*

## 3D scans: none with a reuse licence found

Searched on 1 November 2026: the Sketchfab API (queries thanjavur, tanjore, brihadeeswara, brihadisvara, brihadeshwara, "big temple tanjore", rajarajan, dvarapala, dwarapalaka, "chola temple", gangaikonda), Wikimedia Commons (3D/STL files), and the web generally (CyArk, Scan the World, Factum, museum sites).

- **No photogrammetry of the Rajarajan gopuram's guardians or panels was found anywhere.**
- **Thanjavur models on Sketchfab** are all whole-temple models, none downloadable and none licensed for reuse:
  - [Thanjavur periya kovil](https://sketchfab.com/3d-models/thanjavur-periya-kovil-7d699c578405400684b65f5047d74509) (Senthamizh Vani A P)
  - [Brihadeeshwara Mandir, Thanjavur](https://sketchfab.com/3d-models/brihadeeshwara-mandir-thanjavur-bcd05c0ac54a460883af7b8d9f4686c7) (Yuvaan Purohit)
  - [Brihadisvara Temple](https://sketchfab.com/3d-models/brihadisvara-temple-b80c75f91dad4994a0e7000467433ac9) (Dinesh.Jallu, modelled in Maya)
  - two AI-generated ones (Meshy), by Inspanim and Arvindh23
- **Other guardian scans with open licences** exist, but they are not Thanjavur and are not Chola:
  - an 8th-century dvarapala at the Minneapolis Institute of Art, [CC0, downloadable](https://sketchfab.com/3d-models/dvarapala-guardian-figure-8th-century-ce-9b2c5e718b714964afb8482cc702d386)
  - two Khmer guardian models by Nheata, CC BY, downloadable
  - two Harvard Art Museums models ("1943.53.40" and "1943.53.41", modelled by CAEA, University of Chicago), CC BY, downloadable. These came up in a search for guardians, but the subject was not checked.
  - Javanese (Singasari) guardians by Hasanovic, not downloadable

  The downloadable ones could stand in as generic forms, but they would not be the Thanjavur figures.
- **Commons** has no 3D files of the temple.

## Not done

- **S1, S2 and N5:** no clear frontal photograph found (see above).
- **The panels' subjects:** not identified one by one, except where noted. The IGNCA's list (Kalyanasundara, Kirata-Arjuna, Kamantaka) and eSamskriti's (Kannappa Nayanar and others) are recorded in `research/gopuram.md`.
- **Flickr originals:** Richard Mortel's full album on Flickr may hold further close-ups not copied to Commons, under the same CC BY 2.0. Not checked, because the workspace cannot reach Flickr.

## West face (court side)

Gathered 3 November 2026. Twelve files, all named `west-…`.

### Licences for the west-face files

| Photographer | Licence | Files |
|---|---|---|
| Richard Mortel | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/), no share-alike | `west-corner-north.png`, `west-corner-south.png`, `west-porch-north.png`, `west-porch-south.png`, `west-panel-N1.jpg` to `west-panel-N4.jpg` (8 files) |
| Thamizhpparithi Maari | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), **share-alike** | `west-panel-S1.jpg` to `west-panel-S4.jpg` (4 files). As on the east face, these crops must be shared under CC BY-SA 3.0 or a compatible licence. |

**Share-alike was used only where nothing else would do.** The only CC BY photographs of the south half of the base are Mortel's frontal views (42) and (59). In them the south panels are in shade, at about half the resolution, and partly behind visitors and a signboard. So for S1–S4 the choice was not equal, and Thamizhpparithi Maari's close view was used. For everything else a Mortel photograph was at least as good, and was used.

Suggested credit lines:
- *West-face niche figures and north base panels: photos by Richard Mortel (CC BY 2.0), cropped and background removed.*
- *West-face south base panels: photos by Thamizhpparithi Maari (CC BY-SA 3.0), cropped; these crops are shared under CC BY-SA 3.0.*

### Layout and how positions are named

From the passage outward, each half of the west face has:
1. **A porch pavilion** projecting beside the passage. It is two-level, with a small door in its base and a window in its wall. Above its cornice is a small niche with a **seated figure**.
2. **An outer bay.** Its wall storey has a tall **corner niche with a standing figure**. Its base has **four panel units**, numbered **1 to 4 from the porch outward**. Unit 4 is a narrow strip at the outer end.

`N` is the north half, which is on the left as you face the gateway from the court, looking east. `S` is the south half.

- **Basis for the layout.** Two whole-face views were used for reference only, not cropped:
  - Thamizhpparithi Maari's frontal view, ["A beautiful stone work on Rajarajan Entrance The Big Temple"](https://commons.wikimedia.org/wiki/File:%22A_beautiful_stone_work_on_Rajarajan_Entrance_The_Big_Temple%22.JPG) (CC BY-SA 3.0, 22 Sep 2012). This is PH2 in `research/gopuram.md`.
  - Mortel's frontal view (59), [Commons page](https://commons.wikimedia.org/wiki/File:Brihadishwara_Temple,_Dedicated_to_Shiva,_built_by_Rajaraja_I,_completed_in_1010,_Thanjavur_(59)_(37497300751).jpg) (CC BY 2.0).
- **Confidence:** the layout is about 85%. Each file's position carries its own figure below.
- **The two halves' bases differ.**
  - The south bay's panels hold two or three rows of small scenes, like the east face.
  - The north bay's panels hold one row of large figures.
  - The north unit 4 is plain, uncarved blocks.
- **Possible identity of the porch figures, about 60%.** The south porch figure sits under a **many-headed serpent hood**. eSamskriti mentions "2 sub shrines of Indra and Nagaraja" on either side of the entrance (see `research/gopuram.md`, ES). The hood fits Nagaraja. The north figure is crowned and seated; that it is Indra is not verified.
- **Corner figures:** standing, with a tall crown, one hand raised palm-out at the chest and the other at the hip. Not identified.

### Niche figures (transparent PNG)

The masks were made differently by size:
- **`west-corner-south.png`:** BiRefNet, the same model as for the east guardians.
- **The three small figures:** BiRefNet and GrabCut alone both failed on them. They kept the niche pilaster or the niche's back wall. So these masks are an outline **traced by hand** and then refined with OpenCV's GrabCut, and their edges are approximate.

The three small files are left at the source's own resolution, not enlarged, so they are small.

| File | Source | Region of the original (x, y, w, h) | Edits | Notes | Position confidence |
|---|---|---|---|---|---|
| `west-corner-south.png` (320 × 1000) | Mortel (174), [Commons page](https://commons.wikimedia.org/wiki/File:Brihadishwara_Temple,_Dedicated_to_Shiva,_built_by_Rajaraja_I,_completed_in_1010,_Thanjavur_(174)_(23645360418).jpg) · [original](https://upload.wikimedia.org/wikipedia/commons/a/aa/Brihadishwara_Temple%2C_Dedicated_to_Shiva%2C_built_by_Rajaraja_I%2C_completed_in_1010%2C_Thanjavur_%28174%29_%2823645360418%29.jpg) (5940 × 3910, 1 Sep 2017) | 3049, 1076, 830, 2594 | Cropped, scaled to 1400 px tall, background removed with BiRefNet-general-lite. A second pass on the lower half restored a leg the first pass dropped, and the two masks were blended below the waist. Trimmed, scaled to 1000 px tall, reduced to a 256-colour palette. | Close, frontal, in even shade. The feet merge into the pedestal and are cut at the ankles. | about 80%: the pose matches the south corner figure in the frontal views, and sky shows beyond the niche's outer side. Mortel took it at sunset, two minutes after his close view (168) of the west face. |
| `west-corner-north.png` (134 × 456) | Mortel (168), [Commons page](https://commons.wikimedia.org/wiki/File:Brihadishwara_Temple,_Dedicated_to_Shiva,_built_by_Rajaraja_I,_completed_in_1010,_Thanjavur_(168)_(37239659700).jpg) · [original](https://upload.wikimedia.org/wikipedia/commons/8/8c/Brihadishwara_Temple%2C_Dedicated_to_Shiva%2C_built_by_Rajaraja_I%2C_completed_in_1010%2C_Thanjavur_%28168%29_%2837239659700%29.jpg) (6000 × 4000) | 596, 2754, 134, 456 | Cropped. The mask was made at 2.55× size, hand-traced and GrabCut-refined, and the result was scaled back to the source's size. | Seen from below and from the north-west, in warm evening light, and soft. The raised arm is partly lost in the mask. This was the sharpest of the four views compared. | about 90% |
| `west-porch-north.png` (104 × 134) | Mortel (42), [Commons page](https://commons.wikimedia.org/wiki/File:Brihadishwara_Temple,_Dedicated_to_Shiva,_built_by_Rajaraja_I,_completed_in_1010,_Thanjavur_(42)_(36785937204).jpg) · [original](https://upload.wikimedia.org/wikipedia/commons/7/76/Brihadishwara_Temple%2C_Dedicated_to_Shiva%2C_built_by_Rajaraja_I%2C_completed_in_1010%2C_Thanjavur_%2842%29_%2836785937204%29.jpg) (5948 × 3920, 1 Sep 2017) | 1799, 2391, 104, 134 | As for the north corner figure (mask made at 5.7× size). | The cutout keeps the slab behind the figure. In this low view the lap is cut off by the niche's lower edge; the higher frontal view PH2 shows the figure seated. | about 90% |
| `west-porch-south.png` (118 × 136) | Mortel (42), as above | 3796, 2375, 118, 136 | As above (5.6× size) | The cutout keeps the serpent hood. Same lower edge as the north one. | about 90% |

### Base panels (JPG)

**Edits to every panel file:** cropped to the panel's frame and saved as JPEG (quality 90 for S, 92 for N). Nothing else was changed, and nothing was scaled.

| File | Position | Source | Region of the original (x, y, w, h) | Notes |
|---|---|---|---|---|
| `west-panel-S1.jpg` (405 × 740) | S1, next to the porch | T. Maari, ["A view of collection of details on the backside of Rajarajan Entrance of The Big Temple"](https://commons.wikimedia.org/wiki/File:%22A_view_of_collection_of_details_on_the_backside_of_Rajarajan_Entrance_of_The_Big_Temple%22.JPG) · [original](https://upload.wikimedia.org/wikipedia/commons/2/2c/%22A_view_of_collection_of_details_on_the_backside_of_Rajarajan_Entrance_of_The_Big_Temple%22.JPG) (2256 × 1504, 22 Sep 2012, 14:17) | 120, 450, 405, 740 | Three rows. The bottom one shows a rider on a large animal. |
| `west-panel-S2.jpg` (488 × 740) | S2 | same | 672, 448, 488, 740 | The bottom row is only roughed out, apparently unfinished. |
| `west-panel-S3.jpg` (608 × 760) | S3, the widest | same | 1282, 460, 608, 760 | Three rows plus a strip of small figures at the foot. |
| `west-panel-S4.jpg` (178 × 440) | S4, the narrow strip at the outer end | same | 1982, 720, 178, 440 | The photo is slightly oblique here. |
| `west-panel-N1.jpg` (280 × 305) | N1, next to the porch | Mortel (42), as above | 1145, 3230, 280, 305 | Standing figures. **The lower right is hidden behind a visitor's head.** |
| `west-panel-N2.jpg` (245 × 305) | N2 | same | 905, 3230, 245, 305 | A figure with arms raised. The bottom right corner is slightly obstructed. |
| `west-panel-N3.jpg` (285 × 305) | N3 | same | 620, 3230, 285, 305 | A large standing figure with smaller figures beside it. |
| `west-panel-N4.jpg` (115 × 305) | N4, the outer end | same | 500, 3230, 115, 305 | Plain, uncarved blocks |

- **Why S1–S4 are named as the south half (about 85%).** The close view's four units match, in width order and row pattern, the four south-bay units in the frontal view PH2. The north bay looks different.
- **Why N1–N4 come from Mortel (42).** It is sunlit and about two and a half times the resolution of PH2. Mortel (59) shows the north panels unobstructed, but it is noticeably softer. PH2 is unobstructed but only about 120 px tall for the whole panel row.

### West face: searched, not found or not done

- **Where I searched:**
  - Commons categories "Gopurams of the Brihadisvara Temple" (all of it), "Brihadisvara Temple porch", and "Reliefs and sculptures at the Brihadisvara Temple". In the last, only the first ~140 of ~375 thumbnails were checked; many failed to load.
  - The complete Commons sets of Richard Mortel (2017), Vengolis (2016) and Thamizhpparithi Maari (2012).
- **Missing close-ups:** no close-up of either porch niche, or of the north corner niche, was found. Those three files are 100–460 px tall and only usable at small sizes on the model.
- **Not included:** the stucco figures on the upper tiers. They are 17th-century Nayaka additions (IGNCA, in `research/gopuram.md`) and were not asked for.
- **3D scans:** not searched again for the west face. The east-face search above found no scans of this gopuram's sculpture at all.
