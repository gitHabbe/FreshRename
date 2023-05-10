import re
from os import DirEntry
from pathlib import PosixPath, WindowsPath

from dataclasses import dataclass
from sys import platform


class PathPicker:
    path_dict = {
        "win32": WindowsPath,
        "linux": PosixPath,
    }

    def __init__(self, path: str):
        self.pather = self.path_dict.get(platform)(path)

    def full_path(self) -> WindowsPath | PosixPath:
        return self.pather.absolute()

    def file_name(self) -> str:
        return self.pather.name


@dataclass
class LocalFileOriginal:
    entry: DirEntry
    regexMatch: re.Match

    @property
    def uid(self) -> list:
        season = self.regexMatch.group(1).zfill(2)
        episode = self.regexMatch.group(2).zfill(2)
        file_type = self.entry.name.split(".")[-1]
        file_type = file_type if file_type == "srt" else ""
        return [season, episode, file_type]

    @property
    def path(self) -> WindowsPath | PosixPath:
        path_picker = PathPicker(self.entry.path)
        return path_picker.full_path()
