import questionary
from models.LocalPath import LocalPath
from models.namePatterns.PatternSelector import patterns


class CommandLine:
    cli = questionary
    localPath = LocalPath()

    def confirmPath(self):
        cachedPath = self.localPath.path()
        print(f"Last path: {cachedPath}")
        samePath = "Use same path?"
        return self.cli.confirm(samePath).ask()

    def newPath(self):
        return self.cli.text("asdf").ask()

    def selectPattern(self):
        patternOptions = list(patterns.keys())
        chosenPattern = self.cli.select(
            message="Select pattern",
            choices=patternOptions,
            pointer="→"
        ).ask()
        print(chosenPattern)
        return patterns.get(chosenPattern)
        # if not confirmed:

        # print(confirmed)


CommandLine().selectPattern()
