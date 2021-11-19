from os import DirEntry
import re


class LocalFile:
    def __init__(self, entry: DirEntry, match: re.match) -> None:
        self.entry = entry
        self.match = match
        self.uid = self.__uid()

    def path(self) -> str:
        path = self.entry.path.split("\\")[:-1]
        return "/".join(path)

    def __uid(self) -> list:
        season = self.match.group(1).zfill(2)
        episode = self.match.group(2).zfill(2)
        uid = [season, episode, ""]
        fileType = self.entry.name.split(".")[-1]
        if fileType == "srt":
            uid[-1] = "srt"
        return uid
