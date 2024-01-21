import json
from typing import Type

from OSAction import OSAction
from models.Rename import Rename
from models.RequestShow import RequestShow
from models.TvShowRootPath import TvShowRootPath
from models.UserInput import UserInput
from models.namePatterns.NamePattern import NameStrategy
from models.namePatterns.PatternSelector import patterns


class CommandLine:

    def __init__(self, questionary_library: UserInput, request_show: RequestShow, os_action: OSAction):
        self.__request_show = request_show
        self.__questionary = questionary_library
        self.__os_action = os_action
        self.test_data = []
        self.__tv_show_root_path = TvShowRootPath()

    def run(self):
        show_name: str = self.__questionary.ask_tv_show_name()
        show_response: list = self.__confirm_show(show_name)
        is_old_path: bool = self.__confirm_path()
        if not is_old_path:
            self.__new_path()
        episodes_data: json = self.__request_show.episodes(show_response)
        episodes_path: str = self.__episodes_path()
        name_strategy: NameStrategy = self.__choose_pattern()
        self.__os_action.build_cache(episodes_path)
        self.__os_action.fill_file_list(episodes_data, name_strategy)
        file_list = self.__os_action.rename.file_list
        self.__list_changes(file_list)
        is_confirmed: bool = self.__confirm_rename(file_list)
        if is_confirmed:
            self.__os_action.rename.rename_files()
        else:
            self.test_data: list = self.__os_action.rename.file_list
            print("No changes made")
            return

    def __confirm_show(self, show_name) -> list:
        show_response = self.__request_show.name(show_name)[0]
        show_name: str = show_response['show']['name']
        user_confirm: bool = self.__questionary.confirm_tv_show_name(show_name)
        if not user_confirm:
            new_show = self.__questionary.ask_tv_show_name()
            self.__confirm_show(new_show)
        return show_response

    def __confirm_path(self) -> bool:
        cached_path: str = self.__tv_show_root_path.get_path()
        print(f"Last path: {cached_path}")
        same_path = "Use same path?"
        return self.__questionary.confirm_tv_show_path(same_path)

    def __new_path(self) -> str:
        new_path: str = self.__questionary.ask_tv_show_path()
        self.__tv_show_root_path.save_path(new_path)
        return new_path

    def __episodes_path(self) -> str:
        return self.__tv_show_root_path.get_path()["last_path"]

    def __choose_pattern(self) -> NameStrategy:
        pattern_options = list(patterns.keys())
        chosen_pattern: str = self.__questionary.choose_name_strategy(pattern_options)
        name_pattern_class: Type[NameStrategy] = patterns.get(chosen_pattern)
        return name_pattern_class()

    @staticmethod
    def __list_changes(file_list: list) -> None:
        for fileItem in file_list:
            old = f"Old: {fileItem['oldName']}"
            print(old)
            new = f"New: {fileItem['newName']}"
            print(new)

    def __confirm_rename(self, file_list: list) -> bool:
        if len(file_list) == 0:
            print("\033[91m" + "No changes found" + "\033[0;0m")
            return False
        return self.__questionary.confirm_tv_show_rename()
