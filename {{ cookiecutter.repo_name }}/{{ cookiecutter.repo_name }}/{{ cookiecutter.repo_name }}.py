{{ cookiecutter.shebang_python }}

import argparse
import logging
import sys
from pathlib import Path

import {{ cookiecutter.repo_name }} as root
from {{ cookiecutter.repo_name }}.utils import parse_config


ERROR_CONFIG = 1
ERROR_CONFIG_PARSING = 2


def parse_cmdline() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=f'{{ cookiecutter.name }} {root.__version__}'
    )

    parser.add_argument('-c', '--config', default=None,
                        help='configuration file', metavar='<config_file>')

    return parser.parse_args()


def main() -> None:
    logging.basicConfig(format=root.LOG_FMT, level=root.LOG_LVL)
    log = logging.getLogger(__name__)

    root.ARGS = parse_cmdline()

    try:
        if root.ARGS.config is None:
            raise FileNotFoundError('<undef>')

        root.CONFIG = parse_config(root.ARGS.config)

        if not root.CONFIG:
            log.error("Can't parse configuration file: %s", root.ARGS.config)
            sys.exit(ERROR_CONFIG_PARSING)
    except FileNotFoundError as exc:
        log.error('Configuration file not found: %s', exc.args[0])
        log.info('Use `-c` command line argument to specify a correct one')
        sys.exit(ERROR_CONFIG)

    root.DEBUG = root.CONFIG['main']['debug']

    if root.DEBUG:
        log.info('Debug mode is ON')
        log.info('Running configuration: %s', Path(root.ARGS.config).resolve())


if __name__ == '__main__':
    main()
