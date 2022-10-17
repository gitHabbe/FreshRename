import subprocess
from dataclasses import dataclass


@dataclass
class OSPath:
    path: str


class WindowsPath(OSPath):
    def formatted_path(self):
        return self.path if self.path[-1] == "\\" else self.path + "\\"


class UnixPath(OSPath):
    def formatted_path(self):
        if "\\" in self.path:
            command = subprocess.check_output(["wslpath", "-a", f"{self.path}"])
            self.path = command.decode("utf-8").strip()
            print(f"Root folder: {self.path}")
        return self.path if self.path[-1] == "/" else self.path + "/"