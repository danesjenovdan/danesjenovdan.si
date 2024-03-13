from django import template

register = template.Library()


@register.filter
def startswith(value, arg):
    return value.startswith(arg)


@register.filter
def idlist(value):
    return [obj.id for obj in value]
