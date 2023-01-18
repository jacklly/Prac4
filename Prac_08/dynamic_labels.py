from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ["Jack", "Blake", "Blair", "Lara", "Londyn"]


class DynamicLabels(App):

    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in NAMES:
            temp_label = Label(text=str(name))
            self.root.ids.main.add_widget(temp_label)
        return self.root


DynamicLabels().run()
