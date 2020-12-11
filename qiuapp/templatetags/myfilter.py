from django import template

register = template.Library()

@register.filter("replace")
def myreplace(value,arg):
    return value.replace(arg,"!")