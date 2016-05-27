from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def displayLink(url):
	""" Takes a full url and returns the Top Level Domain for display """
	return url.split("://")[1].split("/")[0]

