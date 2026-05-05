import app_shell
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import StringProperty
import os
import custom_widgets
from Model.plant_data_model import PlantDataModel
from Model.pot_model import PotModel

Window.size = (412, 917)
Window.clearcolor = (1, 1, 1, 1)

class GreenThumbApp(App):
    base_path = StringProperty(os.path.dirname(os.path.abspath(__file__)))

    def build(self):
        self.plant_data_model = PlantDataModel(self.base_path + "\\resources\\data\\plants.xml")
        self.pot_model = PotModel()
        self.shell = app_shell.AppShell()
        return self.shell
    
if __name__ == "__main__":
    app = GreenThumbApp()
    app.run()