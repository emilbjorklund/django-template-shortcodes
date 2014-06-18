# django-template-shortcodes

THIS IS EXPERIMENTAL STUFF. Don't use it. Probably.

This package provides some [WordPress
shortcode](http://en.support.wordpress.com/shortcodes/) support for Django
templates. It is heavily based on [AGoodId's version of django-shortcodes](https://github.com/AGoodId/django-shortcodes) (in turn based on https://code.google.com/p/django-shortcodes/), as well as [WP Export Parser](https://github.com/RealGeeks/wp_export_parser) for the regex parts, lifted from WordPress.

## Installation

Clone the [Git repository](https://github.com/emilbjorklund/django-shortcodes). Not on pypi yet.

## Usage

    {% load shortcodes_filters %}
    {{ text|shortcodes|safe }}
