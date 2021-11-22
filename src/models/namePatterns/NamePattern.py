from abc import abstractmethod, ABC


class NameBase:
    # season: str
    # episode: str
    def __init__(self, season="", episode=""):
        self.season = season
        self.episode = episode


class NameStrategy(ABC, NameBase):

    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError


class LowerLetters(NameStrategy):
    # Example: s01e01
    def name(self):
        return f"s{self.season}e{self.episode} - "


class UpperLetters(NameStrategy):
    # Example: S01E01
    def name(self):
        return f"S{self.season}E{self.episode} - "


class LowerX(NameStrategy):
    # Example: 01x01
    def name(self):
        return f"{self.season}x{self.episode} - "


class UpperX(NameStrategy):
    # Example: 01X01
    def name(self):
        return f"{self.season}X{self.episode} - "
