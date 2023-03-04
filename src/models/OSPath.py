import subprocess
from dataclasses import dataclass


@dataclass
class OSPath:
    path: str

    def change_separators(self) -> None:
        raise NotImplementedError


class WindowsPath(OSPath):
    def change_separators(self) -> None:
        self.path = self.path.replace('/', '\\')

    def add_path_ending(self):
        return self.path if self.path[-1] == "\\" else self.path + "\\"


class UnixPath(OSPath):
    def change_separators(self) -> None:
        self.path = self.path.replace('\\', '/')

    def add_path_ending(self):
        if "\\" in self.path:
            command = subprocess.check_output(["wslpath", "-a", f"{self.path}"])
            self.path = command.decode("utf-8").strip()
            print(f"Root folder: {self.path}")
        return self.path if self.path[-1] == "/" else self.path + "/"
