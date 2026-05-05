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
        # 1. Initialize the parent Screen class
        super(AddPlantScreen, self).__init__(**kwargs)

    def on_pre_enter(self, *args):
        self.populate_plants()

    def populate_plants(self, filter=''):
        pass # remove the pass statement when the method is implemented.

        # 1. Get Running app.  
        #    Hint: The App library has a built-in command
        #          called "get_running_app" that returns a reference to the running
        #          App object (defined in app.py)
        #          this will allow us to call the model functions
        

        # 2. clear widgets from the plant choice list.
        

        # 3. Grab the plant data from the model by calling its List Plants with Commmon
        #    Name method. 
       
       
        # 4. Loop through the plant data retrieved in Step 3...
        
            # 4-a. Create a radio widget based on the custom radio widget made in
            #      custom_widgets.
            
            # 4-b. Assign the data from the plant model to the custom radios text and id
            #      properties.
            
            # 4-c. Add the radio widget to the options list by calling "add_widget"
            
        
    def on_confirm_press(self):
        pass # remove the pass statement when the method is implemented.
        
        # 1. Loop through the radio buttons in the plants list.
        #    Hint: the plant choice list has a "children" property
        #    that returns a list of the child widgets (which are the radio
        #    options)
        
            # 1-a. Determine if the item is selected by using the custom
            #      radio icons is_selected property.

                # 1-a-I. Use try-except, excepting on a Key error 

                    # 1-a-I-a. Get the running app
                    
                    # 1-a-I-b. Call the plant data models GetPlantByID
                    #          passing it the id of the plant item option's
                    #          id field.

                    # 1-a-I-c. Create a new Pot model object by calling the 
                    #          Add Pot method in the pot model.
                    
                    # 1-a-I-d. Set the plant option's is_selected to false
                    #          to deselect it from the list.

                    # 1-a-I-e. Clear the Pot ID textbox to reset it.

                    # 1-a-I-f. Call the shell's change screen method
                    #          to return to the home page.

                # 1-a-II. On KeyError, set the error message label to an appropriate
                #         message to indicate that the pot ID is already used.

    def on_filter_change(self):
        # This is called when the filter is changed to filter the plant 
        # options.
        # Note that this will only work when populate plants is fully implemented.
        self.populate_plants(self.txtPlantFilter.text)


Builder.load_file(os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + '\\add_plant_screen.kv')