import asyncio
from loader import dp, bot
import handlers
import site_API
import database
import config_data
import logging

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
