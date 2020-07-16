from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker, MDDatePicker
from datetime import datetime

KV = '''
FloatLayout:

    MDRaisedButton:
        text: "Open time picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_time_picker()
    
    MDRaisedButton:
        text: "Open Date picker"
        pos_hint: {'center_x': .5, 'center_y': .4}
        on_release: app.show_date_picker()

'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_time_picker(self):
        '''Open time picker dialog.'''

        time_dialog = MDTimePicker()
        time_dialog.bind(time = self.get_time)
        time_dialog.open()

    def show_date_picker(self):
        min_date = datetime.strptime("2020:02:15", '%Y:%m:%d').date()
        max_date = datetime.strptime("2020:02:20", '%Y:%m:%d').date()
        date_dialog = MDDatePicker(
            callback=self.get_date,
            min_date=min_date,
            max_date=max_date,
        )
        date_dialog.open()

    def get_date(self, instance, date):

        return date

    def get_time(self, instance, time):

        return time

Test().run()