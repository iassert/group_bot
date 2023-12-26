from .db           import DB
from .query.create import CREATE
from .query.insert import INSERT
from .query.select import SELECT


class UserBots:
    @staticmethod
    def add_userbot(phone: str, creator_id: int, user_id: int) -> bool:
        db_ = DB()
        
        if not db_.execute(INSERT.userbot.format(
            phone    = phone, 
            creator_id = creator_id,
            user_id  = user_id
        )): return False

        if not db_.commit():
            return False
        
        return True

    @staticmethod
    def get_creator_id(user_id: int) -> int | None:
        db_ = DB()

        if not db_.execute(SELECT.creator_id.format(
            user_id = user_id
        )): return

        res = db_.fetchone()
        if res is not None:
            return int(res[0])

    @staticmethod
    def _get_phone_userbots():
        db_ = DB()
        if not db_.execute(SELECT.phone_userbots):
            return
        
        return db_.fetchall()


db_ = DB()
db_.execute(CREATE.userbots)
db_.commit()
