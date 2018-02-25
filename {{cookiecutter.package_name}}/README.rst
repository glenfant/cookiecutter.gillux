{%- set rst_ul = "=" * cookiecutter.distro_name|length -%}
{{ rst_ul }}
{{ cookiecutter.distro_name }}
{{ rst_ul }}

{{ cookiecutter.short_description }}

FIXME: provide a two paragraphs summary of this package

Full documentation and API
==========================

FIXME: Provide the URL of the documentation (@ readthedocs.org ?)

Developer notes
===============

Please use a virtualenv to maintain this package, but I should not need to say that.

Grab the source from the SCM repository:

.. code:: console

  $ python setup.py develop
  $ pip install {{ cookiecutter.distro_name }}[dev]

Run the tests:

.. code:: console

  $ python setup.py test
  $ python run_tests.py

{%- if cookiecutter.use_sphinx %}
Build the Sphinx documentation:

.. code:: console

  $ python setup.py build_sphinx
  $ firefox build/sphinx/html/index.html
{% endif -%}

License
=======

This software is protected by the terms of {{ cookiecutter.license }}.

Links
=====

FIXME: Provide real links

Project home page

  http://www.mystuff.com/project

Source code

  http://www.mystuff.com/source

Issue tracker

  http://www.mystuff.com/issues
