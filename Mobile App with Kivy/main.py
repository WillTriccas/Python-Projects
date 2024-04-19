import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
from glob import glob
from pathlib import Path
import random
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from hoverable import HoverBehavior 

Builder.load_file('design.kv')

class RootWidget(ScreenManager):
    pass

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    
    def login(self, username, password):
        with open('users.json') as myfile:
            users = json.load(myfile)
        if username in users and users[username]['password'] == password:
            self.manager.current = "main_application_screen"
        else:
            self.ids.incorrect_login.text = "Wrong Username or Password! please try again"

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as myfile:
            users = json.load(myfile)

        users[uname] = {'username': uname, 'password': pword, 
        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json", 'w') as myfile:
            json.dump(users, myfile)

    def sign_up_success(self):
        self.manager.current = "sign_up_success_screen"
    def go_back(self):
        self.manager.current = "login_screen"
        self.manager.transition.direction = 'right'

class SignUpSuccessScreen(Screen):
    def log_in_page(self):
        self.manager.current = "login_screen"
        self.manager.transition.direction = 'right'

class MainApplicationScreen(Screen):
    def log_out(self):
        self.manager.transition.direction ='right'
        self.manager.current = "login_screen"

    def get_quote(self, feelings):
        feelings = feelings.lower()
        available_quotes = glob("quotes/*txt")

        available_quotes = [Path(filename).stem for filename in available_quotes]

        if feelings in available_quotes:
            with open(f"quotes/{feelings}.txt", encoding= "utf8") as myfile:
                quotes = myfile.readlines()

            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling!"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass     
        

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ =='__main__':
    MainApp().run()