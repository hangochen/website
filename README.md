# Hangu Chen — Personal Academic Website

Static site: `index.html` + `style.css` + your CV PDF. No build tools.

## Preview locally
Double-click `index.html`, or run `python3 -m http.server` in this folder and open http://localhost:8000.

## Publish free on GitHub Pages
1. Create a GitHub account if you don't have one.
2. Create a new repository named **`yourusername.github.io`** (use your actual GitHub username — this exact name makes it your main site).
3. Upload `index.html`, `style.css`, and `ChenHangu_Vitae_20260712.pdf` (drag-and-drop via the repo's "Add file → Upload files", then Commit).
4. Go to **Settings → Pages**. Under "Build and deployment", set Source to **Deploy from a branch**, branch **main**, folder **/ (root)**. Save.
5. Wait 1–2 minutes. Your site is live at `https://yourusername.github.io`.

## Custom domain (optional, later)
Buy a domain (e.g. yourname.com), then in Settings → Pages add it under "Custom domain" and follow the DNS instructions.

## Things to personalize
- **Photo**: add `headshot.jpg` to the folder and uncomment the `<img class="headshot">` line in `index.html`.
- **Profile links**: replace the `#` placeholders (Google Scholar, SSRN, LinkedIn) in `index.html` with your real URLs.
- Update the CV PDF filename in `index.html` if you rename the file.
