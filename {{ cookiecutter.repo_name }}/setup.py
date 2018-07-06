{{ cookiecutter.shebang_python }}
{{ cookiecutter.shebang_coding }}

import sys
import types

from io import StringIO
from os import path as op
from os.path import join
from textwrap import dedent

from setuptools import (
    find_packages,
    setup,
)
from setuptools.command.test import test as TestCommand

import {{ cookiecutter.repo_name }}


def _read(filename: str) -> str:
    try:
        fp = open(join(op.dirname(__file__), filename))
        try:
            return fp.read()
        finally:
            fp.close()
    except (IOError, OSError):  # IOError/2.7, OSError/3.5
        return str()


def _read_requirements(filename: str) -> List[str]:
    is_valid = lambda _: _ and not any(_.startswith(ch) for ch in ['#', '-'])

    data = getattr(types, 'UnicodeType', str)(_read(filename))
    return list((_.strip() for _ in StringIO(data) if is_valid(_.strip())))  # type: ignore


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        super().initialize_options()
        self.pytest_args = []

    def run_tests(self):
        # Import here, cause outside the eggs aren't loaded.
        import pytest

        errno = pytest.main(args=self.pytest_args)
        sys.exit(errno)


setup_params = dict(
    name='{{ cookiecutter.class_name }}',
    version={{ cookiecutter.repo_name }}.__version__,
    description='{{ cookiecutter.brief }}',
    long_description=dedent("""
        {{ cookiecutter.description | replace('\n', '\n        ') }}
        """).strip(),
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    url='{{ cookiecutter.url }}',

    classifiers=dedent("""
        Natural Language :: English
        Development Status :: 1 - Planning
        Operating System :: POSIX :: Linux
        Programming Language :: Python
        Programming Language :: Python :: {{ cookiecutter.python_version }}
        """),
    license='{{ cookiecutter.license }}',
    keywords=[],

    packages=find_packages(),
    # package_dir={'': 'src'},  # tell distutils packages are under `src`
    include_package_data=True,
    # package_data={
    #     # If any package contains *.txt files, include them:
    #     '': ['*.txt'],
    #     # And include any *.dat files found in the `data` subdirectory
    #     # of the `mypkg` package, also:
    #     'mypkg': ['data/*.dat'],
    # },
    # # ...but exclude README.txt from all packages
    # exclude_package_data={'': ['README.txt']},
    # data_files=[
    #     ('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
    #     ('config', ['cfg/data.cfg']),
    #     ('/etc/init.d', ['init-script']),
    # ],
    zip_safe=False,

    # entry_points={
    #     'console_scripts': [
    #         'foo = {{ cookiecutter.repo_name }}.some_module:main_func',
    #         'bar = other_module:some_func',
    #     ],
    #     'gui_scripts': [
    #         'baz = my_package_gui:start_func',
    #     ]
    # },

    install_requires=_read_requirements('requirements.txt'),
    # extras_require={
    #     'PDF':  ['ReportLab>=1.2', "RXP'],
    #     'reST': ['docutils>=0.3'],
    # },
    setup_requires=[
        'wheel',
{%- if cookiecutter.enable_sphinx == 'true' %}
        'sphinx',
        'sphinx-pypi-upload3',
{%- endif %}
    ],
    tests_require=_read_requirements('requirements-test.txt'),

    cmdclass={'test': PyTest},
)


def main() -> None:
    setup(**setup_params)


if __name__ == '__main__':
    main()
