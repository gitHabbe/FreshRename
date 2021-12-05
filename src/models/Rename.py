import os
from models.DirTraverse import DirTraverse
from models.LocalFile import LocalFile
from models.namePatterns.NamePattern import NameStrategy


class Rename:
    fileList = []

    def __init__(self, dirTraverse: DirTraverse, jsonData, nameStrategy: NameStrategy) -> None:
        self.dirTraverse = dirTraverse
        self.jsonData = jsonData
        self.nameStrategy = nameStrategy

    def __fileItem(self, localFile: LocalFile, episode) -> dict:
        self.__setStrategy(localFile)
        fileData = {}
        fileType = localFile.entry.name.split(".")[-1]
        fileData["oldName"] = localFile.match.string
        fileData["oldFile"] = localFile.entry.path
        fileData["newName"] = f"{self.nameStrategy.name()}{episode['name']}.{fileType}"
        fileData["newFile"] = f"{localFile.path()}/{fileData['newName']}"
        return fileData

    def __setStrategy(self, localFile: LocalFile):
        seasonNum, episodeNum, _ = localFile.uid
        self.nameStrategy.season = seasonNum
        self.nameStrategy.episode = episodeNum

    def __appendFileList(self, localFile: LocalFile, episode) -> None:
        fileItem = self.__fileItem(localFile, episode)
        if fileItem["oldName"] == fileItem["newName"]:
            return
        self.fileList.append(fileItem)

    def fillFileList(self):
        store = self.dirTraverse.cache.store
        for episode in self.jsonData:
            seasonNum, episodeNum = self.__uid(episode)
            localFile = store.get(seasonNum + episodeNum)
            if localFile is None:
                continue
            self.__appendFileList(localFile, episode)
            localFile = store.get(seasonNum + episodeNum + "srt")
            if localFile is None:
                continue
            self.__appendFileList(localFile, episode)

    def renameFiles(self):
        for singleFile in self.fileList:
            os.rename(singleFile["oldFile"], singleFile["newFile"])

    @staticmethod
    def __uid(episode) -> list:
        seasonNum = str(episode["season"]).zfill(2)
        episodeNum = str(episode["number"]).zfill(2)
        return [seasonNum, episodeNum]
