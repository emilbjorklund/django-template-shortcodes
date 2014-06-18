from django.test import TestCase
from django.template import Template, RequestContext
from django.test.client import RequestFactory
from django.test.utils import setup_test_environment
setup_test_environment()

class CommonTestCase(TestCase):
   def assertAllFine(self):
       return True

class LibraryTest(CommonTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.c = RequestContext(self.factory.get('/'))
        self.c['text'] = ''
        self.maxDiff = None
        self.t = Template('{% load shortcode_filters %}{{ text|shortcodes|safe }}')


    def test_library_load_tag(self):
        t = Template("{% load shortcode_filters %}")
        request = self.factory.get('/foo')
        context = RequestContext(request)
        t.render(context)
        self.assertAllFine()

    def test_short_youtube_tag_output(self):
        self.c['text'] = '[youtube=http://www.youtube.com/watch?v=JaNH56Vpg-A]'
        result = self.t.render(self.c)
        self.assertEqual(result, '<iframe width="425" height="344" src="http://www.youtube.com/watch?v=JaNH56Vpg-A" frameborder="0" allowfullscreen></iframe>')

    def test_youtube_with_id(self):
        self.c['text'] = '[youtube src=http://www.youtube.com/watch?v=JaNH56Vpg-A]'
        result = self.t.render(self.c)
        self.assertEqual(result, '<iframe width="425" height="344" src="http://www.youtube.com/watch?v=JaNH56Vpg-A" frameborder="0" allowfullscreen></iframe>')


    def test_youtube_tag_output_with_width_and_id(self):
        self.c['text'] = '[youtube src="http://www.youtube.com/watch?v=JaNH56Vpg-A" width="800"]'
        result = self.t.render(self.c)
        self.assertEqual(result, '<iframe width="800" height="648" src="http://www.youtube.com/watch?v=JaNH56Vpg-A" frameborder="0" allowfullscreen></iframe>')

    def test_caption(self):
        self.c['text'] = '[caption id="attachment_6" \
           align="alignright" \
           width="300"]<img src="http://localhost/Kanagawa2-300x205.jpg"\
           alt="Kanagawa" title="The Great Wave" width="300" height="205"\
           class="size-medium wp-image-6" /> The Great Wave[/caption]'
        result = self.t.render(self.c)

        self.assertHTMLEqual(result, """<figure id="attachment_6" class="align-alignright" 
                    style="width: 300px"><img alt="Kanagawa" class="size-medium wp-image-6" 
                    height="205" src="http://localhost/Kanagawa2-300x205.jpg" 
                    title="The Great Wave" width="300"/><figcaption>
                    <p>The Great Wave</p>
                    </figcaption>
                    </figure>""")

    def test_caption_with_attribute(self):
        self.c['text'] = '[caption id="attachment_6" \
           align="alignright" caption="The Great Wave"\
           width="300"]<img src="http://localhost/Kanagawa2-300x205.jpg"\
           alt="Kanagawa" title="The Great Wave" width="300" height="205"\
           class="size-medium wp-image-6" />[/caption]'
        result = self.t.render(self.c)
        self.assertHTMLEqual(result, """<figure id="attachment_6" class="align-alignright" 
                    style="width: 300px"><img alt="Kanagawa" class="size-medium wp-image-6" 
                    height="205" src="http://localhost/Kanagawa2-300x205.jpg" 
                    title="The Great Wave" width="300" /><figcaption>
                    <p>The Great Wave</p>\
                    </figcaption>\
                    </figure>""")

    def test_caption_simple(self):
        self.c['text'] = '[caption caption="An image"]<img src="" alt="">[/caption]'
        result = self.t.render(self.c)
        self.assertHTMLEqual(result, '<figure><img src="" alt=""><figcaption><p>An image</p></figcaption></figure>')

    def test_caption_nocaption(self):
        result = self.t.render(self.c)
        self.assertHTMLEqual(result, '<figure><img src="" alt=""></figure>')

    def test_simple_gmaps(self):
        self.c['text'] = '[gmaps url="http://maps.google.com/?q=Malmo"]'
        result = self.t.render(self.c)
        self.assertHTMLEqual(result, '<iframe width="556" height="313" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.com/?q=Malmo&amp;ie=UTF8&amp;output=embed"></iframe>')

    def test_simple_gmaps_width(self):
        self.c['text'] = '[gmaps url="http://maps.google.com/?q=Malmo" width="800"]'
        result = self.t.render(self.c)
        self.assertHTMLEqual(result, '<iframe width="800" height="313" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.com/?q=Malmo&amp;ie=UTF8&amp;output=embed"></iframe>')

    def test_simple_iframe_width(self):
        self.c['text'] = '[iframe url="http://maps.google.com/?q=Malmo" width="800"]'
        result = self.t.render(self.c)
        self.assertHTMLEqual(result, '<iframe width="800" height="313" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.com/?q=Malmo"></iframe>')

    def test_vimeo_simple(self):
        self.c['text'] = '[vimeo=foo]'
        result = self.t.render(self.c)
        self.assertHTMLEqual(result, '<iframe src="http://player.vimeo.com/video/foo?title=0&amp;byline=0&amp;portrait=0" width="556" height="313" frameborder="0" webkitAllowFullScreen allowFullScreen></iframe>')
