from tkinter import StringVar, Frame, Entry, Label, Button


class FormWrapper:
    showSearchForm = True
    showConfirmForm = False

    def __init__(self, parent: Frame):
        self.tvShow = ""
        self.frame = Frame(parent)
        self.searchForm = Frame(self.frame)
        self.buildSearchForm()
        self.confirmForm = Frame(self.frame)
        self.frame.grid()

    def buildSearchForm(self):
        inputType = StringVar()
        showEntry = Entry(self.searchForm, textvariable=inputType, width=40)
        showEntry.grid(pady=10, padx=5, row=0, column=1)
        showEntry.bind("<Return>", lambda event, widget=showEntry: self.toggle())

        showLabel = Label(self.searchForm, text="TV Show:")
        showLabel.grid(row=0, column=0, padx=5)

        searchButton = Button(self.searchForm, text="Search")
        searchButton.grid(row=0, column=2)
        searchButton.bind("<Button-1>", lambda x: self.toggleSearchForm(showEntry.get()))

        self.searchForm.grid()

    def buildConfirmForm(self):
        showLabel = Label(self.confirmForm, text=self.tvShow)
        showLabel.grid(row=0, column=0, padx=5)

        yesButton = Button(self.confirmForm, text="YES", bg="green", fg="white")
        yesButton.grid(row=0, column=1)
        yesButton.bind("<Button-1>", lambda x: self.toggle())

        noButton = Button(self.confirmForm, text="NO", bg="red", fg="white")
        noButton.grid(row=0, column=2)
        noButton.bind("<Button-1>", lambda x: self.toggleConfirmForm())

        self.confirmForm.grid()

    def toggleSearchForm(self, tvshow):
        self.tvShow = tvshow
        print(tvshow)
        self.searchForm.grid_remove()
        self.buildConfirmForm()

    def toggleConfirmForm(self):
        self.tvShow = ""
        self.confirmForm.grid_remove()
        self.buildSearchForm()
