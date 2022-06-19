from tkinter import StringVar, Frame, Entry, Label, Button, messagebox

from src.frontend.Graphical.SearchForm import SearchForm
from src.models.RequestShow import RequestShow


class FormWrapper:
    showSearchForm = True
    showConfirmForm = False

    def __init__(self, parent: Frame):
        self.showName = ""
        self.frame = Frame(parent)
        # self.searchForm = Frame(self.frame)
        self.searchForm = SearchForm(self.frame)
        self.searchForm.build()
        self.confirmForm = Frame(self.frame)
        self.frame.grid()

    # def buildSearchForm(self):
    #     inputType = StringVar()
    #     showEntry = Entry(self.searchForm, textvariable=inputType, width=40)
    #     showEntry.grid(pady=10, padx=5, row=0, column=1)
    #     showEntry.bind("<Return>", lambda event, widget=showEntry: self.requestShow(showEntry.get()))
    #     showEntry.focus()
    #
    #     showLabel = Label(self.searchForm, text="TV Show:")
    #     showLabel.grid(row=0, column=0, padx=5)
    #
    #     searchButton = Button(self.searchForm, text="Search")
    #     searchButton.grid(row=0, column=2)
    #     searchButton.bind("<Button-1>", lambda x: self.requestShow(showEntry.get()))
    #
    #     self.searchForm.grid()

    def buildConfirmForm(self):
        showLabel = Label(self.confirmForm, text=self.showName)
        showLabel.grid(row=0, column=0, padx=5)

        yesButton = Button(self.confirmForm, text="YES", bg="green", fg="white")
        yesButton.grid(row=0, column=1)
        yesButton.bind("<Button-1>", lambda x: self.confirmShow())

        noButton = Button(self.confirmForm, text="NO", bg="red", fg="white")
        noButton.grid(row=0, column=2)
        noButton.bind("<Button-1>", lambda x: self.toggleConfirmForm())

        self.confirmForm.grid()

    # def requestShow(self, term: str):
    #     requester = RequestShow()
    #     try:
    #         tvShow = requester.name(term)
    #         print(term)
    #         self.showName = tvShow["show"]["name"]
    #         self.toggleSearchForm()
    #     except IndexError:
    #         messagebox.showerror("Error", f"Tv-Show '{term}' not found")
    #         print("ERROR")

    @staticmethod
    def confirmShow():
        print("Correct show")

    def toggleSearchForm(self):
        self.searchForm.grid_remove()
        self.buildConfirmForm()

    def toggleConfirmForm(self):
        self.showName = ""
        self.confirmForm.grid_remove()
        self.buildSearchForm()
