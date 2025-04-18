import telebot
from flask import Flask, request

TOKEN = '8167272283:AAHWEBeN6aBFfDq1u4JXlElAq2yH29AI74s'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

EXCHANGE_RATE = 250  # سعر الصرف الثابت

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'ok', 200

@app.route('/')
def webhook_setup():
    bot.remove_webhook()
    bot.set_webhook(url='https://YOUR_RENDER_URL/' + TOKEN)
    return 'Webhook set!', 200

@bot.message_handler(commands=['temu'])
def convert_price(message):
    try:
        price_dzd = float(message.text.split()[1])
        price_usd = price_dzd / 135
        real_price_dzd = price_usd * EXCHANGE_RATE
        response = f"سعر Temu: {price_dzd:.2f} DZD\n"
        response += f"السعر الحقيقي: {real_price_dzd:.2f} DZD (على أساس {EXCHANGE_RATE} DZD/$)"
        bot.reply_to(message, response)
    except:
        bot.reply_to(message, "من فضلك أدخل السعر بعد الأمر /temu\nمثال: /temu 14000")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
