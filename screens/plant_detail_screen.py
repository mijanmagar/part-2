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
        pass # remove this when the function is completed.
        
        # 1. Set the "pot" attribute to the passed in pot object.

        # 2. Assign the properties that have a one-way binding to front-end
        #    widgets to populate the front end with the plant data.
        #    Hint:  The "pot" object has a plant attribute that
        #    holds the plant data for this pot.

        # 3. Clear the Tips list by calling "clear_widgets"

        # 4. grab the tips for the plant and loop through it,
        #    adding each plant tip to the front-end tips list.
        

Builder.load_file(os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + '\\plant_detail_screen.kv')