from tkinter import ttk, Tk, StringVar, Widget


class Graphical:
    root = Tk()
    root.geometry("500x400")
    root.title("FreshRename")

    def centerFrame(self):
        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)
        positionRight = int(self.root.winfo_screenwidth() / 2 - windowWidth / 2) - 200
        positionDown = int(self.root.winfo_screenheight() / 2 - windowHeight / 2) - 200
        self.root.geometry(f"+{positionRight}+{positionDown}")


class PrimaryFrame:
    graphical = Graphical
    __primaryFrame = ttk.Frame(graphical.root)
    __primaryFrame.grid()

    def hideWidget(self, widget: Widget):
        widget.grid_remove(self)

    def textField(self):
        text = StringVar()
        ttk.Entry(self.__primaryFrame, textvariable=text, width=40).grid(pady=10, padx=5, row=0, column=1)

    def label(self):
        label = ttk.Label(self.__primaryFrame, text="TV Show:")
        label.grid(row=0, column=0, padx=5)

    def button(self):
        button = ttk.Button(self.__primaryFrame, text="Search")
        button.grid(row=0, column=2)

    def render(self):
        self.__primaryFrame.mainloop()


graphical = Graphical()
graphical.centerFrame()
primaryFrame = PrimaryFrame()
primaryFrame.textField()
primaryFrame.label()
primaryFrame.button()
primaryFrame.render()

