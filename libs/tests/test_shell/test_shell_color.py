# -*- coding: utf-8 -*-

from django.test.testcases import TestCase
from libs.shell import Color, ShellColor, Style, print_color


class Test_ShellColor(TestCase):

    ''' Tests the ShellColor class '''

    def test_str(self):
        ''' Test str ShellColor '''
        shell_color = ShellColor()
        for text_color in Color:
            shell_color.text_color = text_color
            for test_style in Style:
                shell_color.text_style = test_style
                for font_color in Color:
                    shell_color.font_color = font_color
                    self.assertNotEqual(str(shell_color), '')

    def test__eq__(self):
        ''' __eq__ work as intended. '''
        color = ShellColor(Color.BLUE, Style.LIGHT, Color.GREEN)
        self.assertEqual(color, ShellColor(text_color=Color.BLUE,
                                           text_style=Style.LIGHT,
                                           font_color=Color.GREEN))
        self.assertNotEqual(color, ShellColor())
        self.assertNotEqual(color, ShellColor(text_style=Style.LIGHT))
        self.assertNotEqual(color, ShellColor(font_color=Color.GREEN))
        self.assertNotEqual(color, ShellColor(text_color=Color.BLUE))
        self.assertNotEqual(color, ShellColor())
        self.assertNotEqual(color, 'This object is not a ShellColor')

    def test_print_color(self):
        ''' Test the color in shell '''
        middle_thing = '{0}{1}{2}'.format(ShellColor(Color.RED),
                                          ' another ShellColor ',
                                          ShellColor())
        shell_color = ShellColor()
        for text_color in Color:
            shell_color.text_color = text_color
            for test_style in Style:
                shell_color.text_style = test_style
                print('Test for {0} and {1}'.format(Color(text_color),
                                                    Style(test_style)))
                for font_color in Color:
                    shell_color.font_color = font_color
                    color = str(shell_color)
                    text = '{}ShellColor with {} inside'.format(color,
                                                                middle_thing)
                    print_color(text, shell_color)

    def test_exception_print_color(self):
        ''' We can't use another object than a shell color in print_color '''
        self.assertRaises(TypeError, print_color, 'Text to print', 42)
        self.assertRaises(TypeError, print_color, 'Text to print', '42')
        self.assertRaises(TypeError, print_color, 'Text to print', 42.73)

    def test_print_unicode(self):
        """ We can print a unicode text. """
        print_color(u"‖This is a text in unicode‖", ShellColor())
