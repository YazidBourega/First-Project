import telebot

TOKEN = '8167272283:AAHWEBeN6aBFfDq1u4JXlElAq2yH29AI74s'
bot = telebot.TeleBot(TOKEN)

EXCHANGE_RATE = 250  # سعر الصرف الثابت

@bot.message_handler(commands=['temu'])
def convert_price(message):
    try:
        price_dzd = float(message.text.split()[1])
        price_usd = price_dzd / 135  # السعر الرسمي التقريبي
        real_price_dzd = price_usd * EXCHANGE_RATE
        response = f"سعر Temu: {price_dzd:.2f} DZD\n"
        response += f"السعر الحقيقي: {real_price_dzd:.2f} DZD (على أساس {EXCHANGE_RATE} DZD/$)"
        bot.reply_to(message, response)
    except:
        bot.reply_to(message, "من فضلك أدخل السعر بعد الأمر /temu\nمثال: /temu 14000")

bot.polling()