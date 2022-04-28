import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

kivy.require("2.0.0")

class Touch(Widget):
    button = ObjectProperty(None)

    def touchdown(self, touch):
        print("Mouse Down", touch)
        self.button.opacity(0.5)

    def touchup(self, touch):
        pass

    def touchmove(self, touch):
        print("Mouse Up", touch)
        self.button.opacity(1)



class MyGrid(Widget):
    # def __init__(self, **kwargs):
    #     super(MyGrid, self).__init__(**kwargs)
    #     self.cols = 2

    #     self.label1 = Label(text="Name")
    #     self.add_widget(self.label1)

    #     self.name = TextInput(multiline=False)
    #     self.add_widget(self.name)

    #     self.label2 = Label(text="E-mail")
    #     self.add_widget(self.label2)

    #     self.mail = TextInput(multiline=False)
    #     self.add_widget(self.mail)

    #     self.label3 = Label(text="Age")
    #     self.add_widget(self.label3)

    #     self.age = TextInput(multiline=False)
    #     self.add_widget(self.age)

    #     self.button1 = Button(text="Submit")
    #     self.button2 = Button(text="Reset")

    #     self.add_widget(self.button1)
    #     self.button1.bind(on_press=self.func_button1)

    #     self.add_widget(self.button2)
    #     self.button2.bind(on_press=self.func_button2)


    # def func_button1(self, instance):
    #     print(f"Name : {self.name.text}\nEmail : {self.mail.text}\nAge : {self.age.text}")

    # def func_button2(self, instance):
    #     self.name.text = ""
    #     self.mail.text = ""
    #     self.age.text = ""

    # name = ObjectProperty(None)
    # email = ObjectProperty(None)

    # def clicked(self):
    #     print(f"Name : {self.name.text}\nEmail : {self.email.text}")

    pass

class MyApp(App):

    def build(self):
        return Touch()


if __name__ == "__main__":
    MyApp().run()

