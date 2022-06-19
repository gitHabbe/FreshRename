from tkinter import StringVar, Frame, Entry, Label, Button, messagebox

from src.frontend.Graphical.SearchForm import SearchForm
from src.models.RequestShow import RequestShow


class FormWrapper:
    show_search_form = True
    show_confirm_form = False

    def __init__(self, parent: Frame):
        self.show_name = ""
        self.frame = Frame(parent)
        # self.searchForm = Frame(self.frame)
        self.search_form = SearchForm(self.frame)
        self.search_form.build()
        self.confirm_form = Frame(self.frame)
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

    def build_confirm_form(self):
        show_label = Label(self.confirm_form, text=self.show_name)
        show_label.grid(row=0, column=0, padx=5)

        yes_button = Button(self.confirm_form, text="YES", bg="green", fg="white")
        yes_button.grid(row=0, column=1)
        yes_button.bind("<Button-1>", lambda x: self.confirm_show())

        no_button = Button(self.confirm_form, text="NO", bg="red", fg="white")
        no_button.grid(row=0, column=2)
        no_button.bind("<Button-1>", lambda x: self.toggle_confirm_form())

        self.confirm_form.grid()

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
    def confirm_show():
        print("Correct show")

    def toggle_search_form(self):
        self.search_form.grid_remove()
        self.build_confirm_form()

    def toggle_confirm_form(self):
        self.show_name = ""
        self.confirm_form.grid_remove()
        self.buildSearchForm()
