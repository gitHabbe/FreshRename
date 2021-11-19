from operator import itemgetter
from models.DirTraverse import DirTraverse
from models.LocalFile import LocalFile
from models.namePatterns.NamePattern import LowerLetters, UpperX, LowerX


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
        lowerLetters = LowerX(seasonNum, episodeNum)
        oldName = f"{localFile.match.string}"
        oldFile = f"{localFile.path()}/{oldName}"
        newName = lowerLetters.name() + f"{episode['name']}.{fileType}"
        newFile = f"{localFile.path()}/{newName}"
        return {
            "old": oldFile,
            "new": newFile
        }

    def __appendFileList(self, localFile: LocalFile, episode) -> None:
        fileItem = self.__fileItem(localFile, episode)
        old, new = itemgetter("old", "new")(fileItem)
        print(old)
        print(new)
        # seasonNum, episodeNum, fileType = localFile.uid
        # lowerLetters = LowerLetters(seasonNum, episodeNum)
        # oldName = f"{localFile.match.string}"
        # oldFile = f"{localFile.path()}/{oldName}"
        # newName = lowerLetters.name() + f"{episode['name']}.{fileType}"
        # newFile = f"{localFile.path()}/{newName}"
        # print(oldName, newName)
        # if item.oldName == item.newName:
        #     return
        # # if newFile == oldFile:
        # #     return
        # else:
        #     print(f"Old: {oldName}")
        #     print(f"New: {newName}")
        #     self.fileList.append({
        #         "old": oldFile,
        #         "new": newFile
        #     })

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

    def renameFiles(self):
        for singleFile in self.fileList:
            print(singleFile)

    @staticmethod
    def __uid(episode) -> list:
        seasonNum = str(episode["season"]).zfill(2)
        episodeNum = str(episode["number"]).zfill(2)
        return [seasonNum, episodeNum]
        # cached = seasonNum + episodeNum
        # return seasonNum, episodeNum, cached

    # def askConfirmation(self) -> None:
    #     if len(self.__cache.fileList) == 0:
    #         print("\033[91m" + "No changes found" + "\033[0;0m")
    #         return
    #     confirmation = input("Rename to according to this? [y/n]: ")
    #     if confirmation.lower() == "y":
    #         for singleFile in self.__cache.fileList:
    #             print(singleFile)
    #             os.rename(singleFile["old"], singleFile["new"])
    #         print("\033[1;32m" + "File names successfully changed!" + "\033[0;0m")
    #     else:
    #         print("\033[91m" + "File names not changed!" + "\033[0;0m")
