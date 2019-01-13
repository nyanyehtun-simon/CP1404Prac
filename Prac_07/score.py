from kivy.app import App
from kivy.lang import Builder


class GreetApp(App):

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('score.kv')
        return self.root

    def handle_greet(self):
        score = int(self.root.ids.input_name.text)
        status = ''
        if score > 75:
            status = 'Distinction'
        elif score >= 65:
            status = 'Credit'
        elif score > 60:
            status = 'Pass'
        else:
            status = 'Fail'
        self.root.ids.output_label.text = "Score Status: " + status

    def clear_text(self):
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''

GreetApp().run()
