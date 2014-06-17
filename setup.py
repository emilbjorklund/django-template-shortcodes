from distutils.core import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="django-shortcodes",
    version="0.0.1",
    description="WordPress shortcode support for Django",
    author="Emil Björklund",
    author_email="emil.bjorklund@inuse.se",
    maintainer="Emil Björklund",
    maintainer_email="emil.bjorklund@inuse.se",
    url="https://github.com/emilbjorklund/django-shortcodes",
    license="MIT",
    packages=[
        "shortcodes",
        "shortcodes.parsers",
        "shortcodes.templatetags",
    ],
    long_description=read("README.markdown"),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)
