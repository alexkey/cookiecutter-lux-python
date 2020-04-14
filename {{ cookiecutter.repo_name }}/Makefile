SHELL = /bin/bash


##
# Definitions

### Error codes

ERROR_PYTHON_VERSION = 10
ERROR_PYTHON_TESTTOOL = 20


### Main defs

PACKAGE_NAME = {{ cookiecutter.repo_name }}
PACKAGE_VERSION = {{ cookiecutter.version }}

srcdir = $(CURDIR)/$(PACKAGE_NAME)
builddir = $(CURDIR)/build
distdir = $(CURDIR)/dist
{%- if cookiecutter.enable_sphinx == 'true' %}
docdir = $(CURDIR)/doc
autodocdir = $(docdir)/autodoc
{%- endif %}


### Tools

tools =

ifeq ($(shell uname -s),Darwin)
	SED = gsed
else
	SED = sed
endif

ifeq ($(shell which ${SED}),)
	tools += $(SED)
endif

GREPTOOL = rg
ifeq ($(shell which ${GREPTOOL}),)
	GREPTOOL = egrep
endif

AWK = awk
ifeq ($(shell which ${AWK}),)
	tools += $(AWK)
endif


### Python

PYTHON = python3
PYTHON_BIN = $(shell which ${PYTHON})
ifeq ($(PYTHON_BIN),)
	tools += $(PYTHON)
endif

PIP = $(PYTHON) -m pip

PYTHON3_VER = {{ cookiecutter.python_version }}
PYTHON_VERSION_INFO = $(shell ${PYTHON} -c 'if 1: \
	from sys import version_info; \
	print("{v.major}.{v.minor}.{v.micro}".format(v=version_info)) \
	')
PYTHON_INFO = $(PYTHON_BIN) -> $(PYTHON_VERSION_INFO)

VIRTUALENV = virtualenv
VIRTUALENV_BIN = $(shell which ${VIRTUALENV})
ifeq ($(VIRTUALENV_BIN),)
	tools += $(VIRTUALENV)
endif

VENV_DIR = .venv

PYTHON_STD_PKGS = \
	pip \
	setuptools \
	wheel

TESTTOOL = pytest


### Docker

DOCKER = docker
ifeq ($(shell which ${DOCKER}),)
	tools += $(DOCKER)
endif

DOCKER_PS_ARGS = -s

DOCKER_BASE_IMAGE = python:$(PYTHON3_VER)-slim-buster
DOCKER_PORT = 8088

{%- if cookiecutter.enable_sphinx == 'true' %}


### Documentation

doctools =

SPHINX_BUILDDIR = $(docdir)/_build
SPHINX_STATIC = $(docdir)/_static
SPHINX_TEMPLATES = $(docdir)/_templates

AUTODOC_EXCLUDE_MODULES =

SPHINX = sphinx-build
ifeq ($(shell which ${SPHINX}),)
	doctools += $(SPHINX)
endif

SPHINX_OPTS = -d "$(SPHINX_BUILDDIR)/doctrees" "$(docdir)"

SPHINX_APIDOC = sphinx-apidoc
ifeq ($(shell which ${SPHINX_APIDOC}),)
	doctools += $(SPHINX_APIDOC)
endif
{%- endif %}


##
# All

