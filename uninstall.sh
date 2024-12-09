#!/usr/bin/bash

if [ "${EUID}" -ne 0 ]; then
    echo "Error: you must run this script as root";
    exit 1;
fi

if ! rm /usr/bin/tshow; then
    echo "Error: couldn't remove execute 'tshow' file in /usr/bin";
    exit 1;
else
    echo "Uninstall was successful."
    exit 0;
fi