"""
{% set rst_ul = "=" * cookiecutter.distro_name|length -%}
{{ rst_ul }}
{{ cookiecutter.distro_name }}
{{ rst_ul }}

{{ cookiecutter.short_description }}
"""

import sys
import logging
import pkg_resources

# Custom logger
LOG = logging.getLogger(name=__name__)
LOG.addHandler(logging.NullHandler())

# PEP 396 style version marker
try:
    __version__ = pkg_resources.get_distribution({{ cookiecutter.distro_name | pprint }}).version
except:
    LOG.warning("Could not get the package version from pkg_resources")
    __version__ = 'unknown'

# FIXME: This is just for checking doctests setup. You may remove this function.
# See tests/test_doctests.py from this distro root
def identity(obj):
    """Returns the ``obj`` parameter itself

    :param obj: The parameter to be returned
    :return: ``obj`` itself

        >>> identity(5)
        5
        >>> foo = 2
        >>> identity(foo) is foo
        True
    """
    return obj
