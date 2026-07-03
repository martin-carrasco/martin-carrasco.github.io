"""Convert _bibliography/papers.bib to _data/publications.json.

Usage:
    python3 scripts/bibtex_to_json.py

Outputs _data/publications.json consumed by the Jekyll minimal layout.
Adapted from the AIDOS lab website pipeline (aidos-lab.github.io).

Dependencies:
    pip install bibtexparser nameparser

author+an annotation conventions
---------------------------------
  equal / first  ->  co-first / equal contribution  (rendered as *)
  last           ->  senior / co-last author         (rendered as +)
  highlight      ->  bold (non-owner; ignored here — owner is auto-detected)
"""

import json
import re
import sys
from pathlib import Path

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import author, convert_to_unicode
from nameparser import HumanName

REPO_ROOT = Path(__file__).parent.parent
BIB_FILE = REPO_ROOT / "_bibliography" / "papers.bib"
OUT_FILE = REPO_ROOT / "_data" / "publications.json"

OWNER_LAST = "Carrasco"
OWNER_FIRST = ("Martin", "M.")

# co-first / equal marker
MARK_EQUAL = "<sup>✱</sup>"
# senior / last-author marker
MARK_LAST = "<sup>†</sup>"

# Comprehensive LaTeX accent -> Unicode mapping.
# Handles both \'x (brace-free) and \'{x} (braced) forms.
LATEX_ACCENTS = {
    # acute
    "'a": "á", "'e": "é", "'i": "í", "'o": "ó", "'u": "ú",
    "'y": "ý", "'A": "Á", "'E": "É", "'I": "Í", "'O": "Ó",
    "'U": "Ú", "'Y": "Ý", "'c": "ć", "'s": "ś", "'z": "ź",
    "'n": "ń", "'C": "Ć", "'S": "Ś", "'Z": "Ź", "'N": "Ń",
    # grave
    "`a": "à", "`e": "è", "`i": "ì", "`o": "ò", "`u": "ù",
    "`A": "À", "`E": "È", "`I": "Ì", "`O": "Ò", "`U": "Ù",
    # umlaut / diaeresis
    '"a': "ä", '"e': "ë", '"i': "ï", '"o': "ö", '"u': "ü",
    '"A': "Ä", '"E': "Ë", '"I': "Ï", '"O': "Ö", '"U': "Ü",
    # circumflex
    "^a": "â", "^e": "ê", "^i": "î", "^o": "ô", "^u": "û",
    "^A": "Â", "^E": "Ê", "^I": "Î", "^O": "Ô", "^U": "Û",
    # tilde
    "~a": "ã", "~n": "ñ", "~o": "õ",
    "~A": "Ã", "~N": "Ñ", "~O": "Õ",
    # cedilla
    "c{c}": "ç", "c{C}": "Ç", "cc": "ç", "cC": "Ç",
    # caron
    "v{c}": "č", "v{s}": "š", "v{z}": "ž",
    "v{C}": "Č", "v{S}": "Š", "v{Z}": "Ž",
    # ligatures / special
    "ae": "æ", "AE": "Æ", "oe": "œ", "OE": "Œ",
    "ss": "ß", "l": "ł", "L": "Ł",
    "o": "ø", "O": "Ø",
}


