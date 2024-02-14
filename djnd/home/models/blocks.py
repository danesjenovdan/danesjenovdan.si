from wagtail import blocks


class ModuleBlock(blocks.StreamBlock):

    class Meta:
        label = "Modul"
        abstract = True
        # template = "home/blocks/block.html"
