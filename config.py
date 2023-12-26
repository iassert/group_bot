from aiogram.bot.api import TelegramAPIServer


class Config:
    TOKEN: str
    CREATOR_ID: int

    MAIN_GROUP_ID: int
    
    DATABASE: str
    USER:     str
    PASSWORD: str
    HOST:     str
    PORT:     str
    
    LOCAL_SERVER: TelegramAPIServer = TelegramAPIServer.from_base('http://localhost:8081')
