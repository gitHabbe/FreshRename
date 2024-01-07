import json
import os
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class TvShowRootPath:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path: ClassVar[str] = f"{ROOT_DIR}/../private/cache.json"

    def get_path(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def save_path(self, path: str):
        current_path = self.get_path()
        current_path["last_path"] = path
        with open(self.file_path, "w") as file:
            json.dump(current_path, file)
            return current_path["last_path"]
