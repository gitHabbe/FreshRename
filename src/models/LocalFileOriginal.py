import os
from dataclasses import dataclass
from pathlib import PosixPath, WindowsPath
from re import Match
from sys import platform

from models.LocalFileEntry import LocalFileEntry


@dataclass
class LocalFileOriginal:
    dir_entry: LocalFileEntry
    regex_match: Match

    @property
    def uid(self) -> list:
        season = self.regex_match.group(1).zfill(2)
        episode = self.regex_match.group(2).zfill(2)
        file_type = self.dir_entry.name.split(".")[-1]
        file_type = file_type if file_type == "srt" else ""
        return [season, episode, file_type]

    @property
    def path(self) -> WindowsPath | PosixPath:
        path_picker = PathPicker(self.dir_entry.path)
        return path_picker.full_path

    @staticmethod
    def separator():
        return os.sep


class PathPicker:
    path_dict = {
        "win32": WindowsPath,
        "linux": PosixPath,
    }

    def __init__(self, path: str):
        self.file_path = self.path_dict.get(platform)(path)

    @property
    def full_path(self) -> WindowsPath | PosixPath:
        return self.file_path.absolute()

    @property
    def file_name(self) -> str:
        return self.file_path.name
