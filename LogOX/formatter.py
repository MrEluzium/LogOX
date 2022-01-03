"""
Copyright 2022 Artem Voronov <mreluzium@mail.ru>

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import logging
from logging import Formatter, PercentStyle


class FormatterOX(Formatter):
    """
    Redefining the functionality of the basic formatter to change the format depending on message log level
    In this case we add filename and line number to debug messages
    """
    _BASE_FORMAT = "[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
    _DEBUG_FORMAT = "[%(asctime)s] [%(filename)s:%(lineno)d] %(name)s:%(levelname)s: %(message)s"
    _DATE_FORMAT = "%d/%b/%Y %H:%M:%S"

    def __init__(self):
        super().__init__(fmt=FormatterOX._BASE_FORMAT, datefmt="%d/%b/%Y %H:%M:%S", style='%', validate=True)

        self._debug_style = PercentStyle(FormatterOX._DEBUG_FORMAT)
        self._debug_style.validate()

    def formatMessage(self, record):
        if record.levelno == logging.DEBUG:
            return self._debug_style.format(record)
        return self._style.format(record)
