{{ cookiecutter.shebang_coding }}
{{ cookiecutter.shebang_shell }}

set -eo pipefail


APT_DEPS=(
    "sudo"
    "htop"
    "sysv-rc-conf"

    "curl"
    "wget"
    "git"

    "links"
)

APT_DEPS_DEVELOP=(
    "build-essential"
    "cmake"
    "pkg-config"
    "libtool"
    "valgrind"
    "strace"

    "python-software-properties"
    "python-dev"

    "libncurses5-dev"
)

APT_DEPS_EDIT=(
    "vim"
    "emacs23-nox"
    "mc"
)

APT_DEPS_XORG=(
    "virtualbox-guest-dkms"

    "xorg"
    "fonts-droid"
    "wmaker"
    "sakura"
)

PIP_DEPS=(
    "setuptools"
    "wheel"
    "virtualenv"
    "ipython"
    "ipdb"
)


function main () {
    # APT sources & dependencies.
    apt-get update -q
    apt-get install -qy \
        ${APT_DEPS[*]} \
        ${APT_DEPS_DEVELOP[*]} \
        ${APT_DEPS_EDIT[*]}
        # ${APT_DEPS_XORG[*]}

    # Pip.
    wget -qO- https://bootstrap.pypa.io/get-pip.py | python
    pip install -U ${PIP_DEPS[*]}
}


main "$@"
