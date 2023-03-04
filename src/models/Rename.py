import os
from dataclasses import dataclass

from models.DirTraverse import DirTraverse
from models.LocalFileOriginal import LocalFileOriginal
from models.namePatterns.NamePattern import NameStrategy


@dataclass
class Rename:
    __dir_traverse: DirTraverse
    __json_data: list
    __name_strategy: NameStrategy
    fileList = []

    def __file_item(self, local_file: LocalFileOriginal, episode) -> dict:
        self.__set_strategy(local_file)
        file_data = {}
        file_type = local_file.entry.name.split(".")[-1]
        file_data["oldName"] = local_file.match.string
        file_data["oldFile"] = local_file.entry.path
        file_data["newName"] = f"{self.__name_strategy.name()}{episode['name']}.{file_type}"
        file_data["newName"] = file_data["newName"].replace(":", "-")
        newFilePath = local_file.path()
        file_data["newFile"] = f"{newFilePath}{file_data['newName']}"
        return file_data

    def __set_strategy(self, local_file: LocalFileOriginal):
        season_num, episode_num, _ = local_file.uid
        self.__name_strategy.season = season_num
        self.__name_strategy.episode = episode_num

    def __append_file_list(self, local_file: LocalFileOriginal, episode) -> None:
        file_item = self.__file_item(local_file, episode)
        if file_item["oldName"] == file_item["newName"]:
            return
        self.fileList.append(file_item)

    def fill_file_list(self):
        store = self.__dir_traverse.cache.store
        for episode in self.__json_data:
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
            old_file = singleFile["oldFile"]
            new_file = singleFile["newFile"]
            os.rename(old_file, new_file)

    @staticmethod
    def __uid(episode) -> list:
        season_num = str(episode["season"]).zfill(2)
        episode_num = str(episode["number"]).zfill(2)
        return [season_num, episode_num]
