from models.DirTraverse import DirTraverse
from models.Rename import Rename


class OSAction:

    def __init__(self, operative_system):
        self.__os = operative_system
        self.dir_traverse = DirTraverse(self.__os)
        self.rename = Rename(self.__os)

    def fill_file_list(self, store, episodes_data, name_strategy):
        self.rename.fill_file_list(store, episodes_data, name_strategy)

    def get_local_files(self, episodes_path):
        return self.dir_traverse.get_local_files(episodes_path)
