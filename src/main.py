from frontend.CommandLine.CommandLine import CommandLine
from models.DirTraverse import DirTraverse
from src.models.Rename import Rename


class FreshRename:
    cli = CommandLine()

    def runCommandLine(self):
        showName = self.cli.chooseShowName()
        showResponse = self.cli.confirmShow(showName)
        isOldPath = self.cli.confirmPath()
        if not isOldPath:
            self.cli.newPath()
        episodes = self.cli.requestShowData(showResponse)
        episodesPath = self.cli.episodesPath()
        nameStrategy = self.cli.choosePattern()
        dirTraverse = DirTraverse(episodesPath)
        dirTraverse.buildCache()
        rename = Rename(dirTraverse, episodes, nameStrategy)
        rename.fillFileList()
        self.cli.listChanges(rename.fileList)
        isConfirmed = self.cli.confirmRename(rename.fileList)
        if isConfirmed:
            rename.renameFiles()
        else:
            print("No changes made")
            exit()


if __name__ == '__main__':
    # print(platform)
    FreshRename().runCommandLine()
