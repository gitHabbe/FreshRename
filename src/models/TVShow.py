import json

from models.RequestShow import RequestShow


class TVShow:
    with open("../cache.json", "r") as f:
        __jsonData = json.load(f)

    requester = RequestShow()
    search = ""

    def askDirectoryPath(self) -> str:
        cachedPath = self.__jsonData["last_path"]
        print(f"Last path: {cachedPath}")
        path = input("Folder path: ")
        if path == "":
            return cachedPath
        self.__jsonData["last_path"] = path
        with open("cache.json", "w") as f:
            json.dump(self.__jsonData, f)
        return path

    def askShowName(self):
        self.search = input("TV-show search: ")
        showResponse = self.requester.name(self.search)
        userConfirm = input(f"Is '{showResponse['show']['name']}' correct TV-show? [y/n]: ")
        if userConfirm.lower() == "y" or userConfirm.lower() == "":
            return self.requester.episodes(showResponse)

    @staticmethod
    def confirmRename(fileList):
        if len(fileList) == 0:
            print("\033[91m" + "No changes found" + "\033[0;0m")
            return False
        for fileItem in fileList:
            print(f"Old: {fileItem['oldName']}")
            print(f"New: {fileItem['newName']}")
        isYes = input("Rename files? (y/n): ")
        if isYes == "y":
            return True
        return False


