from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.boxlayout import MDBoxLayout


class Component(MDBoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.orientation = 'vertical'    
        self.add_widget(
            MDLabel(
                text = 'a message from Pr1266', 
                halign = 'center', 
                theme_text_color = 'Error',  
                font_style = 'H6',
            )
        )

        self.add_widget(
            MDLabel(
                text = 'a message from Pr1266', 
                halign = 'center', 
                theme_text_color = 'Primary',  
                font_style = 'H1',
            )
        )

        self.add_widget(
            MDLabel(
                text = 'a message from Pr1266', 
                halign = 'center', 
                theme_text_color = 'Secondary',  
                font_style = 'H3',
            )
        )
        
        self.add_widget(MDIcon(icon = 'language-python', halign = 'center', color = (1, 1, 1, 1)))
        
class DemoApp(MDApp):

    def build(self):
        
        #TODO baraye theme Dark :
        #!self.theme_cls.theme_style = "Dark"
        comp = Component()
        return comp

DemoApp().run()