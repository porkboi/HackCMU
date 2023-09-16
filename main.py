from kivymd.app import MDApp
#from kivyauth.google_auth import initialize_google, login_google, logout_google
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.button import *
from kivy.uix.textinput import TextInput
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.selectioncontrol.selectioncontrol import MDSwitch
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.dialog import MDDialog
from kivymd.icon_definitions import md_icons
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.graphics import RoundedRectangle
from datetime import datetime
from test import *
from openAI import *

Window.size = (350, 600)

class query:
    def __init__(self):
        self.numsun = 0
        self.orborbper = 0
        self.planetradius = 0
        self.starradius = 0
        self.starmass = 0
        self.starmetallic = 0
        self.planetmass = 0
        self.hostname = ""

class menuScreen(Screen):
    dialog = None
    def on_enter(self, *args):
        super().on_enter(*args)
        topappbar = MDTopAppBar(title = "Bearth.ai", 
                                right_action_items=[["help", self.buttonPress4]], 
                                pos_hint = {"center_x": .5, 
                                            "center_y": .95}
                                            )
        #add Labels
        title = MDLabel(text = "Planet Generator", 
                        pos_hint = {"center_x": .64, 
                                    "center_y": .85}, 
                                    font_style = "H4"
                                    )
        self.output = MDLabel(text = "Awaiting Output...",
                         size_hint = (.45, .05),  
                         pos_hint = {"center_x": .7, 
                                     "center_y": .25},
                                     font_style = "Body2"
                                     )
        #add Search Mechanism
        self.textInput = TextInput(hint_text = "No. Suns (eg. 2)",
                                   size_hint = (.6, .05), 
                                   pos_hint = {"center_x": .4,
                                               "center_y": .76}
                                               )
        self.textInput2 = TextInput(hint_text = "Orbital Period in Days",
                                    size_hint = (.6, .05), 
                                    pos_hint = {"center_x": .4,
                                                "center_y": .70}
                                                )
        self.textInput3 = TextInput(hint_text = "Planet Radius in no. Earths",
                                    size_hint = (.6, .05), 
                                    pos_hint = {"center_x": .4,
                                                "center_y": .64}
                                                )
        self.textInput4 = TextInput(hint_text = "Stellar Radius",
                                    size_hint = (.6, .05), 
                                    pos_hint = {"center_x": .4,
                                                "center_y": .58}
                                                )
        self.textInput5 = TextInput(hint_text = "Stellar Mass",
                                    size_hint = (.6, .05), 
                                    pos_hint = {"center_x": .4,
                                                "center_y": .52}
                                                )
        #add buttons
        searchbutton = MDIconButton(icon="search-web",
                                    size_hint = (.04, .04),
                                    on_release = self.buttonPress6,
                                    pos_hint = {"center_x": .8,
                                                "center_y": .56}
                                                )
        imfeelinglucky = MDRaisedButton(text="I'm feeling lucky!", 
                                        on_release=self.buttonPress5,
                                        pos_hint = {"center_x": .5,
                                                    "center_y": .45}
                                                    )
        #image subclass
        self.aimg = AsyncImage(source='',
                               size_hint = (.25, .2),
                               pos_hint = {"center_x": .15,
                                           "center_y": .25}
                               )
        self.aimg2 = AsyncImage(source='',
                               size_hint = (.25, .2),
                               pos_hint = {"center_x": .32,
                                           "center_y": .25}
                               )

        self.add_widget(topappbar)
        self.add_widget(title)
        self.add_widget(self.textInput)
        self.add_widget(self.textInput2)
        self.add_widget(self.textInput3)
        self.add_widget(self.textInput4)
        self.add_widget(self.textInput5)
        self.add_widget(imfeelinglucky)
        self.add_widget(searchbutton)
        self.add_widget(self.aimg)
        self.add_widget(self.aimg2)
        self.add_widget(self.output)

    def buttonPress4(self,obj):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Help:",
                text="Bearth.ai helps to generate hypothetical planets based on many different parameters and aspects!\nHave fun toggling around and observing possible correlations!",
                buttons=[
                    MDRaisedButton(
                        text="OKAY",
                        on_release=lambda _: self.dialog.dismiss()
                    )
                ],
            )
        self.dialog.open()

    def buttonPress5(self, obj):
        if self.textInput.text == "":
            query.numsun = float(random.randint(1, 4))
            self.textInput.text = str(query.numsun)
        else:
            query.numsun = float(self.textInput.text)
        if self.textInput2.text == "":
            query.orborbper = random.uniform(3.85, 76.68)
            self.textInput2.text = str(query.orborbper)
        else:
            query.orborbper = float(self.textInput2.text)
        if self.textInput3.text == "":
            query.planetradius = random.uniform(1.5, 12.5)
            self.textInput3.text = str(query.planetradius)
        else:
            query.planetradius = float(self.textInput3.text)
        if self.textInput4.text == "":
            query.starradius = random.uniform(0.77, 1.37)
            self.textInput4.text = str(query.starradius)
        else:
            query.starradius = float(self.textInput4.text)
        if self.textInput5.text == "":
            query.starmass = random.uniform(0.8, 1.16)
            self.textInput5.text = str(query.starmass)
        else:
            query.starmass = float(self.textInput5.text)
        query.starmetallic = model_stellarM([query.numsun, 
                                                 query.orborbper, 
                                                 query.planetradius, 
                                                 query.starradius,
                                                 query.starmass
                                                 ])
        query.planetmass = model_planetMass([query.numsun, 
                                                 query.orborbper, 
                                                 query.planetradius, 
                                                 query.starradius,
                                                 query.starmass,
                                                 query.starmetallic
                                                 ])
        query.hostname = locate_star(query.starmetallic)
        funfacts = getFunFacts(query.numsun, query.orborbper, query.planetradius, query.starradius, query.starmass)
        a, b, c = getDallEPrompt(query.planetmass, query.planetradius, query.starmetallic)
        x, y = getPlanetImage(a, b, c)
        self.aimg.source =  x
        self.aimg2.source = y
        self.output.text = f"Host Star System: {query.hostname}, Star Metallic: {str(query.starmetallic)[:7]}, Planet Mass: {str(query.planetmass)[:7]}\n" + funfacts

    def buttonPress6(self, obj):
        #print(float(self.textInput.text))
        query.numsun = float(self.textInput.text)
        query.orborbper = float(self.textInput2.text)
        query.planetradius = float(self.textInput3.text)
        query.starradius = float(self.textInput4.text)
        query.starmass = float(self.textInput5.text)
        query.starmetallic = model_stellarM([query.numsun, 
                                                 query.orborbper, 
                                                 query.planetradius, 
                                                 query.starradius,
                                                 query.starmass
                                                 ])
        query.planetmass = model_planetMass([query.numsun, 
                                                 query.orborbper, 
                                                 query.planetradius, 
                                                 query.starradius,
                                                 query.starmass,
                                                 query.starmetallic
                                                 ])
        query.hostname = locate_star(query.starmetallic)
        funfacts = getFunFacts(query.numsun, query.orborbper, query.planetradius, query.starradius, query.starmass)
        a, b, c = getDallEPrompt(query.planetmass, query.planetradius, query.starmetallic)
        x, y = getPlanetImage(a, b, c)
        self.aimg.source =  x
        self.aimg2.source = y
        self.output.text = f"Host Star System: {query.hostname}, Star Metallic: {str(query.starmetallic)[:7]}, Planet Mass: {str(query.planetmass)[:7]}\n" + funfacts
 
class mathvisionApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        sm = ScreenManager()
        sm.add_widget(menuScreen(name="menu"))
        return sm

if __name__ == '__main__':
    mathvisionApp().run()