import os
import subprocess
from sys import platform
from models.Cache import Cache


class DirTraverse:
    cache = Cache()

    def __init__(self, root: str) -> None:
        self.__path = os.path.realpath(root)

    @staticmethod
    def __format_path(path: str) -> str:
        if platform == "win32":
            return WindowsPath(path).formatted_path()
        elif platform == "linux":
            return UnixPath(path).formatted_path()

    def __entries_from_dir(self):
        formatted_path = self.__format_path(self.__path)
        return os.scandir(formatted_path)

    # noinspection PyTypeChecker
    def build_cache(self) -> None:
        entries = self.__entries_from_dir()
        for entry in entries:
            self.__is_folder(entry)
            self.cache.add_store(entry)
        entries.close()

    def __is_folder(self, entry: os.DirEntry):
        if entry.is_dir():
            self.__path = entry.path
            self.build_cache()


class OSPath:
    def __init__(self, path: str):
        self.path = path


class WindowsPath(OSPath):

    def formatted_path(self):
        return self.path if self.path[-1] == "\\" else self.path + "\\"


class UnixPath(OSPath):

    def formatted_path(self):
        if "\\" in self.path:
            command = subprocess.check_output(["wslpath", "-a", f"{self.path}"])
            self.path = command.decode("utf-8").strip()
            print(f"Root folder: {self.path}")
        return self.path if self.path[-1] == "/" else self.path + "/"
