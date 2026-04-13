#!/usr/bin/env python3
"""Download every image referenced by the local HTML pages, mirroring the
remote URL path structure (e.g. https://diservicesinc.com/web/images/foo.png
becomes ./web/images/foo.png)."""

import os
import re
import ssl
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
BASE_URL = "https://diservicesinc.com/"
IMG_EXTS = ("jpg", "jpeg", "png", "gif", "svg", "webp", "ico", "bmp", "avif")

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

ATTR_RE = re.compile(
    r"""(?:src|href|data-src|data-bg|data-lazy|data-original|poster)\s*=\s*['"]([^'"]+\.(?:%s))(?:\?[^'"]*)?['"]"""
    % "|".join(IMG_EXTS),
    re.IGNORECASE,
)
URL_RE = re.compile(
    r"""url\(\s*['"]?([^'")]+\.(?:%s))(?:\?[^'")]*)?['"]?\s*\)""" % "|".join(IMG_EXTS),
    re.IGNORECASE,
)

def extract_image_urls(html: str) -> set[str]:
    urls = set()
    for m in ATTR_RE.finditer(html):
        urls.add(m.group(1))
    for m in URL_RE.finditer(html):
        urls.add(m.group(1))
    return urls

def absolutize(url: str) -> str:
    if url.startswith("//"):
        return "https:" + url
    if url.startswith(("http://", "https://")):
        return url
    return urllib.parse.urljoin(BASE_URL, url.lstrip("/"))

def download(url: str, dest: Path) -> tuple[bool, str]:
    if dest.exists() and dest.stat().st_size > 0:
        return True, "exists"
    try:
        parts = urllib.parse.urlsplit(url)
        safe_path = urllib.parse.quote(parts.path)
        encoded_url = urllib.parse.urlunsplit(
            (parts.scheme, parts.netloc, safe_path, parts.query, parts.fragment)
        )
        req = urllib.request.Request(encoded_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as resp:
            data = resp.read()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        return True, f"{len(data)}B"
    except Exception as e:
        return False, str(e)

def main() -> int:
    # Collect all unique image URLs across every local html file.
    all_urls: set[str] = set()
    for html_file in sorted(ROOT.glob("*.html")):
        html = html_file.read_text(encoding="utf-8", errors="ignore")
        all_urls.update(extract_image_urls(html))

    print(f"Found {len(all_urls)} unique image references across local HTML files\n")

    # Only download images that live on diservicesinc.com (skip third parties).
    target_host = urllib.parse.urlparse(BASE_URL).netloc
    ok = fail = skipped = 0

    for rel in sorted(all_urls):
        abs_url = absolutize(rel)
        parsed = urllib.parse.urlparse(abs_url)
        if parsed.netloc and parsed.netloc != target_host:
            print(f"SKIP (external) {abs_url}")
            skipped += 1
            continue

        # Mirror the URL path locally: /web/images/foo.png -> ./web/images/foo.png
        rel_path = parsed.path.lstrip("/")
        if not rel_path or rel_path.endswith("/"):
            continue
        dest = ROOT / rel_path

        success, info = download(abs_url, dest)
        status = "OK " if success else "ERR"
        print(f"{status} {rel_path}  ({info})")
        if success:
            ok += 1
        else:
            fail += 1

    print(f"\nDone. {ok} downloaded/cached, {fail} failed, {skipped} skipped.")
    return 0 if fail == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
