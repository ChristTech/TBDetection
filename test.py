from kivy import Config
Config.set('graphics', 'multisamples', '0')

import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


from kivy.lang.builder import Builder
from kivymd.app import MDApp


class MyApp(MDApp):
    def build(self):
        file = Builder.load_file("test1.kv")
        return file


if __name__ == '__main__':
    MyApp().run()