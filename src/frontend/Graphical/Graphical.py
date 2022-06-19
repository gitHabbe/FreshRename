from tkinter import Tk


class Graphical:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x400")
        self.root.title("FreshRename")
        self.__center_frame()
        self.__addExitEvent()

    def __center_frame(self):
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        print("Width:", window_width, "Height:", window_height)
        position_right = int(self.root.winfo_screenwidth() / 2 - window_width / 2) - 200
        position_down = int(self.root.winfo_screenheight() / 2 - window_height / 2) - 200
        self.root.geometry(f"+{position_right}+{position_down}")

    def __addExitEvent(self):
        self.root.bind("<Escape>", lambda x: self.root.destroy())

    def loop(self):
        self.root.mainloop()
