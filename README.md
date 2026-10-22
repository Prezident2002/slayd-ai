# SlaydAI: mustaqil ish taqdimoti Mini App

## Tarkibi
- `webapp/index.html` — Mini App interfeysi (bitta fayl, HTML+CSS+JS). Telegram WebApp skripti ulangan.
- `bot/bot.py` — aiogram 3 bot skeleti (Mini App'ni ochadi, ma'lumotni qabul qiladi).

## Oqim
1. Universitet (to'liq nomi, fakultet, yo'nalish) → yo'nalish aniqlanadi
2. Mavzu, til (uz/ru/en), slaydlar soni
3. Shablon: mavzu va OTM profiliga mos yo'nalishning 6 varianti + boshqa yo'nalishlar (jami 16)
4. Titul ma'lumotlari (fan, F.I.Sh., guruh, o'qituvchi, shahar, yil)
5. Reja: Kirish, 3 bo'lim, Xulosa, Foydalanilgan adabiyotlar → yaratish

## Ishga tushirish
1. `webapp/` papkasini HTTPS hostingga joylang (GitHub Pages, Netlify, Vercel).
2. BotFather'da bot yarating, tokenni `bot/bot.py` ga yozing, `WEBAPP_URL` ni qo'ying.
3. `pip install aiogram && python bot/bot.py`

## Botga yuboriladigan JSON
{"topic","lang","pages","template":"arch:2","info":{"univ","fac","dir","subj","name","group","teacher","city","year"}}
Eslatma: `sendData` faqat klaviatura tugmasi (ReplyKeyboard) orqali ochilgan Mini App'da ishlaydi va Mini App'ni yopadi.

## Hali qilinmagan (keyingi bosqich)
- Claude API: reja va bo'lim matnlari
- Veb-qidiruv: ishonchli manbalar, adabiyotlar ro'yxati (GOST/APA), faqat haqiqatan topilgan havolalar
- Rasmlar: Wikimedia Commons / Unsplash (litsenziyasi ochiq)
- .pptx generatsiyasi: python-pptx, har yo'nalishga 5-10 ta o'z shablonimiz
- Shablon tanlash: hozir kalit so'zlar bo'yicha, keyin Claude tahlili
