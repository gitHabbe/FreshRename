class OSEntryMock:
    def __init__(self, name: str, path: str, is_directory: bool):
        self.name = name
        self.path = path
        self.is_directory = is_directory

    def is_dir(self) -> bool:
        return self.is_directory
