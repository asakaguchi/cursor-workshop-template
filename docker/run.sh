#!/bin/bash

cd "$(dirname "$0")/.."

IMAGE_NAME=$(basename "$PWD" | tr '[:upper:]' '[:lower:]')
CONTAINER_NAME="${IMAGE_NAME}-$(date +%Y%m%d%H%M%S)"

# Get user and group information
USER_ID=$(id -u)
GROUP_ID=$(id -g)
USER_NAME=$(id -un)
GROUP_NAME=$(id -gn)

# Check if running in interactive mode
if [ -t 0 ]; then
    TTY_OPTION="-it"
else
    TTY_OPTION=""
fi

# Check for NVIDIA GPU support
GPU_OPTION=""
if command -v nvidia-smi &> /dev/null && docker info | grep -q nvidia; then
    GPU_OPTION="--gpus all"
fi

# Run the container
docker run \
    $TTY_OPTION \
    --rm \
    --name "$CONTAINER_NAME" \
    $GPU_OPTION \
    --shm-size=32g \
    --net host \
    -e DISPLAY=$DISPLAY \
    -e USER_ID=$USER_ID \
    -e GROUP_ID=$GROUP_ID \
    -e USER_NAME=$USER_NAME \
    -e GROUP_NAME=$GROUP_NAME \
    -v "$PWD":/app \
    -v "$HOME:$HOME" \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -w /app \
    "$IMAGE_NAME:latest" \
    "${@:-bash}"