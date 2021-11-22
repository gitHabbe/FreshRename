import questionary

from models.DirTraverse import DirTraverse
from models.LocalPath import LocalPath
from models.Rename import Rename
from models.RequestShow import RequestShow
from models.namePatterns.NamePattern import NameStrategy
from models.namePatterns.PatternSelector import patterns


class CommandLine:
    cli = questionary
    localPath = LocalPath()

    def confirmPath(self):
        cachedPath = self.localPath.path()
        print(f"Last path: {cachedPath}")
        samePath = "Use same path?"
        return self.cli.confirm(samePath).ask()

    def newPath(self):
        newPath = self.cli.text("Input new path:").ask()
        self.localPath.savePath(newPath)
        return newPath

    def selectPattern(self) -> NameStrategy:
        patternOptions = list(patterns.keys())
        chosenPattern = self.cli.select(
            message="Select pattern",
            choices=patternOptions,
            pointer="→"
        ).ask()
        namePatternClass = patterns.get(chosenPattern)
        return namePatternClass()

    def askShowName(self):
        showName = self.cli.text("TV-show search:").ask()
        return showName

    def requestShowData(self):
        showName = self.askShowName()
        requestShow = RequestShow()
        tvShow = requestShow.name(showName)
        episodes = requestShow.episodes(tvShow)
        return episodes

    def getFileList(self):
        jsonEpisodes = self.requestShowData()
        if not self.confirmPath():
            self.newPath()
        namePattern: NameStrategy = self.selectPattern()
        path = self.localPath.path()
        dirTraverse = DirTraverse(path)
        dirTraverse.buildCache()
        rename = Rename(dirTraverse, jsonEpisodes, namePattern)
        rename.fillFileList()
        self.listChanges(rename.fileList)
        renameConfirm = self.confirmRename(rename.fileList)
        if not renameConfirm:
            return
        rename.renameFiles()

    def confirmRename(self, fileList: list):
        if len(fileList) == 0:
            print("\033[91m" + "No changes found" + "\033[0;0m")
            return False
        return self.cli.confirm("Rename files?").ask()

    @staticmethod
    def listChanges(fileList: list):
        for fileItem in fileList:
            print(f"Old: {fileItem['oldName']}")
            print(f"New: {fileItem['newName']}")
