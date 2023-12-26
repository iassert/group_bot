import asyncio
import logging

from aiogram.types      import Message
from aiogram.utils 		import executor
from aiogram.dispatcher import Dispatcher, FSMContext

from Accest.markups         import Markups
from Accest.translation.ttr import ttr

from Bot.bot import Bot_

from Data.userbots import UserBots

from config import Config


class Main:
	"""
    > - input something
    < - output something

    * - state
    # - message
	! - command
    [] - keyboard
	** - call func {
		info
	}
    """

	async def start(message: Message, state: FSMContext) -> None:
		"""
		>* - '*'
		>! - "start"

		<* - finish
		<# - ttr.t1
		<[] - Markups.start(btr.t1)
		"""
		await state.finish()
		await Bot_(message).answer(ttr.t1, reply_markup = Markups.start)

	async def restart() -> None:
		from .auth import Auth

		userbots_ = UserBots._get_phone_userbots()
		if userbots_ is None:
			return
		
		for phone, *_ in userbots_:
			asyncio.create_task(
				Auth._register_app_message_handler(phone)
			)

	async def on_startup(_) -> None:
		asyncio.create_task(Main.restart())

		Bot_.me = await Bot_.bot.get_me()
		Bot_.id = Bot_.me.id
		Bot_.username = Bot_.me.username

		await Bot_.send_message(Config.CREATOR_ID, "Бот запущен")


	async def on_shutdown(dp: Dispatcher) -> None:
		logging.warning('Shutting down..')

		await Bot_.send_message(Config.CREATOR_ID, "Бот Выключен")

		logging.warning('Bye!')

	def main() -> None:
		executor.start_polling(
			dispatcher   = Bot_.dp,
			skip_updates = True,
			on_startup   = Main.on_startup,
			on_shutdown  = Main.on_shutdown,
			timeout		 = Bot_.timeout,
		)


if __name__ == '__main__':
    Main.main()
