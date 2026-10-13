# Republic of the Congo (CG) — législation en Markdown

Part of [LawCodex](https://github.com/LawCodex): the legislation of every country as plain Markdown in git.

**Minimal repository: the Constitution of the Republic of the Congo** (in French, the official language).

Retrieved 2026-10-13.

<!-- COUNTS -->
| Directory | Files |
|---|---|
| `constitution/` | 1 |
| **Total** | **1** |
<!-- /COUNTS -->

## Contents

```
constitution/constitution.md   Constitution of 25 October 2015 (adopted by referendum), as amended by
                               loi constitutionnelle n° 2-2022 of 7 January 2022 (revision of article 157)
```

## Source

| Document | URL |
|---|---|
| Constitution en vigueur — Secrétariat général du Gouvernement (SGG), "Droit congolais" | https://sgg.cg/droit-congolais/constitution.html |

The SGG page gives the consolidated text in HTML and links to the Journal officiel special issues (JO 2015 édition
spéciale n° 8 of 6 November 2015; JO 2022 édition spéciale n° 1).

## Not covered / known gaps — why this repository is minimal

* The SGG website (https://sgg.cg) is the official source of Congolese law: it hosts the Journal officiel (PDF
  issues since 1958), consolidated codes ("Codes en vigueur": labour, family, criminal procedure, mining,
  hydrocarbons, forestry, public procurement...) and earlier constitutions. However, its **legal notice prohibits
  any total or partial reproduction of the site or its content ("textes") without the prior and express
  authorisation of the Secrétariat général du Gouvernement**. In accordance with LawCodex rules, the site was not
  crawled: only the Constitution page (an official text of constitutional value) was retrieved.
  Bulk publication of the codes and laws would need the SGG's consent (contact: infos@sgg.cg).
* The Presidency website (presidence.cg) also offers the Constitution (a print of a third-party web page) but its
  terms likewise forbid reproduction. The Constitutional Court website (cour-constitutionnelle.cg) loads its
  documents with JavaScript only. The National Assembly website had no legislation.
* No laws, ordinances, decrees or codes are included.

## Copyright

The Constitution is an official text of the Republic of the Congo; official texts of a legislative nature are
excluded from copyright protection (OAPI Bangui Agreement, Annex VII). The Markdown conversion is provided as is;
the authoritative text is the one published in the *Journal officiel de la République du Congo*.

## Regenerating

```sh
python3 scripts/cg_fetch.py    # downloads the SGG page to ../_raw/cg/ and writes the Markdown
python3 scripts/cg_readme.py   # updates the counts table
```
