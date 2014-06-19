import re

from shortcodes import parsers

from .parsers import youtube, caption, gmaps, iframe, vimeo

TAGS_WE_CAN_PARSE = {
    'youtube': youtube,
    'caption': caption,
    'gmaps': gmaps,
    'iframe': iframe,
    'vimeo': vimeo,
}


def get_regex():
    """
    The shortcode regex from 
    https://github.com/WordPress/WordPress/blob/947aa049003582acca152001ad0de39877321e3e/wp-includes/shortcodes.php,
    converted to work in Python.
    """
    tagregexp = tagregexp = '|'.join([re.escape(t) for t in TAGS_WE_CAN_PARSE.keys()])

    return re.compile(r''.join([
        '\\[',
        '(\\[?)',
        '(%s)' % tagregexp,
        '\\b', # This line is changed from WP:s implementation.
        '('
            '[^\\]\\/]*'
            '(?:',
                '\\/(?!\\])',
                '[^\\]\\/]*',
            ')*?',
        ')',
        '(?:',
            '(\\/)',
            '\\]',
        '|',
            '\\]',
            '(?:',
                '(',
                    '[^\\[]*', # This line is changed: python doesn't allow double multipliers.
                    '(?:',
                        '\\[(?!\\/\\2\\])',
                        '[^\\[]*', # This line is changed: python doesn't allow double multipliers.
                    ')*', # This line is changed: python doesn't allow double multipliers.
                ')'
                '\\[\\/\\2\\]',
            ')?',
        ')'
        '(\\]?)']))


def shortcode_exists(tag):
    return tag in TAGS_WE_CAN_PARSE

def replace_tags(match):
    """
    Get the name of the encountered shortcode, its attributes and its contents.

    If a valid shortcode exists for that name, try to run the `parse()` function
    from that module. The parser should return the new HTML.

    The result from the shortcode parser is returned.
    """
    tag = match.group(2) # the 'name' of the shortcode saved.
    atts = match.group(3) # the substring containing all attributes.
    contents = match.group(5) # Anything inside the shortcode

    if shortcode_exists(tag):
        att_dict = parse_shortcode_atts(atts)
        return TAGS_WE_CAN_PARSE[tag].parse(att_dict, contents)

def parse_shortcode_atts(att_text):

    atts = {} # Hold the attributes as a dict.

    # Match the individual attributes inside the shortcode:
    pattern = r'(\w+)\s*=\s*"([^"]*)"(?:\s|$)|(\w+)\s*=\s*\'([^\']*)\'(?:\s|$)|(\w+)\s*=\s*([^\s\'"]+)(?:\s|$)|"([^"]*)"(?:\s|$)|(\S+)(?:\s|$)'
    
    # Remove non-breaking spaces and invisible spaces, while 
    # matching attribute string to the pattern above:
    raw_atts = re.findall(pattern, att_text.replace(u"\u00A0", " ").replace(u"\u200b", " "))

    # This is basically translated from the WordPress codebase.
    # It aims to look at the resulting match groups in the array from the pattern,
    # and ascribe them places in the atts-dict.
    if raw_atts:
        for m in raw_atts:
            if m[1] != '':
                atts[m[0].lower()] = m[1]
            elif m[2] != '':
                atts[m[2].lower()] = m[3]
            elif m[4] != '':
                atts[m[4].lower()] = m[5]
            elif m[6] != '' and len(m[6]) > 0:
                atts['id'] = m[6]
            elif m[7]:
                atts['idval'] = m[7];
    return atts

def parse(value, request):
    """
    Parse the contents of a piece of text/markup in the template, and run 
    `replace_tags()` on the matches when using the regex found in `get_regex()`
    """
    
    pattern = get_regex()
    return re.sub(pattern, replace_tags, value)

def remove(value, request):
    """
    Remove all shortcodes from the content.
    """
    pattern = get_regex()
    return re.sub(pattern, '', value)

