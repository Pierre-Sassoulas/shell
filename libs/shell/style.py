#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
.. module:: Style
:platform: Unix
:synopsis:  The Style used in ShellColor for the text style.

.. moduleauthor:: Pierre Sassoulas <pierre.sassoulas@gmail.com>
"""


class Style(object):

    NONE = 0
    BOLD = 1
    LIGHT = 2
    UNDERLINE = 4
    BLINK = 5
    INVERSE = 7
    HIDDEN = 8

    style_to_string = {
        0: 'none',
        1: 'bold',
        2: 'light',
        4: 'underline',
        5: 'blink',
        7: 'inverse',
        8: 'hidden',
        '': 'undefined',
        }

    def __init__(self, style):
        '''
            Constructor Style
            :return: A Style.
        '''

        self.style = style

    def __str__(self):
        '''
            To string Style
            :return: A string representing a Style.
        '''

        return Style.style_to_string[self.style]

    def __eq__(self, other):
        '''
            Equal Style
        '''

        return self.style == other.style


