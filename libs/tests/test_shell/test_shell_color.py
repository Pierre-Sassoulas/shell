#!/usr/bin/python
# -*- coding: utf-8 -*-

from shell import Color, ShellColor, Style
from django.test.testcases import TestCase
from shell_const import COLORS, STYLES


class Test_ShellColor(TestCase):

    ''' Tests the ShellColor class '''

    def test_str(self):
        ''' Test str ShellColor '''

        shell_color = ShellColor()
        for text_color in COLORS:
            shell_color.text_color = text_color
            for test_style in STYLES:
                shell_color.text_style = test_style
                for font_color in COLORS:
                    shell_color.font_color = font_color
                    spam = str(shell_color)
                    self.assertNotEqual(spam, '')

    def test_del_eq(self):
        ''' Test that del work as intended. '''

        shell_color = ShellColor(Color.BLUE, Style.LIGHT, Color.GREEN)
        self.assertNotEqual(shell_color, ShellColor())
        self.assertNotEqual(shell_color, ShellColor(Color.BLACK, Style.LIGHT, Color.GREEN))
        del shell_color.text_color
        self.assertEqual(shell_color, ShellColor(Color.NONE, Style.LIGHT, Color.GREEN))
        del shell_color.text_style
        self.assertEqual(shell_color, ShellColor(Color.NONE, Style.NONE, Color.GREEN))
        del shell_color.font_color
        self.assertEqual(shell_color, ShellColor())
        self.assertNotEqual(shell_color, 'This object is not a ShellColor but a string')


