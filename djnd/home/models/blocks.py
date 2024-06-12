from django.db import models
from django.utils.translation import get_language
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Locale
from wagtail.snippets.blocks import SnippetChooserBlock

from .snippets import Promoted


class PageColors(models.TextChoices):
    WHITE = "white", "Bela"
    MINT = "mint", "Meta"
    RED = "red", "Rdeča"
    GREEN = "green", "Zelena"
    BLUE = "blue", "Modra"
    YELLOW = "yellow", "Rumena"
    LAVENDER = "lavender", "Sivka"


class NetworksBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    description = blocks.TextBlock()
    networks = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("name", blocks.CharBlock()),
                ("link", blocks.URLBlock(required=False)),
                ("image", ImageChooserBlock(required=False)),
            ],
        ),
    )

    # def get_context(self, value, parent_context=None):
    #     context = super().get_context(value, parent_context=parent_context)

    #     language_code = get_language()
    #     locale = Locale.objects.get(language_code=language_code)
    #     context["networks"] = Network.objects.filter(locale_id=locale.id)

    #     return context

    class Meta:
        label = "Mreže"
        template = "home/blocks/networks_block.html"


class DonorsBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    current_donors = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("name", blocks.CharBlock()),
                ("link", blocks.URLBlock(required=False)),
                ("image", ImageChooserBlock(required=False)),
            ],
        ),
    )
    past_donors = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("name", blocks.CharBlock()),
                ("link", blocks.URLBlock(required=False)),
                ("image", ImageChooserBlock(required=False)),
            ],
        ),
    )

    class Meta:
        label = "Donatorji"
        template = "home/blocks/donors_block.html"


class PillarsBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    description = blocks.TextBlock()
    pillars = blocks.ListBlock(blocks.PageChooserBlock(target_model="home.PillarPage"))

    class Meta:
        label = "Stebri delovanja"
        template = "home/blocks/pillars_block.html"


class ContactBlock(blocks.StructBlock):

    class Meta:
        label = "Vizitka in občasnik"
        template = "home/blocks/contact_block.html"


class NewsletterBlock(blocks.StructBlock):
    color_scheme = blocks.ChoiceBlock(
        choices=PageColors.choices,
        default=PageColors.WHITE,
        label="Barvna shema",
    )

    class Meta:
        label = "Prijava na Občasnik"
        template = "home/blocks/newsletter_block.html"


class SupportBlock(blocks.StructBlock):
    color_scheme = blocks.ChoiceBlock(
        choices=PageColors.choices,
        default=PageColors.WHITE,
        label="Barvna shema",
    )

    class Meta:
        label = "Podpora"
        template = "home/blocks/support_block.html"


class FinancialInformationBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    reports_url = blocks.URLBlock(
        required=False, label="Letna vsebinska in finančna poročila"
    )

    class Meta:
        label = "Finančno poslovanje"
        template = "home/blocks/financial_information_block.html"


class TextContentBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    text = blocks.RichTextBlock()
    button = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("button_text", blocks.CharBlock()),
                ("link", blocks.URLBlock(required=False, label="Zunanja povezava")),
                (
                    "page_link",
                    blocks.PageChooserBlock(required=False, label="Povezava na stran"),
                ),
                (
                    "color",
                    blocks.ChoiceBlock(
                        choices=PageColors.choices,
                        default=PageColors.WHITE,
                        label="Barva gumba",
                    ),
                ),
            ],
        ),
        max_num=1,
        min_num=0,
    )

    class Meta:
        label = "Besedilo"
        template = "home/blocks/text_content_block.html"


class TableBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    table = blocks.ListBlock(
        blocks.StructBlock(
            [("title", blocks.CharBlock()), ("description", blocks.TextBlock())]
        )
    )

    class Meta:
        label = "Tabela"
        template = "home/blocks/table_block.html"


class PromotedBlock(blocks.StructBlock):
    promoted_snippet = SnippetChooserBlock(Promoted)

    class Meta:
        label = "Izpostavljeno"
        template = "home/blocks/promoted_block.html"


class ModuleBlock(blocks.StreamBlock):
    contact_block = ContactBlock()
    pillars_block = PillarsBlock()
    networks_block = NetworksBlock()
    text_content_block = TextContentBlock()
    table_block = TableBlock()
    donors_block = DonorsBlock()
    financial_information_block = FinancialInformationBlock()
    promoted_block = PromotedBlock()

    class Meta:
        label = "Modul"


class BlogPageBlock(blocks.StreamBlock):
    text_content_block = TextContentBlock()
    newsletter_block = NewsletterBlock()
    support_block = SupportBlock()
    promoted_block = PromotedBlock()

    class Meta:
        label = "Modul"
