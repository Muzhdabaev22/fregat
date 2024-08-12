from django import template

register = template.Library()

@register.filter
def index(List, i):
    return List[int(i)]


@register.simple_tag
def to_list(*args):
    return args
