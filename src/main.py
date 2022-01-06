from frontend.CommandLine.CommandLine import CommandLine
from frontend.Graphical.Graphical import Graphical
from models.DirTraverse import DirTraverse
from models.Rename import Rename
from src.frontend.Graphical.Body import Body
from src.frontend.Graphical.SearchForm import FormWrapper


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

    @staticmethod
    def runGraphical():
        graphical = Graphical()
        body = Body(graphical.root)
        formWrapper = FormWrapper(body.frame)
        graphical.loop()


if __name__ == '__main__':
    # print(platform)
    FreshRename().runCommandLine()
    # FreshRename().runGraphical()
