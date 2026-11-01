"""Compact re-runnable showcase parity check (stdlib only).

Extracts and compares actual release facts and link targets across trilingual
docs sets (RU vs UK vs EN) and all active README language versions:
  - Six required README editions: EN, UK, RU, ES, PT-BR, ZH-CN
  - Three required docs locales: RU (docs/), UK (docs/uk/), EN (docs/en/)
  - FirstInstall versions and download links
  - Release tag URLs
  - SHA-256 installer checksums (cross-locale parity & intra-file consistency)
  - Installer byte sizes (normalized digits, supporting local notations and '字节')
  - Language switcher mutual links and active language highlighting
  - HTML data-status counts, DOM IDs, lang / hreflang / canonical tags
  - Compact release label dynamically matching the active release tag and alpha status
  - Relative links and anchor validity
  - Prohibition of '/releases/latest' in link targets

Usage: python tools/check_bilingual.py [repo_root]
Exit 0 = no errors. Prints ERROR/WARN lines and summary.
"""
import re
import sys
import pathlib
import unicodedata
from urllib.parse import urlsplit, unquote

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

README_LANGS = [
    ("README.md", "English"),
    ("README.uk.md", "Українська"),
    ("README.ru.md", "Русский"),
    ("README.es.md", "Español"),
    ("README.pt-BR.md", "Português (Brasil)"),
    ("README.zh-CN.md", "简体中文"),
]

DOC_TRIPLETS = [
    ("docs/index.html", "docs/uk/index.html", "docs/en/index.html"),
    ("docs/roadmap.md", "docs/uk/roadmap.md", "docs/en/roadmap.md"),
    ("docs/first-start.md", "docs/uk/first-start.md", "docs/en/first-start.md"),
]

# Keep DOC_PAIRS alias for compatibility if imported externally
DOC_PAIRS = [(ru, en) for ru, _uk, en in DOC_TRIPLETS] + [
    (ru, uk) for ru, uk, _en in DOC_TRIPLETS
]

BANNED_EN_CALQUES = [
    r"\bcontours?\b",
    r"\bposition care\b",
    r"\bclock proof\b",
    r"\barming\b",
]
CYR = re.compile(r"[\u0400-\u04FF]")
RU_ONLY_LETTERS = re.compile(r"[ъыэёЪЫЭЁ]")
errors, warns = [], []

existing_readmes = [p for p, _ in README_LANGS if (ROOT / p).exists()]
pending_readmes = [p for p, _ in README_LANGS if not (ROOT / p).exists()]
if pending_readmes:
    errors.append(f"Missing required README translations: {', '.join(pending_readmes)}")

missing_docs = [
    p for triplet in DOC_TRIPLETS for p in triplet if not (ROOT / p).exists()
]
if missing_docs:
    errors.append(f"Missing required docs files: {', '.join(missing_docs)}")


def text(p):
    return (ROOT / p).read_text(encoding="utf-8")


def slug(h):
    h = re.sub(r"[`*_\[\]()]", "", h.strip().lower())
    h = "".join(
        c
        for c in h
        if c.isalnum() or c in " -" or unicodedata.category(c).startswith("L")
    )
    return h.replace(" ", "-")


def anchors_md(p):
    out, seen = set(), {}
    for line in text(p).splitlines():
        m = re.match(r"^#{1,6}\s+(.*)", line)
        if m:
            s = slug(m.group(1))
            n = seen.get(s, 0)
            seen[s] = n + 1
            out.add(s if n == 0 else f"{s}-{n}")
    return out


def anchors_html(p):
    return set(re.findall(r'\bid="([^"]+)"', text(p)))


def links(p):
    t = text(p)
    if p.endswith(".md"):
        return re.findall(r"\]\(([^)\s]+)", t) + re.findall(r'(?:src|href)="([^"]+)"', t)
    return re.findall(r'(?:href|src)="([^"]+)"', t)


