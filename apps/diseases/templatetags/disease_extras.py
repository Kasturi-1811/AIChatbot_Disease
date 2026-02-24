from django import template

register = template.Library()

@register.filter
def get_lang_field(obj, field_name):
    if not hasattr(obj, "get_field"):
        return ""
    return obj.get_field(field_name)
