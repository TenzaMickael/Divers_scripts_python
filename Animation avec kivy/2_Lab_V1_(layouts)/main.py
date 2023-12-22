from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsExemple(GridLayout):
    compteur = 1
    compteur_actif = BooleanProperty(False)
    mon_texte  = StringProperty("1")
    #slider_value_txt = StringProperty("0")
    text_input_str = StringProperty("Votre nom")
    
    def on_button_click(self):
        print("Button click")
        if self.compteur_actif:
            self.compteur += 1
            self.mon_texte = str(self.compteur)
        
    def on_toggle_button_state(self, widget):
        #print(f"toggle state {widget.state}")
        if widget.state == "normal":
            print("OFF")
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            print("ON")
            widget.text = "ON"
            self.compteur_actif = True
            
    def on_switch_active(self, widget):
        print(f"Switch : {widget.active}")
        
    #def on_slider_value(self, widget):
        #print(f"Slider : {int(widget.value)}")
        #self.slider_value_txt = str(int(widget.value))
        
        
    def on_text_validate(self, widget):
        self.text_input_str = widget.text
            
        


class LeLabApp(App):
    pass


LeLabApp().run()

