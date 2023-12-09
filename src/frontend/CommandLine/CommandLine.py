import questionary

from models.DirTraverse import DirTraverse
from models.LocalPath import LocalPath
from models.Rename import Rename
from models.RequestShow import RequestShow
from models.namePatterns.NamePattern import NameStrategy
from models.namePatterns.PatternSelector import patterns


class CommandLine:
    __cli = questionary
    __localPath = LocalPath()
    __requestShow = RequestShow()

    def run(self):
        show_name = self.__choose_show_name()
        show_response = self.__confirm_show(show_name)
        is_old_path = self.__confirm_path()
        if not is_old_path:
            self.__new_path()
        episodes = self.__request_show_data(show_response)
        episodes_path = self.__episodes_path()
        name_strategy = self.__choose_pattern()
        dir_traverse = DirTraverse(episodes_path)
        dir_traverse.build_cache()
        rename = Rename(dir_traverse, episodes, name_strategy)
        rename.fill_file_list()
        self.__list_changes(rename.fileList)
        is_confirmed = self.__confirm_rename(rename.fileList)
        if is_confirmed:
            rename.rename_files()
        else:
            print("No changes made")
            exit()

    def __choose_show_name(self) -> str:
        return self.__cli.text("TV-show search:").ask()

    def __confirm_path(self) -> bool:
        cached_path: str = self.__localPath.get_path()
        print(f"Last path: {cached_path}")
        same_path = "Use same path?"
        return self.__cli.confirm(same_path).ask()

    def __confirm_show(self, show_name) -> list:
        show_response = self.__requestShow.name(show_name)[0]
        show_name: str = show_response['show']['name']
        user_confirm: bool = self.__cli.confirm(f"Is '{show_name}' correct TV-show?").ask()
        if not user_confirm:
            new_show = self.__choose_show_name()
            self.__confirm_show(new_show)
        return show_response

    def __new_path(self) -> str:
        new_path: str = self.__cli.text("Input new path:").ask()
        self.__localPath.save_path(new_path)
        return new_path

    def __request_show_data(self, show_response) -> list:
        return self.__requestShow.episodes(show_response)

    def __episodes_path(self):
        return self.__localPath.get_path()["last_path"]

    def __choose_pattern(self) -> NameStrategy:
        pattern_options = list(patterns.keys())
        chosen_pattern: str = self.__cli.select(
            message="Select pattern",
            choices=pattern_options,
            pointer="→"
        ).ask()
        name_pattern_class = patterns.get(chosen_pattern)
        return name_pattern_class()

    def __confirm_rename(self, file_list: list) -> bool:
        if len(file_list) == 0:
            print("\033[91m" + "No changes found" + "\033[0;0m")
            return False
        return self.__cli.confirm("Rename files?").ask()

    @staticmethod
    def __list_changes(file_list: list) -> None:
        for fileItem in file_list:
            old = f"Old: {fileItem['oldName']}"
            print(old)
            new = f"New: {fileItem['newName']}"
            print(new)
