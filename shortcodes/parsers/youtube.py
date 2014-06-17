from django.template import Template, Context
from django.conf import settings

def parse(attrs, tag_contents=None):
  id = None
  # Run through the passed attribute list and attempt to populate:
  tag_atts = dict([(a[0], a[1]) for a in attrs if a[0] != ''])

  # There's a shortform for the embed tags, which trips up the regex
  # a bit, and puts the src, including the = before it as the 8th item
  # in the list.
  #
  # Attempt to pull that out if no id arg was found:
  if not 'id' in tag_atts.keys():
    ids = [a[7] for a in attrs if len(a) > 7 and a[7] != '']
    if len(ids) == 1:
      tag_atts['id'] = ids[0][1:] # Lose the '=' at the beginning.

  tag_atts['width'] = int(tag_atts.get('width', getattr(settings, 'SHORTCODES_YOUTUBE_WIDTH', 425)))
  tag_atts['height'] = int(tag_atts.get('height', 0))
	
  if tag_atts['height'] == 0:
    tag_atts['height'] = int(round(tag_atts['width'] / 425.0 * 344.0))

  html = '<iframe width="{{ width }}" height="{{ height }}" '
  html += 'src="{{ id }}" frameborder="0" allowfullscreen></iframe>'
	
  template = Template(html)
  context = Context(tag_atts)
	
  if tag_atts['id']:
    return template.render(context)
  else:
    return 'Video not found'
