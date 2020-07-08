from manimlib.imports import *
import os
import pyclbr

CELL_LEN = 1.5
RED = "#FC544B"
YELLOW = "#FAC735"
LIGHT_GREEN = "#2AD444"
GREEN = "#1F9F32"
DARK_GREEN = "#11661E"
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


def create_grid(len, stroke_color=DARK_GREY, fill_color=GREY):
    grid = VGroup()
    for i in range(0, len):
        cell = VGroup()
        cell.add(Square(
            side_length=CELL_LEN,
            stroke_width=3,
            sheen_factor=0.8,
            sheen_direction=UP,
            fill_color=fill_color,
            fill_opacity=0.1))
        cell.add(Square(
            side_length=CELL_LEN,
            stroke_color=stroke_color,
            stroke_width=3,
        ))
        grid.add(cell)
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


class Copy(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def construct(self):
        ROTATION = 2
        ORIGINAL_SHIFT = 0.5
        SHIFT = 1.5
        THE_WORD = "Matrix"

        # Create and add grid
        grid = create_grid(len(THE_WORD))
        grid.shift(ORIGINAL_SHIFT*UP)
        self.add(grid)

        # Create, align & add word
        word = Text(THE_WORD,
                    font='Merriweather',
                    color=ALMOST_BLACK,
                    size=2)
        word.shift(ORIGINAL_SHIFT*UP)
        x_mask = [1, 0, 0]
        for i in range(0, len(grid)):
            word[i].move_to(grid[i].get_center(), coor_mask=x_mask)
        self.add(word)

        self.wait()
        self.play(
            ApplyMethod(word.shift, (SHIFT-ORIGINAL_SHIFT)*UP),
            ApplyMethod(grid.shift, (SHIFT-ORIGINAL_SHIFT)*UP)
        )

        end_grid = create_grid(len(THE_WORD), DARK_GREEN, GREEN)
        end_grid.shift(SHIFT*DOWN)

        self.play(FadeIn(end_grid))

        end_word = word.copy()
        end_word.set_opacity(.3)
        self.add(end_word)

        rotation_middle_idx = len(THE_WORD)-ROTATION
        for i in range(0, len(THE_WORD)):
            shift = 2*SHIFT*DOWN
            if i < rotation_middle_idx:
                char_shift = ROTATION
                shift = shift+char_shift*CELL_LEN*RIGHT
            else:
                char_shift = len(THE_WORD)-ROTATION
                shift = shift+char_shift*CELL_LEN*LEFT
            self.play(ApplyMethod(end_word[i].shift, shift), run_time=0.7)
            self.play(ApplyMethod(end_word[i].set_opacity, 1), run_time=0.2)

        self.wait()

        self.play(
            FadeOut(word),
            FadeOut(grid)
        )

        self.play(
            ApplyMethod(end_word.shift, (SHIFT+ORIGINAL_SHIFT)*UP),
            ApplyMethod(end_grid.shift, (SHIFT+ORIGINAL_SHIFT)*UP)
        )

        self.wait()

        self.play(
            FadeOut(end_word),
            FadeOut(end_grid)
        )
        word.shift((SHIFT-ORIGINAL_SHIFT)*DOWN)
        grid.shift((SHIFT-ORIGINAL_SHIFT)*DOWN)
        self.play(
            FadeIn(word),
            FadeIn(grid)
        )


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
