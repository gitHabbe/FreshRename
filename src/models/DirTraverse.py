import nt
import os
from models.Cache import Cache


class DirTraverse:
    cache = Cache()

    def __init__(self, root: str) -> None:
        self.__path = os.path.realpath(root)

    @staticmethod
    def __formatPath(path: str) -> str:
        return path if path[-1] == "\\" else path + "\\"

    def __entriesFromDir(self):
        formattedPath = self.__formatPath(self.__path)
        return os.scandir(formattedPath)

    # noinspection PyTypeChecker
    def buildCache(self) -> None:
        entries = self.__entriesFromDir()
        for entry in entries:
            self.__isFolder(entry)
            self.cache.addStore(entry)
        entries.close()

    def __isFolder(self, entry: nt.DirEntry):
        if entry.is_dir():
            self.__path = entry.path
            self.buildCache()
