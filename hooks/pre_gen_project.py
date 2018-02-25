# See http://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html

import keyword
import re
import sys

python_name_rx = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]+$')

def validate_package_name():
    pkg_name = "{{ cookiecutter.package_name }}"
    for level, namespace in enumerate(pkg_name.split('.')):
        # Legal Python name
        if not python_name_rx.match(namespace):
            print("Forbidden: '{}' is not a valid Python package name".format(pkg_name))
            sys.exit(1)

        # Not a keyword
        if keyword.iskeyword(namespace):
            print("Forbidden: '{}' contains a Python keyword.".format(pkg_name))
            sys.exit(1)

        # Not a builtin
        try:
            exec("x = {}".format(namespace), {}, {})
        except NameError:
            pass
        else:
            print("Forbidden: illegal usage of builtin in '{}'.".format(pkg_name))
            sys.exit(1)

        # Root not a module from stdlib or already installed
        if level > 0:
            continue
        try:
            exec("import {}".format(namespace), {}, {})
        except ImportError:
            pass
        else:
            print("Warning: top level of '{}' is already an installed module.".format(pkg_name))
            print("It could not work as expected. Please consider renaming '{}'.".format(namespace))
            sys.exit(1)

validate_package_name()
