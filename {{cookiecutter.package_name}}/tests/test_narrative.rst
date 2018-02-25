{% set rst_ul = "=" * cookiecutter.distro_name|length -%}
{{ rst_ul }}
{{ cookiecutter.distro_name }}
{{ rst_ul }}

FIXME: Write down the tests for your package

.. code:: pycon

   >>> dummy() is None
   True
