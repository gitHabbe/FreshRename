from models.DirTraverse import DirTraverse


class OSAction:

    def __init__(self, operative_system, dir_traverse: DirTraverse):
        self.__os = operative_system
        self.dir_traverse = dir_traverse

    def build_cache(self, new_path):
        self.dir_traverse.build_cache(new_path)