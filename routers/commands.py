from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}! Use /help command to get message with help.")

@router.message(Command("myid"))
async def cmd_myid(message: types.Message):
    await message.answer(f"Your id: <code>{message.from_user.id}</code>", parse_mode="HTML")

@router.message(Command("myname"))
async def cmd_myname(message: types.Message):
    if message.from_user.last_name == None:
        await message.answer(f"Your name:\n\n"
                            f"Full name: <code>{message.from_user.first_name}</code>\n"
                            f"First name: <code>{message.from_user.first_name}</code>\n"
                            f"Last name: you haven't set last name\n", parse_mode="HTML")
    else:
        await message.answer(f"Your name:\n\n"
                            f"Full name: <code>{message.from_user.full_name}</code>\n"
                            f"First name: <code>{message.from_user.first_name}</code>\n"
                            f"Last name: <code>{message.from_user.last_name}</code>\n", parse_mode="HTML")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    return await message.answer(f"Commands for <b>What is my id bot</b>:\n\n"
        f"/start - restart bot\n"
        f"/help - show this message\n"
        f"/myid - show your id\n"
        f"/myname - show your name",
        parse_mode="HTML")
