#!/usr/bin/python
# -*- coding: utf-8 -*-

from shell import Color, ShellColor, ShellInterface, Style
from django.test.testcases import TestCase
from shell.shell_interface import MAXIMUM_TIME_WITHOUT_FEEDBACK
from shell_const import COLORS, STYLES
import time


class Test_ShellInterface(TestCase):

    ''' Tests the ShellInterface class '''

    def setUp(self):
        self.shell = ShellInterface()

    def test_print_color(self):
        ''' Test the color in shell '''

        middle_thing = '{0}{1}{2}'.format(ShellColor(Color.RED).color, ' another color ',
                                          ShellColor().color)
        shell_color = ShellColor()
        for text_color in COLORS:
            shell_color.text_color = text_color
            for test_style in STYLES:
                shell_color.text_style = test_style
                print('Test for {0} and {1}'.format(Color(text_color), Style(test_style)))
                for font_color in COLORS:
                    shell_color.font_color = font_color
                    color = str(shell_color)
                    text = '{0} colored with {1} inside'.format(color, middle_thing)
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

    def test_progress_bar_full(self):
        ''' This function test the progress bar in different context '''

        test_in_progress = True
        percentage = 20
        begin_time = time.time()
        self.shell.start_progress_bar()
        while test_in_progress:
            time.sleep(0.2)
            percentage += 3
            elapsed_time = time.time() - begin_time
            self.shell.update_progress_bar(percentage)
            if elapsed_time > MAXIMUM_TIME_WITHOUT_FEEDBACK + 2:
                test_in_progress = False
                self.shell.finish_progress_bar()
        self.assertTrue(True)

    def test_progress_bar_fail(self):
        ''' This function test the progress bar in different context '''

        self.assertRaises(RuntimeError, self.shell.update_progress_bar, 73)
        self.shell.start_progress_bar()
        self.shell.update_progress_bar(0)
        self.shell.update_progress_bar(-50)
        self.shell.update_progress_bar(500)

        # Un-Initialize when there is no progress bar shown because it was very fast

        self.shell.finish_progress_bar()

    def test_print_unicode(self):
        self.shell.print_color(u"‖This is a text in unicode‖", ShellColor())


