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
