from frontend.CommandLine.CommandLine import CommandLine


class FreshRename:

    @staticmethod
    def run_command_line():
        command_line = CommandLine()
        command_line.run()


if __name__ == '__main__':
    FreshRename().run_command_line()
    # FreshRename().run_graphical()
