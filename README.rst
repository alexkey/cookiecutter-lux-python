=======================
cookiecutter-lux-python
=======================

Cookiecutter_ template for a Python package.

The boilerplate Python project that aims to create facility for maintaining of
the package easily. It considering tools for building, testing and distribution.


Get Started
-----------

This template provides a basic structure for an idiomatic Python package with a
convenient Makefile-facility and additional helpers.

Template can be configured using Cookiecutter_'s CLI or by altering parameters
directly in `<cookiecutter.json>`_.


Requirements
------------

There are a couple of tools for building, packaging, documentation and so on,
that must be installed.

Main tools are:

* GNU sed (``brew install gnu-sed`` for macOS),

* ack (optionally),

* awk,

* Docker,

* Vagrant (optionally),

* *virtualenv* at global level.

To check availability of main tools just type ``make``.

Tools for documenting the package:

* *Sphinx* package (sphinx-build, sphinx-apidoc),

* MacTeX_ distribution (optionally; pdflatex CLI tool, fonts, styles – for
  rendering docs in PDF format).

To check availability of documentation tools type ``make doc``.


Makefile Targets and Features
-----------------------------

* Compile Pip requirements from ``requirements.in`` to ``requirements.txt``::

    make requirements

* Auto creation of virtual environment using ``requirements.txt`` and
  ``requirements-test.txt``::

    make venv

* Installing package into a virtual environment in so-called "development mode"
  and removing it later::

    # after `make venv`

    make install

    # (hard working here)

    make uninstall

* Testing the package using PyTest_::

    make check

* Building and packaging::

    # Binary wheel distribution
    make dist

    # Build tarball with sources (source distribution)
    make sdist

* Local docker statistics::

    # Display system-wide information
    docker-info

    # Show all images and containers
    docker-stats

    # Same as `stats`, but more details provided
    docker-statsall

* Build and run interactive containers::

    # Build image from scratch
    docker-build

    # Run temporary container in an interactive mode
    docker-run

* Docker cleaners::

    # Clean dangling images
    docker-clean

    # Clean built containers
    docker-distclean

    # Remove all unused images, built containers and volumes
    docker-mostlyclean

* Render project's documentation using Sphinx_::

    make apidoc  # to create an API documentation

    make html
    # or
    make pdf

* Managing Vagrant_ virtual machines::

    # Update the machine within current Vagrant environment
    make vagrant-update

    # Start and provision the Vagrant environment
    make vagrant-up

    # Connect to the machine via SSH as root
    make vagrant-ssh

    # Stop the machine
    make vagrant-halt

    # Stop and delete all traces of the machine
    make vagrant-destroy

* `GNU-style cleaners`_::

    # Clean the project's directrory (Python related caches)
    make clean

    # Clean the project's build output (Eggs, ditributions, builds)
    make distclean

    # Delete almost everything (including Vagrant data and virtual environment)
    make mostlyclean




.. _Cookiecutter: https://github.com/audreyr/cookiecutter/
.. _PyTest: https://docs.pytest.org/en/latest/
.. _Sphinx: http://www.sphinx-doc.org/
.. _Vagrant: https://www.vagrantup.com/
.. _`GNU-style cleaners`: https://www.gnu.org/prep/standards/html_node/Standard-Targets.html#Standard-Targets
