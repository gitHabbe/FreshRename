import questionary

from models.LocalPath import LocalPath
from models.RequestShow import RequestShow
from models.namePatterns.NamePattern import NameStrategy
from models.namePatterns.PatternSelector import patterns


class CommandLine:
    __cli = questionary
    __localPath = LocalPath()
    __requestShow = RequestShow()

    def confirmPath(self) -> bool:
        cachedPath: str = self.__localPath.path()
        print(f"Last path: {cachedPath}")
        samePath = "Use same path?"
        return self.__cli.confirm(samePath).ask()

    def newPath(self) -> str:
        newPath: str = self.__cli.text("Input new path:").ask()
        self.__localPath.savePath(newPath)
        return newPath

    def episodesPath(self):
        return self.__localPath.path()

    def choosePattern(self) -> NameStrategy:
        patternOptions = list(patterns.keys())
        chosenPattern: str = self.__cli.select(
            message="Select pattern",
            choices=patternOptions,
            pointer="→"
        ).ask()
        namePatternClass = patterns.get(chosenPattern)
        return namePatternClass()

    def chooseShowName(self) -> str:
        return self.__cli.text("TV-show search:").ask()

    def confirmShow(self, showName) -> list:
        showResponse = self.__requestShow.name(showName)
        showName: str = showResponse['show']['name']
        userConfirm: bool = self.__cli.confirm(f"Is '{showName}' correct TV-show?").ask()
        if not userConfirm:
            newShow = self.chooseShowName()
            self.confirmShow(newShow)
        return showResponse

    def requestShowData(self, showResponse) -> list:
        return self.__requestShow.episodes(showResponse)

    def confirmRename(self, fileList: list) -> bool:
        if len(fileList) == 0:
            print("\033[91m" + "No changes found" + "\033[0;0m")
            return False
        return self.__cli.confirm("Rename files?").ask()

    @staticmethod
    def listChanges(fileList: list):
        for fileItem in fileList:
            old = f"Old: {fileItem['oldName']}"
            new = f"New: {fileItem['newName']}"
            print(old)
            print(new)
