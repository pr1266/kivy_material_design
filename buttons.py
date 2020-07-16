from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDRaisedButton
    

class Component(MDFloatLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.orientation = 'vertical'    
        self.add_widget(
            MDFlatButton(
            text = 'flat button', 
            pos_hint = {'center_x': 0.5, 'center_y': 0.2}
            )
        )

        self.add_widget(
            MDRaisedButton(
            text = 'Raised button', 
            pos_hint = {'center_x': 0.5, 'center_y': 0.4}
            )
        )

        self.add_widget(
            MDRectangleFlatButton(
            text = 'rectangle flat button', 
            pos_hint = {'center_x': 0.5, 'center_y': 0.6}
            )
        )

        self.add_widget(
            MDIconButton(
            icon = 'android',
            pos_hint = {'center_x': 0.5, 'center_y': 0.8}
            )
        )

class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        comp = Component(pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(comp)
        return screen

DemoApp().run()