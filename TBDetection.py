import kivy
from kivymd.tools.hotreload.app import MDApp
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText
from kivy.core.window import Window
from kivy.lang import Builder

Window.size = ('960dp', '720dp')

KV = """
MDBoxLayout:
    adaptive_height: True
    md_bg_color: app.theme_cls.primaryColor
"""

class TBAPP(MDApp):
    
    def build(self):
        return Builder.load_string(KV)