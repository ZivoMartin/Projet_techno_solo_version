from controller import Controller
from model import Model
from view import View
import tkinter as tk

class Main:

    def __init__(self):
        view = View()
        model = Model(view)
        controller = Controller(view, model)
        view.window.mainloop()

Main()