import json
import unittest

import questionary
from approvaltests.approvals import verify

from frontend.CommandLine.CommandLine import CommandLine
from models.RequestShow import RequestShow


class TestCommandLine(unittest.TestCase):
    def setUp(self):
        self.mock_request_show_adapter = RequestShowAdapter(RequestShow())

    def test_tv_show_entourage(self):
        mock_questionary_adapter = QuestionaryAdapter(questionary, "Entourage", "C:\Entourage")
        command_line = CommandLine(self.mock_request_show_adapter, mock_questionary_adapter)
        command_line.run()
        episode_list_data_as_string = self.__format_dict_list(command_line.test_data)
        verify(episode_list_data_as_string)

    def test_tv_show_invincible(self):
        mock_questionary_adapter = QuestionaryAdapter(questionary, "Invincible", "C:\Invincible.2021.S01")
        command_line = CommandLine(self.mock_request_show_adapter, mock_questionary_adapter)
        command_line.run()
        episode_list_data_as_string = self.__format_dict_list(command_line.test_data)
        verify(episode_list_data_as_string)

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
    def name(tv_show_term: str) -> list:
        tv_show_list = [
            {
                "show": {
                    "id": 2013997,
                    "name": "Invincible",
                }
            },
            {
                "show": {
                    "id": 559,
                    "name": "Entourage",
                }
            }
        ]
        for tv_show in tv_show_list:
            if tv_show["show"]["name"] == tv_show_term:
                return [tv_show]
        return tv_show_list

    @staticmethod
    def episodes(tv_show) -> list:
        with open("../test/RequestShowData.json", "r") as tv_show_mock:
            tv_show_dict = json.load(tv_show_mock)
            for tv_show_name in tv_show_dict:
                if tv_show_name == tv_show["show"]["name"]:
                    return tv_show_dict[tv_show_name]
            return tv_show_dict["Invincible"]


class QuestionaryAdapter:

    def __init__(self, questionary_library, tv_show_name, tv_show_path="C:\Invincible.2021.S01"):
        self.questionary = questionary_library
        self.tv_show_name = tv_show_name
        self.tv_show_path = tv_show_path
        self.answer = ""

    def ask(self):
        return self.answer

    def text(self, message):
        if message == "TV-show search:":
            self.answer = self.tv_show_name
        elif message == "Input new path:":
            self.answer = self.tv_show_path

        return self

    def confirm(self, message):
        if message == f"Is '{self.tv_show_name}' correct TV-show?":
            self.answer = True
        elif message == "Use same path?":
            self.answer = False
        elif message == "Rename files?":
            self.answer = False

        return self

    def select(self, message, choices, pointer):
        if message == "Select pattern":
            self.answer = choices[0]

        return self
