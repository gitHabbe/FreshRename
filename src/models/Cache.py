import os
import re
from models.LocalFile import LocalFile
from models.Regex import FileRegex


class Cache:
    store = {}

    def add_store(self, entry: os.DirEntry) -> None:
        match = self.__get_match(entry)
        if match is None:
            return
        local_file = LocalFile(entry, match)
        uid = "".join(local_file.uid)
        self.store[uid] = local_file

    @staticmethod
    def __get_match(entry: os.DirEntry) -> re.Match:
        regex = FileRegex(entry)
        match = regex.findMatch()
        return match

    def __repr__(self):
        pretty = ""
        for key, value in self.store.items():
            pretty += f"{key}: {value.entry.name}\n"

        return pretty
