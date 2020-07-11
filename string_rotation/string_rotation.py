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


def create_cell(text, stroke_color=DARK_GREY, fill_color=GREY):
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
    idx = Text(text,
               font='Merriweather',
               color=stroke_color,
               size=0.4)
    idx.align_to(cell[1], UR)
    idx.shift(0.1*LEFT + 0.1*DOWN)
    cell.add(idx)
    return cell


def create_grid(len, stroke_color=DARK_GREY, fill_color=GREY):
    grid = VGroup()
    for i in range(0, len):
        grid.add(create_cell(str(i), stroke_color, fill_color))
    grid.arrange_submobjects(RIGHT, buff=0)
    return grid


class TitleImage(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "pixel_height": 1280,
            "pixel_width": 720,
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

        all = VGroup(updated_word, word, arrow)
        all.scale(1.5)
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
        word.scale(1.5)
        word2 = word.copy()
        self.add(word)

        self.wait()

        arc = Arc(radius=1.82, angle=math.radians(-180))
        arc.shift(SHIFT_UP*UP)
        self.wait()

        # Animate movement
        PREFIX_LEN = 4
        prefix_shift = 1.4
        prefix, suffix = split_word(word, PREFIX_LEN)
        self.play(
            ApplyMethod(prefix.shift, prefix_shift * RIGHT),
            MoveAlongPath(suffix, arc)
        )

        self.wait()

        self.play(FadeOut(word))
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


class InPlaceWrong(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def move_char(self, word, src_ch, start, dst):
        dst_idx = dst % len(word)
        moving_ch = src_ch.copy()
        moving_ch.set_opacity(1)
        ch_2 = word[dst_idx]
        dist = dst - start
        src_ch_dst = src_ch.get_center() + dist*CELL_LEN*RIGHT
        if (dst > dst_idx):
            dist = len(word) - dist
            src_ch_dst = src_ch.get_center() + dist*CELL_LEN*LEFT
        arc_1 = ArcBetweenPoints(src_ch.get_center(), src_ch_dst, angle=-TAU/4)
        self.play(
            MoveAlongPath(moving_ch, arc_1),
            ApplyMethod(ch_2.set_opacity, 0),
            run_time=0.7)
        return moving_ch

    def construct(self):
        ROTATION = 2
        SHIFT_UP = 0.5
        SHIFT_DOWN = 2
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

        original_word = word.copy()

        self.wait()

        new_word = VGroup()
        idx = 0
        letter_m = self.move_char(word, word[0], idx, ROTATION+idx)
        new_word.add(letter_m)
        idx = idx+1
        letter_a = self.move_char(word, word[1], idx, ROTATION+idx)
        new_word.add(letter_a)
        idx = idx+1
        letter_t = self.move_char(word, new_word[idx-2], idx, ROTATION+idx)
        new_word.add(letter_t)
        idx = idx+1
        letter_r = self.move_char(word, new_word[idx-2], idx, ROTATION+idx)
        new_word.add(letter_r)
        idx = idx+1
        letter_i = self.move_char(word, new_word[idx-2], idx, ROTATION+idx)
        new_word.add(letter_i)
        idx = idx+1
        letter_x = self.move_char(word, new_word[idx-2], idx, ROTATION+idx)
        new_word.add(letter_x)
        idx = idx+1

        self.wait()

        self.play(
            FadeOut(word),
            FadeOut(new_word),
            FadeOut(grid)
        )
        self.play(
            FadeIn(original_word),
            FadeIn(grid)
        )


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


class CopyBetter(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def construct(self):
        ROTATION = 2
        SHIFT_UP = 0.5
        SHIFT_DOWN = 2
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

        original_word = word.copy()

        self.wait()

        var_grid = create_grid(2)
        var_grid.shift(SHIFT_DOWN*DOWN)

        self.play(FadeIn(var_grid))

        arcs_up = VGroup()
        for i in range(0, ROTATION):
            ch = word[-i-1]
            start = ch.get_center()
            mid = start + (SHIFT_UP+SHIFT_DOWN)*DOWN
            mid[0] = var_grid[-i-1].get_center()[0]
            end = ch.get_center() + CELL_LEN*(len(THE_WORD)-ROTATION)*LEFT
            arc_down = ArcBetweenPoints(start, mid, angle=-TAU/4)
            arc_up = ArcBetweenPoints(mid, end, angle=-TAU/4)
            arcs_up.add(arc_up)
            self.play(MoveAlongPath(ch, arc_down), run_time=0.7)

        for i in range(ROTATION, len(THE_WORD)):
            shift = ROTATION*CELL_LEN*RIGHT
            self.play(ApplyMethod(word[-i-1].shift, shift), run_time=0.7)

        for i in range(0, ROTATION):
            # Last character moving up
            ch = word[-i-1]
            self.play(MoveAlongPath(ch, arcs_up[i]), run_time=0.7)

        self.play(FadeOut(var_grid))

        self.wait()

        self.play(
            FadeOut(word),
            FadeOut(grid)
        )
        self.play(
            FadeIn(original_word),
            FadeIn(grid)
        )


class InPlaceSlow(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def construct(self):
        ROTATION = 2
        SHIFT_UP = 0.5
        SHIFT_DOWN = 2
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

        original_word = word.copy()

        self.wait()

        var_grid = create_cell("tmp")
        var_grid.shift(SHIFT_DOWN*DOWN)

        self.play(FadeIn(var_grid))

        for step in range(0, ROTATION):
            # Last character moving down
            last_ch = word[-1-step]
            start = last_ch.get_center()
            diff = CELL_LEN*(len(THE_WORD)-1)
            mid = start + (SHIFT_UP+SHIFT_DOWN)*DOWN + diff/2*LEFT
            end = last_ch.get_center() + diff*LEFT
            arc_down = ArcBetweenPoints(start, mid, angle=-TAU/4)
            arc_up = ArcBetweenPoints(mid, end, angle=-TAU/4)
            self.play(MoveAlongPath(last_ch, arc_down), run_time=0.7)

            # Middle characters going right
            for i in range(len(THE_WORD)-2-step, -1-step, -1):
                idx = i % len(THE_WORD)
                shift = CELL_LEN*RIGHT
                self.play(ApplyMethod(word[idx].shift, shift), run_time=0.7)

            # Last character moving up
            self.play(MoveAlongPath(last_ch, arc_up), run_time=0.7)

        self.play(FadeOut(var_grid))

        self.wait()

        self.play(
            FadeOut(word),
            FadeOut(grid)
        )
        self.play(
            FadeIn(original_word),
            FadeIn(grid)
        )


class InPlaceFast(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def reverse(self, word, start, end):
        half = math.floor((end - start)/2)
        for i in range(0, half):
            ch_1 = word[start+i]
            ch_2 = word[end-i-1]
            dist = end - 1 - start - i*2
            ch_1_end = ch_1.get_center() + dist*CELL_LEN*RIGHT
            arc_1 = ArcBetweenPoints(ch_1.get_center(), ch_1_end)
            ch_2_end = ch_2.get_center() + dist*CELL_LEN*LEFT
            arc_2 = ArcBetweenPoints(ch_2.get_center(), ch_2_end)
            self.play(
                MoveAlongPath(ch_1, arc_1),
                MoveAlongPath(ch_2, arc_2),
                run_time=0.7)

    def construct(self):
        ROTATION = 2
        SHIFT_UP = 0.5
        SHIFT_DOWN = 2
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

        original_word = word.copy()

        self.wait()

        rotation_middle_idx = len(THE_WORD)-ROTATION

        # Reverse the prefix
        self.reverse(word, 0, rotation_middle_idx)
        self.wait(0.5)

        # Reverse the suffix
        self.reverse(word, rotation_middle_idx, len(THE_WORD))
        self.wait(0.5)

        # Refresh the word (to work with good indexes)
        also_word = Text("rtaMxi",
                    font='Merriweather',
                    color=ALMOST_BLACK,
                    size=2)
        also_word.shift(SHIFT_UP*UP)
        x_mask = [1, 0, 0]
        for i in range(0, len(grid)):
            also_word[i].move_to(grid[i].get_center(), coor_mask=x_mask)
        self.add(also_word)
        self.remove(word)
        self.reverse(also_word, 0, len(THE_WORD))

        self.wait(2)

        self.play(
            FadeOut(also_word),
            FadeOut(grid)
        )
        self.play(
            FadeIn(original_word),
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
