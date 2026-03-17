from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}! Use /help command to get message with help.")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    return await message.answer(f"Commands for <b>What is my id bot</b>:\n\n"
        f"/start - restart bot\n"
        f"/help - show this message\n",
        parse_mode="HTML")
