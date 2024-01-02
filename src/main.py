from frontend.CommandLine.CommandLine import CommandLine
from models.RequestShow import RequestShow
from models.UserInput import UserInput


class FreshRename:

    @staticmethod
    def run_command_line():
        command_line = CommandLine(UserInput(), RequestShow())
        command_line.run()


if __name__ == '__main__':
    FreshRename().run_command_line()
    # FreshRename().run_graphical()


