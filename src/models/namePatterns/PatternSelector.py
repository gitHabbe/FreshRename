from models.namePatterns.NamePattern import UpperLetters, LowerLetters, UpperX, LowerX

patterns = {
    "S01E01 - Episode name here": UpperLetters,
    "s01e01 - Episode name here": LowerLetters,
    "01X01 - Episode name here": UpperX,
    "01x01 - Episode name here": LowerX
}
