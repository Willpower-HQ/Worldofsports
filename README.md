# Willpower World of Sports — F1 Austin GP 2026

Sponsorship deck for **The World of Sports Summit** by Willpower, at the Formula 1
United States Grand Prix, Austin TX (COTA) — October 22, 2026.

**Live site:** [willpowerworldofsports.netlify.app/world-of-sports-2026.html](https://willpowerworldofsports.netlify.app/world-of-sports-2026.html)

---

## What's in this repo

| File / Folder | Description |
|---|---|
| `world-of-sports-2026.html` | The full sponsorship deck — one self-contained file (HTML + inline CSS + JS) |
| `cota-bg.jpg` | Blurred COTA track photo used as the site-wide background |
| `WH Thumbnails/` | Event photos, podium/tier images, textures |
| `Educational Content Path/assets/logos/` | Local brand logos used in the deck (e.g. `aescape.png`) |

> **Note:** most partner logos load from Willpower's logo database over Cloudinary
> (`willpowerhq.com/data/logos.json`), so they work anywhere. A handful of logos and
> the `cota-bg.jpg` background are local files — they must stay in the repo for the
> deck to display correctly.

---

## Deck pages

Navigate with the on-screen dots, the ◄ / ► buttons, or the arrow keys. Nine slides, in order:

1. **Overview** — Hero, key stats (attendees, brand revenue, venue)
2. **Our Network** — Auto-scrolling wall of partner brand logos
3. **New for 2026** — Marquee "podium" moments (Tom Brady × Aescape, Longevity Lounge, CPG Market, F1 Paddock Club)
4. **The Audience** — Who's in the room: value channels, titles, segments
5. **Why We're Here** — The three partnership pillars
6. **Itinerary** — Full run-of-day schedule + activations
7. **Sponsorship** — Four tiers: Title, Platinum, Gold, Silver
8. **Past Events** — Track record, laid out as a race circuit
9. **Partner** — Call to action + contact

---

## Preview locally

The deck loads local images, so serve it over a local web server (don't just double-click the file):

```bash
cd "path/to/repo"
python3 -m http.server 8080
# visit http://localhost:8080/world-of-sports-2026.html
```

---

## Making changes & deploying

Edit `world-of-sports-2026.html` (or have Claude Code do it), then commit and push —
Netlify auto-deploys from `main` within ~30 seconds.

```bash
git add world-of-sports-2026.html cota-bg.jpg "WH Thumbnails" "Educational Content Path"
git commit -m "describe your change"
git push
```

> ⚠️ **Do not commit the large video files.** The working folder contains multi-GB
> `.mov` recordings (e.g. `Full panel.mov`) that must never be pushed — they exceed
> GitHub/Netlify limits and will break deploys. Add them to `.gitignore`:
>
> ```gitignore
> # Large media — do not deploy
> *.mov
> *.band
> *.zip
> ```
>
> Commit only the deck and its image assets (the folders listed above).

---

## Editing with Claude Code

The fastest way to update the deck is with **Claude Code** — describe the change in
plain English and it edits `world-of-sports-2026.html` for you.

1. Install Claude Code: [claude.ai/code](https://claude.ai/code)
2. Clone and open the repo:
   ```bash
   git clone https://github.com/events-willpower/willpowerworldofsports.git
   cd willpowerworldofsports
   ```
3. Ask for changes, e.g.:
   - *"Change the Overview headline to..."*
   - *"Add a brand to the logo wall on page 2"*
   - *"Update the Platinum tier pricing on the Sponsorship page"*
4. Commit and push (see above). The live site updates automatically.

---

## Adding collaborators

- **GitHub:** Settings → Collaborators → Add people
- **Netlify:** [app.netlify.com/projects/willpowerworldofsports](https://app.netlify.com/projects/willpowerworldofsports) → Team → Members

---

## Contact

[events@drinkwillpower.com](mailto:events@drinkwillpower.com)
