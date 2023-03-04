from abc import abstractmethod, ABC
from dataclasses import dataclass


@dataclass
class NameBase:
    season: str = ""
    episode: str = ""


class NameStrategy(ABC, NameBase):
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError


class LowerLetters(NameStrategy):
    def name(self):  # Example: s01e01
        return f"s{self.season}e{self.episode} - "


class UpperLetters(NameStrategy):
    def name(self):  # Example: S01E01
        return f"S{self.season}E{self.episode} - "


class LowerX(NameStrategy):
    def name(self):  # Example: 01x01
        return f"{self.season}x{self.episode} - "


class UpperX(NameStrategy):
    def name(self):  # Example: 01X01
        return f"{self.season}X{self.episode} - "
