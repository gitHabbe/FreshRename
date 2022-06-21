import os
from models.DirTraverse import DirTraverse
from models.LocalFile import LocalFile
from models.namePatterns.NamePattern import NameStrategy


class Rename:
    fileList = []

    def __init__(self, dir_traverse: DirTraverse, json_data, name_strategy: NameStrategy) -> None:
        self.dirTraverse = dir_traverse
        self.jsonData = json_data
        self.nameStrategy = name_strategy

    def __file_item(self, local_file: LocalFile, episode) -> dict:
        self.__set_strategy(local_file)
        file_data = {}
        file_type = local_file.entry.name.split(".")[-1]
        file_data["oldName"] = local_file.match.string
        file_data["oldFile"] = local_file.entry.path
        file_data["newName"] = f"{self.nameStrategy.name()}{episode['name']}.{file_type}"
        file_data["newFile"] = f"{local_file.path()}/{file_data['newName']}"
        return file_data

    def __set_strategy(self, local_file: LocalFile):
        season_num, episode_num, _ = local_file.uid
        self.nameStrategy.season = season_num
        self.nameStrategy.episode = episode_num

    def __append_file_list(self, local_file: LocalFile, episode) -> None:
        file_item = self.__file_item(local_file, episode)
        if file_item["oldName"] == file_item["newName"]:
            return
        self.fileList.append(file_item)

    def fill_file_list(self):
        store = self.dirTraverse.cache.store
        for episode in self.jsonData:
            season_num, episode_num = self.__uid(episode)
            local_file = store.get(season_num + episode_num)
            if local_file is None:
                continue
            self.__append_file_list(local_file, episode)
            local_file = store.get(season_num + episode_num + "srt")
            if local_file is None:
                continue
            self.__append_file_list(local_file, episode)

    def rename_files(self):
        for singleFile in self.fileList:
            os.rename(singleFile["oldFile"], singleFile["newFile"])

    @staticmethod
    def __uid(episode) -> list:
        season_num = str(episode["season"]).zfill(2)
        episode_num = str(episode["number"]).zfill(2)
        return [season_num, episode_num]
