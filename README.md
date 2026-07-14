# Willpower — The World of Sports Summit (F1 Austin GP 2026)

Sponsorship deck for **The World of Sports Summit** by Willpower, held during the
Formula 1 United States Grand Prix in Austin, TX (COTA) — **October 22, 2026**.

The entire deck is a **single self-contained HTML file** — `world-of-sports-2026.html` —
with all CSS and JavaScript inlined. No build step, no dependencies.

**Current live version (draft):**
[6a56581979f0ad41d0d209d8--willpowerworldofsports.netlify.app/world-of-sports-2026.html](https://6a56581979f0ad41d0d209d8--willpowerworldofsports.netlify.app/world-of-sports-2026.html)

> ⚠️ The main URL (`willpowerworldofsports.netlify.app`) is **not** current — the
> account's Netlify auto-deploy is paused by a billing cap ("credit usage exceeded").
> Until that's cleared in the Netlify dashboard, share the **draft link** above, which
> is redeployed on every change.

---

## What's in this repo

| File / Folder | Description |
|---|---|
| `world-of-sports-2026.html` | The full deck — one file (HTML + inline CSS + JS) |
| `cota-bg.jpg` | Blurred COTA track photo used as the site-wide background |
| `WH Thumbnails/` | Event photos, podium/tier images, textures |
| `Educational Content Path/assets/logos/` | Local brand logos (e.g. `aescape.png`, `hyrox.png`) |

> Most partner logos load from Willpower's logo database over Cloudinary
> (`willpowerhq.com/data/logos.json`), so they work anywhere. A handful of logos and
> the `cota-bg.jpg` background are local files that must stay in the repo.

---

## The deck (9 pages)

1. **Overview** — Hero, key stats (attendees, brand revenue, venue)
2. **Our Network** — Auto-scrolling wall of partner brand logos
3. **New for 2026** — Marquee moments (Tom Brady × Aescape, Longevity Lounge, CPG Market, F1 Paddock Club)
4. **The Audience** — Who's in the room: value channels, titles, segments
5. **Why We're Here** — The three partnership pillars
6. **Itinerary** — Full run-of-day schedule + activations
7. **Sponsorship** — Four tiers: Title, Platinum, Gold, Silver
8. **Past Events** — Track record, laid out as a race circuit
9. **Partner** — Call to action + contact

### How it navigates

- **Desktop:** a paginated slide deck — use the dots, the ◄ / ► buttons, or the arrow keys.
- **Mobile (≤ 760px):** the deck flattens into a single continuous **vertical scroll**
  (no footer), so it reads naturally on a phone.

The **brand wall** (page 2) renders two ways from the same content: a 6-column layout on
desktop and a dedicated 3-column layout on phones (so the columns never wrap into two rows
and leave a gap across the middle).

---

## Preview locally

The deck loads local images, so serve it over a web server (don't just double-click it):

```bash
cd "path/to/repo"
python3 -m http.server 8080
# visit http://localhost:8080/world-of-sports-2026.html
```

---

## Making changes & deploying

Edit `world-of-sports-2026.html` (or have Claude Code do it), then commit and push.

```bash
git add world-of-sports-2026.html cota-bg.jpg "WH Thumbnails" "Educational Content Path"
git commit -m "describe your change"
git push
```

Netlify is configured to auto-deploy from `main` — **but that is currently blocked by the
billing cap.** Once billing is restored, pushes will publish automatically to the main URL.
In the meantime, deploy a draft from a clean folder (the working folder contains multi-GB
video files that must never be uploaded):

```bash
# copy only the deck + assets into a clean dir, then:
netlify deploy --dir=/path/to/clean-folder
# note the "Draft URL" it prints — that's the shareable link
```

> ⚠️ **Never commit or deploy the large media files.** The working folder contains multi-GB
> `.mov` recordings (e.g. `Full panel.mov`) that exceed GitHub/Netlify limits and will break
> deploys. Keep them out of commits:
>
> ```gitignore
> # Large media — do not deploy
> *.mov
> *.band
> *.zip
> ```

---

## Editing with Claude Code

The fastest way to update the deck is with **Claude Code** — describe the change in plain
English and it edits `world-of-sports-2026.html` for you.

1. Install Claude Code: [claude.ai/code](https://claude.ai/code)
2. Clone and open the repo:
   ```bash
   git clone https://github.com/events-willpower/willpowerworldofsports.git
   cd willpowerworldofsports
   ```
3. Ask for changes, e.g.:
   - *"Change the Overview headline to…"*
   - *"Add a brand to the logo wall on page 2"*
   - *"Update the Platinum tier pricing on the Sponsorship page"*
4. Commit and push (see above).

---

## Adding collaborators

- **GitHub:** Settings → Collaborators → Add people
- **Netlify:** [app.netlify.com/projects/willpowerworldofsports](https://app.netlify.com/projects/willpowerworldofsports) → Team → Members

---

## Contact

[events@drinkwillpower.com](mailto:events@drinkwillpower.com)
