# Hangu Chen — Personal Academic Website

A buildless GitHub Pages website: `index.html`, `style.css`, `site.js`, and `headshot.jpg`.

## Preview before publishing

Open `index.html` in a browser, or run `python3 -m http.server 8000` from this folder and visit `http://localhost:8000`.

Keep redesign work on its review branch. Changes reach the live website only after an approved merge into the existing GitHub Pages source branch. No hosting or domain configuration changes are needed.

## Design and behavior

- DU Crimson `#BA0C2F` and DU Gold `#A89968`, with white, black, and DU Dark Grey `#54565B`.
- A continuous, responsive page with native section anchors. Existing `#about`, `#research`, `#teaching`, `#conferences`, and `#awards` URLs remain valid.
- All sections remain readable without JavaScript. The email links fall back to a readable address when JavaScript is disabled.
- Optional dark mode uses lighter text accents for contrast and remembers the visitor's choice when storage is available.
- Existing Google Analytics configuration and social metadata are retained.

## Checks

```sh
python3 -m unittest -v test_site.py
node --check site.js
```

The automated checks cover internal anchor targets, unique IDs, asset references, external link attributes, no-JavaScript content, and primary text contrast in both themes. Also review desktop and narrow layouts, direct section links, back/forward navigation, and theme persistence in a browser before merging.

## Content updates

Edit biography, research, teaching, conferences, awards, and profile links in `index.html`. Keep the existing academic text unless Hangu approves a content change. Edit the email address assembly in `site.js` and its readable fallback in `index.html` together.
