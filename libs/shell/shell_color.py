# -*- coding: utf-8 -*-

"""
.. module:: ShellColor
:platform: Unix
"""

from libs.shell.color import Color
from libs.shell.style import Style


class ShellColor(object):

    """
        A class giving the adequate string to print before a text for coloring
        it in shell with a text color, a text style, and a font color.
    """

    def __init__(self, text_color=None, text_style=None, font_color=None):
        if text_color is None:
            text_color = Color.NONE
        if text_style is None:
            text_style = Style.NONE
        if font_color is None:
            font_color = Color.NONE
        self.text_color = text_color
        self.text_style = text_style
        self.font_color = font_color

    def __eq__(self, other):
        text_color = self.text_color == other.text_color
        text_style = self.text_style == other.text_style
        font_color = self.font_color == other.font_color
        return text_color and text_style and font_color

    def __repr__(self):
        ''' Return a string in color representing the ShellColor itself.'''
        text = "Text color : {},".format(self.text_color.name)
        text += " Text Style : {},".format(self.text_style.name)
        text += " Font color : {}".format(self.font_color.name)
        return self.colorize_text(text)

    def __str__(self):
        '''An invisible string that will trigger ANSI coloring in terminal.'''
        ansi_style = "\033[{}".format(self.text_style.value)
        if self.text_color != Color.NONE or self.font_color != Color.NONE:
            ansi_style += ';'
        if self.font_color != Color.NONE:
            ansi_style += '4{0}'.format(self.font_color.value)
            if self.text_color != Color.NONE:
                ansi_style += ';'
        if self.text_color != Color.NONE:
            ansi_style += '3{0}'.format(self.text_color.value)
        return "{}m".format(ansi_style)

    def colorize_text(self, text):
        ''' Permit to get a colored text in order to print it
        :return: A string colored in the ShellColor '''
        # We end the color after the text with a default ShellColor
        return '{0}{1}{2}'.format(self, text, ShellColor())


def print_color(object_, color):
    ''' Print a text in color in shell and reset the color effect.

    If some part of the text to print are already in color they stay in
    this color. If they are reseted the color effect apply again until the
    end.
    :param object object_: Any object with a __str__ function (which may be
        a string containing ANSI coloring)
    :param ShellColor color: The color to use. '''
    if not isinstance(color, ShellColor):
        msg = "Got '{}' but expected 'ShellColor'".format(color.__class__)
        raise TypeError(msg)
    text_to_print = unicode(object_)
    # We can't print unicode in terminal so we re-encode
    # pylint: disable=redefined-variable-type
    text_to_print = text_to_print.encode('utf-8')
    # We replace each "end of color" we find by by end of color + our color,
    # in order to stay in the same color  if we encounter a colored string
    # inside the string we have to color while keeping the inside colored
    # string in its color.
    color_end = str(ShellColor())
    recolored_text = text_to_print.replace(color_end, color_end + str(color))
    print color.colorize_text(recolored_text)
