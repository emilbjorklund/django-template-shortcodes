import hashlib
import re

from begood.contrib.shortcodes import parsers
from django.core.cache import cache

def import_parser(name):
  try:
    mod = __import__(name)
  except ValueError:
    return None
  components = name.split('.')
  for comp in components[1:]:
    mod = getattr(mod, comp)
  return mod

def parse(value, request):
  ex = re.compile(r'\[(.*?)\]')
  groups = ex.findall(value)
  pieces = {}
  parsed = value
  
  for item in groups:
    cache_key = memcached_safe_key(item)
  
    if ' ' in item:
      name, space, args = item.partition(' ')
      args = __parse_args__(args)
    else:
      name = item
      args = {}
    
    args['request'] = request
    try:
      module = import_parser('begood.contrib.shortcodes.parsers.' + name)
      function = getattr(module, 'parse')
      result = function(args)
      try:
        parsed = re.sub(r'\[' + re.escape(item) + r'\]', result, parsed)
      except:
        pass
    except (ImportError, AttributeError):
      pass
  return parsed

def __parse_args__(value):
  ex = re.compile(r'[ ]*(\w+)=([^" ]+|"[^"]*")[ ]*(?: |$)')
  groups = ex.findall(value)
  kwargs = {}

  for group in groups:
    if group.__len__() == 2:
      item_key = group[0]
      item_value = group[1]
      
      if item_value.startswith('"'):
        if item_value.endswith('"'):
          item_value = item_value[1:]
          item_value = item_value[:item_value.__len__() - 1]
      
      kwargs[item_key] = item_value
    return kwargs

def memcached_safe_key(string, block_size=2**14):
  md5 = hashlib.md5()
  md5.update(string)
  return md5.hexdigest()