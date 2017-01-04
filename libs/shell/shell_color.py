# -*- coding: utf-8 -*-

"""
.. module:: ShellColor
:platform: Unix
:synopsis:  A class giving the adequate string to print before a text for
   coloring it in shell with a text color a text style and a font color.
"""

from libs.shell.color import Color
from libs.shell.style import Style

class ShellColor(object):

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
        return True

    def get_colored_text(self, text):
        ''' Permit to get a colored text in order to print it
        :return: A string colored in the ShellColor '''
        return '{0}{1}{2}'.format(self, text, ShellColor())

    def __define_text_style(self):
        ''' Return the string to put in terminal in order to get the text style.

        The text style is always defined, if it is not set, it reset to normal.
        :return: A string that must not be used by other function than
            ShellColor.color() '''
        if self.text_color != Color.NONE or self.font_color != Color.NONE:
            return '{0};'.format(self.text_style.value)
        else:
            return '{0}'.format(self.text_style.value)

    def __define_font_color(self):
        ''' Return the string to put in terminal in order to get the font color.
            The font color may not be defined.

        :return: A string that must not be used by other function than
            ShellColor.color() '''
        if self.font_color != Color.NONE:
            if self.text_color != Color.NONE:
                return '4{0};'.format(self.font_color.value)
            else:
                return '4{0}'.format(self.font_color.value)
        else:
            return ''

    def __define_text_color(self):
        ''' Return the string to put in terminal in order to get the text color.
            The text color may not be defined.

        :return: A string that must not be used by other function than
            ShellColor.color() '''
        if self.text_color != Color.NONE:
            return '3{0}'.format(self.text_color.value)
        else:
            return ''

    def __repr__(self):
        ''' To string ShellColor
        :return: A string in color representing the ShellColor itself.'''
        str = "Text color : {},".format(self.text_color.name)
        str += " Text Style : {},".format(self.text_style.name)
        str += " Font color : {}".format(self.font_color.name)
        return self.get_colored_text(str)
    
    def __str__(self):
        ''' To string ShellColor
        :return: A string in color representing the ShellColor itself.'''
        # The order here is important (or we have to modify the define_* functions)
        result = "\033[{}{}{}m".format(
            self.__define_text_style(),
            self.__define_font_color(),
            self.__define_text_color()
        )
        return result
