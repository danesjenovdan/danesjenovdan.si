from django import template
from wagtail.models import Locale

register = template.Library()


@register.filter
def startswith(value, arg):
    return value.startswith(arg)


@register.filter
def idlist(value):
    return [obj.id for obj in value]


@register.filter
def get_translated_m2m_ids(value, field_name):
    # hack to get translated m2m fields, there must be a better way?
    if value.locale.language_code != "sl":
        sl = Locale.objects.get(language_code="sl")

        if sl_value := value.get_translation_or_none(sl):
            sl_objs = getattr(sl_value, field_name).all()

            ids = []
            for sl_obj in sl_objs:
                if obj := sl_obj.get_translation_or_none(value.locale):
                    ids.append(obj.id)

            return ids

    return [obj.id for obj in getattr(value, field_name).all()]


@register.filter
def debug_print(value):
    print(value)
    print(type(value))
    return value
