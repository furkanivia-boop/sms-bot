import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

# .env dosyasından TOKEN'i al
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Katılma isteği geldiğinde tetiklenen fonksiyon
async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    user_id = user.id

    # Butonlar
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📁 Grup Videolarım 👅", url="https://t.me/kanal1")],
        [InlineKeyboardButton("🎥 Ünlüyle Sızan Video 💦", url="https://t.me/kanal2")],
        [InlineKeyboardButton("🔓 Ücretsiz Arşivim", url="https://t.me/kanal3")],
        [InlineKeyboardButton("🎬 Özel İçerikler", url="https://t.me/kanal4")],
        [InlineKeyboardButton("👀 En Çok İzlenen Video", url="https://t.me/kanal5")],
        [InlineKeyboardButton("🔥 Bugünlük Özel Video", url="https://t.me/kanal6")],
        [InlineKeyboardButton("📦 2GB Arşiv", url="https://t.me/kanal7")],
        [InlineKeyboardButton("🤫 Şifreli Videolar", url="https://t.me/kanal8")],
        [InlineKeyboardButton("🚫 Yasaklı Görüntüler", url="https://t.me/kanal9")],
        [InlineKeyboardButton("💌 Talep ve Sohbet Hattı", url="https://t.me/kanal10")]
    ])

    try:
        with open("video.mp4", "rb") as video:
            await context.bot.send_video(
                chat_id=user_id,
                video=video,
                caption="📸 İFŞA VİDEOLARIM AŞAĞIDA. TIKLA, GİR 💦👇",
                reply_markup=keyboard
            )
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Uygulama başlat
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(handle_join_request))
app.run_polling()
