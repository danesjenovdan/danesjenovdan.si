from django import template
from django.http import QueryDict
from wagtail.models import Locale, Page

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
def is_page(value):
    return isinstance(value, Page)


@register.filter
def sl_is_promoted(value):
    if value.locale.language_code == "sl":
        return value.promoted

    sl = Locale.objects.get(language_code="sl")
    if sl_value := value.get_translation_or_none(sl):
        return sl_value.promoted

    return False


@register.filter
def has_any_tags(value, field_names):
    field_names = field_names.split("|")

    if value.locale.language_code == "sl":
        for field_name in field_names:
            if getattr(value, field_name).exists():
                return True
    else:
        sl = Locale.objects.get(language_code="sl")
        if sl_value := value.get_translation_or_none(sl):
            for field_name in field_names:
                if getattr(sl_value, field_name).exists():
                    return True

    return False


@register.filter
def sl_activity_tags(value, field_name):
    if value.locale.language_code == "sl":
        return getattr(value, field_name).all()

    sl = Locale.objects.get(language_code="sl")
    if sl_value := value.get_translation_or_none(sl):
        return getattr(sl_value, field_name).all()

    return []


@register.filter
def query_string_without_offset(request):
    query_string: QueryDict = request.GET.copy()
    query_string.pop("offset", None)
    return query_string.urlencode()


@register.filter
def debug_print(value):
    print(f"~~{value}~~")
    print(type(value))
    # print(vars(value))
    return value


@register.filter
def show_for_language(value, language_code):
    languages = value["show_languages"]
    return language_code in languages


@register.filter
def flag_emoji_for_language(language_code):
    return {
        "sl": "🇸🇮",
        "en": "🇬🇧",
    }.get(language_code, "")


def get_referrer_params(request):
    referrers = [
        request.META.get("HTTP_REFERER"),
        *request.GET.getlist("referer"),
        *request.GET.getlist("referrer"),
    ]
    referrers = [r for r in referrers if r]
    get_params = {
        "referrer": ", ".join(referrers),
    }
    for key in request.GET:
        if key.startswith("utm_"):
            value = ", ".join(request.GET.getlist(key))
            get_params[key] = value
    return {
        **get_params,
    }


@register.simple_tag
def set_referrer_params(request, default_params_string=""):
    referrer_params = get_referrer_params(request)
    query_dict = QueryDict(default_params_string, mutable=True)
    for key, value in referrer_params.items():
        if value:
            query_dict[key] = value
    query_string = query_dict.urlencode()
    return query_string
