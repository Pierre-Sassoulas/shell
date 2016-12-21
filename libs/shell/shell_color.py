# -*- coding: utf-8 -*-

"""
.. module:: ShellColor
   :platform: Unix
   :synopsis:  A class giving the adequate string to print before a text for coloring it in shell
   with a text color a text style and a font color.

.. moduleauthor:: Pierre Sassoulas <pierre.sassoulas@gmail.com>
"""

from color import Color
from style import Style


class ShellColor(object):

    def __init__(
        self,
        text_color=Color.NONE,
        text_style=Style.NONE,
        font_color=Color.NONE,
        ):
        ''' Constructor ShellColor
        :param text_color: The color of the text
        :param text_style: The style of the text
        :param font_color: The color of the font
        :return: A ShellColor'''

        self.text_color = text_color
        self.text_style = text_style
        self.font_color = font_color

    def __eq__(self, other):
        ''' Method for comparing two ShellColor
        :return: Boolean '''

        return Color(self.text_color) == Color(other.text_color) and Style(self.text_style) \
            == Style(other.text_style) and Color(self.font_color) == Color(other.font_color)

    def get_text_color(self):
        return self.__text_color

    def get_text_style(self):
        return self.__text_style

    def get_font_color(self):
        return self.__font_color

    def set_text_color(self, color):
        self.__text_color = color

    def set_text_style(self, style):
        self.__text_style = style

    def set_font_color(self, color):
        self.__font_color = color

    def del_text_color(self):
        self.__text_color = Color.NONE

    def del_text_style(self):
        self.__text_style = Style.NONE

    def del_font_color(self):
        self.__font_color = Color.NONE

    text_color = property(get_text_color, set_text_color, del_text_color,
                          'The text color (shell.Color)')
    text_style = property(get_text_style, set_text_style, del_text_style,
                          'The text style (shell.Style)')
    font_color = property(get_font_color, set_font_color, del_font_color,
                          'The font color (shell.Color)')

    def get_colored_text(self, text):
        ''' Permit to get a colored text in order to print it
        :return: A string colored in the ShellColor '''

        return '{0}{1}{2}'.format(self.color, text, ShellColor().color)

    @property
    def color(self):
        ''' Give the text to put in shell in order to color the next outputs
        :return: A string to put in terminal in order to get the text color, text style and font color defined. '''

        # The order here is important (or we have to modify the define_* functions)

        resultat = "\033[" + self.__define_text_style()
        resultat += self.__define_font_color()
        resultat += self.__define_text_color()
        return resultat + 'm'

    def __define_text_style(self):
        ''' Return the string to put in terminal in order to get the text style.
        The text style is always defined, if it is not set, it reset to normal.
        :return: A string that must not be used by other function than ShellColor.color() '''

        if self.text_color != Color.NONE or self.font_color != Color.NONE:
            return '{0};'.format(self.text_style)
        else:
            return '{0}'.format(self.text_style)

    def __define_font_color(self):
        ''' Return the string to put in terminal in order to get the font color.
            The font color may not be defined.
            :return: A string that must not be used by other function than ShellColor.color() '''

        if self.font_color != Color.NONE:
            if self.text_color != Color.NONE:
                return '4{0};'.format(self.font_color)
            else:
                return '4{0}'.format(self.font_color)
        else:
            return ''

    def __define_text_color(self):
        ''' Return the string to put in terminal in order to get the text color.
            The text color may not be defined.
            :return: A string that must not be used by other function than ShellColor.color() '''

        if self.text_color != Color.NONE:
            return '3{0}'.format(self.text_color)
        else:
            return ''

    def __str__(self):
        ''' To string ShellColor
        :return: A string in color representing the ShellColor itself.'''

        if self.text_style != Style.HIDDEN:
            color = self.color
        else:

            # If the text style is hidden we use a normal text style
            # in order to be able to read that the text style is hidden

            color = ShellColor(self.text_color, Style.NONE, self.font_color).color
        return "{0}Text color : {1}, Text Style\
 : {2}, Font color : {3}{4}".format(color,
                Color(self.text_color), Style(self.text_style), Color(self.font_color),
                ShellColor().color)


