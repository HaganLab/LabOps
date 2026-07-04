# How to Share Something Here

This folder is a template. To share a slide deck, notes, a Word doc, an HTML file, or anything else with the lab:

1. **Copy this `TEMPLATE` folder** into `Blog/` and rename your copy to something short and unique (e.g. `Blog/jane-hpc-tips/`). Folder names should be lowercase with hyphens, no spaces.
2. **Drop your file into that folder** — any format is fine (`.pptx`, `.docx`, `.pdf`, `.md`, `.html`, whatever you have).
3. **Edit `metadata.json`** in your folder:
   - `contributor` — your name
   - `title` — a short, descriptive title
   - `date` — `YYYY-MM-DD`, used to sort and group entries by month
   - `description` — one or two sentences on what it is
   - `format` — optional; a short tag like `slides`, `notes`, or `doc`. Delete this line entirely if you don't want one.
   - `file` — the exact filename of the file you dropped in step 2
4. **Commit and push** (or open a PR). The [Blog page](../../Blog.html) updates automatically within a week via a scheduled GitHub Action — no need to touch any other files.

See `Blog/example-submission/` for a filled-in example.
