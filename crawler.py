import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time


def crawl_site(start_url, max_pages=50, max_depth=3):
    visited = set()
    queue = [(start_url, 0)]
    pages = []

    domain = urlparse(start_url).netloc
    headers = {"User-Agent": "Mozilla/5.0"}

    while queue and len(pages) < max_pages:
        url, depth = queue.pop(0)

        if url in visited or depth > max_depth:
            continue

        visited.add(url)

        try:
            response = requests.get(url, headers=headers, timeout=4)
            html = response.text
        except:
            continue

        page_data = {"url": url, "status_code": response.status_code, "html": html}
        pages.append(page_data)

        yield page_data, int((len(pages) / max_pages) * 100), url

        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all("a", href=True)

        for a in links:
            href = a["href"]
            new_url = urljoin(url, href)
            new_domain = urlparse(new_url).netloc

            # Only follow internal links
            if new_domain != domain:
                continue

            # Skip files (PDFs, images, etc)
            skip_ext = (
                ".pdf", ".jpg", ".jpeg", ".png", ".gif",
                ".zip", ".rar", ".doc", ".docx", ".mp4", ".mp3"
            )
            if new_url.lower().endswith(skip_ext):
                continue

            # Prevent loops caused by parameters
            if new_url.count("?") > 2:
                continue

            if new_url not in visited:
                queue.append((new_url, depth + 1))
