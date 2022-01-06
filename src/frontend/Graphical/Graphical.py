from tkinter import Tk


class Graphical:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x400")
        self.root.title("FreshRename")
        self.__centerFrame()
        self.__addExitEvent()

    def __centerFrame(self):
        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        print("Width:", windowWidth, "Height:", windowHeight)
        positionRight = int(self.root.winfo_screenwidth() / 2 - windowWidth / 2) - 200
        positionDown = int(self.root.winfo_screenheight() / 2 - windowHeight / 2) - 200
        self.root.geometry(f"+{positionRight}+{positionDown}")

    def __addExitEvent(self):
        self.root.bind("<Escape>", lambda x: self.root.destroy())

    def loop(self):
        self.root.mainloop()
