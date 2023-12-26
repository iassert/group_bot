import typing
import logging

from aiogram       import Bot, types
from aiogram.types import base, Message, MessageEntity,\
    InlineKeyboardMarkup, ReplyKeyboardMarkup,\
    ReplyKeyboardRemove, ForceReply, User

from aiogram.dispatcher                 import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import Config

from Log.log import Log

logging.basicConfig(level = logging.INFO)



class Bot_:
    bot: Bot = Bot(token = Config.TOKEN, server = Config.LOCAL_SERVER)
    dp: Dispatcher = Dispatcher(bot, storage = MemoryStorage())
    
    me: User = None
    id: int = None
    username: str = None


    timeout: int = 300
    sleep: int = 5

    def __init__(self, message: Message):
        self._message: Message = message
    

    async def answer(self,
        text:       base.String,
        parse_mode: typing.Optional[base.String] = "html",
        entities:   typing.Optional[typing.List[MessageEntity]] = None,
        disable_web_page_preview: typing.Optional[base.Boolean] = True,
        disable_notification:     typing.Optional[base.Boolean] = None,
        protect_content:          typing.Optional[base.Boolean] = None,
        allow_sending_without_reply: typing.Optional[base.Boolean] = True,
        reply_markup: typing.Union[
            InlineKeyboardMarkup,
            ReplyKeyboardMarkup,
            ReplyKeyboardRemove,
            ForceReply,
            None,
        ] = None,
        reply: base.Boolean = False
    ) -> Message:
        try:
            return await self._message.answer(
                text,
                parse_mode,
                entities,
                disable_web_page_preview,
                disable_notification,
                protect_content,
                allow_sending_without_reply,
                reply_markup,
                reply
            )
        except Exception as ex:
            Log(self._message.chat.id).error(ex)

    async def answer_photo(self,
        photo: typing.Union[base.InputFile, base.String],
        caption: typing.Optional[base.String] = None,
        parse_mode: typing.Optional[base.String] = "html",
        caption_entities: typing.Optional[typing.List[MessageEntity]] = None,
        disable_notification: typing.Optional[base.Boolean] = None,
        protect_content: typing.Optional[base.Boolean] = None,
        allow_sending_without_reply: typing.Optional[base.Boolean] = None,
        reply_markup: typing.Union[
            InlineKeyboardMarkup,
            ReplyKeyboardMarkup,
            ReplyKeyboardRemove,
            ForceReply,
            None,
        ] = None,
        reply: base.Boolean = False,
    ):
        try:
            return await self._message.answer_photo(
                photo,
                caption,
                parse_mode,
                caption_entities,
                disable_notification,
                protect_content,
                allow_sending_without_reply,
                reply_markup,
                reply
            )
        except Exception as ex:
            Log(self._message.chat.id).error(ex)

    async def answer_document(self, 
        document:   typing.Union[base.InputFile, base.String],
        thumb:      typing.Union[typing.Union[base.InputFile, base.String], None] = None,
        caption:    typing.Optional[base.String] = None,
        parse_mode: typing.Optional[base.String] = None,
        caption_entities:       typing.Optional[typing.List[MessageEntity]] = None,
        disable_content_type_detection: typing.Optional[base.Boolean] = None,
        disable_notification:   typing.Optional[base.Boolean] = None,
        protect_content:        typing.Optional[base.Boolean] = None,
        allow_sending_without_reply: typing.Optional[base.Boolean] = None,
        reply_markup: typing.Union[
            InlineKeyboardMarkup,
            ReplyKeyboardMarkup,
            ReplyKeyboardRemove,
            ForceReply,
            None,
        ] = None,
        reply: base.Boolean = False,
    ) -> Message:
        try:
            return await self._message.answer_document(
                document,
                thumb, 
                caption, 
                parse_mode, 
                caption_entities,
                disable_content_type_detection,
                disable_notification,
                protect_content,
                allow_sending_without_reply,
                reply_markup,
                reply
            )
        except Exception as ex:
            Log(self._message.chat.id).error(ex)
        

    async def send_message(
        chat_id:    typing.Union[base.Integer, base.String],
        text:       base.String,
        parse_mode: typing.Optional[base.String] = "html",
        entities:   typing.Optional[typing.List[types.MessageEntity]] = None,
        disable_web_page_preview:    typing.Optional[base.Boolean] = True,
        message_thread_id:           typing.Optional[base.Integer] = None,
        disable_notification:        typing.Optional[base.Boolean] = None,
        protect_content:             typing.Optional[base.Boolean] = None,
        reply_to_message_id:         typing.Optional[base.Integer] = None,
        allow_sending_without_reply: typing.Optional[base.Boolean] = None,
        reply_markup: typing.Union[
            types.InlineKeyboardMarkup,
            types.ReplyKeyboardMarkup,
            types.ReplyKeyboardRemove,
            types.ForceReply, 
            None
        ] = None,
    ) -> types.Message:
        try:
            return await Bot_.bot.send_message(
                chat_id,
                text,
                parse_mode,
                entities,
                disable_web_page_preview,
                message_thread_id,
                disable_notification,
                protect_content,
                reply_to_message_id,
                allow_sending_without_reply,
                reply_markup,
            )
        except Exception as ex:
            Log(chat_id).error(ex)
    
    async def send_photo(
        chat_id:    typing.Union[base.Integer, base.String],
        photo:      typing.Union[base.InputFile, base.String],
        caption:    typing.Optional[base.String] = None,
        parse_mode: typing.Optional[base.String] = "html",
        caption_entities:  typing.Optional[typing.List[types.MessageEntity]] = None,
        message_thread_id: typing.Optional[base.Integer] = None,
        disable_notification: typing.Optional[base.Boolean] = None,
        protect_content:      typing.Optional[base.Boolean] = None,
        reply_to_message_id:  typing.Optional[base.Integer] = None,
        allow_sending_without_reply: typing.Optional[base.Boolean] = None,
        reply_markup: typing.Union[
            types.InlineKeyboardMarkup,
            types.ReplyKeyboardMarkup,
            types.ReplyKeyboardRemove,
            types.ForceReply, 
            None
        ] = None,
        has_spoiler: typing.Optional[base.Boolean] = None,
    ) -> types.Message:
        try:
            return await Bot_.bot.send_photo(
                chat_id,
                photo,
                caption,
                parse_mode,
                caption_entities,
                message_thread_id,
                disable_notification,
                protect_content,
                reply_to_message_id,
                allow_sending_without_reply,
                reply_markup,
                has_spoiler
            )
        except Exception as ex:
            Log(chat_id).error(ex)
    
    async def send_video(
        chat_id:  typing.Union[base.Integer, base.String],
        video:    typing.Union[base.InputFile, base.String],
        duration: typing.Optional[base.Integer] = None,
        width:    typing.Optional[base.Integer] = None,
        height:   typing.Optional[base.Integer] = None,
        thumb:    typing.Union[base.InputFile, base.String, None] = None,
        caption:  typing.Optional[base.String] = None,
        parse_mode:           typing.Optional[base.String] = None,
        caption_entities:     typing.Optional[typing.List[types.MessageEntity]] = None,
        supports_streaming:   typing.Optional[base.Boolean] = None,
        message_thread_id:    typing.Optional[base.Integer] = None,
        disable_notification: typing.Optional[base.Boolean] = None,
        protect_content:      typing.Optional[base.Boolean] = None,
        reply_to_message_id:  typing.Optional[base.Integer] = None,
        allow_sending_without_reply: typing.Optional[base.Boolean] = None,
        reply_markup: typing.Union[
            types.InlineKeyboardMarkup,
            types.ReplyKeyboardMarkup,
            types.ReplyKeyboardRemove,
            types.ForceReply, 
            None
        ] = None,
        has_spoiler: typing.Optional[base.Boolean] = None,
    ) -> types.Message:

        try:
            return await Bot_.bot.send_video(
                chat_id,
                video,
                duration,
                width,
                height,
                thumb,
                caption,
                parse_mode,
                caption_entities,
                supports_streaming,
                message_thread_id,
                disable_notification,
                protect_content,
                reply_to_message_id,
                allow_sending_without_reply,
                reply_markup,
                has_spoiler
            )
        except Exception as ex:
            Log(chat_id).error(ex) 
    
    async def send_media_group(
        chat_id: typing.Union[base.Integer, base.String],
        media:   typing.Union[types.MediaGroup, typing.List],
        message_thread_id:    typing.Optional[base.Integer] = None,
        disable_notification: typing.Optional[base.Boolean] = None,
        protect_content:      typing.Optional[base.Boolean] = None,
        reply_to_message_id:  typing.Optional[base.Integer] = None,
        allow_sending_without_reply: typing.Optional[base.Boolean] = None,
    ) -> typing.List[types.Message]:
        try:
            return await Bot_.bot.send_media_group(
                chat_id,
                media,
                message_thread_id,
                disable_notification,
                protect_content,
                reply_to_message_id,
                allow_sending_without_reply
            )
        except Exception as ex:
            Log(chat_id).error(ex)


    async def delete(self) -> base.Boolean:
        try:
            return await self._message.delete()
        except Exception as ex:
            Log(self._message.chat.id).error(ex)

    async def delete_message(
        chat_id: typing.Union[base.Integer, base.String],
        message_id: base.Integer
    ) -> base.Boolean:
        try:
            return await Bot_.bot.delete_message(chat_id, message_id)
        except Exception as ex:
            Log(chat_id).error(ex)


    async def get_chat_member(
        chat_id: typing.Union[base.Integer, base.String],
        user_id: base.Integer
    ) -> types.ChatMember:
        try:
            return await Bot_.bot.get_chat_member(chat_id, user_id)
        except Exception as ex:
            Log(chat_id).error(ex)