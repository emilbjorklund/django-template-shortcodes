from begood.contrib.shortcodes import parser
from django import template

register = template.Library()

def shortcodes_replace(value):
  """
  A filter for parsing a string on the format ``[shortcode keyword=value]``
  using the shortcodes parser method.
  """
  return parser.parse(value)

register.filter('shortcodes', shortcodes_replace)