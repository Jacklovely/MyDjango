from django import template
import time

register = template.Library()

@register.simple_tag(name="current_time")
def get_current_time():
    timestr = time.strftime("%Y-%m-%d %H-%M-%S")
    return timestr
