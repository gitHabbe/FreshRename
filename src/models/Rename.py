import re

from models.LocalFileOriginal import LocalFileOriginal
from models.namePatterns.NamePattern import NameStrategy, UpperLetters


class Rename:

    def __init__(self, operating_system):
        self.__os = operating_system
        self.__name_strategy: NameStrategy = UpperLetters()
        self.file_list: list = []

    def fill_file_list(self, store, request_show_episode_data, name_strategy):
        self.__name_strategy = name_strategy
        for episode in request_show_episode_data:
            season_num, episode_num = self.__uid(episode)
            local_file = store.get(season_num + episode_num)
            if local_file is None:
                continue
            self.__append_file_list(local_file, episode)
            local_file = store.get(season_num + episode_num + "srt")
            if local_file is None:
                continue
            self.__append_file_list(local_file, episode)

    @staticmethod
    def __uid(episode) -> list:
        season_num = str(episode["season"]).zfill(2)
        episode_num = str(episode["number"]).zfill(2)
        return [season_num, episode_num]

    def __append_file_list(self, local_file: LocalFileOriginal, episode) -> None:
        file_item = self.__file_item(local_file, episode)
        if file_item["oldName"] == file_item["newName"]:
            return
        self.file_list.append(file_item)

    def __file_item(self, local_file: LocalFileOriginal, episode) -> dict:
        self.__set_strategy(local_file)
        file_data = {}
        file_type = local_file.dir_entry.name.split(".")[-1]
        file_data["oldName"] = local_file.regex_match.string
        file_data["oldFile"] = local_file.dir_entry.path
        illegal_file_characters = "[\\\/:\"*?<>|]"
        filtered_episode_name = re.sub(illegal_file_characters, "-", episode["name"])
        file_data["newName"] = f"{self.__name_strategy.name()}{filtered_episode_name}.{file_type}"
        file_data["newName"] = file_data["newName"].replace(":", "-")
        old_path = local_file.path.parents[0]
        file_data["newFile"] = f"{old_path}{local_file.separator()}{file_data['newName']}"
        return file_data

    def __set_strategy(self, local_file: LocalFileOriginal):
        season_num, episode_num, _ = local_file.uid
        self.__name_strategy.season = season_num
        self.__name_strategy.episode = episode_num

    def rename_files(self):
        for singleFile in self.file_list:
            old_file = singleFile["oldFile"]
            new_file = singleFile["newFile"]
            self.__os.rename(old_file, new_file)
