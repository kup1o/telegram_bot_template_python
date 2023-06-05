from aiogram import types
from dispatcher import dp
import config

@dp.message_handler(commands="ping", commands_prefix="!/")
async def cmd_ping_bot(message: types.Message):
  if message.from_user.id in config.BOT_OWNERS:
    await message.reply("<b>👊 Up & Running!</b>\n\n")
  else:
    await message.reply("<b>Sorry! Bot is in the developing stage. It is allowed to use only for the developer. Stay tuned for news on his Telegram Channel</b>\n\n")
