import os

from pyrogram        import Client
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.types  import User
from pyrogram.raw.types              import Updates
from pyrogram.raw.functions.channels import CreateChannel
from pyrogram.handlers.handler       import Handler

from .client import Client_

from Log.log import Log


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, phone: str, *args):
        if phone not in cls._instances:
            instance = super().__call__(phone, *args)
            cls._instances[phone] = instance

        return cls._instances[phone]


class UserBot(metaclass = SingletonMeta):
    def __init__(self, phone: str) -> None:  
        self.__phone: str = phone
        self.__app: Client = Client(self.__path(), 13661403, "047935f77d19049125d7df7a869e3b48")


    async def get_me(self) -> User:
        self.__app.me = await self.__app.get_me()
        return await self.__app.get_me()


    async def get_user_id(self) -> int | None:
        try:
            me_ = await self.get_me()
            return me_.id
        except Exception as ex:
            Log(self.__phone).error(ex)


    async def start(self) -> bool:
        try:
            await self.__app.start()
            Log(self.__phone).info("start")
            
            return True
        except Exception as ex:
            Log(self.__phone).error(ex)
        return False

    async def connect(self) -> bool:
        try:
            await self.__app.connect()
            Log(self.__phone).info("connect")
            
            return True
        except Exception as ex:
            Log(self.__phone).error(ex)
        return False


    async def stop(self) -> bool:
        try:
            await self.__app.stop()
            Log(self.__phone).info("stop")
            
            return True
        except Exception as ex:
            Log(self.__phone).error(ex)
        return False

    async def disconnect(self) -> bool:
        try:
            await self.__app.disconnect()
            Log(self.__phone).info("disconnect")
            
            return True
        except Exception as ex:
            Log(self.__phone).error(ex)
        return False


    def del_single_obj(self):
        if self.__phone in SingletonMeta._instances:
            del SingletonMeta._instances[self.__phone]

    def to_Client_(self) -> Client_:
        return Client_(self.__app)

    def add_handler(self,
        handler: Handler,
        group: int = 0
    ) -> bool:
        try:
            self.__app.add_handler(
                handler,
                group
            )
            return True
        except Exception as ex:
            Log(self.__phone).error(ex)
        return False


    async def phone(self, phone_: str) -> bool:
        try:
            self._phone = phone_
            self._sent_code = await self.__app.send_code(phone_)
            Log(self.__phone).info(f"{phone_}: send code")

            return True
        except Exception as ex:
            Log(self.__phone).error(ex)
        return False
    
    async def code(self, code_: str) -> int:
        try:
            signed_in = await self.__app.sign_in(self._phone, self._sent_code.phone_code_hash, code_)
            
            if isinstance(signed_in, User):
                Log(self.__phone).info("add")
                return 0
        except SessionPasswordNeeded:
            Log(self.__phone).info("need password")
            return 1
        except Exception as ex:
            Log(self.__phone).error(ex)
        return 2
    
    async def password(self, password: str) -> bool:
        try:
            await self.__app.check_password(password)
            Log(self.__phone).info("app: password is correct")

            return True
        except Exception as ex:
            Log(self.__phone).error(ex)
        return False


    def __path(self):
        dir_ = os.path.dirname(os.path.realpath(__file__))
        dir_ = os.path.dirname(dir_)

        session_dir = os.path.join(dir_, "session")

        if not os.path.exists(session_dir):
            os.mkdir(session_dir)

        return os.path.join(session_dir, self.__phone)
