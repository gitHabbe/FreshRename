import json
import unittest
from unittest.mock import MagicMock

from approvaltests.approvals import verify

from OSAction import OSAction
from frontend.CommandLine.CommandLine import CommandLine
from models.RequestShow import RequestShow
from models.UserInput import UserInput


class OSEntryMock:
    def __init__(self, name: str, path: str, is_directory: bool):
        self.name = name
        self.path = path
        self.is_directory = is_directory

    def is_dir(self) -> bool:
        return self.is_directory


class OSMock:
    def __init__(self, tv_show_name):
        self.tv_show_name = tv_show_name

    def scandir(self, path):
        entries = []
        with open("../test/LocalFileData.json", "r") as local_file_entries:
            local_file_entries_data = json.load(local_file_entries)[self.tv_show_name]
            for local_file_entry_data in local_file_entries_data:
                entry = OSEntryMock(local_file_entry_data["name"], local_file_entry_data["path"], False)
                entries.append(entry)
        return entries

    def rename(self, old_file_name, new_file_name):
        pass


class TestCommandLine(unittest.TestCase):

    def test_tv_show_entourage(self):
        user_input = UserInput()
        tv_show_name = "Entourage"
        user_input.ask_tv_show_name = MagicMock(return_value=tv_show_name)
        user_input.confirm_tv_show_name = MagicMock(return_value=True)
        user_input.ask_tv_show_path = MagicMock(return_value="C:\Entourage")
        user_input.confirm_tv_show_path = MagicMock(side_effect=[False, True])
        user_input.choose_name_strategy = MagicMock(return_value="S01E01 - Episode name here")
        user_input.confirm_tv_show_rename = MagicMock(return_value=False)
        user_input.confirm_tv_show_rename = MagicMock(return_value=True)

        request_show = RequestShow()
        request_show.name = MagicMock(return_value=[{"show": {"id": 559, "name": tv_show_name}}])
        with open("../test/RequestShowData.json", "r") as tv_show_mock:
            load = json.load(tv_show_mock)[tv_show_name]
            request_show.episodes = MagicMock(return_value=load)

        action = OSAction(OSMock(tv_show_name))
        os_action = action
        self.__verify_tv_show(user_input, request_show, os_action)

    def test_tv_show_invincible(self):
        user_input = UserInput()
        tv_show_name = "Invincible"
        user_input.ask_tv_show_name = MagicMock(return_value=tv_show_name)
        user_input.confirm_tv_show_name = MagicMock(return_value=True)
        user_input.ask_tv_show_path = MagicMock(return_value="C:\Invincible.2021.S01")
        user_input.confirm_tv_show_path = MagicMock(side_effect=[False, True])
        user_input.choose_name_strategy = MagicMock(return_value="01x01 - Episode name here")
        user_input.confirm_tv_show_rename = MagicMock(return_value=False)

        request_show = RequestShow()
        request_show.name = MagicMock(return_value=[{"show": {"id": 2013997, "name": tv_show_name}}])
        with open("../test/RequestShowData.json", "r") as tv_show_mock:
            load = json.load(tv_show_mock)[tv_show_name]
            request_show.episodes = MagicMock(return_value=load)

        action = OSAction(OSMock(tv_show_name))
        os_action = action
        self.__verify_tv_show(user_input, request_show, os_action)

    def __verify_tv_show(self, user_input, request_show, os_action):
        command_line = CommandLine(user_input, request_show, os_action)
        command_line.run()
        episode_list_data_as_string = self.__format_dict_list(os_action.rename.file_list)
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
