from frontend.CommandLine.CommandLine import CommandLine
# from frontend.Graphical.Graphical import Graphical
# from src.frontend.Graphical.Body import Body
# from src.frontend.Graphical.FormWrapper import FormWrapper


class FreshRename:

    @staticmethod
    def run_command_line():
        command_line = CommandLine()
        command_line.run()

    # @staticmethod
    # def run_graphical():
        # graphical = Graphical()
        # body = Body(graphical.root)
        # form_wrapper = FormWrapper(body.frame)
        # graphical.loop()


if __name__ == '__main__':
    FreshRename().run_command_line()
    # FreshRename().run_graphical()
