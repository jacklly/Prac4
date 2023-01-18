from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

ONE_MILE = 1.60934  # km


class ConvertMilesKm(App):
    result_screen = StringProperty()

    def build(self):
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        miles = self.root.ids.miles_text.text
        try:
            answer = float(miles) * ONE_MILE
        except ValueError:
            answer = 0
            self.root.ids.miles_text.text = '0.0'
        self.result_screen = str(answer)

    def handle_up(self):
        miles = self.root.ids.miles_text.text
        up_value = float(miles) + 1
        self.root.ids.miles_text.text = str(up_value)
        self.handle_conversion()

    def handle_down(self):
        miles = self.root.ids.miles_text.text
        down_value = float(miles) - 1
        self.root.ids.miles_text.text = str(down_value)
        self.handle_conversion()


ConvertMilesKm().run()
