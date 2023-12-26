from pyrogram import Client, types, enums

from Log.log import Log

from datetime import datetime
from typing import Union, List, Optional

class Client_:
    def __init__(self, client: Client) -> None:
        self.__client: Client = client


    def get_client(self):
        return self.__client

    async def get_me(self) -> types.User:
        self.__client.me = self.__client.get_me()
        return await self.__client.get_me()


    async def copy_message(self,
        chat_id:      Union[int, str],
        from_chat_id: Union[int, str],
        message_id:   int,
        caption:      str = None,
        parse_mode:   Optional[enums.ParseMode] = None,
        caption_entities: List[types.MessageEntity] = None,
        disable_notification: bool = None,
        reply_to_message_id:  int = None,
        schedule_date:    datetime = None,
        protect_content:  bool = None,
        reply_markup: Union[
            types.InlineKeyboardMarkup,
            types.ReplyKeyboardMarkup,
            types.ReplyKeyboardRemove,
            types.ForceReply
        ] = None
    ) -> types.Message:
        try:
            return await self.__client.copy_message(
                chat_id, 
                from_chat_id, 
                message_id, 
                caption, 
                parse_mode, 
                caption_entities, 
                disable_notification,
                reply_to_message_id,
                schedule_date,
                protect_content,
                reply_markup
            )
        except Exception as ex:
            Log(self.__client.phone_number).error(ex)

    async def copy_media_group(self,
        chat_id:      Union[int, str],
        from_chat_id: Union[int, str],
        message_id:   int,
        captions:     Union[List[str], str] = None,
        disable_notification: bool = None,
        reply_to_message_id:  int = None,
        schedule_date: datetime = None,
    ) -> List[types.Message] | None:
        try:
            return await self.__client.copy_media_group(
                chat_id, 
                from_chat_id, 
                message_id, 
                captions, 
                disable_notification,
                reply_to_message_id,
                schedule_date
            )              
        except Exception as ex:
            Log(self.__client.phone_number).error(ex)


    async def send_message(self,
        chat_id: Union[int, str],
        text:    str,
        parse_mode: Optional[enums.ParseMode] = None,
        entities:   List[types.MessageEntity] = None,
        disable_web_page_preview: bool = True,
        disable_notification:     bool = None,
        reply_to_message_id: int = None,
        schedule_date:       datetime = None,
        protect_content:     bool = None,
        reply_markup: Union[
            types.InlineKeyboardMarkup,
            types.ReplyKeyboardMarkup,
            types.ReplyKeyboardRemove,
            types.ForceReply
        ] = None
    ) -> types.Message | None:
        try:
            return await self.__client.send_message(
                chat_id,
                text,
                parse_mode,
                entities,
                disable_web_page_preview,
                disable_notification,
                reply_to_message_id,
                schedule_date,
                protect_content,
                reply_markup
            )
        except Exception as ex:
            Log(self.__client.phone_number).error(ex)