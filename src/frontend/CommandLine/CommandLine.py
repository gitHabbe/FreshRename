import questionary

from models.LocalPath import LocalPath
from models.RequestShow import RequestShow
from models.namePatterns.NamePattern import NameStrategy
from models.namePatterns.PatternSelector import patterns


class CommandLine:
    __cli = questionary
    __localPath = LocalPath()
    __requestShow = RequestShow()

    def choose_show_name(self) -> str:
        return self.__cli.text("TV-show search:").ask()

    def confirm_show(self, show_name) -> list:
        show_response = self.__requestShow.name(show_name)
        show_name: str = show_response['show']['name']
        user_confirm: bool = self.__cli.confirm(f"Is '{show_name}' correct TV-show?").ask()
        if not user_confirm:
            new_show = self.choose_show_name()
            self.confirm_show(new_show)
        return show_response

    def confirm_path(self) -> bool:
        cached_path: str = self.__localPath.path()
        print(f"Last path: {cached_path}")
        same_path = "Use same path?"
        return self.__cli.confirm(same_path).ask()

    def new_path(self) -> str:
        new_path: str = self.__cli.text("Input new path:").ask()
        self.__localPath.save_path(new_path)
        return new_path

    def request_show_data(self, show_response) -> list:
        return self.__requestShow.episodes(show_response)

    def episodes_path(self):
        return self.__localPath.path()

    def choose_pattern(self) -> NameStrategy:
        pattern_options = list(patterns.keys())
        chosen_pattern: str = self.__cli.select(
            message="Select pattern",
            choices=pattern_options,
            pointer="→"
        ).ask()
        name_pattern_class = patterns.get(chosen_pattern)
        return name_pattern_class()

    def confirm_rename(self, file_list: list) -> bool:
        if len(file_list) == 0:
            print("\033[91m" + "No changes found" + "\033[0;0m")
            return False
        return self.__cli.confirm("Rename files?").ask()

    @staticmethod
    def list_changes(file_list: list):
        for fileItem in file_list:
            old = f"Old: {fileItem['oldName']}"
            new = f"New: {fileItem['newName']}"
            print(old)
            print(new)
