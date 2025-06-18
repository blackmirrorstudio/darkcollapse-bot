import asyncio
import logging
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InputFile

API_TOKEN = "7656837442:AAHV3QVSnyhc2523m6CmPMzD7FIGWmHe0c4"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Главное меню — кнопки через именованный аргумент
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📦 Katalog & Cennik 💰"),
            KeyboardButton(text="📲 Kontakt")
        ]
    ],
    resize_keyboard=True
)

# Кнопка «назад»
back_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🤏Wróć")]],
    resize_keyboard=True
)

CATALOG_TEXT = """
1. <b>☘️ Green Ghost</b>
Do relaksu

1g – 50 zł
2g – 90 zł
5g – 200 zł
10g – 350 zł
⸻
2. <b>🍬 Happy Drops (MDM@)</b>
Słodycz

1 szt – 50 zł
2 szt – 80 zł
5 szt – 160 zł
10 szt – 280 zł
⸻
3. <b>🧼 Crystal Clean (p1ko)</b>
Pudrowa precyzja. Działa głęboko 👹

0.1g – 30 zł
0.2g – 50 zł
0.5g – 100 zł
1g – 170 zł
⸻
4. <b>🔥 Alfa-PVP</b>
Mocna stymulacja, szybki start ⚡

0.25g – 50 zł  
0.5g – 100 zł  
1g – 150 zł  
⸻
5. <b>🐍 mefedr0n Venom</b>
Zimna euforia, serpentynowy flow 🐾

0.5g – 45 zł  
1g – 60 zł  
5g – 250 zł
"""

@dp.message(F.text == "📦 Katalog & Cennik 💰")
async def catalog_handler(message: Message):
    await message.answer(
        CATALOG_TEXT,
        reply_markup=back_kb,
        parse_mode=ParseMode.HTML
    )
    
@dp.message(Command("start"))
async def start_handler(message: Message):
    photo = FSInputFile(path="image.jpg")
    await message.answer_photo(
        photo=photo,
        caption="👇 Wybierz opcję:",
        reply_markup=main_kb
    )

@dp.message(F.text == "📦 Katalog & Cennik 💰")
async def catalog_handler(message: Message):
    await message.answer(CATALOG_TEXT, reply_markup=back_kb)

@dp.message(F.text == "📲 Kontakt")
async def contact_handler(message: Message):
    await message.answer(
        "🛒 Aby złożyć zamówienie klikaj @DarkCollapse_Op\nI kontaktuj się z operatоrem 📞",
        reply_markup=back_kb
    )

@dp.message(F.text == "🤏Wróć")
async def back_handler(message: Message):
    await message.answer("👇 Wybierz opcję:", reply_markup=main_kb)

async def main():
    # Убираем старый webhook, чтобы заработал polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
