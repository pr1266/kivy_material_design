from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder

class UserName(MDTextField):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = "enter your username"
        self.helper_text = 'or click on forgot username'
        self.helper_text_mode = 'on_focus'
        self.icon_right = 'android'
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.size_hint_x = None
        self.width = 300

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        self.username = UserName()
        button = MDRectangleFlatButton(text = 'Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                       on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self,obj):
        print(self.username.text)


DemoApp().run()