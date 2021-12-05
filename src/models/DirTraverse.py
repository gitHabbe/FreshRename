import os
import subprocess
from sys import platform
from models.Cache import Cache


class DirTraverse:
    cache = Cache()

    def __init__(self, root: str) -> None:
        self.__path = os.path.realpath(root)

    @staticmethod
    def __formatPath(path: str) -> str:
        if platform == "win32":
            return WindowsPath(path).formattedPath()
        elif platform == "linux":
            return UnixPath(path).formattedPath()

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

    def __isFolder(self, entry: os.DirEntry):
        if entry.is_dir():
            self.__path = entry.path
            self.buildCache()


class OSPath:
    def __init__(self, path: str):
        self.path = path


class WindowsPath(OSPath):

    def formattedPath(self):
        return self.path if self.path[-1] == "\\" else self.path + "\\"


class UnixPath(OSPath):

    def formattedPath(self):
        if "\\" in self.path:
            command = subprocess.check_output(["wslpath", "-a", f"{self.path}"])
            self.path = command.decode("utf-8").strip()
            print(f"Root folder: {self.path}")
        return self.path if self.path[-1] == "/" else self.path + "/"
