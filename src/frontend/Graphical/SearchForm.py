from tkinter import StringVar, messagebox
from tkinter.ttk import Entry, Label, Button, Frame
from src.frontend.Graphical.ToggleFrame import ToggleFrame
from src.models.RequestShow import RequestShow


class SearchForm(ToggleFrame):
    def __init__(self, parent: Frame):
        self.searchForm = Frame(parent)
        # self.confirmForm = confirmForm
        self.showName = ""
        # self.frames = frames

    def build(self):
        inputType = StringVar()
        showEntry = Entry(self.searchForm, textvariable=inputType, width=40)
        showEntry.grid(pady=10, padx=5, row=0, column=1)
        showEntry.bind("<Return>", lambda event, widget=showEntry: self.requestShow(showEntry.get()))
        showEntry.focus()

        showLabel = Label(self.searchForm, text="TV Show:")
        showLabel.grid(row=0, column=0, padx=5)

        searchButton = Button(self.searchForm, text="Search")
        searchButton.grid(row=0, column=2)
        searchButton.bind("<Button-1>", lambda x: self.requestShow(showEntry.get()))

        self.searchForm.grid()

    def close(self):
        self.searchForm.grid_remove()

    def requestShow(self, term: str):
        requester = RequestShow()
        try:
            tvShow = requester.name(term)
            self.showName = tvShow["show"]["name"]
            self.close()
        except IndexError:
            messagebox.showerror("Error", f"Tv-Show '{term}' not found")
            print("ERROR")

    # def toggleFrames(self):
    #     for frame in self.frames:
    #         frame.grid_remove()