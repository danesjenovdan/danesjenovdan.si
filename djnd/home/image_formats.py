from wagtail.images.formats import get_image_format, unregister_image_format

# unregistering the default image formats breaks if you have already created images with them
# unregister_image_format("left")
# unregister_image_format("right")
get_image_format("left").filter_spec = "width-1600"
get_image_format("right").filter_spec = "width-1600"

get_image_format("fullwidth").filter_spec = "width-1600"
