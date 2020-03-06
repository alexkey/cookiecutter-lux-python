=======================
cookiecutter-lux-python
=======================

Cookiecutter_ template for a Python package.

The boilerplate Python project that aims to create facility for maintaining of the package
easily. It considering tools for building, testing and distribution.


Get Started
-----------

This template provides a basic structure for an idiomatic Python package with a convenient
Makefile-facility and additional helpers.

Template can be configured using Cookiecutter_'s CLI or by altering parameters directly in
`<cookiecutter.json>`_.


Requirements
------------

There are a couple of tools for building, packaging, documentation and so on, that must be
installed.

* GNU sed (``brew install gnu-sed`` for macOS),

* ripgrep (optionally),

* awk,

* Docker,

* *Virtualenv*,

* *Sphinx* (for sphinx-build and sphinx-apidoc).

To check availability of main tools just type ``make`` or ``make doc``.


Features
--------

* To get help about available Makefile targets type::

    make help

Creating the virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Compile Pip requirements from ``requirements.in`` to ``requirements.txt`` using *pip-tools*
   (via Docker)::

    make requirements

2. Create the new virtual environment based on ``requirements.txt`` and
   ``requirements-test.txt``::

    make venv

3. Install the package into a virtual environment in so-called "development mode"::

    source .venv/bin/activate
    make install

    # ...hard working here...

    make uninstall
    deactivate

Testing the package
~~~~~~~~~~~~~~~~~~~

Pytest_ is used as a test tool by default.

* To run tests type (within a virtual environment)::

    make check

Building the package from scratch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Create a source distribution (tarball with sources)::

    make sdist
    ls -al dist/*.tar.gz

* Create a binary (wheel) distribution::

    make dist
    ls -al dist/*.whl

Dealing with containers
~~~~~~~~~~~~~~~~~~~~~~~

* Display system-wide information::

    make docker-info

* Show all images, containers and volumes::

    make docker-stats

* Build the image according to ``Dockerfile``::

    make docker-build

* Run temporary container in an interactive mode::

    make docker-run

* Remove all unused images, built containers and volumes::

    make docker-clean

Documenting the project using Sphinx_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Build an API documentation::

    make apidoc

2. Build the documentation as a standalone HTML files::

    make html
    open doc/_build/html/index.html

`GNU-style cleaners`_
~~~~~~~~~~~~~~~~~~~~~

* Clean the project's directory (precompiled and temporary files)::

    make clean

* Clean the project's build output (eggs, distributions, builds)::

    make distclean

* Delete almost everything (including virtual environment)::

    make mostlyclean


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Pytest: https://docs.pytest.org/en/latest
.. _Sphinx: http://www.sphinx-doc.org
.. _`GNU-style cleaners`: https://www.gnu.org/prep/standards/html_node/Standard-Targets.html#Standard-Targets
