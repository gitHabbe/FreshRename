from os import DirEntry
import re


class FileRegex:
    patterns = [r"[Ss](\d?\d)[Ee](\d?\d)", r"(\d?\d)[Xx](\d?\d)"]

    def __init__(self, entry: DirEntry) -> None:
        self.__entry = entry

    def findMatch(self) -> re.Match or None:
        for pattern in self.patterns:
            match = re.search(pattern, self.__entry.name)
            if match is None:
                continue
            if len(match.groups()) >= 2:
                return match
