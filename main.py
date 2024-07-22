import asyncio

from loader import dp, bot
import handlers
from site_API.core import api_core

import config_data
import logging


async def main():
    logging.basicConfig(
        filename='bot.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    api_core()

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
