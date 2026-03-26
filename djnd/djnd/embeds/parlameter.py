import hashlib
import json
import re

import requests
from wagtail.embeds.exceptions import EmbedNotFoundException
from wagtail.embeds.finders.base import EmbedFinder

parlameter_urls = [
    r"^https?://kartica\.parlameter\.si/.+$",
    r"^https?://glej\.[^/]+\.parlameter\.si/.+$",
    r"^https?://gledaj\..parlametar\.hr/.+$",
    r"^https?://gledaj\.[^/]+\.parlametar\.hr/.+$",
    r"^https?://parlacards-[^/]+\.lb\.djnd\.si/.+$",
]


class ParlameterEmbedFinder(EmbedFinder):
    _patterns = None

    def __init__(self):
        self._patterns = []

        for url in parlameter_urls:
            self._patterns.append(re.compile(url))

    def accept(self, url):
        for pattern in self._patterns:
            if re.match(pattern, url):
                return True
        return False

    def _get_embed_data(self, url):
        try:
            r = requests.get(url, headers={"User-agent": "Mozilla/5.0"}, timeout=10)
            r.raise_for_status()
            html = r.text
        except requests.RequestException:
            return {}

        embed_data = {}

        # get title and image from og tags
        og_title = re.search(r'<meta property="og:title" content="(.+?)"', html)
        og_image = re.search(r'<meta property="og:image" content="(.+?)"', html)

        if og_title:
            embed_data["title"] = og_title.group(1)
        if og_image:
            embed_data["thumbnail_url"] = og_image.group(1)

        return embed_data

    def find_embed(self, url, max_width=None, max_height=None):
        embed_data = self._get_embed_data(url)

        if "template=share" in url:
            url = url.replace("template=share", "template=embed")

        embed_url = url
        embed_hash = hashlib.md5(embed_url.encode("utf-8")).hexdigest()

        html = f"""
            <iframe id="parlameter_embed_{embed_hash}" frameborder="0" width="100%" style="max-width:100%;" src="{embed_url}"></iframe>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/4.3.2/iframeResizer.min.js"></script>
            <script>iFrameResize({{checkOrigin:false}},"#parlameter_embed_{embed_hash}");</script>
        """

        return {
            "title": embed_data.get("title", "Parlameter"),
            "author_name": "Parlameter",
            "provider_name": "Parlameter",
            "type": "card",
            "thumbnail_url": embed_data.get("thumbnail_url", ""),
            "width": "",
            "height": "",
            "html": html,
        }


embed_finder_class = ParlameterEmbedFinder
