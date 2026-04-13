import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import config
from routers import commands
from aiohttp import web
import os


bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

# --- ping router ---
async def ping(request):
    return web.Response(text="ok")
async def start_web():
    app = web.Application()
    app.router.add_get("/ping", ping)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_routers(commands.router)

    print("Bot successfully opened!")
    await start_web()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