def _fix_latex_accents(text: str) -> str:
    """Replace LaTeX accent sequences with Unicode characters."""
    def replace_braced(m):
        cmd, content = m.group(1), m.group(2)
        key = cmd + content
        if key in LATEX_ACCENTS:
            return LATEX_ACCENTS[key]
        if content and (cmd + content[0]) in LATEX_ACCENTS:
            return LATEX_ACCENTS[cmd + content[0]] + content[1:]
        return m.group(0)

    text = re.sub(r"\\(['\"`^~])\{([^}]+)\}", replace_braced, text)

    def replace_bare(m):
        key = m.group(1) + m.group(2)
        return LATEX_ACCENTS.get(key, m.group(0))

    text = re.sub(r"\\(['\"`^~])([a-zA-Z])", replace_bare, text)

    def replace_named(m):
        return LATEX_ACCENTS.get(m.group(1), m.group(0))

    text = re.sub(r"\\(ae|AE|oe|OE|ss|[lLoO])\b", replace_named, text)
    text = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", text)
    text = re.sub(r"[{}]", "", text)
    text = text.replace("---", "—").replace("--", "–")
    text = text.replace("``", "“").replace("''", "”")
    text = text.replace("~", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def customizations(record):
    record = convert_to_unicode(record)
    record = author(record)
    return record


def _initial(name: str, pad: str = "") -> str:
    return pad + name[0] + "." if name else ""


def parse_annotations(raw: str) -> dict:
    result = {}
    if not raw:
        return result
    for part in raw.split(";"):
        part = part.strip()
        if "=" not in part:
            continue
        idx_str, cmds_str = part.split("=", 1)
        idx = int(idx_str.strip()) - 1
        result[idx] = [c.strip() for c in cmds_str.split(",")]
    return result


def format_authors(authors: list, annotations_raw: str) -> str:
    """Return HTML string.

    Markers:
      MARK_EQUAL  equal / co-first authorship  (author+an: equal or first)
      MARK_LAST   senior / co-last authorship   (author+an: last)
    Site owner is wrapped in <strong>.
    """
    annotations = parse_annotations(annotations_raw)
    parts = []

    for i, auth in enumerate(authors):
        auth_clean = _fix_latex_accents(auth)
        name_parts = auth_clean.split(",")
        name_str = " ".join(n.strip() for n in reversed(name_parts))
        name = HumanName(name_str)

        first = _initial(name.first) + (_initial(name.middle, " ") if name.middle else "")
        last = _fix_latex_accents(name.last)
        display = f"{first}&nbsp;{last}" if first else last

        cmds = annotations.get(i, [])
        is_self = (last == OWNER_LAST and
                   (name.first in OWNER_FIRST or _initial(name.first) in OWNER_FIRST))

        if is_self:
            display = f"<strong>{display}</strong>"
        if "equal" in cmds or "first" in cmds:
            display += MARK_EQUAL
        if "last" in cmds:
            display += MARK_LAST

        parts.append(display)

    if len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        return f"{parts[0]} and {parts[1]}"
    else:
        return ", ".join(parts[:-1]) + ", and " + parts[-1]


def get_venue(paper: dict) -> str:
    entry_type = paper.get("ENTRYTYPE", "")
    if entry_type == "article":
        journal = _fix_latex_accents(paper.get("journal", ""))
        if re.search(r"arxiv", journal, re.IGNORECASE) or journal == "Preprint":
            return "Preprint"
        return journal
    elif entry_type in ("inproceedings", "incollection"):
        return _fix_latex_accents(paper.get("booktitle", ""))
    elif entry_type == "misc":
        hw = _fix_latex_accents(paper.get("howpublished", ""))
        return hw.strip("{} ")
    elif entry_type in ("mastersthesis", "phdthesis"):
        degree = "M.Sc." if entry_type == "mastersthesis" else "Ph.D."
        return f"{degree} thesis, {paper.get('school', '')}"
    return ""


def to_json(paper: dict, order: int) -> dict | None:
    title = _fix_latex_accents(paper.get("title", "")).replace("\n", " ")
    authors_raw = paper.get("author", [])
    if not authors_raw:
        return None

    authors_display = format_authors(authors_raw, paper.get("author+an", ""))
    venue = get_venue(paper)
    year = paper.get("year", "")
    url = paper.get("url", "") or ""
    code = paper.get("code", "") or ""
    preview = paper.get("preview", "") or ""
    poster = paper.get("poster", "") or ""
    tldr = _fix_latex_accents(paper.get("tldr", "") or "").strip()
    keywords = [k.strip() for k in paper.get("keywords", "").split(",") if k.strip()]

    result = {
        "id": paper["ID"],
        "title": title,
        "authors_display": authors_display,
        "venue": venue,
        "year": year,
        "order": order,
        "keywords": keywords,
    }
    if url:
        result["url"] = url
    if code:
        result["code"] = code
    if preview:
        result["preview"] = preview
    if poster:
        result["poster"] = poster
    if tldr:
        result["tldr"] = tldr

    return result


def main():
    if not BIB_FILE.exists():
        print(f"Error: {BIB_FILE} not found", file=sys.stderr)
        sys.exit(1)

    parser = BibTexParser(common_strings=True, customization=customizations)
    with open(BIB_FILE) as f:
        db = bibtexparser.load(f, parser=parser)

    papers = list(reversed(db.entries))
    data = []
    for i, paper in enumerate(papers):
        if "author" not in paper:
            continue
        result = to_json(paper, i)
        if result is not None:
            data.append(result)

    OUT_FILE.parent.mkdir(exist_ok=True)
    with open(OUT_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Wrote {len(data)} publications to {OUT_FILE}")


if __name__ == "__main__":
    main()
