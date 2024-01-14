import json
from os.path import dirname, abspath
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class TvShowRootPath:
    __ROOT_DIR = dirname(abspath(__file__))
    __path: ClassVar[str] = f"{__ROOT_DIR}/../private/cache.json"

    def get_path(self):
        with open(self.__path, "r") as file:
            return json.load(file)

    def save_path(self, path: str):
        current_path = self.get_path()
        current_path["last_path"] = path
        with open(self.__path, "w") as file:
            json.dump(current_path, file)
            return current_path["last_path"]
