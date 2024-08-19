from wagtail import hooks
from wagtail.rich_text import LinkHandler
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.rich_text.converters.html_to_contentstate import BlockElementHandler
from draftjs_exporter.dom import DOM

from django.utils.html import escape
from django.utils.text import slugify

from .forms import (
    ActivityAdminModelForm,
    BlogPageAdminPageForm,
    NewsletterPageAdminPageForm,
    TeamMemberAdminModelForm,
)
from .models.pages import BlogPage, NewsletterPage
from .models.snippets import (
    Activity,
    ActivityCategory,
    ActivityProject,
    Promoted,
    TeamMember,
    TeamMemberCategory,
)

BlogPage.base_form_class = BlogPageAdminPageForm
NewsletterPage.base_form_class = NewsletterPageAdminPageForm

Activity.base_form_class = ActivityAdminModelForm
TeamMember.base_form_class = TeamMemberAdminModelForm


class ActivityViewSet(SnippetViewSet):
    model = Activity
    list_display = ["title", "date", "promoted"]
    list_filter = {
        "title": ["icontains"],
        "promoted": ["exact"],
        "pillar_page": ["exact"],
        "category": ["exact"],
        "project": ["exact"],
    }


class ActivityCategoryViewSet(SnippetViewSet):
    model = ActivityCategory
    list_display = ["name", "order"]


class ActivityProjectViewSet(SnippetViewSet):
    model = ActivityProject
    list_display = ["name", "order"]


register_snippet(ActivityViewSet)
register_snippet(ActivityCategoryViewSet)
register_snippet(ActivityProjectViewSet)
register_snippet(Promoted)
register_snippet(TeamMember)
register_snippet(TeamMemberCategory)


class NewTabExternalLinkHandler(LinkHandler):
    identifier = 'external'

    @classmethod
    def expand_db_attributes(cls, attrs):
        href = attrs['href']
        return '<a href="%s" target="_blank">' % escape(href)


def header_with_name(props):
    type_ = props.get('block', {}).get('type', '')
    text = props.get('block', {}).get('text', '')
    tag = 'div'
    if type_ == 'header-two':
        tag = 'h2'
    if type_ == 'header-three':
        tag = 'h3'
    if type_ == 'header-four':
        tag = 'h4'
    return DOM.create_element(tag, {}, DOM.create_element('a', {'id': slugify(text), 'class': 'anchor'}), props['children'])


@hooks.register("register_rich_text_features")
def more_rich_text_features(features):
    features.default_features.append("blockquote")

    features.register_link_type(NewTabExternalLinkHandler)

    features.register_converter_rule('contentstate', 'h2', {
        'from_database_format': {
            'h2': BlockElementHandler('header-two'),
        },
        'to_database_format': {
            'block_map': {'header-two': header_with_name}
        }
    })
    features.register_converter_rule('contentstate', 'h3', {
        'from_database_format': {
            'h3': BlockElementHandler('header-three'),
        },
        'to_database_format': {
            'block_map': {'header-three': header_with_name}
        }
    })
    features.register_converter_rule('contentstate', 'h4', {
        'from_database_format': {
            'h4': BlockElementHandler('header-four'),
        },
        'to_database_format': {
            'block_map': {'header-four': header_with_name}
        }
    })
    
