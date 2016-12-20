#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
.. module:: Color
:platform: Unix
:synopsis:  The Color used in ShellColor. It can represent the text color or the font color.

.. moduleauthor:: Pierre Sassoulas <pierre.sassoulas@gmail.com>
"""


class Color(object):

    NONE = ''
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    NAVY = 4
    PURPLE = 5
    BLUE = 6
    WHITE = 7

    color_to_string = {
        0: 'black',
        1: 'red',
        2: 'green',
        3: 'yellow',
        4: 'navy',
        5: 'purple',
        6: 'blue',
        7: 'white',
        '': 'none',
        }

    def __init__(self, color):
        ''' Constructor Color
            :return: A Color. '''

        self.color = color

    def __str__(self):
        ''' To string Color
            :return: A string representing the Color. '''

        return Color.color_to_string[self.color]

    def __eq__(self, other):
        ''' Equal Color
            :param other: An other Color.
            :return: A boolean. '''

        return self.color == other.color