def extract_shas(t):
    return [h.lower() for h in re.findall(r"\b[a-fA-F0-9]{64}\b", t)]


def extract_first_install_versions(t):
    return re.findall(r"GoldenBreeze-FirstInstall-([0-9a-zA-Z.-]+)\.exe", t)


def extract_release_tags(t):
    return re.findall(r"/releases/tag/v?([0-9a-zA-Z.-]+)", t)


def extract_byte_sizes(t):
    raw_sizes = re.findall(
        r"(\d[\d\s\u00a0,.]*\d)\s*(?:байт\w*|bytes?|Б|B|字节)\b", t, re.IGNORECASE
    )
    cleaned = set()
    for s in raw_sizes:
        digits = re.sub(r"[\s\u00a0,.]", "", s)
        if len(digits) >= 6:  # only substantial file byte counts
            cleaned.add(digits)
    return cleaned


def extract_compact_label(t):
    m = re.search(r'<span class="header-release-btn__short"[^>]*>([^<]+)</span>', t)
    return m.group(1).strip() if m else None


def extract_active_release(t, fi_versions, release_tags):
    # Primary download link in hero / top CTA
    m = re.search(
        r'releases/download/v?([^/]+)/GoldenBreeze-FirstInstall-([0-9a-zA-Z.-]+)\.exe',
        t,
        re.IGNORECASE,
    )
    if m:
        return m.group(1)
    if fi_versions:
        # In single-release docs or sorted versions
        return fi_versions[0]
    if release_tags:
        return release_tags[0]
    return None


all_docs = sorted(
    set(existing_readmes)
    | {x for triplet in DOC_TRIPLETS for x in triplet if (ROOT / x).exists()}
    | {"docs/github-pages.md", "docs/CONTENT-MAINTENANCE.md"}
)

# 1. Structural link and anchor checks across all docs
for p in all_docs:
    base = (ROOT / p).parent
    for l in links(p):
        if "/releases/latest" in l:
            errors.append(f"{p}: forbidden '/releases/latest' link target {l}")
        u = urlsplit(l)
        if u.scheme or l.startswith("mailto:"):
            continue
        target = (base / unquote(u.path)).resolve() if u.path else (ROOT / p).resolve()
        if u.path:
            if not target.exists():
                errors.append(f"{p}: broken relative link {l}")
                continue
        if (
            p.startswith("docs/")
            and u.path
            and not str(target).startswith(str((ROOT / "docs").resolve()))
        ):
            warns.append(
                f"{p}: link leaves Pages root /docs (works on GitHub, 404 on Pages): {l}"
            )
        if u.fragment and target.is_file():
            rel = target.relative_to(ROOT).as_posix()
            ids = (
                anchors_html(rel)
                if rel.endswith(".html")
                else anchors_md(rel)
                if rel.endswith(".md")
                else None
            )
            if ids is not None and u.fragment not in ids:
                errors.append(f"{p}: missing anchor #{u.fragment} in {rel}")

# 2. Language switcher and mutual links validation in existing READMEs
for p, my_lang in README_LANGS:
    if p not in existing_readmes:
        continue
    t = text(p)
    for target_p, lang_name in README_LANGS:
        if target_p == p:
            if f"<strong>{lang_name}</strong>" not in t and f"<b>{lang_name}</b>" not in t:
                errors.append(f"{p}: active language '{lang_name}' must be formatted with strong/b without link")
        else:
            if f'href="{target_p}"' not in t:
                errors.append(f"{p}: missing link to {target_p} ({lang_name})")

