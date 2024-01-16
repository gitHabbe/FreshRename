import os

from frontend.CommandLine.CommandLine import CommandLine
from models.DirTraverse import DirTraverse
from models.RequestShow import RequestShow
from models.UserInput import UserInput


class OSAction:

    def __init__(self, operative_system, dir_traverse: DirTraverse):
        self.__os = operative_system
        self.__dir_traverse = dir_traverse


def main():
    dir_traverse = DirTraverse("")
    os_operations = OSAction(os, dir_traverse)

    request_show = RequestShow()
    user_input = UserInput()

    command_line = CommandLine(user_input, request_show, os_operations)
    command_line.run()


if __name__ == '__main__':
    main()
