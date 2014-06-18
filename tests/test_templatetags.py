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
        self.request = self.factory.get('/foo')
        self.context = RequestContext(self.request)
        self.context['caption_snippet'] = '[caption id="attachment_6" \
                align="alignright" \
                width="300"]<img src="http://localhost/Kanagawa2-300x205.jpg"\
                alt="Kanagawa" title="The Great Wave" width="300" height="205"\
                class="size-medium wp-image-6" /> The Great Wave[/caption]"'
        self.context['youtube'] = '[youtube id=http://www.youtube.com/watch?v=JaNH56Vpg-A]'
        self.maxDiff = None


    def test_library_load_tag(self):
        t = Template("{% load shortcode_filters %}")
        request = self.factory.get('/foo')
        context = RequestContext(request)
        t.render(context)
        self.assertAllFine()

    def test_short_youtube_tag_output(self):
        t = Template('{% load shortcode_filters %}{{ youtube|shortcodes|safe }}')
        request = self.factory.get('/foo')
        context = RequestContext(request)
        context['youtube'] = '[youtube=http://www.youtube.com/watch?v=JaNH56Vpg-A]'
        result = t.render(context)
        self.assertEqual(result, '<iframe width="425" height="344" src="http://www.youtube.com/watch?v=JaNH56Vpg-A" frameborder="0" allowfullscreen></iframe>')

    def test_youtube_tag_output_with_width(self):
        t = Template('{% load shortcode_filters %}{{ youtube|shortcodes|safe }}')
        request = self.factory.get('/foo')
        context = RequestContext(request)
        context['youtube'] = '[youtube id="http://www.youtube.com/watch?v=JaNH56Vpg-A" width="800"]'
        result = t.render(context)
        self.assertEqual(result, '<iframe width="800" height="648" src="http://www.youtube.com/watch?v=JaNH56Vpg-A" frameborder="0" allowfullscreen></iframe>')

    def test_caption(self):
        t = Template('{% load shortcode_filters %}{{ caption_snippet|shortcodes|safe }}')
        request = self.factory.get('/foo')
        context = RequestContext(request)
        context['caption_snippet'] = '[caption id="attachment_6" \
           align="alignright" \
           width="300"]<img src="http://localhost/Kanagawa2-300x205.jpg"\
           alt="Kanagawa" title="The Great Wave" width="300" height="205"\
           class="size-medium wp-image-6" /> The Great Wave[/caption]"'
        result = t.render(context)
        self.assertHTMLEqual(result, """<figure id="attachment_6" align="alignright" 
                    style="width: 300px"><img alt="Kanagawa" class="size-medium wp-image-6" 
                    height="205" src="http://localhost/Kanagawa2-300x205.jpg" 
                    title="The Great Wave" width="300"/><figcaption>
                    <p>The Great Wave</p>
                    </figcaption>
                    </figure>""")

    def test_caption_with_attribute(self):
        t = Template('{% load shortcode_filters %}{{ caption_snippet|shortcodes|safe }}')
        request = self.factory.get('/foo')
        context = RequestContext(request)
        context['caption_snippet'] = '[caption id="attachment_6" \
           align="alignright" caption="The Great Wave"\
           width="300"]<img src="http://localhost/Kanagawa2-300x205.jpg"\
           alt="Kanagawa" title="The Great Wave" width="300" height="205"\
           class="size-medium wp-image-6" />[/caption]"'
        result = t.render(context)
        print('RESULT: \n', result, '---------------------------------------------------------')
        self.assertHTMLEqual(result, """<figure id="attachment_6" align="alignright" 
                    style="width: 300px"><img alt="Kanagawa" class="size-medium wp-image-6" 
                    height="205" src="http://localhost/Kanagawa2-300x205.jpg" 
                    title="The Great Wave" width="300" /><figcaption>
                    <p>The Great Wave</p>\
                    </figcaption>\
                    </figure>""")


if __name__ == "__main__":
    unittest.main()
