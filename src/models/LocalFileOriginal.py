import os
from os import DirEntry
from re import Match
from dataclasses import dataclass
from sys import platform

from models.OSPath import WindowsPath, UnixPath


@dataclass
class LocalFileOriginal:
    entry: DirEntry

    @property
    def uid(self) -> list:
        season = self.match.group(1).zfill(2)
        episode = self.match.group(2).zfill(2)
        file_type = self.entry.name.split(".")[-1]
        file_type = file_type if file_type == "srt" else ""
        return [season, episode, file_type]

    def path(self) -> str:
        path = os.sep.join(self.entry.path.split(os.sep)[:-1])
        if platform == "win32":
            path_formatter = WindowsPath(path)
        elif platform == "linux":
            path_formatter = UnixPath(path)
        path_formatter.change_separators()
        return path_formatter.add_path_ending()
