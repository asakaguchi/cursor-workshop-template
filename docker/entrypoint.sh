#!/bin/bash

USER_ID=${USER_ID:-1000}
GROUP_ID=${GROUP_ID:-1000}

# Remove default ubuntu user
userdel -r ubuntu >/dev/null 2>&1 || true

# Create group and user if they don't exist
if ! getent group appuser >/dev/null 2>&1; then
    groupadd -g $GROUP_ID appuser
fi

if ! getent passwd appuser >/dev/null 2>&1; then
    useradd -u $USER_ID -g $GROUP_ID -m -s /bin/bash appuser
fi

# Add user to sudo group
usermod -aG sudo appuser

# Execute command
if [ $# -eq 0 ]; then
    exec gosu appuser sleep infinity
else
    exec gosu appuser "$@"
fi