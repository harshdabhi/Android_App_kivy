from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField ## for user input
from kivy.lang import Builder  # to add feature 
from kivymd.uix.button import MDFillRoundFlatButton

username_helper="""
MDTextField:
    hint_text:"Enter User"
    icon_right:"android"
    helper_text:"or click on icon"
    helper_text_mode:"persistent"
    pos_hint:{'center_x':0.5,'center_y':0.5}
    size_hint_x:None
    width:300


"""

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Yellow'
        self.theme_cls.theme_style='Dark'
        screen=Screen()

        #### will use below code to add user input and when builder is used then MDtextField is not used 
        # username=MDTextField(text='Enter User',pos_hint={'center_x':0.5,'center_y':0.5},
        #                      size_hint_x=None,width=300)
        
        
        self.username=Builder.load_string(username_helper)
        button=MDFillRoundFlatButton(text="Click Me",pos_hint={'center_x':0.5,'center_y':0.4},
                                     on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)

        return screen
    
    def show_data(self, *args): 
        print(self.username.text)
    
DemoApp().run()