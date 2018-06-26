from django import template

register = template.Library()

@register.filter(name='my_cut')
def cut(value, arg):
    """
    Custom filter to cut all arg occurances in value that has to be a string
    """
    return value.replace(arg, '')
