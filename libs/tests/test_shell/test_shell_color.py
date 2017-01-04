# -*- coding: utf-8 -*-

from django.test.testcases import TestCase
import time

from libs.shell import Color, ShellColor, Style, ShellInterface


class Test_ShellColor(TestCase):

    ''' Tests the ShellColor class '''

    def setUp(self):
        self.shell = ShellInterface()

    def test_str(self):
        ''' Test str ShellColor '''
        shell_color = ShellColor()
        for text_color in Color:
            shell_color.text_color = text_color
            for test_style in Style:
                shell_color.text_style = test_style
                for font_color in Color:
                    shell_color.font_color = font_color
                    spam = str(shell_color)
                    self.assertNotEqual(spam, '')

    def test_del_eq(self):
        ''' Test that del work as intended. '''
        shell_color = ShellColor(Color.BLUE, Style.LIGHT, Color.GREEN)
        self.assertNotEqual(shell_color, ShellColor())
        self.assertNotEqual(shell_color, ShellColor(Color.BLACK, Style.LIGHT, Color.GREEN))
        self.assertEqual(shell_color, ShellColor(Color.NONE, Style.LIGHT, Color.GREEN))
        self.assertEqual(shell_color, ShellColor(Color.NONE, Style.NONE, Color.GREEN))
        self.assertEqual(shell_color, ShellColor())
        self.assertNotEqual(shell_color, 'This object is not a ShellColor but a string')

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
                print('Test for {0} and {1}'.format(Color(text_color), Style(test_style)))
                for font_color in Color:
                    shell_color.font_color = font_color
                    color = str(shell_color)
                    text = '{0}ShellColor with {1} inside'.format(color, middle_thing)
                    self.shell.print_color(text, shell_color)
        self.assertTrue(True)

    def test_exception_print_color(self):
        ''' Test that we can't use another object than a shell color to print with ShellInterface '''
        # Test str of private exception NotAShellColorException
        try:
            self.shell.print_color('Text to print', 42)
        except Exception, e:
            print(e)
        self.assertRaises(Exception, self.shell.print_color, 'Text to print', 42)
        self.assertRaises(Exception, self.shell.print_color, 'Text to print', '42')
        self.assertRaises(Exception, self.shell.print_color, 'Text to print', self.shell)
        self.assertRaises(Exception, self.shell.print_color, 'Text to print', 42.73)

    def test_print_unicode(self):
        self.shell.print_color(u"‖This is a text in unicode‖", ShellColor())
