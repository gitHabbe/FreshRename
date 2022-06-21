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
        show_name = command_line.chooseShowName()
        show_response = command_line.confirmShow(show_name)
        is_old_path = command_line.confirmPath()
        if not is_old_path:
            command_line.newPath()
        episodes = command_line.requestShowData(show_response)
        episodes_path = command_line.episodesPath()
        name_strategy = command_line.choosePattern()
        dir_traverse = DirTraverse(episodes_path)
        dir_traverse.build_cache()
        rename = Rename(dir_traverse, episodes, name_strategy)
        rename.fill_file_list()
        command_line.listChanges(rename.fileList)
        is_confirmed = command_line.confirmRename(rename.fileList)
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
