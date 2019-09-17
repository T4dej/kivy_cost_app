import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore

store = JsonStore("data.json")


class MyGrid(Widget):
    name = ObjectProperty(None)
    amount = ObjectProperty(None)
    date = ObjectProperty(None)

    def btn(self):
        print("Name: ", self.name.text, "Znesek: ", self.amount.text, "Datum: ", self.date.text)
        store.put(self.name.text, value=self.amount.text, date=self.date.text)
        self.name.text = ""
        self.amount.text = ""
        self.date.text = ""

    # def btn_result(self):
    #     for key, entry in store.get(all()):
    #         print(key, entry)

    def btn_result(self):
        for key in store:
            print(key)
            #print(store.keys())   #izpiše vse ključe
            #print(store.get('voda'))   #izpiše vrednosti na ključu
            #print(store.get(self.name, self.amount, self.date))


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
