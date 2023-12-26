from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from .translation.btr import btr


class Markups:
    def markup(bt: list[list[str]] | list[str] | str | int = None) -> ReplyKeyboardMarkup:
        markup_ = ReplyKeyboardMarkup(resize_keyboard = True)
        
        if bt is None:
            return markup_
        
        if not isinstance(bt, list):
            bt = [bt]

        if not isinstance(bt[0], list):
            bt = [bt]
        
        for i in bt:
            markup_.row(*[KeyboardButton(j) for j in i])

        return markup_
    
    def inline(bt: list[list[str, str]]) -> InlineKeyboardMarkup:
        markup_ = InlineKeyboardMarkup()

        if not isinstance(bt[0], list):
            bt = [bt]

        if not isinstance(bt[0][0], list):
            bt = [bt]

        for i in bt:
            row = []
            for j, k in i:
                row.append(InlineKeyboardButton(j, callback_data = k))
            markup_.row(*row)

        return markup_

    empty = ReplyKeyboardRemove()
    start = markup(btr.t1.data)
    back  = markup(btr.t2.data)