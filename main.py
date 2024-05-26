import asyncio
from loader import dp, bot
import handlers
import site_API
from database.core import db_start
import config_data
import logging



async def main():
    logging.basicConfig(
        filename='bot.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    await db_start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
