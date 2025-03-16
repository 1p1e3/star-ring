"""
封装的 loguru 日志模块，提供便捷的日志记录功能
"""
import datetime
import os
import sys
from pathlib import Path
from loguru import logger


class Logger:
    def __init__(self):
        format_string = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}"

        self._logger = logger

        self._logger.remove()


        self._logger.add(
            sink=sys.stderr,
            format=format_string,
            colorize=True
        )


    def get_logger(self):
        return self._logger

