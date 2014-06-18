from django.template import Template, Context
from django.conf import settings

def parse(attrs, tag_contents=None):
  url = attrs.get('url')
  width = int(attrs.get('width', getattr(settings, 'SHORTCODES_IFRAME_WIDTH', 556)))
  height = int(attrs.get('height', 313))
	
  html = '<iframe width="{{ width }}" height="{{ height }}" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="{{ url|safe }}"></iframe>'
  
  template = Template(html)
  context = Context(
    {
      'url': url,
      'width': width,
      'height': height
    }
  )
	
  if url:
    return template.render(context)
  else:
    return 'Missing URL for iframe'
