import os

import telebot
from dotenv import load_dotenv
from convert import text_to_speech, speech_to_text


load_dotenv()
bot = telebot.TeleBot(os.getenv("API_TOKEN"))


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, text="Пришлите текстовое или голосовое сообщение")


@bot.message_handler(content_types=["text"])
def tts(message):
    text = message.text
    text_to_speech(text)
    with open("text_to_speech.mp3", "rb") as f:
        bot.send_voice(message.chat.id, f)


@bot.message_handler(content_types=["voice"])
def stt(message):
    file = bot.get_file(message.voice.file_id)
    bts = bot.download_file(file.file_path)
    with open("voice.ogg", "wb") as f:
        f.write(bts)
    text = speech_to_text()
    bot.send_message(message.chat.id, text=text)


bot.infinity_polling(none_stop=True)
