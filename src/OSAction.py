from models.DirTraverse import DirTraverse
from models.Rename import Rename


class OSAction:

    def __init__(self, operative_system):
        self.__os = operative_system
        self.dir_traverse = DirTraverse(self.__os)
        self.rename = Rename(self.__os)
