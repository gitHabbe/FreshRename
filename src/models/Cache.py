import re
from dataclasses import dataclass, field

from models import LocalFileEntry
from src.models.LocalFileOriginal import LocalFileOriginal
from src.models.Regex import FileRegex


@dataclass
class Cache:
    store: dict = field(default_factory=dict)

    def add_store(self, entry: LocalFileEntry) -> None:
        match = self.__get_match(entry)
        if match is None:
            return
        local_file = LocalFileOriginal(entry, match)
        uid = "".join(local_file.uid)
        self.store[uid] = local_file

    @staticmethod
    def __get_match(entry: LocalFileEntry) -> Match:
        regex = FileRegex(entry)
        return regex.find_match()

    def __repr__(self) -> str:
        pretty = ""
        for key, value in self.store.items():
            pretty += f"{key}: {value.dir_entry.name}\n"
        return pretty
