import os

from models.OSAction import OSAction
from frontend.CommandLine.CommandLine import CommandLine
from models.RequestShow import RequestShow
from models.UserInput import UserInput


def main():
    user_input = UserInput()
    request_show = RequestShow()
    os_action = OSAction(os)

    command_line = CommandLine(user_input, request_show, os_action)
    command_line.run()


if __name__ == '__main__':
    main()
