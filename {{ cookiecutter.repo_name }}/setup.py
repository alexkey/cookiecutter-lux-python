{{ cookiecutter.shebang_python }}

import string
import sys
import types

from pathlib import Path
from textwrap import dedent
from typing import List

from setuptools import (
    find_packages,
    setup,
)

import {{ cookiecutter.repo_name }} as root


def read_requirements(file: str) -> List[str]:
    if not Path(file).is_file():
        raise FileNotFoundError(file)

    alphabet = f'{string.digits}{string.ascii_lowercase}_-=.'

    with open(file) as fd:
        return list(
                    filter(
                           lambda x: (
                                      (x[0] in string.ascii_lowercase if x else False) and
                                      all(c in alphabet for c in x)
                                      ),
                           map(lambda s: s.split('#', 1)[0].strip().lower(), fd)
                           )
                    )


setup_params = dict(
    name='{{ cookiecutter.name | lower | replace('_', '-') }}',

    version=root.__version__,

    description='{{ cookiecutter.brief }}',

    long_description=dedent("""
        {{ cookiecutter.description | replace('\n', '\n        ') }}
        """).strip(),

    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    url='{{ cookiecutter.url }}',

    classifiers=dedent("""
        Natural Language :: English
        Operating System :: POSIX :: Linux
        Programming Language :: Python :: {{ cookiecutter.python_version }}
        """),
    license='{{ cookiecutter.license }}',
    keywords=[],

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    entry_points={
        'console_scripts': [
            '{{ cookiecutter.repo_name }} = {{ cookiecutter.repo_name }}.{{ cookiecutter.repo_name }}:main',
        ]
    },

    install_requires=read_requirements('requirements.txt'),
    extras_require={},
    setup_requires=[
{%- if cookiecutter.enable_sphinx == 'true' %}
        'sphinx',
{%- endif %}
        'wheel',
    ],
    tests_require=read_requirements('requirements-test.txt')
)


def main() -> None:
    setup(**setup_params)


if __name__ == '__main__':
    main()
