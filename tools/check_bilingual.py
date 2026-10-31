"""Compact re-runnable showcase parity check (stdlib only).

Extracts and compares actual release facts and link targets across bilingual
docs pairs (RU vs EN) and all active README language versions:
  - Five required README editions: EN, RU, ES, PT-BR, ZH-CN
  - FirstInstall versions and download links
  - Release tag URLs
  - SHA-256 installer checksums (cross-pair parity & intra-file consistency)
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
    ("README.ru.md", "Русский"),
    ("README.es.md", "Español"),
    ("README.pt-BR.md", "Português (Brasil)"),
    ("README.zh-CN.md", "简体中文"),
]

DOC_PAIRS = [
    ("docs/index.html", "docs/en/index.html"),
    ("docs/roadmap.md", "docs/en/roadmap.md"),
    ("docs/first-start.md", "docs/en/first-start.md"),
]

BANNED_EN_CALQUES = [
    r"\bcontours?\b",
    r"\bposition care\b",
    r"\bclock proof\b",
    r"\barming\b",
]
CYR = re.compile(r"[\u0400-\u04FF]")
errors, warns = [], []

existing_readmes = [p for p, _ in README_LANGS if (ROOT / p).exists()]
pending_readmes = [p for p, _ in README_LANGS if not (ROOT / p).exists()]
if pending_readmes:
    errors.append(f"Missing required README translations: {', '.join(pending_readmes)}")


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
    | {x for pair in DOC_PAIRS for x in pair}
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

# 4. Dynamic fact parity and consistency across documentation pairs (RU vs EN)
for ru, en in DOC_PAIRS:
    tr, te = text(ru), text(en)

    # --- SHA-256 Checksums ---
    shas_ru = extract_shas(tr)
    shas_en = extract_shas(te)
    set_shas_ru = set(shas_ru)
    set_shas_en = set(shas_en)

    # Intra-file consistency: multiple occurrences in a document must not conflict.
    if len(set_shas_ru) > 1:
        errors.append(f"{ru}: multiple conflicting SHA-256 checksums within file: {set_shas_ru}")
    if len(set_shas_en) > 1:
        errors.append(f"{en}: multiple conflicting SHA-256 checksums within file: {set_shas_en}")

    # Cross-pair parity.
    if set_shas_ru != set_shas_en:
        errors.append(f"SHA-256 mismatch between {ru} ({set_shas_ru}) and {en} ({set_shas_en})")

    # --- FirstInstall Versions & Tags ---
    fi_ru = extract_first_install_versions(tr)
    fi_en = extract_first_install_versions(te)
    set_fi_ru = set(fi_ru)
    set_fi_en = set(fi_en)

    # In single-release documents, repetitions must be consistent.
    if not ru.endswith(".html"):
        if len(set_fi_ru) > 1:
            errors.append(f"{ru}: multiple conflicting FirstInstall versions: {set_fi_ru}")
        if len(set_fi_en) > 1:
            errors.append(f"{en}: multiple conflicting FirstInstall versions: {set_fi_en}")

    if set_fi_ru != set_fi_en:
        errors.append(f"FirstInstall versions mismatch between {ru} ({set_fi_ru}) and {en} ({set_fi_en})")

    tags_ru = set(extract_release_tags(tr))
    tags_en = set(extract_release_tags(te))
    if tags_ru != tags_en:
        errors.append(f"Release tags mismatch between {ru} ({tags_ru}) and {en} ({tags_en})")

    # --- Byte sizes (normalized digits) ---
    bytes_ru = extract_byte_sizes(tr)
    bytes_en = extract_byte_sizes(te)
    if bytes_ru != bytes_en:
        errors.append(f"Installer byte size mismatch between {ru} ({bytes_ru}) and {en} ({bytes_en})")

    # --- English quality checks (as non-blocking WARN) ---
    te_prose = re.sub(r"<[^>]+>", " ", te) if en.endswith(".html") else te
    for pat in BANNED_EN_CALQUES:
        if re.search(pat, te_prose, flags=re.IGNORECASE):
            warns.append(f"{en}: literal calque/jargon warning matching {pat!r}")

    # --- HTML Structure & Metadata ---
    if ru.endswith(".html"):
        for st in ("released", "inprogress", "planned", "deferred"):
            c1 = len(re.findall(f'data-status="{st}"', tr))
            c2 = len(re.findall(f'data-status="{st}"', te))
            if c1 != c2:
                errors.append(f"data-status {st}: RU={c1} EN={c2}")

        if set(re.findall(r'\bid="([^"]+)"', tr)) != set(re.findall(r'\bid="([^"]+)"', te)):
            errors.append("DOM id sets differ between RU and EN index.html")

        if 'lang="ru"' not in tr[:200] or 'lang="en"' not in te[:200]:
            errors.append("html lang attribute mismatch")

        for req in ('rel="canonical"', 'hreflang="ru"', 'hreflang="en"', 'hreflang="x-default"'):
            if req not in tr or req not in te:
                errors.append(f"missing {req} in HTML pair")

        # --- Dynamic Compact Release Label Validation ---
        label_ru = extract_compact_label(tr)
        label_en = extract_compact_label(te)
        if not label_ru:
            errors.append("docs/index.html missing compact release label (.header-release-btn__short)")
        if not label_en:
            errors.append("docs/en/index.html missing compact release label (.header-release-btn__short)")

        if label_ru and label_en:
            if label_ru != label_en:
                errors.append(f"Compact release label differs: RU='{label_ru}' vs EN='{label_en}'")

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
            and "README.ru.md" not in line
            and "Русск" not in line
        ):
            warns.append(f"{en}:{i}: Cyrillic in EN file")

for e in errors:
    print("ERROR", e)
for w in warns:
    print("WARN ", w)
print(f"errors={len(errors)} warnings={len(warns)}")
sys.exit(1 if errors else 0)
