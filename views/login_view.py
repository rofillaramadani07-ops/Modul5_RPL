import tkinter as tk

class LoginView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.geometry("300x200")