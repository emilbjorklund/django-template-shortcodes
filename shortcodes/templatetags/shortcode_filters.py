from shortcodes import parser
from django import template

register = template.Library()

def shortcodes_replace(value, request=None):
    """
    A filter for parsing a string on the format ``[shortcode keyword=value]``
    using the shortcodes parser method.
    """
    return parser.parse(value, request)
    
register.filter('shortcodes', shortcodes_replace)

def shortcodes_remove(value, request=None):
    """
    A filter for removing shortcodes and the content inside them.
    """
    return parser.remove(value, request)


register.filter('removeshortcodes', shortcodes_remove)
