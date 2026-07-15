#!/usr/bin/env python3
"""
Exporta posts de um WordPress via REST API e converte pra formato Roq.

Uso:
    pip install requests markdownify pyyaml
    python wp_to_roq.py

Gera:
    content/posts/YYYY-MM-DD-slug.md
    public/images/wp/<caminho-original>
"""

import os
import re
import sys
import html
import json
import pathlib
import urllib.parse
from datetime import datetime

import requests
import yaml
from markdownify import markdownify as md

BASE = "https://www.igfasouza.com/blog"
API = f"{BASE}/wp-json/wp/v2"
POSTS_DIR = pathlib.Path("content/posts")
IMG_DIR = pathlib.Path("public/images/wp")
SESSION = requests.Session()
SESSION.verify = False  # cert expirado no domínio
requests.packages.urllib3.disable_warnings()


def fetch_all(endpoint):
    """Pagina até esgotar."""
    out, page = [], 1
    while True:
        r = SESSION.get(f"{API}/{endpoint}",
                        params={"per_page": 100, "page": page, "_embed": 1})
        if r.status_code == 400:  # sem mais páginas
            break
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        out.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return out


def slugify_from_url(url):
    """Extrai slug do wp-content/uploads/... pra path local."""
    p = urllib.parse.urlparse(url).path
    return p.split("wp-content/uploads/", 1)[-1].lstrip("/")


def download_image(url):
    if not url.startswith("http"):
        return None
    local_rel = slugify_from_url(url)
    local_abs = IMG_DIR / local_rel
    if local_abs.exists():
        return f"/images/wp/{local_rel}"
    local_abs.parent.mkdir(parents=True, exist_ok=True)
    try:
        r = SESSION.get(url, timeout=30)
        r.raise_for_status()
        local_abs.write_bytes(r.content)
        print(f"  img -> {local_rel}")
        return f"/images/wp/{local_rel}"
    except Exception as e:
        print(f"  !! falhou baixar {url}: {e}", file=sys.stderr)
        return url


def rewrite_images(markdown_text):
    """Troca URLs de wp-content/uploads por caminho local + baixa."""
    def repl(m):
        alt, url = m.group(1), m.group(2)
        new_url = download_image(url) or url
        return f"![{alt}]({new_url})"
    return re.sub(r"!\[([^\]]*)\]\((https?://[^\)]+)\)", repl, markdown_text)


def clean_title(t):
    return html.unescape(t).strip()


def build_frontmatter(post, tags, categories, cover_url):
    date = datetime.fromisoformat(post["date"]).strftime("%Y-%m-%d")
    fm = {
        "layout": "post",
        "title": clean_title(post["title"]["rendered"]),
        "date": date,
        "slug": post["slug"],
        "tags": sorted(set(tags + categories)),
    }
    excerpt = html.unescape(re.sub(r"<[^>]+>", "", post["excerpt"]["rendered"])).strip()
    if excerpt:
        fm["description"] = excerpt[:200]
    if cover_url:
        fm["image"] = cover_url
    return fm


def extract_embedded_terms(post):
    tags, cats = [], []
    for group in post.get("_embedded", {}).get("wp:term", []):
        for term in group:
            if term["taxonomy"] == "post_tag":
                tags.append(term["name"])
            elif term["taxonomy"] == "category":
                cats.append(term["name"])
    return tags, cats


def extract_featured(post):
    media = post.get("_embedded", {}).get("wp:featuredmedia", [])
    if media and media[0].get("source_url"):
        return download_image(media[0]["source_url"])
    return None


def main():
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    IMG_DIR.mkdir(parents=True, exist_ok=True)

    posts = fetch_all("posts")
    print(f"Baixando {len(posts)} posts...")

    for post in posts:
        slug = post["slug"]
        date = datetime.fromisoformat(post["date"]).strftime("%Y-%m-%d")
        fname = POSTS_DIR / f"{date}-{slug}.md"

        tags, cats = extract_embedded_terms(post)
        cover = extract_featured(post)
        fm = build_frontmatter(post, tags, cats, cover)

        html_body = post["content"]["rendered"]
        # markdownify: converte HTML em markdown gfm-ish
        body = md(html_body, heading_style="ATX", bullets="-", code_language="")
        body = rewrite_images(body)
        # limpeza de sobras comuns do WP
        body = re.sub(r"\n{3,}", "\n\n", body).strip()

        with fname.open("w", encoding="utf-8") as f:
            f.write("---\n")
            yaml.safe_dump(fm, f, allow_unicode=True, sort_keys=False)
            f.write("---\n\n")
            f.write(body)
            f.write("\n")
        print(f"OK  {fname.name}")

    print(f"\nPronto. {len(posts)} posts em {POSTS_DIR}/")


if __name__ == "__main__":
    main()
