class PrintColor:

    @staticmethod
    def red(data: str):
        print(f"\033[91m{data}\033[0m")

    @staticmethod
    def green(data: str):
        print(f"\033[92m{data}\033[0m")