# 3. Dynamic fact parity across all active READMEs
if existing_readmes:
    ref_r = "README.md" if "README.md" in existing_readmes else existing_readmes[0]
    ref_t = text(ref_r)
    ref_shas = set(extract_shas(ref_t))
    ref_fi = set(extract_first_install_versions(ref_t))
    ref_tags = set(extract_release_tags(ref_t))
    ref_bytes = extract_byte_sizes(ref_t)

    for r in existing_readmes:
        tr = text(r)
        r_shas = set(extract_shas(tr))
        if len(r_shas) > 1:
            errors.append(f"{r}: multiple conflicting SHA-256 checksums within file: {r_shas}")
        if r_shas != ref_shas:
            errors.append(f"SHA-256 mismatch between {r} ({r_shas}) and {ref_r} ({ref_shas})")

        r_fi = set(extract_first_install_versions(tr))
        if len(r_fi) > 1:
            errors.append(f"{r}: multiple conflicting FirstInstall versions: {r_fi}")
        if r_fi != ref_fi:
            errors.append(f"FirstInstall versions mismatch between {r} ({r_fi}) and {ref_r} ({ref_fi})")

        r_tags = set(extract_release_tags(tr))
        if r_tags != ref_tags:
            errors.append(f"Release tags mismatch between {r} ({r_tags}) and {ref_r} ({ref_tags})")

        r_bytes = extract_byte_sizes(tr)
        if r_bytes != ref_bytes:
            errors.append(f"Installer byte size mismatch between {r} ({r_bytes}) and {ref_r} ({ref_bytes})")