all: help
ifdef tools
	$(error Can't find tools:${tools})
endif
	@if [[ "$(PYTHON_VERSION_INFO)" == "$(PYTHON3_VER)" ]]; then \
		echo "INFO: Found Python interpreter: $(PYTHON_INFO)"; \
	else \
		echo -n "WARNING: Incompatible Python interpreter version: $(PYTHON_INFO) "; \
		echo "(instead of $(PYTHON3_VER))"; \
		echo "INFO: Try \`make python-install\`"; \
		exit $(ERROR_PYTHON_VERSION); \
	fi


##
# Virtual environment

.PHONY: requirements
# target: requirements - Compile Pip requirements
requirements:
	@echo
	@$(DOCKER) run -it --rm \
		-v "$(CURDIR)/requirements.in:/requirements.in" \
		-v "$(CURDIR)/requirements.txt:/requirements.txt" \
	"$(DOCKER_BASE_IMAGE)" "$(SHELL)" -c \
		'pip install -U pip pip-tools && \
		CUSTOM_COMPILE_COMMAND="make requirements" \
			pip-compile -o requirements.tmp requirements.in && \
		cat requirements.tmp > requirements.txt'

$(VENV_DIR): requirements.txt requirements-test.txt
	@echo
	@$(VIRTUALENV) -p $(PYTHON3_VER) "$(VENV_DIR)";
	@if [[ -d "$(VENV_DIR)" ]]; then \
		\
		source "$(VENV_DIR)/bin/activate"; \
		\
			$(PIP) install -U $(PYTHON_STD_PKGS); \
			$(PIP) install -Ur $<; \
			$(PIP) install -Ur $(word 2,$^); \
		\
		echo ""; \
		$(PIP) list; \
		echo ""; \
		\
		deactivate; \
	fi

.PHONY: venv
# target: venv - Create the virtual environment
venv: $(VENV_DIR)


##
# Building and packaging

.PHONY: sdist
# target: sdist - Create a source distribution
sdist:
	@echo
	@[[ ! -f "$(distdir)"/*.tar.gz ]] && $(PYTHON) setup.py sdist

.PHONY: dist
# target: dist - Create a binary (wheel) distribution
dist:
	@echo
	@[[ ! -f "$(distdir)"/*.whl ]] && $(PYTHON) setup.py bdist_wheel

.PHONY: install
# target: install - Install project sources in "development mode"
install:
	@echo
	@$(PYTHON) setup.py develop

.PHONY: uninstall
# target: uninstall - Uninstall project sources
uninstall:
	@echo
	@$(PYTHON) setup.py develop --uninstall


##
# Testing

.PHONY: check
# target: check - Run tests
check:
	@echo
	@if [[ -n "$(shell which ${TESTTOOL})" ]]; then \
		$(TESTTOOL) "$(srcdir)"; \
	else \
		echo "ERROR: \`$(TESTTOOL)\` binary is missing"; \
		exit $(ERROR_PYTHON_TESTTOOL); \
	fi


##
# Docker

.PHONY: docker-info
# target: docker-info - Display system-wide information
docker-info:
	@echo
	@$(DOCKER) info

.PHONY: docker-stats
# target: docker-stats - Show all images, containers and volumes
docker-stats:
	@echo
	@$(DOCKER) images -a
	@echo
	@$(DOCKER) ps -a $(DOCKER_PS_ARGS)
	@echo
	@$(DOCKER) volume ls

.PHONY: docker-build
# target: docker-build - Build image from scratch
docker-build: dist
	@echo
	@$(DOCKER) build -f "$(CURDIR)/Dockerfile" -t $(PACKAGE_NAME):$(PACKAGE_VERSION) \
		--no-cache .

.PHONY: docker-run
# target: docker-run - Run temporary container in an interactive mode
docker-run:
	@echo
	@$(DOCKER) run -it --rm -p $(DOCKER_PORT):$(DOCKER_PORT) \
		$(PACKAGE_NAME):$(PACKAGE_VERSION)

.PHONY: docker-clean
# target: docker-clean - Remove all unused images, built containers and volumes
docker-clean:
	@echo
	@$(DOCKER) ps -aq | xargs $(DOCKER) rm -fv
	@$(DOCKER) system prune -af --volumes

{%- if cookiecutter.enable_sphinx == 'true' %}


##
# Documentation

.PHONY: doc
doc:
ifdef doctools
	$(error Can't find tools:${doctools})
endif

.PHONY: apidoc
# target: apidoc - Create one reST file with automodule directives per package
apidoc: doc
	@echo
	@$(SPHINX_APIDOC) --force --private -o "$(autodocdir)" $(PACKAGE_NAME) \
		$(foreach module,$(AUTODOC_EXCLUDE_MODULES),$(PACKAGE_NAME)/$(module))

.PHONY: html
# target: html - Render standalone HTML files
html: doc
	@echo
	@$(SPHINX) -b html $(SPHINX_OPTS) "$(SPHINX_BUILDDIR)/html"
{%- endif %}


##
# Auxiliary targets

.PHONY: help
# target: help - Display all callable targets
help:
	@echo
	@$(GREPTOOL) "^\s*#\s*target\s*:\s*" [Mm]akefile \
	| $(SED) -r "s/^\s*#\s*target\s*:\s*//g"


### Cleaners

.PHONY: clean
# target: clean - Clean the project's directory
clean:
	@find "$(CURDIR)" -path "$(CURDIR)/$(VENV_DIR)" -prune -o \
			\
		-name ".cache" -type d -exec rm -rfv {} + -o \
		-name ".mypy_cache" -type d -exec rm -rf {} + -o \
		-name ".pytest_cache" -type d -exec rm -rf {} + -o \
		-name "__pycache__" -type d -exec rm -rf {} + -o \
			\
		-name "*.py[cod]" -exec rm -f {} +

.PHONY: distclean
# target: distclean - Clean the project's build output
distclean:
	@find "$(CURDIR)" -path "$(CURDIR)/$(VENV_DIR)" -prune -o \
			\
		-name ".eggs" -type d -exec rm -rf {} + -o \
		-name "*.dist-info" -type d -exec rm -rf {} + -o \
		-name "*.egg-info" -type d -exec rm -rf {} +
	@rm -rf \
		"$(builddir)" \
		"$(distdir)"

{%- if cookiecutter.enable_sphinx == 'true' %}

	@find "$(CURDIR)" -name "$(autodocdir)/*.rst" -exec rm -f {} +
	@rm -rf \
		"$(SPHINX_BUILDDIR)" \
		"$(SPHINX_STATIC)" \
		"$(SPHINX_TEMPLATES)"
{%- endif %}

.PHONY: mostlyclean
# target: mostlyclean - Delete almost everything
mostlyclean: clean distclean
	@find "$(CURDIR)" -name .DS_Store -exec rm -fv {} +
	@rm -rf "$(VENV_DIR)"
