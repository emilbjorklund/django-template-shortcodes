from django.template import Template, Context
from django.conf import settings

def parse(attrs, tag_contents=None):

  tag_atts = {}

  for att_list in attrs:
    # condense the list (strip empty):
    sparse_list = [val for val in att_list if val]
    if len(sparse_list) > 0 and sparse_list[0][0] == '=':
      tag_atts['id'] = sparse_list[0][1:]
    else:
      if len(sparse_list) == 2:
        tag_atts[sparse_list[0]] = sparse_list[1]

  tag_atts['width'] = int(tag_atts.get('width', getattr(settings, 'SHORTCODES_YOUTUBE_WIDTH', 425)))
  tag_atts['height'] = int(tag_atts.get('height', 0))
	
  if tag_atts['height'] == 0:
    tag_atts['height'] = int(round(tag_atts['width'] / 425.0 * 344.0))

  html = '<iframe width="{{ width }}" height="{{ height }}" '
  html += 'src="{{ id }}" frameborder="0" allowfullscreen></iframe>'
	
  template = Template(html)
  context = Context(tag_atts)
	
  if 'id' in tag_atts:
    return template.render(context)
  else:
    return 'Video not found'
