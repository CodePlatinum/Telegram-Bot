import telebot
from datetime import datetime
import random

TOKEN = '7666674896:AAG95S_eVb4T6ytNZac9C_04x786UgvSJOM'
bot = telebot.TeleBot('7666674896:AAG95S_eVb4T6ytNZac9C_04x786UgvSJOM')


tems_to_study = [
    "Tkinter", "CustomTkinter", "Функції в Python", "Як зробити вікно у Python"
]


Week_days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привіт, я бот Майкл 😃')

@bot.message_handler(commands=['learn'])
def send_learn(message):
    today_date = datetime.now().strftime("%Y-%m-%d")
    weekday = Week_days[datetime.now().weekday()]
    tema_for_study = random.choice(tems_to_study)
    bot.reply_to(message, f"Сьогодні: {today_date}\nДень тижня: {weekday}\nСьогодні тобі треба буде вивчати тему: {tema_for_study}")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Зараз я маю команди /start, /learn і /help')


bot.polling()
