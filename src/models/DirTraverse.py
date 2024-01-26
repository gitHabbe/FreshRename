import os
from sys import platform

from models.OSPath.OSPath import WindowsPath, UnixPath


class DirTraverse:

    def __init__(self, operative_system) -> None:
        self.__os = operative_system
        self.__path = ""

    def get_local_files(self, new_path):
        self.__path: str = os.path.realpath(new_path)
        formatted_path: str = self.__format_path(self.__path)
        return self.__os.scandir(formatted_path)

    @staticmethod
    def __format_path(path: str) -> str:
        if platform == "win32":
            return WindowsPath(path).add_path_ending()
        elif platform == "linux":
            return UnixPath(path).add_path_ending()
