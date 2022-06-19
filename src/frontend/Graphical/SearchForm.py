from tkinter import StringVar, messagebox
from tkinter.ttk import Entry, Label, Button, Frame
from src.frontend.Graphical.IToggleFrame import IToggleFrame
from src.models.RequestShow import RequestShow


class SearchForm(IToggleFrame):
    def __init__(self, parent: Frame):
        self.search_form = Frame(parent)
        # self.confirmForm = confirmForm
        self.show_name = ""
        # self.frames = frames

    def build(self):
        input_type = StringVar()
        show_entry = Entry(self.search_form, textvariable=input_type, width=40)
        show_entry.grid(pady=10, padx=5, row=0, column=1)
        show_entry.bind("<Return>", lambda event, widget=show_entry: self.request_show(show_entry.get()))
        show_entry.focus()

        show_label = Label(self.search_form, text="TV Show:")
        show_label.grid(row=0, column=0, padx=5)

        search_button = Button(self.search_form, text="Search")
        search_button.grid(row=0, column=2)
        search_button.bind("<Button-1>", lambda x: self.request_show(show_entry.get()))

        self.search_form.grid()

    def close(self):
        self.search_form.grid_remove()

    def request_show(self, term: str):
        requester = RequestShow()
        try:
            tv_show = requester.name(term)
            self.show_name = tv_show["show"]["name"]
            self.close()
        except IndexError:
            messagebox.showerror("Error", f"Tv-Show '{term}' not found")
            print("ERROR")

    # def toggleFrames(self):
    #     for frame in self.frames:
    #         frame.grid_remove()