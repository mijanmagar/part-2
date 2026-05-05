from kivy.lang import Builder
import os
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import ColorProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button

class DetailTitleLabel(Label):
    title_text = StringProperty("Example Title")    

class InformationLabel(BoxLayout):
    label_title = StringProperty()
    label_text = StringProperty()
    is_list_item = BooleanProperty(False)

class Textbox(TextInput):
    pass

class AppButton(Button):
    color_green_pressed = ColorProperty(get_color_from_hex("#AFD88C"))
    color_grey_pressed = ColorProperty(get_color_from_hex("#C4C4C4"))
    color_red_pressed = ColorProperty(get_color_from_hex("#D88C8C"))

    color_green = ColorProperty(get_color_from_hex("#759658"))
    color_grey = ColorProperty(get_color_from_hex("#8B8B8B"))
    color_red = ColorProperty(get_color_from_hex("#855050"))

    curr_color = color_grey
    curr_color_pressed = color_grey_pressed

    button_text = StringProperty("Press Me")
    

class CustomRadioItem(ButtonBehavior, BoxLayout):
    text_content = StringProperty("Default Text")
    id = StringProperty("")
    is_selected = BooleanProperty(False)
    group = StringProperty("botanical_group") # Link items together

    def on_release(self):
        # 1. If we are in a parent layout (like a BoxLayout)
        if self.parent:
            # 2. Find all other CustomRadioItems in that same parent
            for child in self.parent.children:
                if isinstance(child, CustomRadioItem) and child.group == self.group:
                    child.is_selected = False
            
            # 3. Select this one
            self.is_selected = True

class CustomToggleSwitch(ButtonBehavior, BoxLayout):
    is_selected = BooleanProperty(False)

    def on_release(self):
        self.is_selected = not self.is_selected



Builder.load_file('custom_widgets.kv')