#!/usr/bin/env python3
"""Export a WoS slide-deck HTML page to a PDF, one page per slide.

Usage:
  make_deck_pdf.py <src_html> <serve_root> <base_url> <n_pages> <out_pdf>

Creates a temp copy of the deck (same dir, so relative assets resolve) with an
injected helper that freezes animations and jumps to ?exportpage=N, then
screenshots each slide with headless Chrome and assembles a 16:9 PDF
(921.6 x 518.4 pt). Needs: Google Chrome, pip install pillow img2pdf.

RERUN THIS whenever a deck's content changes, or the committed PDF goes stale
(it happened once: tier pricing shipped after the first brands export).

    cd <this repo> && python3 -m http.server 8123 &
    python3 tools/make_deck_pdf.py world-of-sports-2026.html . \
        http://localhost:8123 9 World-of-Sports-Sponsorship-2026.pdf
    python3 tools/make_deck_pdf.py world-of-sports-2026-brands.html . \
        http://localhost:8123 9 World-of-Sports-Brand-Partnerships-2026.pdf
    python3 tools/make_deck_pdf.py willpower-events-2026.html . \
        http://localhost:8123 11 Willpower-Events-2026.pdf

The COTA proposal lives in the site repo (billpower21/willpowerbrands-website,
events/world-of-sports-cota.html, 10 pages) — serve that repo's root and write
events/World-of-Sports-COTA-2026.pdf.

Page count = number of .page slides (grep -o 'class="page[\" ]' file | wc -l).
Screenshots land in shots-<deck>/ next to this script (gitignored scratch);
check contact-sheet.jpg before committing the PDF.
"""
import pathlib
import subprocess
import sys
import io

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

HELPER = """
<style id="__export-freeze">
  *, *::before, *::after {
    transition: none !important;
    animation-duration: 0.001s !important;
    animation-delay: 0s !important;
    caret-color: transparent !important;
  }
  html { scroll-behavior: auto !important; }
</style>
<script>
(function(){
  var m = location.search.match(/exportpage=(\\d+)/);
  var n = m ? parseInt(m[1], 10) : 0;
  window.addEventListener('load', function(){
    setTimeout(function(){
      try { goTo(n); } catch(e) {}
      window.scrollTo(0, 0);
    }, 700);
  });
})();
</script>
"""


def main():
    src, serve_root, base_url, n_pages, out_pdf = sys.argv[1:6]
    src = pathlib.Path(src).resolve()
    n_pages = int(n_pages)
    out_pdf = pathlib.Path(out_pdf)
    tmp_html = src.with_name(".export-tmp-" + src.name)
    scratch = pathlib.Path(__file__).parent / ("shots-" + src.stem)
    scratch.mkdir(parents=True, exist_ok=True)

    html = src.read_text()
    assert "</body>" in html
    tmp_html.write_text(html.replace("</body>", HELPER + "</body>", 1))

    rel = tmp_html.relative_to(pathlib.Path(serve_root).resolve()).as_posix()
    pngs = []
    try:
        for i in range(n_pages):
            png = scratch / f"page{i:02d}.png"
            url = f"{base_url}/{rel}?exportpage={i}"
            subprocess.run(
                [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                 "--window-size=1600,900", "--force-device-scale-factor=2",
                 "--virtual-time-budget=12000", f"--screenshot={png}", url],
                check=True, capture_output=True, timeout=120)
            pngs.append(png)
            print(f"  page {i + 1}/{n_pages} captured", flush=True)
    finally:
        tmp_html.unlink(missing_ok=True)

    from PIL import Image
    import img2pdf
    jpegs = []
    for png in pngs:
        im = Image.open(png).convert("RGB")
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=80, optimize=True)
        jpegs.append(buf.getvalue())
    layout = img2pdf.get_fixed_dpi_layout_fun((250, 250))  # 3200px / 12.8in
    out_pdf.write_bytes(img2pdf.convert(jpegs, layout_fun=layout))
    print(f"WROTE {out_pdf} ({out_pdf.stat().st_size // 1024} KB, {n_pages} pages)")

    # contact sheet for QA (<=1200px wide, safe to Read)
    cols, thumb_w = 3, 380
    rows = (n_pages + cols - 1) // cols
    thumb_h = int(thumb_w * 9 / 16)
    sheet = Image.new("RGB", (cols * thumb_w + 8 * (cols + 1),
                              rows * thumb_h + 8 * (rows + 1)), "#222")
    for idx, png in enumerate(pngs):
        im = Image.open(png).convert("RGB").resize((thumb_w, thumb_h))
        r, c = divmod(idx, cols)
        sheet.paste(im, (8 + c * (thumb_w + 8), 8 + r * (thumb_h + 8)))
    sheet_path = scratch / "contact-sheet.jpg"
    sheet.save(sheet_path, "JPEG", quality=85)
    print(f"SHEET {sheet_path}")


if __name__ == "__main__":
    main()
