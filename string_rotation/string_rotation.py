from manimlib.imports import *
import os
import pyclbr

CELL_LEN = 1.75

class StringRotation(Scene):
    def CreateGrid(self, len):
        grid = VGroup()
        for i in range(0, len):
            grid.add(Square(side_length=CELL_LEN))
        grid.arrange_submobjects(RIGHT, buff=0)
        return grid

    def construct(self):
        SHIFT_UP = 0.5
        THE_WORD = "Matrix"
        grid = self.CreateGrid(len(THE_WORD))
        grid.shift(SHIFT_UP*UP)
        self.add(grid)
        word = Text(THE_WORD, font='Roboto Mono')
        word.set_height(1)
        word.shift(SHIFT_UP*UP)
        x_mask = [1, 0, 0]
        for i in range(0, len(grid)):
          word[i].move_to(grid[i].get_center(), coor_mask=x_mask)

        self.add(word)

        self.wait()

        DROP = 1.5

        matr = VGroup(word[0], word[1], word[2], word[3])
        ix = VGroup(word[4], word[5])
        self.play(ApplyMethod(ix.shift, DROP*DOWN))
        ix_len = CELL_LEN*2
        self.play(ApplyMethod(matr.shift, RIGHT*ix_len))
        matr_len = CELL_LEN*4
        self.play(ApplyMethod(ix.shift, LEFT*matr_len))
        self.play(ApplyMethod(ix.shift, DROP*UP))

        self.wait()


if __name__ == "__main__":
    # Call this file at command line to make sure all scenes work with version of manim
    # type "python manim_tutorial_P37.py" at command line to run all scenes in this file
    #Must have "import os" and  "import pyclbr" at start of file to use this
    ###Using Python class browser to determine which classes are defined in this file
    module_name = 'manim_tutorial_P37'   #Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module==module_name:
            print(item.name)
            os.system("python -m manim manim_tutorial_P37.py %s -l" % item.name)  #Does not play files
