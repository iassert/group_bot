from .db           import DB
from .query.create import CREATE
from .query.insert import INSERT
from .query.select import SELECT


class Messages:
    @staticmethod
    def add_msg(me_id: int, from_user_id: int, msg_id: int) -> bool:
        db_ = DB()
        
        if not db_.execute(INSERT.messages.format(
            me_id        = me_id, 
            from_user_id = from_user_id,
            msg_id       = msg_id
        )): return False

        if not db_.commit():
            return False
        
        return True

    
    @staticmethod
    def get_msg_id(me_id: int, from_user_id: int) -> int | None:
        db_ = DB()

        if not db_.execute(SELECT.msg_id.format(
            me_id        = me_id,
            from_user_id = from_user_id
        )): return

        res = db_.fetchone()
        if res is not None:
            return int(res[0])

    @staticmethod
    def get_from_user_id(me_id: int, msg_id: int) -> int | None:
        db_ = DB()

        if not db_.execute(SELECT.from_user_id.format(
            me_id  = me_id,
            msg_id = msg_id
        )): return

        res = db_.fetchone()
        if res is not None:
            return int(res[0])

db_ = DB()
db_.execute(CREATE.messages)
db_.commit()
