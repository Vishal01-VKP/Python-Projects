import kivy
from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        return Label(text="                 Hello World !!! \n\n                    I'm Vishal\n\nAnd this program is made using Kivy .")
        
if __name__ == "__main__":
    MainApp().run()