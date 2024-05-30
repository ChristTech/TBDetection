from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton, MDExtendedFabButtonIcon
import kivymd_extensions.akivymd

Window.size = (360, 650)
# Builder.load_file("TBDetection.kv")


class HomeScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


class TBDetectedScreen(Screen):
    pass


class TBNotDetectedScreen(Screen):
    pass


ScreenManager = ScreenManager()

ScreenManager.add_widget(HomeScreen(name="Home"))
ScreenManager.add_widget(UploadScreen(name="Upload"))
ScreenManager.add_widget(HomeScreen(name="Verified"))
ScreenManager.add_widget(HomeScreen(name="Unverified"))


class TBAPP(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Darkgray"
        file = Builder.load_file('TBDetection.kv')
        return file

if __name__ == '__main__':
    TBAPP().run()
