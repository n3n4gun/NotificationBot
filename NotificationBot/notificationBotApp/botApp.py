import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from botFunctions.botFunctions import BOT_ROUTER

load_dotenv()

NTBot = Bot(os.getenv('TOKEN'))
DispNTBot = Dispatcher()

async def get_bot_start():
    DispNTBot.include_router(BOT_ROUTER)
    
    await DispNTBot.start_polling(NTBot)

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)

    try:
        asyncio.run(get_bot_start())

    except KeyboardInterrupt:
        print('Work is finished')

