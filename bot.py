# Minimal aiogram 3 skeleton: Mini App'ni ochadi va undan kelgan ma'lumotni qabul qiladi.
# pip install aiogram
import asyncio, json, os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# Maxfiy qiymatlar kodga yozilmaydi. Ularni tizim muhitidan bering:
# BOT_TOKEN va WEBAPP_URL.
TOKEN = os.getenv("BOT_TOKEN", "")
WEBAPP_URL = os.getenv("WEBAPP_URL", "")

dp = Dispatcher()

@dp.message(CommandStart())
async def start(m: Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton(text="Taqdimot yaratish", web_app=WebAppInfo(url=WEBAPP_URL))]])
    await m.answer("Mustaqil ish taqdimotini yaratish uchun tugmani bosing", reply_markup=kb)

@dp.message(F.web_app_data)
async def got_data(m: Message):
    d = json.loads(m.web_app_data.data)
    # d = {topic, lang, pages, template ("id:variant"), info:{univ,fac,dir,subj,name,group,teacher,city,year}}
    await m.answer(f"Qabul qilindi: {d['topic']} ({d['lang']}, {d['pages']} slayd)")
    # TODO: 1) Claude API bilan reja va matn  2) veb-qidiruv bilan manbalar
    #       3) rasmlar (Wikimedia/Unsplash)   4) python-pptx bilan .pptx yig'ish va yuborish

async def main():
    if not TOKEN or not WEBAPP_URL:
        raise RuntimeError("BOT_TOKEN va WEBAPP_URL muhit o'zgaruvchilari kiritilishi kerak.")
    await dp.start_polling(Bot(TOKEN))

if __name__ == "__main__":
    asyncio.run(main())
