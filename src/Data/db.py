import logging
import psycopg2

from psycopg2.sql import Composable

from config import Config

from collections.abc import Mapping, Sequence
from typing import Any
from typing_extensions import TypeAlias

_Vars: TypeAlias = Sequence[Any] | Mapping[str, Any] | None


class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)

        return class_._instance


class DB(Singleton):
    def __init__(self):
        self.__con = self.connect()
        self.__cur = self.cursor()


    def connect(self):
        con = None
        try:
            con = psycopg2.connect(
                database  = Config.DATABASE,
                user      = Config.USER,
                password  = Config.PASSWORD,
                host      = Config.HOST,
                port      = Config.PORT
            )
        except Exception as ex:
            logging.error(f"connect is unsuccessful: {ex.__class__.__name__}: {ex}")

        return con
    
    def cursor(self):
        cur = None
        try:
            cur = self.__con.cursor()
        except BaseException as ex:
            logging.error(f"cursor is unsuccessful: {ex.__class__.__name__}: {ex}")

        return cur


    def execute(self, 
        query: str | bytes | Composable,
        vars: _Vars = None
    ) -> bool:
        try:
            self.__cur.execute(query, vars)
            return True
        except Exception as ex:
            self.rollback()
            logging.error(f"execute is unsuccessful: {ex.__class__.__name__}: {ex}")
        return False

    def rollback(self) -> bool:
        try:
            self.__con.rollback()
            return True
        except Exception as ex:
            logging.error(f"rollback is unsuccessful: {ex.__class__.__name__}: {ex}")
        return False


    def commit(self) -> bool:
        try:
            self.__con.commit()
            return True
        except Exception as ex:
            logging.error(f"commit is unsuccessful: {ex.__class__.__name__}: {ex}")
        return False


    def fetchone(self) -> tuple[Any, ...] | None:
        res = None
        try:
            res = self.__cur.fetchone()
        except Exception as ex:
            logging.error(f"fetchone is unsuccessful: {ex.__class__.__name__}: {ex}")
    
        return res
    
    def fetchall(self) -> list[tuple[Any, ...]] | None:
        res = None
        try:
            res = self.__cur.fetchall()
        except Exception as ex:
            logging.error(f"fetchall is unsuccessful: {ex.__class__.__name__}: {ex}")

        return res
    
    def __del__(self):
        if self.__cur is not None:
            self.__cur.close()

        if self.__con is not None:
            self.__con.close()

