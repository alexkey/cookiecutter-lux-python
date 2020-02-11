import argparse
import logging

from typing import (
    Any,
    MutableMapping,
    Optional,
)


__version__ = '{{ cookiecutter.version }}'
__release__ = __version__

DEBUG = False

# Type definitions ==>
CONFIG_TYPE = Optional[MutableMapping[str, Any]]
# <==

ARGS: Optional[argparse.Namespace] = None
CONFIG: CONFIG_TYPE = None

{% raw %}LOG_FMT = '%(levelname)s: %(name)s [%(process)d] {%(filename)s@L%(lineno)d}: %(message)s'{% endraw %}
LOG_LVL = logging.INFO
