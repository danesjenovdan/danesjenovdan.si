from html import escape as html_escape

from django.http import HttpResponse
from django.utils import feedgenerator
from django.utils.http import http_date
from django.utils.translation import gettext as _

TEXT_READ_MORE = _("Poglej objavo!")


def get_image_html_for_rss(image, link):
    desc = ""
    if image:
        try:
            rendition = image.get_rendition("max-600x315")
            if rendition and rendition.full_url:
                alt = html_escape(rendition.alt, quote=True)
                desc += f'<p><a href="{link}" target="_blank"><img width="{rendition.width}" height="{rendition.height}" src="{rendition.full_url}" alt="{alt}"></a></p>'
        except IOError:
            desc += f"<p>ERROR GENERATING IMAGE RENDITION!</p>"
    return f"{desc}"


def get_read_more_html_for_rss(link):
    return f'<p><a href="{link}" target="_blank">{TEXT_READ_MORE}</a></p>'


def rss_preview(page, title, feed_items):
    site = page.get_site()
    feed_title = f"{site.site_name} | {title}"
    feed_description = f"{title} RSS feed"

    html = f"""
    <!DOCTYPE html><html>
    <head>
        <meta charset="utf-8">
        <title>{feed_title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            .content {{
                max-width: 800px;
                margin: 0 auto;
            }}
        </style>
    </head>
    <body>
        <div class="content">
    """

    html += f"""
        <h1>{feed_title}</h1>
        <p>{feed_description}</p>
    """

    for item in feed_items:
        html += "<hr>"
        html += f'<h2><a href="{item["link"]}" target="_blank">{item["title"]}</a></h2>'
        html += f'<p>Published at: {item["pubdate"].isoformat()} | Updated at: {item["updateddate"].isoformat()}</p>'
        html += (
            f'<p>Link: <a href="{item["link"]}" target="_blank">{item["link"]}</a></p>'
        )
        html += f'<p>Unique ID: {item["unique_id"]}</p>'
        html += f'<p>{item["description"]}</p>'

    html += """
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)


def rss_feed(page, title, feed_items):
    site = page.get_site()
    feed_title = f"{site.site_name} | {title}"
    feed_description = f"{title} RSS feed"

    feed = feedgenerator.Rss201rev2Feed(
        title=feed_title,
        description=feed_description,
        link=page.full_url,
        feed_url=page.full_url + "rss/",
        language=page.locale.language_code,
    )

    for item in feed_items:
        is_permalink = item["unique_id"].startswith("http")
        feed.add_item(
            title=item["title"],
            link=item["link"],
            unique_id=item["unique_id"],
            unique_id_is_permalink=is_permalink,
            description=item["description"],
            pubdate=item["pubdate"],
            updateddate=item["updateddate"],
        )

    response = HttpResponse(content_type=feed.content_type)
    if len(feed_items) > 0:
        response.headers["Last-Modified"] = http_date(
            feed.latest_post_date().timestamp()
        )
    feed.write(response, "utf-8")
    return response
