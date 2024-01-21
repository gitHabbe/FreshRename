import os

from OSAction import OSAction
from frontend.CommandLine.CommandLine import CommandLine
from models.DirTraverse import DirTraverse
from models.Rename import Rename
from models.RequestShow import RequestShow
from models.UserInput import UserInput


def main():
    dir_traverse = DirTraverse()
    rename = Rename()
    os_action = OSAction(os, dir_traverse, rename)

    request_show = RequestShow()
    user_input = UserInput()

    command_line = CommandLine(user_input, request_show, os_action)
    command_line.run()


if __name__ == '__main__':
    main()
