import questionary


class UserInput:

    __questionary = questionary

    def ask_tv_show_name(self) -> str:
        return self.__questionary.text("TV-show search:").ask()

    def confirm_tv_show_name(self, show_name: str) -> bool:
        return self.__questionary.confirm(f"Is '{show_name}' correct TV-show?").ask()

    def ask_tv_show_path(self) -> str:
        return self.__questionary.text("Input TV-show path:").ask()

    def confirm_tv_show_path(self, same_path: str) -> bool:
        return self.__questionary.confirm(same_path).ask()

    def choose_name_strategy(self, pattern_options: list[str]) -> str:
        return self.__questionary.select(
            message="Select file name style",
            choices=pattern_options,
            pointer="→"
        ).ask()

    def confirm_tv_show_rename(self) -> bool:
        return self.__questionary.confirm("Rename files?").ask()