from wagtail import blocks

from .snippets import Network, Donor


class NetworksBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    description = blocks.TextBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context["networks"] = Network.objects.all()
        return context

    class Meta:
        label = "Mreže"
        template = "home/blocks/networks_block.html"


class DonorsBlock(blocks.StructBlock):
    title = blocks.CharBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context["current_donors"] = Donor.objects.filter(past=False)
        context["past_donors"] = Donor.objects.filter(past=True)
        return context

    class Meta:
        label = "Donatorji"
        template = "home/blocks/donors_block.html"


class PillarsBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    description = blocks.TextBlock()
    pillars = blocks.ListBlock(blocks.PageChooserBlock())

    class Meta:
        label = "Stebri delovanja"
        template = "home/blocks/pillars_block.html"


class ContactBlock(blocks.StructBlock):

    class Meta:
        label = "Vizitka in občasnik"
        template = "home/blocks/contact_block.html"


class NewsletterBlock(blocks.StructBlock):

    class Meta:
        label = "Prijava na Občasnik"
        template = "home/blocks/newsletter_block.html"


class SupportBlock(blocks.StructBlock):

    class Meta:
        label = "Podpora"
        template = "home/blocks/support_block.html"


class FinancialInformationBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    reports_url = blocks.URLBlock(required=False, label="Letna vsebinska in finančna poročila")

    class Meta:
        label = "Finančno poslovanje"
        template = "home/blocks/financial_information_block.html"


class TextContentBlock(blocks.StructBlock):
    title = blocks.CharBlock()
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
                        choices=[("white", "Bela"), ("green", "Zelena")],
                        default="white",
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
    table = blocks.ListBlock(blocks.StructBlock([
        ("title", blocks.CharBlock()),
        ("description", blocks.TextBlock())
    ]))

    class Meta:
        label = "Tabela"
        template = "home/blocks/table_block.html"


class ModuleBlock(blocks.StreamBlock):
    contact_block = ContactBlock()
    newsletter_block = NewsletterBlock()
    support_block = SupportBlock()
    pillars_block = PillarsBlock()
    networks_block = NetworksBlock()
    text_content_block = TextContentBlock()
    table_block = TableBlock()
    donors_block = DonorsBlock()
    financial_information_block = FinancialInformationBlock()

    class Meta:
        label = "Modul"
