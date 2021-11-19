import os
import re
from src.models.LocalFile import LocalFile
from src.models.Regex import FileRegex


class Cache:
    store = {}
    fileList = []

    def addStore(self, entry: os.DirEntry) -> None:
        match = self.__getMatch(entry)
        if match is None:
            return
        localFile = LocalFile(entry, match)
        uid = "".join(localFile.uid)
        self.store[uid] = localFile

    @staticmethod
    def __getMatch(entry: os.DirEntry) -> re.Match:
        regex = FileRegex(entry)
        match = regex.findMatch()
        return match

    def __repr__(self):
        pretty = ""
        for key, value in self.store.items():
            pretty += f"{key}: {value.entry.name}\n"

        return pretty
