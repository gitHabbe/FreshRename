class NameBase:
    def __init__(self, season, episode):
        self.season = season
        self.episode = episode


class IFileName:
    def name(self) -> str:
        raise NotImplementedError


class LowerLetters(NameBase, IFileName):
    # Example: s01e01
    def name(self):
        return f"s{self.season}e{self.episode} - "


class UpperLetters(NameBase, IFileName):
    # Example: S01E01
    def name(self):
        return f"S{self.season}E{self.episode} - "


class LowerX(NameBase, IFileName):
    # Example: 01x01
    def name(self):
        return f"{self.season}x{self.episode} - "


class UpperX(NameBase, IFileName):
    # Example: 01X01
    def name(self):
        return f"{self.season}X{self.episode} - "
