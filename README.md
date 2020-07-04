# Animations

This repository contains animations crated with [manim](https://github.com/3b1b/manim) library

## How to use

To render the animation in low resolution (for preview) run following command:

```bash
./play.sh string_rotation/string_rotation.py StringRotation -l
```

where `string_rotation/string_rotation.py` is path to the file that contains the scene (relative to root directory) and `StringRotation` is the name of the scene

Animation result would be written to a newly created `media` directory in `video` subdirectory: `media/video/...`.

To render in full quality run the same command but without `-l`. To render full quality gif use `-i` instead of `-l`.

The script `play.sh` uses docker to run `manim` so you should have `docker` installed.

## Using the newest manim version

The official docker image of manim [is outdated](https://hub.docker.com/r/eulertour/manim) so to get the latest version you have to build fresh image. You can do so by checking out [manim repository](https://github.com/3b1b/manim) and then running following command from `3b1b/manim`:

```bash
docker build . -t eulertour/manim:latest
```

This would build fresh manim docker image for local use

### Using fonts in Docker image

If you would like to render a text with a custom font, i.e. `word = Text("Hello world", font='Roboto Mono')` you won't get the desired result even if you have "Roboto Mono" installed on your system. This is because this font has to be installed inside of the Docker image, not your system. To install the font in Docker image do following from `3b1b/manim` (so not from this repository, but from manim repository):

1. Create `fonts` directory in root directory
2. Copy all the desired fonts to this newly created `fonts` directory
3. Open `Dockerfile` and add these lines right before the last line (that starts with `ENTRYPOINT`):

```Dockerfile
COPY ./fonts /usr/share/fonts/
RUN fc-cache -f -v
```
4. Re-build Docker image by running

```bash
docker build . -t eulertour/manim:latest
```

This would install the fonts onto Docker image OS and manim would be able to use these fonts while rendering

## Note on "manimlib"

The `manimlib` directory is stored here for autocomplete to work for easier source code exploration. It will not be used in actual rendering (since all the rendering happens inside of docker image) so any changes to the code inside `manimlib` won't take any effect
