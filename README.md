# Hangu Chen — Personal Academic Website

Static site: `index.html` + `style.css` + your photo. No build tools.

## Preview locally
Double-click `index.html`, or run `python3 -m http.server` in this folder and open http://localhost:8000.

## Publish free on GitHub Pages
1. Create a GitHub account if you don't have one, and turn on two-factor authentication.
2. Create a new repository named **`yourusername.github.io`** (use your actual GitHub username — this exact name makes it your main site).
3. Upload `index.html`, `style.css`, and `headshot.jpg` (drag-and-drop via the repo's "Add file → Upload files", then Commit).
4. Go to **Settings → Pages**. Under "Build and deployment", set Source to **Deploy from a branch**, branch **main**, folder **/ (root)**. Save.
5. Enable **Enforce HTTPS** on the same Pages settings screen.
6. Wait 1–2 minutes. Your site is live at `https://yourusername.github.io`.

## Custom domain (optional, later)
Buy a domain (e.g. yourname.com), then in Settings → Pages add it under "Custom domain" and follow the DNS instructions.

## Things to personalize
- **Photo**: save your headshot as `headshot.jpg` in this folder (the page already points to it).
- **Email**: to change your address later, edit the two lines near the bottom of `index.html`: `var user = 'hangu.chen';` and `var domain = 'utdallas' + '.' + 'edu';`.
- **Profile links**: SSRN and LinkedIn are already set in the header of `index.html`; update the URLs there if they change.
