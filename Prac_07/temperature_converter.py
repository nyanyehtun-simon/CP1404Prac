"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder

__author__ = 'Lindsay Ward'

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('temperature_converter.kv')
        return self.root

    def convert_degrees(self, convert_flag):
        input_degrees = self.get_validated_integer_value()

        if convert_flag == 'f_to_c':
            celsius = 5 / 9 * (input_degrees - 32)
            self.root.ids.output_label.text = str(celsius)
        elif convert_flag == 'c_to_f':
            fahrenheit = input_degrees * 9.0 / 5 + 32  # regarded as celsius
            self.root.ids.output_label.text = str(fahrenheit)

    def get_validated_integer_value(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_temperature.text)
            return value
        except ValueError:
            print('Input should be the valid integer value')
            return 0


MilesConverterApp().run()
