from tkinter.ttk import Frame, Label, Button

from src.frontend.Graphical import SearchForm
from src.frontend.Graphical.Interface.IToggleFrame import IToggleFrame


class ConfirmForm(IToggleFrame):
    def __init__(self, parent: Frame, search_form: SearchForm):
        self.confirm_form = Frame(parent)
        self.search_form = search_form

    def build(self):
        show_label = Label(self.confirm_form, text=self.showName)
        show_label.grid(row=0, column=0, padx=5)

        yes_button = Button(self.confirm_form, text="YES", bg="green", fg="white")
        yes_button.grid(row=0, column=1)
        yes_button.bind("<Button-1>", lambda x: self.confirmShow())

        no_button = Button(self.confirm_form, text="NO", bg="red", fg="white")
        no_button.grid(row=0, column=2)
        no_button.bind("<Button-1>", lambda x: self.toggleConfirmForm())

        self.confirm_form.grid()

    def close(self):
        self.search_form.grid_remove()