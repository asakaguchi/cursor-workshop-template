#!/bin/bash

USER_ID=${USER_ID:-1000}
GROUP_ID=${GROUP_ID:-1000}

# Remove default ubuntu user
userdel -r ubuntu >/dev/null 2>&1 || true

# Create group and user
groupadd -g $GROUP_ID appuser
useradd -u $USER_ID -g $GROUP_ID -m -s /bin/bash appuser

# Add user to sudo group
usermod -aG sudo appuser

# Execute command
if [ $# -eq 0 ]; then
    exec gosu appuser bash
else
    exec gosu appuser "$@"
fi