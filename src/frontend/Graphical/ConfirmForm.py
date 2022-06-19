from tkinter.ttk import Frame, Label, Button

from src.frontend.Graphical import SearchForm
from src.frontend.Graphical.ToggleFrame import ToggleFrame


class ConfirmForm(ToggleFrame):
    def __init__(self, parent: Frame, searchForm: SearchForm):
        self.confirmForm = Frame(parent)
        self.searchForm = searchForm

    def build(self):
        showLabel = Label(self.confirmForm, text=self.showName)
        showLabel.grid(row=0, column=0, padx=5)

        yesButton = Button(self.confirmForm, text="YES", bg="green", fg="white")
        yesButton.grid(row=0, column=1)
        yesButton.bind("<Button-1>", lambda x: self.confirmShow())

        noButton = Button(self.confirmForm, text="NO", bg="red", fg="white")
        noButton.grid(row=0, column=2)
        noButton.bind("<Button-1>", lambda x: self.toggleConfirmForm())

        self.confirmForm.grid()

    def close(self):
        self.searchForm.grid_remove()