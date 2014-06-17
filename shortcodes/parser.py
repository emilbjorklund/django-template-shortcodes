import
import re

from shortcodes import parsers

from .parsers import youtube, caption

TAGS_WE_CAN_PARSE = {
    'youtube': youtube,
    'caption': caption,
}

"""
from https://github.com/RealGeeks/wp_export_parser/blob/master/wp_export_parser/parse_shortcodes.py
"""
def replace_tags(match):
    tag_name = match.group(2)
    tag_atts = match.group(3)
    tag_contents = match.group(5)
    if tag_name in TAGS_WE_CAN_PARSE:
        tag_atts = parse_shortcode_atts(tag_atts)
        return TAGS_WE_CAN_PARSE[tag_name].parse(tag_atts, tag_contents)

def parse_shortcode_atts(atts):
    pattern = r'(\w+)\s*=\s*"([^"]*)"(?:\s|$)|(\w+)\s*=\s*\'([^\']*)\'(?:\s|$)|(\w+)\s*=\s*([^\s\'"]+)(?:\s|$)|"([^"]*)"(?:\s|$)|(\S+)(?:\s|$)'
    return re.findall(pattern, atts)

def parse(value, request):
    """
    I stole this shortcode regex from Wordpress's source.  It is very confusing.
    """
    tagregexp = '|'.join([re.escape(t) for t in TAGS_WE_CAN_PARSE.keys()])
    pattern = re.compile('\\[(\\[?)(' + tagregexp + ')\\b([^\\]\\/]*(?:\\/(?!\\])[^\\]\\/]*)*?)(?:(\\/)\\]|\\](?:([^\\[]*(?:\\[(?!\\/\\2\\])[^\\[]*)*)\\[\\/\\2\\])?)(\\]?)')
    return re.sub(pattern, replace_tags, value)
