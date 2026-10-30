import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView

class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()

    def run(self):
        self.view.mainloop()