# 4. Dynamic fact parity and consistency across documentation triplets (RU vs UK vs EN)
for ru, uk, en in DOC_TRIPLETS:
    if not ((ROOT / ru).exists() and (ROOT / uk).exists() and (ROOT / en).exists()):
        continue
    tr, tu, te = text(ru), text(uk), text(en)
    locales = [(ru, tr, "ru"), (uk, tu, "uk"), (en, te, "en")]

    # --- SHA-256 Checksums ---
    shas_ru = extract_shas(tr)
    set_shas_ru = set(shas_ru)
    for loc_path, loc_text, _ in locales:
        set_shas = set(extract_shas(loc_text))
        if len(set_shas) > 1:
            errors.append(f"{loc_path}: multiple conflicting SHA-256 checksums within file: {set_shas}")
        if set_shas != set_shas_ru:
            errors.append(f"SHA-256 mismatch between {ru} ({set_shas_ru}) and {loc_path} ({set_shas})")

    # --- FirstInstall Versions & Tags ---
    fi_ru = extract_first_install_versions(tr)
    set_fi_ru = set(fi_ru)
    tags_ru = set(extract_release_tags(tr))
    bytes_ru = extract_byte_sizes(tr)

    for loc_path, loc_text, _ in locales:
        set_fi = set(extract_first_install_versions(loc_text))
        if not loc_path.endswith(".html") and len(set_fi) > 1:
            errors.append(f"{loc_path}: multiple conflicting FirstInstall versions: {set_fi}")
        if set_fi != set_fi_ru:
            errors.append(f"FirstInstall versions mismatch between {ru} ({set_fi_ru}) and {loc_path} ({set_fi})")

        tags_loc = set(extract_release_tags(loc_text))
        if tags_loc != tags_ru:
            errors.append(f"Release tags mismatch between {ru} ({tags_ru}) and {loc_path} ({tags_loc})")

        bytes_loc = extract_byte_sizes(loc_text)
        if bytes_loc != bytes_ru:
            errors.append(f"Installer byte size mismatch between {ru} ({bytes_ru}) and {loc_path} ({bytes_loc})")

    # --- English quality checks (as non-blocking WARN) ---
    te_prose = re.sub(r"<[^>]+>", " ", te) if en.endswith(".html") else te
    for pat in BANNED_EN_CALQUES:
        if re.search(pat, te_prose, flags=re.IGNORECASE):
            warns.append(f"{en}: literal calque/jargon warning matching {pat!r}")

    # --- Ukrainian quality check (Russian-only letters in UK docs) ---
    for i, line in enumerate(tu.splitlines(), 1):
        if (
            RU_ONLY_LETTERS.search(line)
            and 'lang="ru"' not in line
            and "Русск" not in line
        ):
            errors.append(f"{uk}:{i}: Russian-only letters [ъыэё] found in Ukrainian document")

    # --- HTML Structure & Metadata ---
    if ru.endswith(".html"):
        for st in ("released", "inprogress", "planned", "deferred"):
            c_ru = len(re.findall(f'data-status="{st}"', tr))
            c_uk = len(re.findall(f'data-status="{st}"', tu))
            c_en = len(re.findall(f'data-status="{st}"', te))
            if not (c_ru == c_uk == c_en):
                errors.append(f"data-status {st}: RU={c_ru} UK={c_uk} EN={c_en}")

        ids_ru = set(re.findall(r'\bid="([^"]+)"', tr))
        ids_uk = set(re.findall(r'\bid="([^"]+)"', tu))
        ids_en = set(re.findall(r'\bid="([^"]+)"', te))
        if ids_ru != ids_uk:
            errors.append(f"DOM id sets differ between RU and UK index.html: diff={ids_ru ^ ids_uk}")
        if ids_ru != ids_en:
            errors.append(f"DOM id sets differ between RU and EN index.html: diff={ids_ru ^ ids_en}")

        if 'lang="ru"' not in tr[:200] or 'lang="uk"' not in tu[:200] or 'lang="en"' not in te[:200]:
            errors.append("html lang attribute mismatch across RU/UK/EN")

        for req in ('rel="canonical"', 'hreflang="ru"', 'hreflang="uk"', 'hreflang="en"', 'hreflang="x-default"'):
            for loc_path, loc_text, _ in locales:
                if req not in loc_text:
                    errors.append(f"missing {req} in {loc_path}")

        # --- Language Switcher Checks in HTML ---
        for loc_path, loc_text, loc_code in locales:
            for sw_code in ("ru", "uk", "en"):
                if f'data-lang-switch="{sw_code}"' not in loc_text:
                    errors.append(f"{loc_path}: missing data-lang-switch=\"{sw_code}\" in header switcher")

        # --- Dynamic Compact Release Label Validation ---
        label_ru = extract_compact_label(tr)
        label_uk = extract_compact_label(tu)
        label_en = extract_compact_label(te)
        for loc_path, lbl in [(ru, label_ru), (uk, label_uk), (en, label_en)]:
            if not lbl:
                errors.append(f"{loc_path} missing compact release label (.header-release-btn__short)")

        if label_ru and label_uk and label_en:
            if not (label_ru == label_uk == label_en):
                errors.append(f"Compact release label differs: RU='{label_ru}' UK='{label_uk}' EN='{label_en}'")

            active_ver = extract_active_release(tr, fi_ru, tags_ru)
            if active_ver:
                m_ver = re.match(r"^v?(\d+\.\d+)", active_ver)
                if m_ver:
                    expected_prefix = f"v{m_ver.group(1)}"
                    if not label_ru.startswith(expected_prefix):
                        errors.append(
                            f"Compact label '{label_ru}' does not match active release prefix '{expected_prefix}' (active: {active_ver})"
                        )
                if "alpha" in active_ver.lower() and "alpha" not in label_ru.lower():
                    errors.append(
                        f"Compact label '{label_ru}' lost alpha designation for active prerelease {active_ver}"
                    )

    # --- Cyrillic detection in English counterparts ---
    for i, line in enumerate(te.splitlines(), 1):
        if (
            CYR.search(line)
            and 'lang="ru"' not in line
            and 'lang="uk"' not in line
            and "README.ru.md" not in line
            and "README.uk.md" not in line
            and "Русск" not in line
            and "Україн" not in line
        ):
            warns.append(f"{en}:{i}: Cyrillic in EN file")

for e in errors:
    print("ERROR", e)
for w in warns:
    print("WARN ", w)
print(f"errors={len(errors)} warnings={len(warns)}")
sys.exit(1 if errors else 0)
