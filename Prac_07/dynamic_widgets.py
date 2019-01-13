from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
import csv

class DynamicWidgets(App):
    csv_data_list = {}

    def build(self):
        self.load_data()
        self.title = "Dynamic widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')

        self.create_widgets()
        return self.root

    def create_widgets(self):
        self.root.ids.button_layout.clear_widgets()

        for button_data in self.csv_data_list:
            button = Button(text=button_data, id=button_data)
            button.bind(on_release=self.show_person_age)

            self.root.ids.button_layout.add_widget(button)

    def show_person_age(self, button_obj):
        self.root.ids.output_label.text = self.csv_data_list[button_obj.id]

    def load_data(self):
        csv_file = open('name_age.csv')
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            self.csv_data_list[row[0]] = row[1]

        print(self.csv_data_list)

DynamicWidgets().run()
