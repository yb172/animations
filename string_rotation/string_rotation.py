from manimlib.imports import *
import os
import pyclbr

CELL_LEN = 1.75
RED = "#FC544B"
YELLOW = "#FAC735"
LIGHT_GREEN = "#2AD444"
DARK_GREEN = "#1F9F32"
MAROON = "#7F2355"
LIGHT_BLUE = "#00D1FF"
BLUE = "#578BF1"
ALMOST_BLACK = "#363535"
DARK_GREY = "#5A5A5A"
GREY = "#7A7A7A"
LIGHT_GREY = "#999999"
ALMOST_WHITE = "#C6C6C6"


def split_word(word, prefix_len):
    prefix = VGroup(*word[0:prefix_len])
    suffix = VGroup(*word[prefix_len:])
    return prefix, suffix


def create_grid(len):
    grid = VGroup()
    for i in range(0, len):
        grid.add(Square(side_length=CELL_LEN, color=ALMOST_BLACK))
    grid.arrange_submobjects(RIGHT, buff=0)
    return grid


class TitleImage(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def construct(self):
        SHIFT_UP = 0.5
        THE_WORD = "Matrix"

        # Create the word with moved suffix
        updated_word = Text("ixMatrix",
                            font='Merriweather',
                            color=ALMOST_BLACK,
                            size=2)
        updated_word.shift(SHIFT_UP*UP)
        updated_word.set_opacity(0.3)
        self.add(updated_word)

        # Create, align & add word
        word = Text(THE_WORD,
                    font='Merriweather',
                    color=ALMOST_BLACK,
                    size=2)
        word.shift(SHIFT_UP*UP)
        word.align_to(updated_word, RIGHT)
        self.add(word)

        # Create an arrow from suffix to its final position
        arrow_start = VGroup(updated_word[-2:]).get_bottom()
        arrow_end = VGroup(updated_word[:2]).get_bottom()
        arrow = CurvedArrow(arrow_start, arrow_end,
                            angle=-TAU / 3,
                            color=ALMOST_WHITE,
                            tip_length=0.25)
        arrow.shift(0.15*DOWN)
        self.add(arrow)

        self.wait()


class StringRotation(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def construct(self):
        SHIFT_UP = 0.5
        DROP_AMOUNT = 1
        THE_WORD = "Matrix"

        # Create, align & add word
        word = Text(THE_WORD,
                    font='Merriweather',
                    color=ALMOST_BLACK,
                    size=2)
        word.shift(SHIFT_UP*UP)
        self.add(word)

        self.wait()

        angle = math.radians(-180)
        arc = Arc(radius=1.23, angle=angle, color=ALMOST_BLACK)
        arc.shift(SHIFT_UP*UP)

        self.wait()

        # Animate movement
        PREFIX_LEN = 4
        suffix_len = len(THE_WORD) - PREFIX_LEN
        # prefix_shift = suffix_len * CELL_LEN
        # suffix_shift = PREFIX_LEN * CELL_LEN
        prefix_shift = 0.92
        suffix_shift = 2.42
        prefix, suffix = split_word(word, PREFIX_LEN)
        # self.play(ApplyMethod(suffix.shift, DROP_AMOUNT*DOWN))
        # self.play(ApplyMethod(prefix.shift, prefix_shift * RIGHT))
        # self.play(ApplyMethod(suffix.shift, suffix_shift * LEFT))
        # self.play(ApplyMethod(suffix.shift, DROP_AMOUNT*UP))
        self.play(
            ApplyMethod(prefix.shift, prefix_shift * RIGHT),
            MoveAlongPath(suffix, arc)
        )

        self.wait()

        self.play(FadeOut(word))
        word2 = Text(THE_WORD,
                     font='Merriweather',
                     color=ALMOST_BLACK,
                     size=2)
        word2.shift(SHIFT_UP*UP)
        self.play(FadeIn(word2))


class WordInCells(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def construct(self):
        SHIFT_UP = 0.5
        THE_WORD = "Matrix"

        # Create and add grid
        grid = create_grid(len(THE_WORD))
        grid.shift(SHIFT_UP*UP)
        self.add(grid)

        # Create, align & add word
        word = Text(THE_WORD,
                    font='Merriweather',
                    color=ALMOST_BLACK,
                    size=2)
        word.shift(SHIFT_UP*UP)
        x_mask = [1, 0, 0]
        for i in range(0, len(grid)):
            word[i].move_to(grid[i].get_center(), coor_mask=x_mask)
        self.add(word)

        self.wait()


if __name__ == "__main__":
    # Call this file at command line to make sure all scenes work with version of manim
    # type "python manim_tutorial_P37.py" at command line to run all scenes in this file
    # Must have "import os" and  "import pyclbr" at start of file to use this
    # Using Python class browser to determine which classes are defined in this file
    module_name = 'manim_tutorial_P37'  # Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module == module_name:
            print(item.name)
            os.system("python -m manim manim_tutorial_P37.py %s -l" % item.name)  # Does not play files
