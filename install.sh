#!/usr/bin/bash

# shellcheck disable=SC1091
source /etc/os-release

if [ "${EUID}" -ne 0 ]; then
    echo "Error: you must run this script as root";
    exit 1;
fi

if ! python3 -V >/dev/null 2>&1; then
    if [ "${ID}" == "ubuntu" ] || [ "${ID}" == "debian" ]; then
        apt update;
        apt install python3 -y;
    elif [ "${OS}" == "centos" ] || [ "${ID}" == "almalinux" ] || [ "${ID}" == "rocky" ]; then
        yum install -y python3;
    elif [ "${ID}" == "fedora" ] || [ "${ID}" == "oracle" ]; then
        dnf -y install python3;
    elif [ "${ID}" == "arch" ]; then
        pacman -S --noconfirm python3;
    else
        echo "Error: this script isn't support on your machine. You can manual install 'python3' and run script again";
        exit 1;
    fi
fi

if ! cp main.py /usr/bin/tshow >/dev/null 2>&1; then
    echo "Error: cannot copy main file into '/usr/bin'. Be sure you run this script as root and 'main.py' is exists.";
    exit 1;
else
    chmod 755 /usr/bin/tshow;
    chmod +x /usr/bin/tshow;
    echo "Install was successful.";
    exit 0;
fi