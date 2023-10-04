""""""

import random

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder

class tamagotchi(MDApp):
    def build(self):
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
                                           on_release=self.show_data)
        generate_random_pet_name = MDRectangleFlatButton(text="Generate random pet name", pos_hint={"center_x": 0.4, "center_y": 0.5},
                                           on_release=self.random_pet_name)

        screen.add_widget(self.pet_name)
        screen.add_widget(create_pet)
        screen.add_widget(generate_random_pet_name)
        return screen

    def random_pet_name(self, obj):
        with open("petnames.txt", "r") as file:
            pet_names = file.read().replace("\n", "").split(",")
        self.pet_name.text = random.choice(pet_names)


    def show_data(self, click):
        print(self.pet_name.text)


if __name__ == "__main__":
    tamagotchi().run()