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
    "teams-mens.html": {
        "title": "Men's Teams",
        "desc": "LCC men's cricket — Saturday Championship, Challenge League and Friday Masters League.",
        "eyebrow": "Teams",
        "banner_title": "Men&rsquo;s Teams",
        "banner_sub": "Saturday Championship &middot; Challenge League &middot; Friday Masters",
        "bodyclass": "teams-mens",
    },
    "teams-womens.html": {
        "title": "Women's Teams",
        "desc": "Women's cricket at Lamma Cricket Club — history, achievements and how to get involved.",
        "eyebrow": "Teams",
        "banner_title": "Women&rsquo;s Teams",
        "banner_sub": "A proud history of women&rsquo;s cricket at LCC",
        "bodyclass": "teams-womens",
    },
    "teams-kids.html": {
        "title": "Kids & Youth",
        "desc": "Youth and junior cricket at Lamma Cricket Club — introducing the next generation to the game.",
        "eyebrow": "Teams",
        "banner_title": "Kids &amp; Youth",
        "banner_sub": "Growing cricket on Lamma for the next generation",
        "bodyclass": "teams-kids",
    },
    "saturday-championship.html": {
        "title": "Saturday Championship",
        "desc": "LCC Saturday Championship side — fixtures, results, standings and leaderboards.",
        "eyebrow": "Leagues",
        "banner_title": "Saturday Championship",
        "banner_sub": "Cricket Hong Kong &amp; Division 2",
        "bodyclass": "saturday-championship",
    },
    "challenge-league.html": {
        "title": "Challenge League",
        "desc": "LCC Challenge League side — fixtures, results, standings and leaderboards.",
        "eyebrow": "Leagues",
        "banner_title": "Challenge League",
        "banner_sub": "Cricket Hong Kong &amp; Division 1",
        "bodyclass": "challenge-league",
    },
    "friday-masters-league.html": {
        "title": "Friday Masters League",
        "desc": "LCC Friday Masters League — fixtures, results, standings, leaderboards and match reports.",
        "eyebrow": "Leagues",
        "banner_title": "Friday Masters League",
        "banner_sub": "Cricket Hong Kong",
        "bodyclass": "friday-masters-league",
    },
    "archive.html": {
        "title": "Archive",
        "desc": "Historical records, past seasons, match reports, tours and events from Lamma Cricket Club.",
        "eyebrow": "Lamma Cricket Club",
        "banner_title": "Archive",
        "banner_sub": "Past seasons, reports, tours &amp; events",
        "bodyclass": "archive",
    },
    "social-events--tours.html": {
        "title": "Social Events & Tours",
        "desc": "From beach cricket tournaments to black-tie balls — LCC's social calendar and tour reports.",
        "eyebrow": "Lamma Cricket Club",
        "banner_title": "Social Events &amp; Tours",
        "banner_sub": "From beach cricket to black-tie balls",
        "bodyclass": "social-events-tours",
    },
    "lcc-merchandise.html": {
        "title": "Merchandise",
        "desc": "Order official Lamma Cricket Club playing kit, headwear and merchandise.",
        "eyebrow": "Club Shop",
        "banner_title": "LCC Merchandise",
        "banner_sub": "Official playing kit &amp; club gear",
        "bodyclass": "lcc-merchandise",
    },
    "club-records.html": {
        "title": "Club Records",
        "desc": "Lamma Cricket Club honours board — members, champions, records, tours and obituaries.",
        "eyebrow": "Lamma Cricket Club",
        "banner_title": "Club Records",
        "banner_sub": "Members, champions, records &amp; tours",
        "bodyclass": "club-records",
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
