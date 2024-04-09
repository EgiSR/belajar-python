# import telebot
# from telebot import types

# api = '6078766022:AAEr9umxk29ZhfjhfJa3A4KWHzYxGpaMzfo'
# bot = telebot.TeleBot(api)

import datetime as dt

print("Masukkan tanggal lahir anda")

tahun = int(input("tahun \t\t: "))
bulan = int(input("bulan \t\t: "))
tanggal = int(input("tanggal \t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"hari lahir anda adalah {tanggal_lahir:%A}")
