from django.template import Template, Context
from django.utils.safestring import mark_safe

try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

def parse(tag_atts, tag_contents):
    """
    From wordpress source: https://github.com/WordPress/WordPress/blob/master/wp-includes/media.php#L620
    return '<div ' . $id . 'class="wp-caption ' . esc_attr($align) . '" style="width: ' . (10 + (int) $width) . 'px">'
    . do_shortcode( $content ) . '<p class="wp-caption-text">' . $caption . '</p></div>';
    
    """
    if not tag_atts:
        return ''
    tag_atts = dict([(a[0], a[1]) for a in tag_atts])
    tag_atts['content'] = mark_safe(tag_contents)

    # Attempt to separate the text from the image, and put that in a figcaption
    # if text is present inside the tag instead of in the caption attribute.
    if tag_contents:
        soup = BeautifulSoup(tag_contents)
        inside_text = soup.get_text()
        if inside_text != '':
            image = soup.img.extract()
            captionpara = BeautifulSoup('<p>'+ inside_text.strip() +'</p>')
            tag_atts['content'] = mark_safe(str(image))
            tag_atts['caption'] = mark_safe(str(captionpara))
            

    context = Context(tag_atts)

    t = Template('<figure {% if id %}id="{{ id }}" {% endif %}{% if align %}align="{{ align }}" {% endif %}{% if width %}style="width: {{ width }}px"{% endif %}>{{ content|safe }}<figcaption>{{ caption|safe }}</figcaption></figure>')
    return t.render(context)