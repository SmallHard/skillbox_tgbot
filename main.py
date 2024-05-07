import asyncio
from loader import dp, bot
import handlers
import site_API
import database
import config_data
import api


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
