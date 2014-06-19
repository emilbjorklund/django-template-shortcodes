from django.template import Template, Context
from django.utils.safestring import mark_safe
from django.conf import settings

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

    tag_atts['content'] = mark_safe(tag_contents)

    # Attempt to separate the text from the image, and put that in a figcaption
    # if text is present inside the tag instead of in the caption attribute.

    if tag_contents:
        # try to get a soup instance from any tag contents passed in:
        try:
            soup = BeautifulSoup(tag_contents)

            # Get the actual image:
            image = soup.img.extract()

            # If there's no image, something is seriously weird.
            if image:
                # Add image to content as markup string:
                tag_atts['content'] = mark_safe(str(image))

                # Add caption text as caption.
                caption = ' '.join(soup.stripped_strings)
                if caption:
                    tag_atts['caption'] = caption
        except:
            pass

            

    context = Context(tag_atts)

    t = Template("""
        {% spaceless %}
        <figure {% if id %}id="{{ id }}"{% endif %}{% if align %}class="align-{{ align }}"{% endif %}{% if width %}style="width: {{ width }}px"{% endif %}>
            {{ content|safe }}
            {% if caption %}
            <figcaption>
                <p>{{ caption|safe }}</p>
            </figcaption>{% endif %}
        </figure>
        {% endspaceless %}""")
    return t.render(context)