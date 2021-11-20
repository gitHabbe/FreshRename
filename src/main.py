# import subprocess
from sys import platform

from models.DirTraverse import DirTraverse
from models.namePatterns.NamePattern import UpperLetters
from src.models.TVShow import TVShow
from src.models.Rename import Rename


class FreshRename:
    # path: str = TVShow.askPath()
    # path = "C:\\Entourage.S05.Season.5.1080p.5.1Ch.BluRay.ReEnc-DeeJayAhmed"
    tvShow = TVShow()
    path = tvShow.askDirectoryPath()
    data = tvShow.askShowName()
    dirTraverse = DirTraverse(path)
    dirTraverse.buildCache()

    def run(self):
        # print(f"Path: {self.path}")
        # print(self.dirTraverse.cache)
        # try:
        #     command = subprocess.check_output(["wslpath", "-a", f"{self.path}"])
        #     path = command.decode("utf-8").strip()
        #     print(f"Root folder: {path}")
        # except FileNotFoundError:
        #     path = self.path
        #
        rename = Rename(self.dirTraverse, self.data)
        rename.fillFileList()
        confirmation = self.tvShow.confirmRename(rename.fileList)
        rename.renameFiles(confirmation)


if __name__ == '__main__':
    print(platform)
    FreshRename().run()
