from django.template import Template, Context
from django.conf import settings

def parse(kwargs):
  id = kwargs.get('id')
  width = int(kwargs.get('width', getattr(settings, 'SHORTCODES_YOUTUBE_WIDTH', 556)))
  height = int(kwargs.get('height', 313))
  jquery = getattr(settings, 'SHORTCODES_YOUTUBE_JQUERY', False)
	
  html = '<iframe src="http://player.vimeo.com/video/{{ id }}?title=0&amp;byline=0&amp;portrait=0" width="{{ width }}" height="{{ height }}" frameborder="0" webkitAllowFullScreen allowFullScreen></iframe>'
    
	
  template = Template(html)
  context = Context(
    {
      'id': id,
      'width': width,
      'height': height
    }
  )
	
  if id:
    return template.render(context)
  else:
    return 'Video not found'