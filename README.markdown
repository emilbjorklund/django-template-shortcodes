# django-template-shortcodes

THIS IS EXPERIMENTAL STUFF. Don't use it. Probably.

This package provides some [WordPress
shortcode](http://en.support.wordpress.com/shortcodes/) support for Django
templates. It is heavily based on [AGoodId's version of django-shortcodes](https://github.com/AGoodId/django-shortcodes) (in turn based on https://code.google.com/p/django-shortcodes/), as well as [WP Export Parser](https://github.com/RealGeeks/wp_export_parser) for the regex parts, lifted from WordPress.

So far, only an experimental implementation of the `[youtube id='http://foo']` or `[youtube=http://foo]` tags, plus the `[caption caption="Foo text"]<img src="http://foo" alt="Foo">[/caption]` or `[caption]<img src="http://foo" alt="Foo">Caption Text Here![/caption]` patterns.

## Installation

Install via pip: `pip install django-template-shortcodes`
Or clone the [Git repository](https://github.com/emilbjorklund/django-shortcodes).

## Usage

    {% load shortcodes_filters %}
    {{ text|shortcodes|safe }}
