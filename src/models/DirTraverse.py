import os
from os import DirEntry
from sys import platform

from models.Cache import Cache
from models.LocalFileEntry import LocalFileEntry
from models.OSPath.OSPath import WindowsPath, UnixPath


class DirTraverse:

    def __init__(self) -> None:
        self.__path = ""
        self.cache = Cache()

    # noinspection PyTypeChecker
    def build_cache(self, new_path) -> None:
        self.__path = os.path.realpath(new_path)
        entries = self.__entries_from_dir()
        for entry in entries:
            self.__is_folder(entry)
            local_file_entry = LocalFileEntry(entry)
            self.cache.add_store(local_file_entry)
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

    def __is_folder(self, entry: DirEntry):
        if entry.is_dir():
            self.__path = entry.path
            self.build_cache(self.__path)
