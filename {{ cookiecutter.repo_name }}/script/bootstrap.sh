{{ cookiecutter.shebang_shell }}
{{ cookiecutter.shebang_coding }}

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
    "python{{ cookiecutter.python_version[0] }}-dev"

    "libncurses5-dev"
)

APT_DEPS_EDIT=(
    "vim"
    "emacs-nox"
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
    # Root password.
    passwd <<EOF
r
r
EOF

    # SSH.
    sed -i "s/prohibit-password/yes/" /etc/ssh/sshd_config
    systemctl restart sshd

    # APT sources & dependencies.
    apt-get update -q
    apt-get install -qy \
        ${APT_DEPS[*]} \
        ${APT_DEPS_DEVELOP[*]} \
        ${APT_DEPS_EDIT[*]}
        # ${APT_DEPS_XORG[*]}

    # Pip.
    wget -qO- https://bootstrap.pypa.io/get-pip.py | python{{ cookiecutter.python_version }}

    mkdir "${HOME}/.pip"
    echo -e "[list]\nformat = {{ cookiecutter.pip_list_format }}" \
        > "${HOME}/.pip/pip.conf"

    pip -q install -U ${PIP_DEPS[*]}
}


main "$@"
