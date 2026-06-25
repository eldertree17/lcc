#!/usr/bin/env python3
"""Assemble Lamma Cricket Club pages from shared partials + per-page body.

Run from anywhere:  python3 build/build.py
Outputs static HTML to the repository root.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PARTIALS = ROOT / "build" / "partials"
PAGES = ROOT / "build" / "pages"

HEAD = (PARTIALS / "head.html").read_text()
HEADER = (PARTIALS / "header.html").read_text()
FOOTER = (PARTIALS / "footer.html").read_text()

# slug -> banner/meta config
PAGES_CONFIG = {
    "index.html": {
        "title": "Home",
        "desc": "Lamma Cricket Club — competitive and social cricket on Lamma Island, Hong Kong, since 1990.",
        "eyebrow": "Lamma Cricket Club",
        "banner_title": "Lamma Cricket Club",
        "banner_sub": "Solidarity · Sustainability · Pride",
        "bodyclass": "index",
    },
    "our-constitution.html": {
        "title": "Our Constitution",
        "desc": "The rules and values of Lamma Cricket Club — membership, governance, discipline and more.",
        "eyebrow": "Lamma Cricket Club",
        "banner_title": "Our Constitution",
        "banner_sub": "Solidarity · Sustainability · Pride",
        "bodyclass": "our-constitution",
    },
    "for-the-record.html": {
        "title": "For the Record",
        "desc": "Lamma Cricket Club honours board — members, champions, club records and tours.",
        "eyebrow": "Lamma Cricket Club",
        "banner_title": "For the Record",
        "banner_sub": "Members, champions, records & tours",
        "bodyclass": "for-the-record",
    },
    "the-executive-committee.html": {
        "title": "The Executive Committee",
        "desc": "Meet the elected Executive Committee of Lamma Cricket Club and their roles & responsibilities.",
        "eyebrow": "Lamma Cricket Club",
        "banner_title": "The Executive Committee",
        "banner_sub": "The people who keep the Club running",
        "bodyclass": "the-executive-committee",
    },
    "club-history.html": {
        "title": "Club History",
        "desc": "From a disused helipad to League Champions — the story of Lamma Cricket Club since 1990.",
        "eyebrow": "Lamma Cricket Club",
        "banner_title": "Club History",
        "banner_sub": "From a disused helipad to League Champions",
        "bodyclass": "club-history",
    },
}


def render(slug, cfg):
    body = (PAGES / slug).read_text()

    head = (HEAD
            .replace("{{TITLE}}", cfg["title"])
            .replace("{{DESC}}", cfg["desc"])
            .replace("{{SLUG}}", slug)
            .replace("{{BODYCLASS}}", cfg["bodyclass"]))

    header = (HEADER
              .replace("{{EYEBROW}}", cfg["eyebrow"])
              .replace("{{TITLE}}", cfg["banner_title"])
              .replace("{{SUB}}", cfg["banner_sub"]))

    return head + header + body + FOOTER


def main():
    for slug, cfg in PAGES_CONFIG.items():
        html = render(slug, cfg)
        (ROOT / slug).write_text(html)
        print(f"  built {slug} ({len(html):,} bytes)")


if __name__ == "__main__":
    print("Building Lamma Cricket Club pages…")
    main()
    print("Done.")
