class logger(object):
    INFO = 0
    WARNING = 1
    ERROR = 2

    PREFIXES = ("[INFO]", "[WARNING]", "[ERROR]")
    COLORS = ("\033[0m", "\033[93m", "\033[91m", "\033[0m")

    @staticmethod
    def log(self, message: str, level: int = INFO):
        if level < 0 or level > 2:
            return
        print(f"{self.COLORS[level]}{self.PREFIXES[level]} {message}{self.COLORS[3]}")

