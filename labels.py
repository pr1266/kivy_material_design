from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.boxlayout import MDBoxLayout

class DemoApp(MDApp):

    def build(self):

        label = MDLabel(
            text = 'a message from Pr1266', 
            halign = 'center', 
            theme_text_color = 'Custom', 
            text_color = (198/255.0, 98/255.0, 81/255.0, 1), 
            font_style = 'H3',
            )

        icon_label = MDIcon(icon = 'language-python', halign = 'center')
        return icon_label

DemoApp().run()