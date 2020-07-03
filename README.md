# Animations

This repository contains animations crated with [manim](https://github.com/3b1b/manim) library

The `manimlib` directory is stored here for autocomplete to work for easier source code exploration.

To render the animation in low resolution (for preview) run following command:

```bash
./play.sh string_rotation/string_rotation.py StringRotation -l
```

The script [uses docker to run `manim`](https://github.com/3b1b/manim/tree/cf656e9c21ec7f23a71a9f93b503294ec74c1b66#using-docker) so you should have `docker` and `docker-compose` installed

where `string_rotation/string_rotation.py` is path to the file that contains the scene (relative to root directory) and `StringRotation` is the name of the scene

To render in full quality run the same command but without `-l`. To render full quality gif use `-i` instead of `-l`.
