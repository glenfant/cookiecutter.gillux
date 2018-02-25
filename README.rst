.. _home:

===================
cookiecutter.gillux
===================

------------

``cookiecutter.gillux`` is just another Python project scaffolding template
for the great `cookiecutter <https://github.com/audreyr/cookiecutter>`_ by
Audrey Roy.

It is the successor of my - now unmaintained - `bobtemplates.gillux
<https://github.com/glenfant/bobtemplates.gillux>`_ I stopped using.

Features
========

- Python 3 only! We don't start anymore new projects with Python 2 today.
- Generic setuptools enabled package
- Any level of namespaced package
- Pre cooked Sphinx skeleton
- Custom shell command (option)
- Tests in their own file layout outside the package source tree.


Files layout for the namespace package ``foo.bar``:

.. code:: console

   README.rst
   setup.py
   setup.cfg
   src/
     foo/
       bar/
         __init__.py
     	 __main__.py  # Optional
   tests/
     # Unittests
     __init__.py
     test_sample.py
   doc/
   	 # Sphinx pre-cooked skeleton
     conf.py
     # ...

Usage
=====

.. code:: console

   cookiecutter https://github.com/glenfant/cookiecutter.gillux

Please read `cookiecutter`_ documentation for other usage options and
configuration.

The cookiecutter wizard questions
=================================

As usual, you may customize the ``cookiecutter.json`` file as described in
`cookiecutter`_ documentation to customize the various options:

``full_name``

  Your full name as it appears in the product metadata and various places. The
  default one is mine: "Gilles Lenfant".

``email``

  Your contact email that will appear on PyPI and in the documentation.

``distro_name``

  The name of your project as Python distro name in PyPI.

``package_name``

  The name of the root package. Must be a valid Python name, dotted name are
  allowed to provide a namespace package (as ``foo.bar.baz``). Usually, the
  same as ``distro_name`` (the default value) but you can choose another one.

``version``

  The initial version of your creation. Default: ``1.0.0``

``cli_command_name``

  Type the name of a shell command that's installed with your package. If a
  name is provided, a ``__main__.py`` module will be added in the package. If
  you don't want a command (you make a pure lib), just leave an empty value.

``use_sphinx```

  Provide a configured skeleton for a Sphinx documentation in the ``doc/`` folder.

``license``

  Choose the license you prefer among the ones proposed.
