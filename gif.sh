set -x
set -e

FILE=$1
RESOLUTION=$2
SCENE=$3

rm -f media/videos/$FILE/$RESOLUTION/frames/*
mkdir -p media/videos/$FILE/$RESOLUTION/frames
ffmpeg -i media/videos/$FILE/$RESOLUTION/$SCENE.mp4 media/videos/$FILE/$RESOLUTION/frames/frame%04d.png
gifski -o media/videos/$FILE/$RESOLUTION/$SCENE.gif media/videos/$FILE/$RESOLUTION/frames/frame*.png
