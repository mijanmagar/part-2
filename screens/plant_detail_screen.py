from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from custom_widgets import InformationLabel

class PlantDetailScreen(Screen):
    pot_id = StringProperty()
    scientific_name = StringProperty("")
    common_name = StringProperty("")
    water_needs = StringProperty("")
    lighting = StringProperty("")
    pruning = StringProperty("")
    soil = StringProperty("")
    bxlTipsList = ObjectProperty()

    def on_enter(self, *args):
        self.__pot = None

    def setup_screen(self, pot):
        # 1. Store the pot object
        self.__pot = pot

        # 2. Assign string properties from the pot's plant data
        self.pot_id = pot.pot_id
        self.scientific_name = pot.plant.scientific_name
        self.common_name = pot.plant.common_name
        self.water_needs = pot.plant.maintenance[0]
        self.lighting = pot.plant.maintenance[1]
        self.pruning = pot.plant.maintenance[2]
        self.soil = pot.plant.maintenance[3]

        # 3. Clear the tips list
        self.bxlTipsList.clear_widgets()

        # 4. Add each tip as an InformationLabel
        for tip in pot.plant.tips:
            tip_label = InformationLabel()
            tip_label.label_title = "Tip"
            tip_label.label_text = tip
            tip_label.is_list_item = True
            self.bxlTipsList.add_widget(tip_label)


Builder.load_file(os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + '\\plant_detail_screen.kv')