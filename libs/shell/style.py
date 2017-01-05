# -*- coding: utf-8 -*-

from enum import Enum


class Style(Enum):

    """
        This class represent the text style in ShellColor.
    """

    NONE = 0
    BOLD = 1
    LIGHT = 2
    UNDERLINE = 4
    BLINK = 5
    INVERSE = 7
    HIDDEN = 8
