'''
Aforgizmo GUI
=============

An App which saves, retrieves, edits and displays aphorisms

This app is written in Python using the Kivy library for cross-platform support (Android, IOS, Windows, Linux, Mac OSX).  See http://kivy.org/docs/guide/packaging.html for instructions on packaging the application for the different platforms.
'''
import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.utils import platform
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from peewee import *
import models

def is_desktop():
    """
    Detect if we are running on the desktop or not
    :return: boolean True if running on a desktop platform or String platform
    """
    if platform in ('linux', 'windows', 'macosx'):
        return True
    else:
        return p


class MainWindow(BoxLayout):
    '''Main UI Widget
    .. versionadded:: 1.0
    .. note:: This new feature will likely blow your mind
    .. warning:: Please take a seat before trying this feature
    '''
    quote_text = ObjectProperty()

    button_random = ObjectProperty()
    quote_text    = ObjectProperty()
    quote_format  = ObjectProperty()
    quote_font    = ObjectProperty()
    author_font   = ObjectProperty()
    button_font   = ObjectProperty()

    def button_random_press(self, *args):
        action = args[0]
        if action == 'random':
            for a in models.Aphorism.select().order_by(fn.Random()).limit(1):
                self.quote_text.text = self.quote_format.format(
                                                        aphorism = a.aphorism,
                                                        author = a.author,
                                                        author_font = self.author_font,
                                                        author_size = int(self.ids.label_text.font_size * 0.75),
                                                        quote_font = self.quote_font)
        else:
            pass


class MainApp(App):
    '''Main Program
    '''
    title = 'Aforgizmo Aphorisms'
    icon = 'assets/img/icon.png'

    def __init__(self):
        App.__init__(self)

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()
