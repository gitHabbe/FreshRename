import os
from models.DirTraverse import DirTraverse
from models.LocalFile import LocalFile
from models.namePatterns.NamePattern import LowerLetters, UpperLetters, UpperX, LowerX, NameStrategy


class Rename:
    fileList = []

    def __init__(self, dirTraverse: DirTraverse, data) -> None:
        self.dirTraverse = dirTraverse
        self.data = data
        # self.askConfirmation()

    @staticmethod
    def __fileItem(localFile: LocalFile, episode) -> dict:
        seasonNum, episodeNum, _ = localFile.uid
        fileType = localFile.entry.name.split(".")[-1]
        namePattern = LowerLetters(seasonNum, episodeNum)
        oldName = localFile.match.string
        oldFile = f"{localFile.path()}/{oldName}"
        newName = f"{namePattern.name()}{episode['name']}.{fileType}"
        newFile = f"{localFile.path()}/{newName}"
        return {
            "old": oldFile,
            "oldName": oldName,
            "new": newFile,
            "newName": newName
        }

    def __appendFileList(self, localFile: LocalFile, episode) -> None:
        fileItem = self.__fileItem(localFile, episode)
        if fileItem["old"] == fileItem["new"]:
            return
        self.fileList.append(fileItem)

    def fillFileList(self):
        store = self.dirTraverse.cache.store
        for episode in self.data:
            seasonNum, episodeNum = self.__uid(episode)
            localFile = store.get(seasonNum + episodeNum)
            if localFile is None:
                continue
            self.__appendFileList(localFile, episode)
            localFile = store.get(seasonNum + episodeNum + "srt")
            if localFile is None:
                continue
            self.__appendFileList(localFile, episode)

    def renameFiles(self, confirm: bool):
        if not confirm:
            print("\033[91m" + "File names not changed!" + "\033[0;0m")
        for singleFile in self.fileList:
            # print(singleFile)
            os.rename(singleFile["old"], singleFile["new"])

    @staticmethod
    def __uid(episode) -> list:
        seasonNum = str(episode["season"]).zfill(2)
        episodeNum = str(episode["number"]).zfill(2)
        return [seasonNum, episodeNum]
