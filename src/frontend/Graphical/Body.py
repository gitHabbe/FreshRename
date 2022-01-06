from tkinter import Frame
from src.frontend.Graphical.Graphical import Graphical


class Body:
    # __graphical = Graphical()

    def __init__(self, parent: Frame):
        self.frame = Frame(parent)
        self.frame.grid()
