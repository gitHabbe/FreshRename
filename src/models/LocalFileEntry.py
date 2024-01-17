from os import DirEntry


class LocalFileEntry:
    def __init__(self, entry: DirEntry):
        self.__entry = entry
        self.name = entry.name
        self.path = entry.path
