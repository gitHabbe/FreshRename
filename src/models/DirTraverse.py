import os
from sys import platform
from typing import AnyStr

from models.Cache import Cache
from models.OSPath import WindowsPath, UnixPath


class DirTraverse:
    cache = Cache()

    def __init__(self, root: str) -> None:
        self.__path = os.path.realpath(root)

    # noinspection PyTypeChecker
    def build_cache(self) -> None:
        entries = self.__entries_from_dir()
        for entry in entries:
            self.__is_folder(entry)
            self.cache.add_store(entry)
        entries.close()

    def __entries_from_dir(self):
        formatted_path = self.__format_path(self.__path)
        return os.scandir(formatted_path)

    @staticmethod
    def __format_path(path: str) -> str:
        if platform == "win32":
            return WindowsPath(path).add_path_ending()
        elif platform == "linux":
            return UnixPath(path).add_path_ending()

    def __is_folder(self, entry: os.DirEntry):
        if entry.is_dir():
            self.__path = entry.path
            self.build_cache()
