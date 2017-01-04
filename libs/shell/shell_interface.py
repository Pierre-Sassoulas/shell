# -*- coding: utf-8 -*-

"""
.. module:: ShellInterface
:platform: Unix
:synopsis: Shellinterface implement a colorful text in shell.
"""

from libs.shell.shell_color import ShellColor

class ShellInterface(object):

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
            msg = "Got '{}' but expected 'ShellColor'".format(color.__class__)
            raise TypeError(msg)
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
