"""
init for the translation_library package
"""

import datetime
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s] (%(asctime)s) %(funcName)s(): %(message)s ['%(pathname)s:%(lineno)s']",
    filename=f"{datetime.datetime.now().strftime("%H:%M:%S_%m-%d-%y")}.log",
)
