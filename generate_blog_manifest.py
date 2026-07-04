import json
import os

# Scans Blog/<submission>/metadata.json (flat, one level, skipping TEMPLATE)
# and regenerates blog-manifest.json, which Blog.Rmd fetches client-side at
# page-load time to render the list. No R/pandoc re-render needed here --
# this only touches the manifest, so this script has zero non-stdlib deps.

BLOG_DIR = "Blog"
OUT = "blog-manifest.json"
REQUIRED_FIELDS = ["contributor", "title", "date", "description", "file"]
PLACEHOLDER_FORMAT = "e.g. slides, notes, doc (optional -- delete this field if you don't want one)"


def load_submissions():
    entries = []
    if not os.path.isdir(BLOG_DIR):
        return entries

    for name in sorted(os.listdir(BLOG_DIR)):
        folder = os.path.join(BLOG_DIR, name)
        if name == "TEMPLATE" or not os.path.isdir(folder):
            continue

        meta_path = os.path.join(folder, "metadata.json")
        if not os.path.isfile(meta_path):
            print(f"Skipping {folder}: no metadata.json found.")
            continue

        try:
            with open(meta_path) as f:
                meta = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Skipping {folder}: metadata.json is not valid JSON ({e}).")
            continue

        missing = [field for field in REQUIRED_FIELDS if not meta.get(field)]
        if missing:
            print(f"Skipping {folder}: missing required field(s) {missing}.")
            continue

        content_path = os.path.join(folder, meta["file"])
        if not os.path.isfile(content_path):
            print(f"Skipping {folder}: file '{meta['file']}' referenced in metadata.json not found.")
            continue

        entry = {
            "contributor": meta["contributor"],
            "title": meta["title"],
            "date": meta["date"],
            "description": meta["description"],
            "folder": name,
            "file": meta["file"],
        }
        format_tag = meta.get("format", "").strip()
        if format_tag and format_tag != PLACEHOLDER_FORMAT:
            entry["format"] = format_tag

        entries.append(entry)

    entries.sort(key=lambda e: e["date"], reverse=True)
    return entries


def main():
    entries = load_submissions()
    with open(OUT, "w") as f:
        json.dump(entries, f, indent=2)
        f.write("\n")
    print(f"{OUT} written with {len(entries)} entr{'y' if len(entries) == 1 else 'ies'}.")


if __name__ == "__main__":
    main()
