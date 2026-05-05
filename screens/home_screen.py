from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.properties import StringProperty, ObjectProperty
from kivy.app import App
from kivy.clock import Clock
import os


class HomeScreen(Screen):
    pot_list = ObjectProperty()

    def on_enter(self, *args):
        Clock.schedule_once(self.populate_view)

    def populate_view(self, dt):
        app = App.get_running_app()
        
        pot_data = app.pot_model.GetAllPots()

        self.pot_list.clear_widgets()

        if len(pot_data) > 0:
            for pot in pot_data:
                pot_view_item = PotListItem()
                pot_view_item.file_name = "daisy.png"
                pot_view_item.pot_id = pot.pot_id
                self.pot_list.add_widget(pot_view_item)
        else:
            message = Label(text="Welcome!  Start by adding a new pot!")
            self.pot_list.add_widget(message)



class PotListItem(ButtonBehavior, BoxLayout):
    file_name = StringProperty("daisy.png")
    pot_id = StringProperty("Pot #XXXX")

    def on_release(self):
        p = self.parent
        while not isinstance(p, Screen):
            p = p.parent

        detail_screen = p.manager.get_screen('plant_detail')

        app = App.get_running_app()
        pot = app.pot_model.GetPot(self.pot_id)
        detail_screen.setup_screen(pot)

        app.shell.change_screen('plant_detail')
        
        return super().on_release()


Builder.load_file(os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + '\\home_screen.kv')