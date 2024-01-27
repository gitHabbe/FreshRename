import json

from test.OSEntryMock import OSEntryMock


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
