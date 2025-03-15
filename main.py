from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

class Calculator(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.formula = "0"

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if self.formula == "0":
            self.formula = ""
        
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if str(instance.text).lower() == "x":
            self.formula += "*"
        else:
            self.formula += str(instance.text)
        
        self.update_label()

    def clear_entry(self, instance):
        self.formula = "0"
        self.update_label()

    def toggle_sign(self, instance):
        if self.formula.startswith("-"):
            self.formula = self.formula[1:]
        else:
            self.formula = "-" + self.formula
        self.update_label()

    def handle_parentheses(self, instance):
        self.formula += "("
        self.update_label()

    def close_parentheses(self, instance):
        self.formula += ")"
        self.update_label()

    def calc_result(self, instance):
        try:
            self.lbl.text = str(eval(self.formula))
            self.formula = "0"
        except ZeroDivisionError:
            self.lbl.text = "Ошибка: деление на ноль"
        except SyntaxError:
            self.lbl.text = "Ошибка синтаксиса"

    def build(self):
        self.formula = "0"
        b1 = BoxLayout(orientation="vertical", padding=25)
        g1 = GridLayout(cols=4, spacing=3, size_hint=(1, .6))

        self.lbl = Label(text="0", font_size=40, halign="right", valign="center", size_hint=(1, .6))
        b1.add_widget(self.lbl)

        g1.add_widget(Button(text="7", on_press=self.add_number))
        g1.add_widget(Button(text="8", on_press=self.add_number))
        g1.add_widget(Button(text="9", on_press=self.add_number))
        g1.add_widget(Button(text="X", on_press=self.add_operation))

        g1.add_widget(Button(text="4", on_press=self.add_number))
        g1.add_widget(Button(text="5", on_press=self.add_number))
        g1.add_widget(Button(text="6", on_press=self.add_number))
        g1.add_widget(Button(text="-", on_press=self.add_operation))

        g1.add_widget(Button(text="1", on_press=self.add_number))
        g1.add_widget(Button(text="2", on_press=self.add_number))
        g1.add_widget(Button(text="3", on_press=self.add_number))
        g1.add_widget(Button(text="+", on_press=self.add_operation))

        g1.add_widget(Widget())  # Пустой виджет для выравнивания
        g1.add_widget(Button(text="0", on_press=self.add_number))
        g1.add_widget(Button(text=".", on_press=self.add_number))
        g1.add_widget(Button(text="=", on_press=self.calc_result))

        g1.add_widget(Button(text="(", on_press=self.handle_parentheses))
        g1.add_widget(Button(text=")", on_press=self.close_parentheses))
        g1.add_widget(Button(text="CE", on_press=self.clear_entry))
        g1.add_widget(Button(text="±", on_press=self.toggle_sign))

        b1.add_widget(g1)
        return b1

if __name__ == "__main__":
    Calculator().run()