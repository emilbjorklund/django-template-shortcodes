from django.template import Template, Context
from django.conf import settings

def parse(kwargs):
  url = kwargs.get('url')
  width = int(kwargs.get('width', getattr(settings, 'SHORTCODES_GMAPS_WIDTH', 556)))
  height = int(kwargs.get('height', 313))
	
  html = '<iframe width="{{ width }}" height="{{ height }}" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="{{ url|safe }}&amp;ie=UTF8&amp;output=embed"></iframe>'
  
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
    return 'Missing URL for Google Maps'
