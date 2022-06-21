from frontend.CommandLine.CommandLine import CommandLine
from frontend.Graphical.Graphical import Graphical
from models.DirTraverse import DirTraverse
from models.Rename import Rename
from src.frontend.Graphical.Body import Body
from src.frontend.Graphical.FormWrapper import FormWrapper


class FreshRename:
    cli = CommandLine()

    def run_command_line(self):
        show_name = self.cli.chooseShowName()
        show_response = self.cli.confirmShow(show_name)
        is_old_path = self.cli.confirmPath()
        if not is_old_path:
            self.cli.newPath()
        episodes = self.cli.requestShowData(show_response)
        episodes_path = self.cli.episodesPath()
        name_strategy = self.cli.choosePattern()
        dir_traverse = DirTraverse(episodes_path)
        dir_traverse.build_cache()
        rename = Rename(dir_traverse, episodes, name_strategy)
        rename.fill_file_list()
        self.cli.listChanges(rename.fileList)
        is_confirmed = self.cli.confirmRename(rename.fileList)
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
    # FreshRename().run_command_line()
    FreshRename().run_graphical()
