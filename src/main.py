from frontend.CommandLine.CommandLine import CommandLine
from frontend.Graphical.Graphical import Graphical
from models.DirTraverse import DirTraverse
from models.Rename import Rename
from src.frontend.Graphical.Body import Body
from src.frontend.Graphical.FormWrapper import FormWrapper


class FreshRename:

    @staticmethod
    def run_command_line():
        command_line = CommandLine()
        show_name = command_line.choose_show_name()
        show_response = command_line.confirm_show(show_name)
        is_old_path = command_line.confirm_path()
        if not is_old_path:
            command_line.new_path()
        episodes = command_line.request_show_data(show_response)
        episodes_path = command_line.episodes_path()
        name_strategy = command_line.choose_pattern()
        dir_traverse = DirTraverse(episodes_path)
        dir_traverse.build_cache()
        rename = Rename(dir_traverse, episodes, name_strategy)
        rename.fill_file_list()
        command_line.list_changes(rename.fileList)
        is_confirmed = command_line.confirm_rename(rename.fileList)
        if is_confirmed:
            rename.rename_files()
        else:
            print("No changes made")
            exit()

    @staticmethod
    def run_graphical():
        graphical = Graphical()
        body = Body(graphical.root)
        form_wrapper = FormWrapper(body.frame)
        graphical.loop()


if __name__ == '__main__':
    FreshRename().run_command_line()
    # FreshRename().run_graphical()
