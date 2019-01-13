from kivy.app import App
from kivy.lang import Builder


class GreetApp(App):

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('greet.kv')
        return self.root

    def handle_greet(self):
        print('Greet')
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_text(self):
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''

GreetApp().run()
