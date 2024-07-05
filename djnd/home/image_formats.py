from wagtail.images.formats import get_image_format, unregister_image_format

unregister_image_format("left")
unregister_image_format("right")

get_image_format("fullwidth").filter_spec = "width-1600"
