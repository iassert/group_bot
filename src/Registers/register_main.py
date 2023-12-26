from Bot.bot import Bot_

from Handlers.main import Main


Bot_.dp.register_message_handler(
    Main.start,
    commands = "start",
    state = "*"
)