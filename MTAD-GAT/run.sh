#!/bin/sh

xhost +local:root

docker run -it \
    --privileged \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="/home/insujin/projects:/projects" \
    -p 8888:8888 \
    --rm \
    --gpus all \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    presto/anomaly/mtad-gat:latest
