# Animations

This repository contains animations crated with [manim](https://github.com/3b1b/manim) library

## Installation

The script `play.sh` [uses docker to run `manim`](https://github.com/3b1b/manim/tree/cf656e9c21ec7f23a71a9f93b503294ec74c1b66#using-docker) so you should have `docker` and `docker-compose` installed.

The official docker image of manim [is outdated](https://hub.docker.com/r/eulertour/manim) so to get the latest version you have to build fresh image. You can do so by checking out manim lib and then running in manim root directory:

```bash
docker build . -t eulertour/manim:latest
```

This would build fresh manim docker image for local use

## How to use

To render the animation in low resolution (for preview) run following command:

```bash
./play.sh string_rotation/string_rotation.py StringRotation -l
```

where `string_rotation/string_rotation.py` is path to the file that contains the scene (relative to root directory) and `StringRotation` is the name of the scene

Animation result would be written to `/play_output/videos/...`.

To render in full quality run the same command but without `-l`. To render full quality gif use `-i` instead of `-l`.

## Note on "manimlib"

The `manimlib` directory is stored here for autocomplete to work for easier source code exploration. It will not be used in actual rendering (since all the rendering happens inside of docker image) so any changes to the code inside `manimlib` won't take any effect
