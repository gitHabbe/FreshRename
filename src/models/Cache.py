import re
from dataclasses import dataclass, field
from os import DirEntry

from src.models.LocalFileOriginal import LocalFileOriginal
from src.models.Regex import FileRegex


@dataclass
class Cache:
    store: dict = field(default_factory=dict)

    def add_store(self, entry: DirEntry) -> None:
        match = self.__get_match(entry)
        if match is None:
            return
        local_file = LocalFileOriginal(entry, match)
        uid = "".join(local_file.uid)
        self.store[uid] = local_file

    @staticmethod
    def __get_match(entry: DirEntry) -> re.Match:
        regex = FileRegex(entry)
        match = regex.find_match()
        return match

    def __repr__(self) -> str:
        pretty = ""
        for key, value in self.store.items():
            pretty += f"{key}: {value.entry.name}\n"
        return pretty
