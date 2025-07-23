import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "AQUÍ_VA_TU_TOKEN_DEL_BOT"
admin_id = 123456789  # Reemplaza con tu ID de Telegram si quieres recibir notificaciones

# Juegos disponibles
juegos = {
    "slots": ["🍒", "🔔", "💎", "🍋", "7️⃣"],
    "penalty": ["Izquierda", "Centro", "Derecha"],
    "mines": ["💣", "💎"],
    "aviator": ["Sube", "Baja"],
    "burgerwim": ["🍔", "🍟", "🥤"],
    "latorre": ["⬆️", "⬇️"],
    "pianotiles": ["🟦", "⬛", "⬜"]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎰 Bienvenido al Bot Predictor de Casino Virtual.\n"
        "Usa /predecir seguido del nombre del juego para recibir una señal.\n"
        "Ejemplo: /predecir slots"
    )
async def predecir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Por favor, escribe el nombre del juego. Ejemplo:\n/predecir slots")
        return

    juego = context.args[0].lower()
    if juego not in juegos:
        await update.message.reply_text(f"Juego no reconocido. Los juegos disponibles son:\n{', '.join(juegos.keys())}")
        return

    señal = random.choice(juegos[juego])
    await update.message.reply_text(f"🎲 Señal para {juego}: {señal}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predecir", predecir))

    print("🤖 Bot corriendo... Ctrl+C para detener.")
    app.run_polling()

if __name__ == '__main__':
    main()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎰 Bienvenido al bot predictor de casino.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
