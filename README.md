# Vimana Grammar

**[Open the model](https://purplefaucet.github.io/temple_project/)**

A 3D model of an idealized Chola temple, after the Brihadisvara temple at Thanjavur, that runs in the browser. It shows the tower (vimana), the three halls in front of it, the cloistered court with its shrines, and the two Chola gateways. You can walk through it at eye level, on a computer or a phone.

The model's point is its evidence. Every element is tagged by how firmly it is known:
- **Rule-derived:** a documented convention puts it there.
- **Inferred:** plausible, but not firmly documented.
- **Invented:** filler with no source.

Every dimension is tagged as coming from a text, from measured buildings, or as an estimate. Tap any part to see its sources, its confidence and its rule in the shape grammar. A "Not verified" list on the page gathers the conflicts and weak points.

## What it draws on

- **Texts:** the *Mayamata* (Bruno Dagens's edition, volume 1) and the *Manasara* (P. K. Acharya's 1933 translation), for proportions.
- **The standard survey:** S. R. Balasubrahmanyam's *Middle Chola Temples* (1975), for measured buildings.
- **Site summaries:** the Archaeological Survey of India, ICOMOS, IGNCA and others.
- **Measurements made for this project:** OpenStreetMap outlines checked against satellite imagery, and photographs of the gateways.

The full sources are listed on the page. The research behind each part is in [`research/`](research/).

## Scope and limits

- **An idealized composite,** made for learning. It is not an exact model of Thanjavur, and no specialist in temple architecture has reviewed it.
- **No sanctum interior and no deity imagery.** Figure sculpture is shown as blank blocks.
- **Many sizes are estimates.** The main unread sources are Mayamata volume 2 and Pichard's architectural study of the temple. Both are listed in the research notes.

## How it was made

Built with Claude, an AI model made by Anthropic. Claude read the sources, wrote the rules and the code, and set the confidence figures, which are its own estimates. The whole app is the single file `index.html`, using [three.js](https://threejs.org/).
