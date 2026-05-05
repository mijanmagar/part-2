from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from screens.home_screen import HomeScreen
from screens.add_plant_screen import AddPlantScreen
from screens.plant_detail_screen import PlantDetailScreen
from screens.settings_screen import SettingsScreen

from kivy.properties import BooleanProperty, StringProperty

class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        self.opacity = 0.5
        return super().on_press()

    def on_release(self):
        self.opacity = 1.0
        return super().on_release()


class AppShell(BoxLayout):
    is_home = BooleanProperty(True)
    navigation_text = StringProperty("Home")
    screen_names = {'home': "Home", 'settings': "Home -> Settings", 'plant_detail': "Home -> Plant Detail",  'add_plant': "Home -> Add Plant" }

    def change_screen(self, screen_name):
        self.ids.sm.current = screen_name
        
        if screen_name == 'home':
            self.is_home = True

        else:
            self.is_home = False

        self.navigation_text = self.resolve_screen(screen_name)

    def resolve_screen(self, screen_name):
        return self.screen_names[screen_name]


Builder.load_file("app_shell.kv")
