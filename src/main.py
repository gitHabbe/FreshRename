from frontend.CommandLine.CommandLine import CommandLine
from models.RequestShow import RequestShow
from models.UserInput import UserInput


def main():
    command_line = CommandLine(UserInput(), RequestShow())
    command_line.run()


if __name__ == '__main__':
    main()
