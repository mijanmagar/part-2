from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

class SettingsScreen(Screen):
    pass

Builder.load_file(os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + '\\settings_screen.kv')