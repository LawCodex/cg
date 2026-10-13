#!/usr/bin/env python3
"""Republic of the Congo: Constitution of 25 October 2015 (as amended by loi constitutionnelle n° 2-2022 of
7 January 2022), from the "Constitution en vigueur" page of the Secrétariat général du Gouvernement (sgg.cg).
Only this single page is fetched: the SGG website's legal notice prohibits reproduction of its content without
authorisation, so the Journal officiel and the consolidated codes it hosts are not crawled.
Usage: python3 cg_fetch.py [--no-download]"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cg_text as T  # noqa

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(os.path.dirname(REPO), "_raw", "cg")
RETRIEVED = os.environ.get("LC_RETRIEVED", "2026-10-13")
URL = "https://sgg.cg/droit-congolais/constitution.html"


def main():
    dest = os.path.join(RAW, "constitution.html")
    if "--no-download" not in sys.argv:
        T.fetch(URL, dest, delay=3)
    lines = T.html_lines(dest, "//div[@class='wysiwyg']")
    st = next(i for i, x in enumerate(lines) if x == "Préambule")
    head, lines = lines[:st], lines[st:]
    # "Titre 1 - ..." -> "TITRE 1 - ..." so that the structurer sees the division
    lines = [re.sub(r"^(Titre|Chapitre|Section|Sous-section)\s+(\d+|premier|unique)\b", lambda m: m.group(1).upper() + " " + m.group(2), x)
             for x in lines]
    out = []
    for x in lines:
        out += [x, ""]
    body = [y for h in head for y in ("*" + h + "*", "")] + ["## Préambule", ""] + T.structure(out[2:], "fr")
    meta = {"title": "Constitution de la République du Congo",
            "identifier": "Constitution du 25 octobre 2015, modifiée par la loi constitutionnelle n° 2-2022 du 7 janvier 2022",
            "type": "constitution", "jurisdiction": "cg", "language": "fr", "date": "2015-10-25",
            "last_amended": "2022-01-07", "status": "in_force", "source": URL,
            "gazette": "Journal officiel de la République du Congo, édition spéciale n° 8 du 6 novembre 2015; JO 2022 édition spéciale n° 1",
            "retrieved": RETRIEVED,
            "note": "Text as published (consolidated) by the Secrétariat général du Gouvernement"}
    T.write_md(os.path.join(REPO, "constitution", "constitution.md"), meta, meta["title"], body)
    print("OK", sum(1 for x in body if x.startswith("#")), "headings")


if __name__ == "__main__":
    main()
