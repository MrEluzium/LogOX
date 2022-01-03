import sys
import logging
from logging import handlers
from datetime import datetime
from pathlib import Path
from LogOX.formatter import FormatterOX

_FORMATTER = FormatterOX()


def _get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(_FORMATTER)
    return console_handler


def _get_file_handler():
    try:
        Path("log").mkdir(exist_ok=True)
    except OSError:
        raise
    else:
        file_handler = handlers.TimedRotatingFileHandler(r'log\{:%Y-%m-%d}.log'.format(datetime.now()), when='D')
        file_handler.setFormatter(_FORMATTER)
        return file_handler


def get_logger(name=None, level=logging.INFO):

    if not name:
        # Getting name of module which the logger is being created
        # __import__('inspect').stack()[1].filename returns caller's full file path
        # .split("\\")[-1] returns module's filename
        # [:-3] removes .py at the end of filename
        name = __import__('inspect').stack()[1].filename.split("\\")[-1][:-3]

    logger = logging.getLogger(name)
    logger.setLevel(level)

    logger.addHandler(_get_console_handler())
    try:
        logger.addHandler(_get_file_handler())
    except OSError:
        logger.exception("Can't create log file. Console-only logging.")

    logger.propagate = False  # Give access to multiply handlers logging
    return logger
