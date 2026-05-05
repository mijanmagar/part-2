from kivy.uix.screenmanager import Screen
from custom_widgets import CustomRadioItem
from kivy.lang import Builder
import os
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

class AddPlantScreen(Screen):
    lstPlantChoiceList = ObjectProperty()
    txtPlantFilter = ObjectProperty()
    txtPotIDInput = ObjectProperty()
    error_message = StringProperty()

    def __init__(self, **kwargs):
        super(AddPlantScreen, self).__init__(**kwargs)

    def on_pre_enter(self, *args):
        self.populate_plants()

    def populate_plants(self, filter=''):
        # 1. Get the running app
        app = App.get_running_app()

        # 2. Clear widgets from the plant choice list
        self.lstPlantChoiceList.clear_widgets()

        # 3. Get filtered plant data from the model
        plants = app.plant_data_model.ListPlantsWithCommonName(filter)

        # 4. Loop through plants and build radio items
        for plant in plants:
            # 4-a. Create a radio widget
            radio = CustomRadioItem()

            # 4-b. Assign plant data to the radio's text and id
            radio.text_content = f"{plant.common_name} ({plant.scientific_name})"
            radio.id = plant.id

            # 4-c. Add the radio widget to the list
            self.lstPlantChoiceList.add_widget(radio)

    def on_confirm_press(self):
        # 1. Loop through the radio buttons
        for item in self.lstPlantChoiceList.children:

            # 1-a. Check if this item is selected
            if item.is_selected:

                # 1-a-I. Try to add the pot, catch duplicate ID error
                try:
                    # 1-a-I-a. Get the running app
                    app = App.get_running_app()

                    # 1-a-I-b. Get the plant by ID
                    plant = app.plant_data_model.GetPlantByID(item.id)

                    # 1-a-I-c. Add the new pot to the pot model
                    app.pot_model.AddPot(self.txtPotIDInput.text, plant)

                    # 1-a-I-d. Deselect the item
                    item.is_selected = False

                    # 1-a-I-e. Clear the Pot ID textbox
                    self.txtPotIDInput.text = ''

                    # 1-a-I-f. Go back to the home screen
                    app.shell.change_screen('home')

                except KeyError:
                    # 1-a-II. Show error for duplicate pot ID
                    self.error_message = "Error: That Pot ID is already in use. Please choose a different ID."

    def on_filter_change(self):
        self.populate_plants(self.txtPlantFilter.text)


Builder.load_file(os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + '\\add_plant_screen.kv')