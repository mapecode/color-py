"""
Print with all colors in Python
@author: mapecode
"""
Black = '\u001b[30m'
Red = '\u001b[31m'
Green = '\u001b[32m'
Yellow = '\u001b[33m'
Blue = '\u001b[34m'
Magenta = '\u001b[35m'
Cyan = '\u001b[36m'
White = '\u001b[37m'
Reset = '\u001b[0m'

Bright_Black = '\u001b[30;1m'
Bright_Red = '\u001b[31;1m'
Bright_Green = '\u001b[32;1m'
Bright_Yellow = '\u001b[33;1m'
Bright_Blue = '\u001b[34;1m'
Bright_Magenta = '\u001b[35;1m'
Bright_Cyan = '\u001b[36;1m'
Bright_White = '\u001b[37;1m'

Background_Black = '\u001b[40m'
Background_Red = '\u001b[41m'
Background_Green = '\u001b[42m'
Background_Yellow = '\u001b[43m'
Background_Blue = '\u001b[44m'
Background_Magenta = '\u001b[45m'
Background_Cyan = '\u001b[46m'
Background_White = '\u001b[47m'

Background_Bright_Black = '\u001b[40;1m'
Background_Bright_Red = '\u001b[41;1m'
Background_Bright_Green = '\u001b[42;1m'
Background_Bright_Yellow = '\u001b[43;1m'
Background_Bright_Blue = '\u001b[44;1m'
Background_Bright_Magenta = '\u001b[45;1m'
Background_Bright_Cyan = '\u001b[46;1m'
Background_Bright_White = '\u001b[47;1m'

Bold = '\u001b[1m'
Underline = '\u001b[4m'
Reversed = '\u001b[7m'


def print_colors_code():
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            print(u"\u001b[38;5;" + code + "m " + code.ljust(4), end=' ')
        print(Reset)


def color_by_code(code):
    code = str(code)
    return u"\u001b[38;5;" + code + "m "


def random_color():
    from random import randint
    return color_by_code(randint(0, 255))


def print_background_colors_code():
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            print(u"\u001b[48;5;" + code + "m " + code.ljust(4), end=' ')
        print(Reset)


def background_color_by_code(code):
    code = str(code)
    return u"\u001b[48;5;" + code + "m"


def random_background_color():
    from random import randint
    return background_color_by_code(randint(0, 255))


