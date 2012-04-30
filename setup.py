from distutils.core import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="django-shortcodes",
    version="0.2.0",
    description="WordPress shortcode support for Django",
    author="Mark Steadman",
    author_email="marksteadman@me.com",
    maintainer="AGoodId",
    maintainer_email="teknik@agoodid.se",
    url="https://github.com/agoodid/django-shortcodes",
    license="MIT",
    packages=[
        "shortcodes",
        "shortcodes.parsers",
        "shortcodes.templatetags",
    ],
    long_description=read("README.markdown"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)
