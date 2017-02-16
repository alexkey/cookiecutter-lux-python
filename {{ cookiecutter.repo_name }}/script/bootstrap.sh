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
    "python{{ cookiecutter.python_version }}-dev"

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

    {%- if cookiecutter.enable_nodejs == 'true' %}

    # Install Node.js v{{ cookiecutter.nodejs_version }}.
    wget -qO- https://deb.nodesource.com/setup_{{ cookiecutter.nodejs_version }}.x | sudo -E bash -
    sudo apt-get install -qy nodejs
    {%- endif %}

    {%- if cookiecutter.enable_redis == 'true' %}

    # Install Redis {{ cookiecutter.redis_version }}.
    local redis_version="{{ cookiecutter.redis_version }}"

    apt-get install -yq tcl8.5

    wget -q http://download.redis.io/releases/redis-${redis_version}.tar.gz
    tar xzf redis-${redis_version}.tar.gz

    (cd redis-${redis_version} && make test install)

    (cd redis-${redis_version}/utils && \
        sed -r "s/^\s*(read\s+-p)/# \1/g" -i install_server.sh && \
        \
        REDIS_PORT={{ cookiecutter.redis_port }} \
        REDIS_CONFIG_FILE={{ cookiecutter.redis_config_file }} \
        REDIS_LOG_FILE={{ cookiecutter.redis_log_file }} \
        REDIS_DATA_DIR={{ cookiecutter.redis_data_dir }} \
        REDIS_EXECUTABLE={{ cookiecutter.redis_executable }} \
            ./install_server.sh)

    update-rc.d redis_{{ cookiecutter.redis_port }} defaults
    {%- endif %}

    {%- if cookiecutter.vagrant_shell_source %}

    # Additional shell source for a custom setup.
    source {{ cookiecutter.vagrant_shared_guest }}/{{ cookiecutter.vagrant_shell_source }}
    {%- endif %}
}


main "$@"
