# Sculpture images: sources, licences and edits

Images of the sculpture on the **east (outer) face of the Rajarajan gopuram** at Thanjavur, for use as textures in the 3D model. Gathered 1 November 2026. Every file here is a crop of a photograph on Wikimedia Commons. None of the photographs is mine.

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
