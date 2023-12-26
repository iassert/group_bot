from aiogram import types

from Accest.translation.btr import btr

from Bot.bot import Bot_

from Handlers.auth import Auth, FormAuth


Bot_.dp.register_message_handler(
    Auth.send_add_userbot,
    regexp = btr.t1.add_userbot,
    state = "*"
)
Bot_.dp.register_message_handler(
    Auth.add_userbot,
    content_types = types.ContentType.TEXT,
    state = FormAuth.add_userbot
)

Bot_.dp.register_message_handler(
    Auth.add_code,
    content_types = types.ContentType.TEXT,
    state = FormAuth.add_code
)

Bot_.dp.register_message_handler(
    Auth.add_password,
    content_types = types.ContentType.TEXT,
    state = FormAuth.add_password
)