=======================
cookiecutter-lux-python
=======================

Cookiecutter_ template for a Python package.

The boilerplate Python project that aims to create facility for maintaining of
the package easily. It considering tools for building, testing and distribution.

Breaking Changes
----------------

**Attention!** There are breaking changes since `version 1.0`_.

Get Started
-----------

This template provides a basic structure for an idiomatic Python package with a
convenient Makefile-facility and additional helpers.

Template can be configured using Cookiecutter_'s CLI or by altering parameters
directly in `<cookiecutter.json>`_.

Features
--------

* Auto creation of virtual environment: ``make venv``.

* Building and packaging: ``make dist``, ``make sdist``, ``make install``,
  ``make uninstall``.

* Testing: ``make check``.

* Render project's documentation using Sphinx_: ``make html``, ``make pdf``.

* Managing Vagrant_ virtual machines: ``make up``, ``make ssh``, ``make halt``,
  ``make destroy``.

* `GNU-style cleaners`_: ``make clean``, ``make distclean``,
  ``make mostlyclean``.

.. _`version 1.0`: https://github.com/alexkey/cookiecutter-lux-python/releases/tag/1.0
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Sphinx: http://www.sphinx-doc.org
.. _Vagrant: https://www.vagrantup.com
.. _`GNU-style cleaners`: https://www.gnu.org/prep/standards/html_node/Standard-Targets.html#Standard-Targets
