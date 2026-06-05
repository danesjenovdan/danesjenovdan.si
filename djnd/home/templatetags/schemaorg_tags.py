from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe
from jsonify.templatetags.jsonify import jsonify

register = template.Library()

JSONLD_HTML_TEMPLATE = """
<script type="application/ld+json">
{{ data }}
</script>
"""

DJND_ORGANIZATION_DATA = {
    "@type": "Organization",
    "name": "Danes je nov dan",
    "url": "https://danesjenovdan.si",
    "logo": {
        "@type": "ImageObject",
        "url": static("img/djnd-logo-dark.svg"),
        "width": "695",
        "height": "235",
    },
}


@register.simple_tag(takes_context=True)
def schemaorg_jsonld(context, page):
    if hasattr(page, "get_jsonld_data"):
        data = page.get_jsonld_data(context)
        json_data = jsonify(data)
        json_data = json_data.replace("</script>", "<\\/script>")
        html = JSONLD_HTML_TEMPLATE.replace("{{ data }}", json_data)
        return mark_safe(html)
    return ""
