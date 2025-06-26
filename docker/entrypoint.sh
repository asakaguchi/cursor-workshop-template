#!/bin/bash

USER_ID=${USER_ID:-1000}
GROUP_ID=${GROUP_ID:-1000}
USER_NAME=${USER_NAME:-appuser}
GROUP_NAME=${GROUP_NAME:-appgroup}

# Remove default ubuntu user
userdel -r ubuntu >/dev/null 2>&1 || true

# Create group if it doesn't exist
if ! getent group $GROUP_NAME >/dev/null 2>&1; then
    groupadd -g $GROUP_ID $GROUP_NAME
fi

# Create user if it doesn't exist
if ! getent passwd $USER_NAME >/dev/null 2>&1; then
    useradd -u $USER_ID -g $GROUP_ID -m -s /bin/bash $USER_NAME
fi

# Add user to sudo group
usermod -aG sudo $USER_NAME

# Allow sudo without password
echo "$USER_NAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USER_NAME

# Change ownership of working directory
chown -R $USER_NAME:$GROUP_NAME /app

# Execute command as the specified user
if [ $# -eq 0 ]; then
    exec gosu $USER_NAME /bin/bash
else
    exec gosu $USER_NAME "$@"
fi