# -*- coding: utf-8 -*-
"""\
{% set rst_ul = "=" * cookiecutter.distro_name|length -%}
{{ rst_ul }}
{{ cookiecutter.distro_name }}
{{ rst_ul }}

Tests package
"""
import unittest

from .resources import tests_directory

def all_tests():
    return unittest.defaultTestLoader.discover(tests_directory)
