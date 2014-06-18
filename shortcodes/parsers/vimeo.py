from django.template import Template, Context
from django.conf import settings

def parse(attrs, tag_contents=None):
  tag_atts = {}

  if not 'id' in attrs.keys():
    if 'idval' in attrs.keys() and attrs['idval'][:1] == '=':
      tag_atts['id'] = attrs['idval'][1:]
  else:
    tag_atts['id'] = attrs['id']
  
  tag_atts['width'] = int(attrs.get('width', getattr(settings, 'SHORTCODES_YOUTUBE_WIDTH', 556)))
  tag_atts['height'] = int(attrs.get('height', 313))
	
  html = '<iframe src="http://player.vimeo.com/video/{{ id }}?title=0&amp;byline=0&amp;portrait=0" width="{{ width }}" height="{{ height }}" frameborder="0" webkitAllowFullScreen allowFullScreen></iframe>'
	
  template = Template(html)
  context = Context(tag_atts)
	
  if 'id' in tag_atts:
    return template.render(context)
  else:
    return 'Video not found'