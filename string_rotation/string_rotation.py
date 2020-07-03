from manimlib.imports import *
import os
import pyclbr


class StringRotation(Scene):
    def construct(self):
        letters = ["R", "e", "v", "o", "l", "v", "e", "r"]
        word = TextMobject(*letters)
        self.add(word)

        # word2 = TextMobject(*letters)
        # word2.set_opacity(0.3)
        # word2.set_height(1)
        # self.add(word2)

        self.wait()

        revol = VGroup(word[0], word[1], word[2], word[3], word[4])
        ver = VGroup(word[5], word[6], word[7])
        self.play(ApplyMethod(ver.shift, DOWN))
        ver_len = ver.get_width() + 0.2
        self.play(ApplyMethod(revol.shift, RIGHT*ver_len))
        revol_len = revol.get_width() + 0.2
        self.play(ApplyMethod(ver.shift, LEFT*revol_len))
        self.play(ApplyMethod(ver.shift, UP))

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
