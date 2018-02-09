------------

.. code:: console
                   _    _                 _   _                 _ _ _
                  | |  (_)               | | | |               (_) | |
    ___ ___   ___ | | ___  ___  ___ _   _| |_| |_ ___ _ __ __ _ _| | |_   ___  __
   / __/ _ \ / _ \| |/ / |/ _ \/ __| | | | __| __/ _ \ '__/ _` | | | | | | \ \/ /
  | (_| (_) | (_) |   <| |  __/ (__| |_| | |_| ||  __/ |_| (_| | | | | |_| |>  <
   \___\___/ \___/|_|\_\_|\___|\___|\__,_|\__|\__\___|_(_)\__, |_|_|_|\__,_/_/\_\
                                                           __/ |
                                                          |___/
------------

``cookiecutter.gillux`` is just another Python project scaffolding template
for the great `cookiecutter <https://github.com/audreyr/cookiecutter>`_ by
Audrey Roy. It is the successor of my - now unmaintained -
`bobtemplates.gillux <https://github.com/glenfant/bobtemplates.gillux>`_ I
stopped using.

Some features:

- Python 3 only, we don't start anymore new projects with Python 2 today.
- Generic setuptools enabled package
- Any level of namespaced package
- Pre cooked Sphinx skeleton
- Custom shell command (option)
- Tests in their own file layout outside the package source tree.


Sample layout:

.. code:: console

   README.rst
   setup.py
   setup.cfg
   src/
     foo/
       bar/
         __init__.py
     	 __main__.py
   tests/
     # Unittests
     __init__.py
     test_sample.py
   doc/
   	 # Sphinx pre-cooked skeleton
