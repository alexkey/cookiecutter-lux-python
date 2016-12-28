SHELL = /bin/bash


##
# Definitions.

.SUFFIXES:

srcdir = $(CURDIR)/{{ cookiecutter.repo_name }}
builddir = $(CURDIR)/build
distdir = $(CURDIR)/dist
docdir = $(CURDIR)/doc

## Tools.

tools =
doctools =

ifeq (Darwin,$(shell uname -s))
	SED = gsed
else
	SED = sed
endif

ifeq (,$(shell which ${SED}))
	tools += $(SED)
endif

VAGRANT = vagrant
ifeq (,$(shell which ${VAGRANT}))
	tools += $(VAGRANT)
endif

## OS specifics.

ifneq (,$(shell which lsb_release))
	OS_CODENAME = $(shell lsb_release -c | sed -E "s/\s*\S+\s+(\S+)/\1/g")
endif

## Virtual environment.

VENV_DIR = $(CURDIR)/.venv

VENV = virtualenv
ifeq (,$(shell which ${VENV}))
	tools += $(VENV)
endif

## Documentation.

PDFLATEX = pdflatex
ifeq (,$(shell which ${PDFLATEX}))
	doctools += $(PDFLATEX)
endif

SPHINX_BUILDDIR = $(docdir)/_build
SPHINX_STATIC = $(docdir)/_static
SPHINX_TEMPLATES = $(docdir)/_templates

SPHINX_OPTS = -d $(SPHINX_BUILDDIR)/doctrees -D latex_paper_size=a4 \
	$(CURDIR)/doc

SPHINX = sphinx-build
ifeq (,$(shell which ${SPHINX}))
	doctools += $(SPHINX)
endif


##
# All.

all: help
ifdef tools
	$(error Can't find tools:${tools})
endif


##
# Virtual environment targets.

$(VENV_DIR): requirements.txt requirements-test.txt
	@$(VENV) -p {{ cookiecutter.python }} "$(VENV_DIR)"
	@"$(VENV_DIR)/bin"/pip install -U setuptools pip
	@"$(VENV_DIR)/bin"/pip install -Ur $<
	@"$(VENV_DIR)/bin"/pip install -Ur $(word 2,$^)

.PHONY: venv
# target: venv – Create the virtual environment
venv: $(VENV_DIR)


##
# Building and packaging targets.

.PHONY: dist
# target: dist – Create a binary (wheel) distribution
dist:
	@[ ! -f "$(distdir)"/*.whl ]
	@python setup.py bdist_wheel

.PHONY: sdist
# target: sdist – Create a source distribution
sdist:
	@[ ! -f "$(distdir)"/*.tar.gz ]
	@python setup.py sdist

.PHONY: install
# target: install – Install project sources in "development mode"
install:
	@python setup.py develop

.PHONY: uninstall
# target: uninstall – Uninstall project sources
uninstall:
	@python setup.py develop --uninstall


##
# Testing targets.

.PHONY: test
# target: test – Run project tests
test:
	@python setup.py test


##
# Documentation targets.

.PHONY: doc
doc:
ifdef doctools
	$(error Can't find tools:${doctools})
endif

.PHONY: html
# target: html – Render standalone HTML files
html:
	@$(SPHINX) -b html $(SPHINX_OPTS) "$(SPHINX_BUILDDIR)/html"

.PHONY: pdf
# target: pdf – Render LaTeX files and run them through pdflatex
pdf:
	@$(SPHINX) -b latex $(SPHINX_OPTS) "$(SPHINX_BUILDDIR)/latex" && \
		$(MAKE) -C "$(SPHINX_BUILDDIR)/latex" all-pdf


##
# Vagrant targets.

.PHONY: up
# target: up – Start and provision the Vagrant environment
up:
	@$(VAGRANT) up

.PHONY: ssh
# target: ssh – Connect to machine via SSH as root
ssh:
	@$(VAGRANT) ssh -- -l root

.PHONY: halt
# target: halt – Stop the Vagrant machine
halt:
	@$(VAGRANT) halt

.PHONY: destroy
# target: destroy – Stop and delete all traces of the Vagrant machine
destroy:
	@$(VAGRANT) destroy


##
# Auxiliary targets.

.PHONY: help
# target: help – Display all callable targets
help:
	@echo
	@egrep "^\s*#\s*target\s*:\s*" [Mm]akefile \
	| $(SED) -r "s/^\s*#\s*target\s*:\s*//g"
	@echo

## Cleaners.

.PHONY: clean
# target: clean – Clean the project's directrory
clean:
	@find "$(VENV_DIR)" \
		-name *.py[cod] -exec rm -fv {} + -o \
		-name __pycache__ -exec rm -rfv {} +

.PHONY: distclean
# target: distclean – Clean the project's build output.
distclean:
	@find "$(CURDIR)" -path "$(VENV_DIR)" -prune -o \
		-name *.egg-info -exec rm -rfv {} + -o \
		-name *.dist-info -exec rm -rfv {} +

	@rm -rfv \
		"$(builddir)" \
		"$(distdir)" \
		"$(SPHINX_BUILDDIR)" \
		"$(SPHINX_STATIC)" \
		"$(SPHINX_TEMPLATES)"

.PHONY: mostlyclean
# target: mostlyclean – Delete almost everything
mostlyclean: clean distclean
	@find "$(CURDIR)" -name .DS_Store -exec rm -fv {} +

	@rm -rfv \
		"$(CURDIR)/.vagrant" \
		"$(VENV_DIR)"
