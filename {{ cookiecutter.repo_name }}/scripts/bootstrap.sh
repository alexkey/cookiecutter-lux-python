{{ cookiecutter.shebang_shell }}
{{ cookiecutter.shebang_coding }}

set -eo pipefail


APT_DEPS=(
    "ack-grep"
    "curl"
    "git"
    "htop"
    "links"
    "sudo"
    "sysv-rc-conf"
    "wget"
)

APT_DEPS_DEVELOP=(
    "build-essential"
    "cmake"
    "libncurses5-dev"
    "libtool"
    "pkg-config"
    "python-software-properties"
    "python{{ cookiecutter.python_version[0] }}-dev"
    "strace"
    "valgrind"
)

APT_DEPS_EDIT=(
    "emacs24-nox"
    "mc"
    "vim"
)

APT_DEPS_XORG=(
    "fonts-droid"
    "sakura"
    "virtualbox-guest-dkms"
    "wmaker"
    "xorg"
)

PIP_DEPS=(
    "ipdb"
    "ipython"
    "setuptools"
    "virtualenv"
    "wheel"
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

    pip{{ cookiecutter.python_version[0] }} -q install -U ${PIP_DEPS[*]}
}


main "$@"
