from dataclasses import dataclass
from os import DirEntry
from re import Pattern, Match, search
from typing import ClassVar

from models.LocalFileEntry import LocalFileEntry


@dataclass
class FileRegex:
    entry: LocalFileEntry
    __patterns: ClassVar[list[Pattern[str]]] = [r"[Ss](\d?\d)[Ee](\d?\d)", r"(\d?\d)[Xx](\d?\d)"]

    def find_match(self) -> Match or None:
        for pattern in self.__patterns:
            match = search(pattern, self.entry.name)
            if match is None:
                continue
            if len(match.groups()) >= 2:
                return match
