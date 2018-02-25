# See http://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html

from datetime import datetime
import io
import pathlib
import shlex
import shutil
import sys


def is_trueish(expression: str) -> bool:
    """True if string and "True", "Yes", "On" (ignorecase), False otherwise"""
    expression = str(expression).strip().lower()
    return expression in {'true', 'yes', 'on'}


def is_falseish(expression: str) ->  bool:
    return not is_trueish(expression)


def build_namespace_dirs():
    """Make namespace package dirs id needed"""
    pkg_name = "{{ cookiecutter.package_name }}"
    parts = pkg_name.split('.')
    if len(parts) > 1:
        # Transform src/foo.bar.baz into src/foo/bar/baz and move content
        parent = pathlib.Path.cwd() / 'src'
        pkg_src = parent / pkg_name
        for name in parts:
            parent /= name
        shutil.copytree(pkg_src, parent)
        shutil.rmtree(pkg_src)


SPHINX_CONF_EPILOG = """

# -- Customization by cookiecutter.gillux --------------------------
import time
import pkg_resources

project = "{{ cookiecutter.distro_name }}"

# The short X.Y version.
version = pkg_resources.get_distribution(project).version
release = version

html_title = "{0} v{1}".format(project, release)
creation_year = %(this_year)s
this_year = time.localtime().tm_year
if this_year > creation_year:
    copyright = '{}-{}, %(organization)s'.format(creation_year, this_year)
else:
    copyright = '{}, %(organization)s'.format(creation_year)
""" % {
    'organization': "{{ cookiecutter.organization }}",
    'this_year': datetime.now().year
}

def build_sphinx_skeleton():
    """Build Sphinx skeleton"""
    # Some checks
    if is_falseish("{{ cookiecutter.use_sphinx }}"):
        return
    try:
        from sphinx.cmd.quickstart import main as sphinx_quickstart
    except ImportError:
        print("Sphinx must be installed to build a Sphinx doc skeleton. Cancel!")
        sys.exit(0)

    # Make the options as expected in sys.argv
    sys_argv = (
        "-q --sep --dot _ -p {{ cookiecutter.distro_name}} "
        '-a "{{ cookiecutter.full_name }}" '
        "--ext-autodoc --ext-todo --ext-ifconfig --ext-viewcode --makefile --batchfile "
        "doc"
        )

    # Build the skeleton
    sphinx_quickstart(shlex.split(sys_argv))

    # Tweak the Sphinx conf.py
    with io.open(pathlib.Path('.') / 'doc' / 'source' / 'conf.py', 'a') as handle:
        handle.write(SPHINX_CONF_EPILOG)


build_namespace_dirs()
build_sphinx_skeleton()
print("Done")
print('Grep "FIXME: ..." in this new skeleton and follow directions...')
