#!/bin/bash

cd "$(dirname "$0")/.."

IMAGE_NAME=$(basename "$PWD" | tr '[:upper:]' '[:lower:]')

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

# Get user and group IDs
USER_ID=$(id -u)
GROUP_ID=$(id -g)

# Run the container
docker run \
    $TTY_OPTION \
    --rm \
    $GPU_OPTION \
    --shm-size=2g \
    --net=host \
    -e DISPLAY=$DISPLAY \
    -e USER_ID=$USER_ID \
    -e GROUP_ID=$GROUP_ID \
    -v "$PWD":/app \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -w /app \
    "$IMAGE_NAME:latest" \
    "${@:-bash}"