# django-template-shortcodes

THIS IS EXPERIMENTAL STUFF. Don't use it. Probably.

This package provides some [WordPress
shortcode](http://en.support.wordpress.com/shortcodes/) support for Django
templates. It is heavily based on [AGoodId's version of django-shortcodes](https://github.com/AGoodId/django-shortcodes) (in turn based on https://code.google.com/p/django-shortcodes/), as well as [WP Export Parser](https://github.com/RealGeeks/wp_export_parser) for the regex parts, lifted from WordPress.

## Supported shortcodes (sort of): 

* `[caption caption="Foo bar"]<img src="" alt="" />[/caption]`
* `[caption]<img src="" alt="" /> Foo bar[/caption]`
* `[youtube=https://www.youtube.com/watch?v=dQw4w9WgXcQ]`
* `[youtube url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"]`
* `[gmaps url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"]`
* `[vimeo url="https://www.vimeo.com/watch?v=dQw4w9WgXcQ"]`
* `[iframe url="https://www.vimeo.com/watch?v=dQw4w9WgXcQ"]`

## Installation

Install via pip: `pip install django-template-shortcodes`
Or clone the [Git repository](https://github.com/emilbjorklund/django-shortcodes).

## Usage

Parse shortcodes:

    {% load shortcodes_filters %}
    {{ text|shortcodes|safe }}

Remove shortcodes (completely, including contents inside):
    
    {% load shortcodes_filters %}
    {{ text|removeshortcodes|safe }}

