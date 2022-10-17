from os import DirEntry
from re import Match
from dataclasses import dataclass


@dataclass
class LocalFile:
    entry: DirEntry
    match: Match

    @property
    def uid(self) -> list:
        season = self.match.group(1).zfill(2)
        episode = self.match.group(2).zfill(2)
        file_type = self.entry.name.split(".")[-1]
        file_type = file_type if file_type == "srt" else ""
        return [ season, episode, file_type ]

    def path(self) -> str:
        path = self.entry.path
        path = path.split("\\")[:-1]
        return "/".join(path)
