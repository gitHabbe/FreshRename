from os import DirEntry
import re


class LocalFile:
    def __init__(self, entry: DirEntry, match: re.match) -> None:
        self.entry = entry
        self.match = match
        self.uid = self.__uid()

    def path(self) -> str:
        path = self.entry.path
        path = path.split("\\")[:-1]
        return "/".join(path)

    def __uid(self) -> list:
        season = self.match.group(1).zfill(2)
        episode = self.match.group(2).zfill(2)
        file_type = self.entry.name.split(".")[-1]
        file_type = file_type if file_type == "srt" else ""
        return [season, episode, file_type]
