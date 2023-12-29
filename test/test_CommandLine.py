import json
import unittest

import questionary
from approvaltests.approvals import verify

from frontend.CommandLine.CommandLine import CommandLine
from models.RequestShow import RequestShow


class TestCommandLine(unittest.TestCase):

    def setUp(self):
        self.mock_request_show_adapter = RequestShowAdapter(RequestShow())
        self.mock_questionary_adapter = QuestionaryAdapter(questionary, "Invincible")
        self.command_line = CommandLine(self.mock_request_show_adapter, self.mock_questionary_adapter)

    def test_init(self):
        self.command_line.run()
        command_line_data = self.__format_dict_list(self.command_line.test_data)
        verify(command_line_data)

    @staticmethod
    def __format_dict_list(episode_list):
        episodes_as_string = ""
        for episode_data in episode_list:
            old_name = "oldName"
            new_name = "newName"
            relevant_data = {
                old_name: episode_data[old_name],
                new_name: episode_data[new_name]
            }
            formatted_episode = json.dumps(relevant_data, indent=4)
            episodes_as_string += formatted_episode + "\n"
        return episodes_as_string


if __name__ == "__main__":
    unittest.main()


class RequestShowAdapter:
    def __init__(self, request_show: RequestShow):
        self.request_show = request_show

    @staticmethod
    def name(tv_show_term: str):
        tv_show_list = [
            {
                "show": {
                    "id": 2013997,
                    "name": "Invincible",
                }
            }
        ]
        for tv_show in tv_show_list:
            if tv_show["show"]["name"] == tv_show_term:
                return [tv_show]
        return tv_show_list

    @staticmethod
    def episodes(tv_show):
        with open("../test/RequestShowData.json", "r") as mockFile:
            return json.load(mockFile)


class QuestionaryAdapter:

    def __init__(self, questionary_library, tv_show_name):
        self.questionary = questionary_library
        self.tv_show_name = tv_show_name
        self.answer = ""

    def ask(self):
        return self.answer

    def text(self, message):
        if message == "TV-show search:":
            self.answer = self.tv_show_name

        return self

    def confirm(self, message):
        if message == "Is 'Invincible' correct TV-show?":
            self.answer = True
        elif message == "Use same path?":
            self.answer = True
        elif message == "Rename files?":
            self.answer = False

        return self

    def select(self, message, choices, pointer):
        if message == "Select pattern":
            self.answer = choices[0]

        return self
