from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_file("LoginPage.kv")

class QuizPageApp(App):
    def build(self):
        return QuizManager()

class QuizManager(ScreenManager):
    pass


#Questions
class Question1Screen(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "error"

class Question2Screen(Screen):
    def answer_question(self, answer):
        if answer.lower() == "broken":
            self.manager.current = "correct"
        else:
            self.ids.invalid_guess.text = "Invalid guess \n\n Try again"
            self.ids.invalid_guess.color = "red"

class CorrectScreen(Screen):
    def next(self):
        self.manager.current = "question2"

class ErrorScreen(Screen):
    def next(self):
        self.manager.current = "question2"


QuizPageApp().run()

class LoginPageApp(App):
    def build(self):
        return LoginManager()

class LoginManager(ScreenManager):
    pass

class LoginPage(Screen):
    pass

class AccountRegister(Screen):
    pass

LoginPageApp().run()