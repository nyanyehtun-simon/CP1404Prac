"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    input_number = NumericProperty(0)

    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 200)
        self.title = "Square Number"
        self.root = Builder.load_file('miles_to_kilometers.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        # result = value / 1000
        # self.root.ids.output_label.text = str(result)

    def input_number_changed(self, value):
        self.input_number = value

    def handle_increment(self):
        self.input_number += 1

        self.root.ids.input_number = self.input_number

    def handle_decrement(self):
        self.input_number -= 1


SquareNumberApp().run()
