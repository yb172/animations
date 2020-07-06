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


class StringRotation(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def create_grid(self, len):
        grid = VGroup()
        for i in range(0, len):
            grid.add(Square(side_length=CELL_LEN))
        grid.arrange_submobjects(RIGHT, buff=0)
        return grid

    def split_word(self, word, prefix_len):
        prefix = VGroup(*word[0:prefix_len])
        suffix = VGroup(*word[prefix_len:])
        return prefix, suffix

    def construct(self):
        SHIFT_UP = 0.5
        DROP_AMOUNT = 1.75
        THE_WORD = "Matrix"

        # Create and add grid
        grid = self.create_grid(len(THE_WORD))
        grid.shift(SHIFT_UP*UP)
        # self.add(grid)

        # Create, align & add word
        color_map = {
            "M": RED,
            "a": YELLOW,
            "t": DARK_GREEN,
            "r": LIGHT_BLUE,
            "i": YELLOW,
            "x": BLUE,
        }
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

        # Animate movement
        PREFIX_LEN = 4
        suffix_len = len(THE_WORD) - PREFIX_LEN
        suffix_shift = suffix_len * CELL_LEN
        prefix_shift = PREFIX_LEN * CELL_LEN
        prefix, suffix = self.split_word(word, PREFIX_LEN)
        self.play(ApplyMethod(suffix.shift, DROP_AMOUNT*DOWN))
        self.play(ApplyMethod(prefix.shift, suffix_shift * RIGHT))
        self.play(ApplyMethod(suffix.shift, prefix_shift * LEFT))
        self.play(ApplyMethod(suffix.shift, DROP_AMOUNT*UP))

        self.wait()

        self.play(FadeOut(word))
        prefix.shift(suffix_shift * LEFT)
        suffix.shift(prefix_shift * RIGHT)
        self.play(FadeIn(word))


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
