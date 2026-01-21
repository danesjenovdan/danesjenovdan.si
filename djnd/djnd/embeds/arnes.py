from datetime import timedelta

import requests
from django.utils import timezone
from wagtail.embeds.exceptions import EmbedNotFoundException
from wagtail.embeds.finders.oembed import OEmbedFinder

arnes_providers = [
    {
        "endpoint": "https://video.arnes.si/api/oembed.{format}",
        "urls": [
            r"^https?://video\.arnes\.si/watch/.+$",
            r"^https?://video\.arnes\.si/embed/.+$",
            r"^https?://video\.arnes\.si/api/asset/.+/play.mp4$",
            r"^https?://video\.arnes\.si/attachments/video/.+$",
        ],
    },
]


class ArnesOEmbedFinder(OEmbedFinder):
    def __init__(self, options=None):
        super().__init__(providers=arnes_providers, options=options)

    def _fix_url(self, url):
        if "/embed/" in url:
            return url.replace("/embed/", "/watch/")
        if "/api/asset/" in url:
            asset_id = url.split("/api/asset/")[1].split("/play.mp4")[0]
            return f"https://video.arnes.si/watch/{asset_id}"
        if "/attachments/video/" in url:
            asset_id = url.split("/attachments/video/")[1].split("/")[1]
            return f"https://video.arnes.si/watch/{asset_id}"
        return url

    def find_embed(self, url, max_width=None, max_height=None):
        # Find provider
        endpoint = self._get_endpoint(url)
        if endpoint is None:
            raise EmbedNotFoundException

        # ADDED: allow different URL formats
        url = self._fix_url(url)

        # Work out params
        params = self.options.copy()
        params["url"] = url
        params["format"] = "json"

        # Perform request
        try:
            r = requests.get(
                endpoint, params=params, headers={"User-agent": "Mozilla/5.0"}
            )
            oembed = r.json()
        except requests.RequestException:
            raise EmbedNotFoundException

        # Convert photos into HTML
        if oembed["type"] == "photo":
            html = '<img src="{}" alt="">'.format(oembed["url"])
        else:
            html = oembed.get("html")

        # Return embed as a dict
        result = {
            "title": oembed.get("title", ""),
            "author_name": oembed.get("author_name", ""),
            "provider_name": oembed.get("provider_name", ""),
            "type": oembed["type"],
            # ADDED: camelCase fallback
            "thumbnail_url": oembed.get("thumbnail_url") or oembed.get("thumbnailUrl"),
            "width": oembed.get("width"),
            "height": oembed.get("height"),
            "html": html,
        }

        try:
            cache_age = int(oembed["cache_age"])
        except (KeyError, TypeError, ValueError):
            pass
        else:
            result["cache_until"] = timezone.now() + timedelta(seconds=cache_age)

        return result


embed_finder_class = ArnesOEmbedFinder
