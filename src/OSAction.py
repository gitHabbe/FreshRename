from models.DirTraverse import DirTraverse
from models.Rename import Rename


class OSAction:

    def __init__(self, operative_system, dir_traverse: DirTraverse, rename: Rename):
        self.rename = rename
        self.__os = operative_system
        self.dir_traverse = dir_traverse

    def build_cache(self, new_path):
        self.dir_traverse.build_cache(new_path)

    def fill_file_list(self, episodes_data, name_strategy):
        self.rename.fill_file_list(self.dir_traverse.cache.store, episodes_data, name_strategy)
