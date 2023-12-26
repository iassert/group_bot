import os
import logging
import traceback

from Accest.translation.ltr import ltr

from logging  import Logger
from datetime import datetime

logging.basicConfig(level = logging.INFO)



class Log:
    def __init__(self, name: str) -> None:
        self.__name: str = name


    def error(self, ex: Exception) -> None:
        logger = self.__get_error_logger()

        for tb in traceback.extract_tb(ex.__traceback__):
            te = ltr.t1.format(
                ex.__class__.__name__, 
                ex, 
                tb.filename, 
                tb.lineno, 
                tb.name, 
                tb.line
            )
            logger.error(te)
            break

    def info(self,  text: str): self.__write("INFO",  text)


    def __get_error_logger(self) -> Logger:
        logger = logging.getLogger(self.__name)

        file_handler = logging.FileHandler(self.__path(), encoding = "utf-8")
        file_error_handler = logging.FileHandler(self.__path("errors"), encoding = "utf-8")

        formatter = logging.Formatter('%(levelname)s' + f":{self.__name}\n" + '%(message)s\n%(asctime)s')

        file_handler.setFormatter(formatter)
        file_error_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(file_error_handler)

        return logger


    def __path(self, name: str = None) -> None:
        if name is None:
            name = self.__name
        return os.path.abspath(__file__).replace(os.path.basename(__file__), f"{name}.log")


    def __write(self, lvl_name: str, text: str) -> None:
        ti = f'{lvl_name}:{self.__name}\n{text}\n{datetime.now().strftime("%d.%m.%Y %H:%M")}\n'

        try:
            with open(self.__path(), "a", encoding = "utf-8") as f:
                f.write(ti)
        except Exception as ex:
            self.error(ex)
