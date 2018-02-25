# -*- coding: utf-8 -*-
"""\
{%- set rst_ul = "=" * cookiecutter.distro_name|length -%}
{{ rst_ul }}
{{ cookiecutter.distro_name }}
{{ rst_ul }}

{{ cookiecutter.short_description }}
"""

# FIXME: Please read http://pythonhosted.org/setuptools/setuptools.html to
#        customize in depth your setup script

from setuptools import setup
import os, sys

version = '1.0.0.dev0'

this_directory = os.path.abspath(os.path.dirname(__file__))

def read(*names):
    return open(os.path.join(this_directory, *names), 'r').read().strip()

{%- if cookiecutter.use_sphinx %}
long_description = '\n\n'.join(
    [read(*paths) for paths in (('README.rst',),
                               ('doc', 'contributors.rst'),
                               ('doc', 'changes.rst'))]
    )
dev_require = ['Sphinx']
{% else %}
long_description = '\n\n'.join(
    [read(*paths) for paths in (('README.rst',),('CHANGES.rst',))]
    )
dev_require = []
{% endif -%}


setup(name='{{ cookiecutter.distro_name }}',
      version=version,
      description="{{ cookiecutter.short_description }}",
      long_description=long_description,
      # FIXME: Add more classifiers from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: {{ cookiecutter.license }}"
          ],
      keywords='',  # FIXME: Add whatefer fits
      author='{{ cookiecutter.full_name }}',
      author_email='{{ cookiecutter.email }}',
      url='http://pypi.python.org/pypi/{{ cookiecutter.distro_name }}',
      license='{{ cookiecutter.license }}',
      packages='{{ cookiecutter.package_name }}',
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # 3rd party
          'setuptools'
          # Others
          ],
      entry_points={
{%- if cookiecutter.cli_command_name|length > 0 %}
          'console_scripts': ['{{ cookiecutter.cli_command_name }}={{ cookiecutter.package_name }}.__main__:main']
{% endif -%}
          },
      tests_require=dev_require,
      test_suite='tests.all_tests',
      extras_require={
          'dev': dev_require
      })
