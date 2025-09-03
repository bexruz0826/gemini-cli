import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
CARD_NUMBER = os.getenv("CARD_NUMBER")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "✈️ Assalomu alaykum!\n"
        "Marhamat, yo‘nalish va sanani kiriting.\n\n"
        "Namuna:\n`Buxoro Moskva 15.09.2025`",
        parse_mode="Markdown"
    )

@dp.message_handler()
async def handle_request(message: types.Message):
    text = f"🆕 Yangi so‘rov!\n\n{message.text}\n👤 Mijoz: @{message.from_user.username or message.from_user.id}"
    await bot.send_message(ADMIN_ID, text)
    await message.answer("✅ So‘rovingiz kassirga yuborildi.\nTez orada variantlar chiqadi.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
