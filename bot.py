import telebot
import random
import time
import datetime
import os

# Lee el token desde la variable de entorno
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Lista de juegos disponibles
juegos = ["🎰 Tragamonedas", "🚀 Aviator", "💣 Mines", "⚽ Penalty", "🍔 Burger Whim", "🎹 Piano Tiles", "🗼 La Torre"]

# Estrategias de ejemplo
estrategias = [
    "🔁 Usa la técnica de duplicar la apuesta solo 2 veces.",
    "🕒 Juega solo entre las 2:00 PM y 4:00 PM, mejor probabilidad.",
    "🔍 Observa 3 rondas sin apostar y luego entra.",
    "💸 Retírate después de 3 victorias seguidas.",
]

# Predicciones automáticas simples
def generar_prediccion():
    juego = random.choice(juegos)
    resultado = random.choice(["Alta probabilidad de ganar", "Riesgo medio", "Mejor evitar por ahora"])
    hora = datetime.datetime.now().strftime("%H:%M")
    return f"🔮 Predicción para {juego} a las {hora}:\n➡️ {resultado}"

# Mensaje de bienvenida
@bot.message_handler(commands=['start', 'ayuda'])
def enviar_bienvenida(message):
    bot.reply_to(message, f"""🎰 Hola {message.from_user.first_name}, soy tu bot de confianza para ganar en estas apuestas. 
Prepárate para recibir señales, predicciones y estrategias para los juegos de casino virtuales.

Usa estos comandos:
👉 /estrategia – para una estrategia útil
👉 /prediccion – para una predicción en tiempo real
👉 /senal – para una señal automática
""")

# Comando para enviar una estrategia aleatoria
@bot.message_handler(commands=['estrategia'])
def enviar_estrategia(message):
    estrategia = random.choice(estrategias)
    bot.reply_to(message, f"📊 Estrategia de hoy:\n{estrategia}")

# Comando para enviar una predicción
@bot.message_handler(commands=['prediccion'])
def enviar_prediccion(message):
    pred = generar_prediccion()
    bot.reply_to(message, pred)

# Comando para enviar una señal aleatoria
@bot.message_handler(commands=['senal'])
def enviar_senal(message):
    juego = random.choice(juegos)
    bot.reply_to(message, f"📡 Señal de entrada:\nJuega ahora {juego} con responsabilidad. ¡Es tu momento de ganar!")

# Inicia el bot
print("Bot activo...")
bot.infinity_polling()
