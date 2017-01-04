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
        text_color = self.text_color == other.text_color
        text_style = self.text_style == other.text_style
        font_color = self.font_color == other.font_color
        return text_color and text_style and font_color

    def __repr__(self):
        ''' To string ShellColor
        :return: A string in color representing the ShellColor itself.'''
        str = "Text color : {},".format(self.text_color.name)
        str += " Text Style : {},".format(self.text_style.name)
        str += " Font color : {}".format(self.font_color.name)
        return self.get_colored_text(str)
    
    def __str__(self):
        '''A string in color to add in a terminal for ANSI coloring.'''
        ansi_style = str(self.text_style.value)
        if self.text_color != Color.NONE or self.font_color != Color.NONE:
            ansi_style += ';'
        if self.font_color != Color.NONE:
            if self.text_color != Color.NONE:
                ansi_style += '4{0};'.format(self.font_color.value)
            else:
                ansi_style += '4{0}'.format(self.font_color.value)
        if self.text_color != Color.NONE:
            ansi_style += '3{0}'.format(self.text_color.value)
        return "\033[{}m".format(ansi_style)

    def get_colored_text(self, text):
        ''' Permit to get a colored text in order to print it
        :return: A string colored in the ShellColor '''
        return '{0}{1}{2}'.format(self, text, ShellColor())
