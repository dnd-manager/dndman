import logging
from colorama import Fore



class Formatter(logging.Formatter):
    """A class for formatting colored logs."""

    FORMAT = "%(prefix)s%(levelname)s{}: %(message)s".format(Fore.RESET)

    LOG_LEVEL_COLOR = {
        "DEBUG": {"prefix": Fore.GREEN},
        "INFO": {"prefix": Fore.CYAN},
        "WARNING": {"prefix": Fore.YELLOW},
        "ERROR": {"prefix": Fore.LIGHTRED_EX},
        "CRITICAL": {"prefix": Fore.RED},
    }

    def format(self, record):
        """Format log records with a default prefix and suffix to terminal color codes that corresponds to the log level name."""
        if not hasattr(record, "prefix"):
            record.prefix = self.LOG_LEVEL_COLOR.get(record.levelname.upper()).get(
                "prefix"
            )

        if not hasattr(record, "suffix"):
            record.suffix = self.LOG_LEVEL_COLOR.get(record.levelname.upper()).get(
                "suffix"
            )

        formatter = logging.Formatter(self.FORMAT)
        return formatter.format(record)

logger = logging.getLogger("dndman")

logger_stream = logging.StreamHandler()
logger_formatter = Formatter()

logger_stream.setFormatter(logger_formatter)
logger.addHandler(logger_stream)