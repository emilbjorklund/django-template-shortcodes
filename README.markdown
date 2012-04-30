# django-shortcodes

This package provides [WordPress
shortcode](http://en.support.wordpress.com/shortcodes/) support for Django
templates. It is based on [django-shortcodes](http://code.google.com/p/django-shortcodes)

## Installation

Use `pip install django-shortcodes` or clone the [Git
repository](https://github.com/agoodid/django-shortcodes).

## Usage

    {% load shortcodes_filters %}
    {{ text|shortcodes|safe }}
