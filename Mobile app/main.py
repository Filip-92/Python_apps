import glob
import json
from pathlib import Path
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.config import Config
from datetime import datetime

from matplotlib.style import available

Builder.load_file('Mobile app/design.kv')
Config.set('graphics', 'width', '150')
Config.set('graphics', 'height', '500')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, username, password):
        with open("Mobile app/users.json") as file:
            users = json.load(file)
        if username in users and users[username]['password'] == password:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "Wrong username or password"


class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, username, password):
        with open("Mobile app/users.json") as file:
            users = json.load(file)

        users[username] = {'username': username, 'password': password, 
            'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("Mobile app/users.json", 'w') as file:
            json.dump(users, file)

        self.manager.current = "sign_up_screen_success"

    def go_back(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "login_screen"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("Mobile app/quotes/*txt")

        available_feelings = [Path(filename).stem for filename in 
                                available_feelings]

        if feel in available_feelings:
            with open(f"Mobile app/quotes/{feel}.txt", encoding='utf-8') as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()