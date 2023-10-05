"""Tamagochi android app created with kivy"""

import random
import re

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder


sm = ScreenManager()



class Tamagotchi(MDApp):
    """"""

    def build(self):
        """"""
        self.theme_cls.primary_palette = "Green"
        screen = Screen()
        text = """
MDTextField:
    hint_text: "Enter pet name"
    helper_text: "or generate random"
    helper_text_mode: "on_focus"
    icon_right: "paw"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    size_hint_x: None
    width:700
"""

        self.pet_name = Builder.load_string(text)
        create_pet = MDRectangleFlatButton(text="Create pet", pos_hint={"center_x": 0.6, "center_y": 0.5},
                                           on_release=self.verify_name)
        generate_random_pet_name = MDRectangleFlatButton(text="Generate random pet name", pos_hint={"center_x": 0.4, "center_y": 0.5},
                                           on_release=self.random_pet_name)

        screen.add_widget(self.pet_name)
        screen.add_widget(create_pet)
        screen.add_widget(generate_random_pet_name)
        return screen


    def random_pet_name(self, *args) -> None:
        """Replaces the text box with a randomly
        generated pet name from a text file"""
        with open("petnames.txt", "r") as file:
            pet_names = file.read().replace("\n", "").split(",")
        self.pet_name.text = random.choice(pet_names)


    def verify_name(self, *args) -> None:
        """Verifies the name of the pet to be correct"""
        self.pet_name.text = self.pet_name.text.strip()
        match = re.fullmatch(r"[A-z\s]+\d*", self.pet_name.text)
        # print(match.group())
        if not match:
            error_text = """Name must be only made out of letters
        and numbers following if desired"""
            dark_orange = (214/255, 128/255, 15/255, 1)
            random_name_popup = Popup(title="Name Error", title_align="center", title_size='25sp',
                size_hint=(None, None), content=Label(text=error_text, color=dark_orange), size=(700, 400),
                title_color=dark_orange, separator_color=dark_orange, background_color=[34/255, 155/255, 130/255, 0.8])
            random_name_popup.open()


if __name__ == "__main__":
    Tamagotchi().run()