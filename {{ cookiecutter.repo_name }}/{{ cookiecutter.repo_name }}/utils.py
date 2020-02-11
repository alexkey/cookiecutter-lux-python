import logging
from pathlib import Path

import toml

import {{ cookiecutter.repo_name }} as root


_LOG = logging.getLogger(__name__)


def parse_config(file: str) -> root.CONFIG_TYPE:
    if not Path(file).is_file():
        raise FileNotFoundError(file)

    log = _LOG
    try:
        return toml.load(file)
    except IndexError:
        log.error('Unable to load TOML')
    except toml.TomlDecodeError:
        log.error('Unable to decode TOML')

    return None
