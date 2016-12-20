#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
.. module:: ShellInterface
:platform: Unix
:synopsis: Shellinterface implement a colorful text in shell and implement a special progressbar
who may or may not appear depending on the time you have to wait

.. moduleauthor:: Pierre Sassoulas <pierre.sassoulas@gmail.com>
"""

from color import Color
from progressbar import ProgressBar, AnimatedMarker, Percentage, ETA, RotatingMarker, Bar
from shell_color import ShellColor
from style import Style
import time

MAXIMUM_TIME_WITHOUT_FEEDBACK = 0.5
MAXVAL = 100

# This is a widget (see the ProgressBar module for more detail),
# you can add whatever you like in it.

complete_widgets = [
    ShellColor(Color.WHITE, Style.BOLD, Color.BLACK).color,
    'Please wait ',
    AnimatedMarker(),
    ' ',
    Percentage(),
    ' ',
    Bar(marker=RotatingMarker()),
    ' ',
    ETA(),
    ' ',
    ShellColor().color,
    ]


class ShellInterface(object):

    def __init__(self, widgets=complete_widgets):
        ''' Constructor ShellInterface
            :return: A ShellInterface '''

        self.__widgets = widgets
        self.__time = None
        self.__progress_bar = None

    def print_color(self, object_to_print, color):
        ''' Print a text in shell with a specific color and reset the color effect. 
            If some part of the text to print are already in color they stay in this color.
            If they are reseted the color effect apply again until the end.
            :param object_to_print: An object which can be a String (which may be a string containing Color) or any object
            :param color: A ShellColor that will be used to color the String in shell. '''

        class NotAShellColorException(Exception):

            ''' print_color Private Exception class. '''

            def __init__(self, not_a_ShellColor):
                ''' :param not_a_ShellColor: An object that is not a ShellColor '''

                self.message = '{0} is not a ShellColor but a {1}'.format(not_a_ShellColor,
                        not_a_ShellColor.__class__.__name__)

            def __str__(self):
                return self.message + ', use a ShellColor to print text in color.'

        if color.__class__.__name__ != 'ShellColor':
            raise NotAShellColorException(color)

        try:
            text_to_print = str(object_to_print)
        except:
            text_to_print = unicode(object_to_print)
            text_to_print = text_to_print.encode('utf-8')

        # We replace each "end of color" we find by by end of color + our color,
        # in order to stay in the same color  if we encounter a colored string
        # inside the string we have to color while keeping the inside colored string
        #  in its color.

        recolored_text = text_to_print.replace(ShellColor().color, ShellColor().color
                                               + color.color)
        print(color.get_colored_text(recolored_text))

    def start_progress_bar(self):
        ''' Start a progress bar in shell. It won't print anything before it have to. '''

        self.__time = time.time()

    def update_progress_bar(self, percentage):
        ''' Display the progress bar or not taking account of the percentage 
            and the time since the beginning.
            :param percentage: The percentage the actual task has reached.  '''

        if self.__progress_bar == None:
            if self.__time == None:
                raise RuntimeError('Uninitialized progress bar in ShellInterface')
            elif time.time() - self.__time < MAXIMUM_TIME_WITHOUT_FEEDBACK:

                # We consider that the treatment is done instantly (no unnecessary feedback)

                return True
            else:

                # We need a feedback

                self.__progress_bar = ProgressBar(widgets=self.__widgets, maxval=MAXVAL)
                self.__progress_bar.start()
        self.__progress_bar.update(percentage)

    def finish_progress_bar(self):
        ''' Finish the progress bar. '''

        self.__time = None
        if self.__progress_bar != None:
            self.__progress_bar.finish()
            self.__progress_bar = None


