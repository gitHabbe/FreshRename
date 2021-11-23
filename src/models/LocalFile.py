from os import DirEntry
import re
from sys import platform
# from models.DirTraverse import WindowsPath, UnixPath


class LocalFile:
    def __init__(self, entry: DirEntry, match: re.match) -> None:
        self.entry = entry
        self.match = match
        self.uid = self.__uid()

    def path(self) -> str:
        path = self.entry.path
        # if platform == "win32":
        #     return WindowsPath(path).formattedPath().split("\\")[:-1]
        # elif platform == "linux":
        #     return UnixPath(path).formattedPath().split("/")[:-1]
        path = path.split("\\")[:-1]
        return "/".join(path)

    def __uid(self) -> list:
        season = self.match.group(1).zfill(2)
        episode = self.match.group(2).zfill(2)
        fileType = self.entry.name.split(".")[-1]
        fileType = fileType if fileType == "srt" else ""
        return [season, episode, fileType]
