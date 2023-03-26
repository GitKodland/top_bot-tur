from ayarlar import ayarlar
import discord
# import * - kütüphanedeki tüm dosyaları içe aktarmanın hızlı bir yoludur
from bot_mantik import *

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
ayricaliklar = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
ayricaliklar.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
istemci = discord.Client(intents=ayricaliklar)


# Bot hazır olduğunda adını yazdıracak!
@istemci.event
async def on_ready():
    print(f'{istemci.user} olarak giriş yaptık')


# Bot bir mesaj aldığında, aynı kanalda mesaj gönderecek!
@istemci.event
async def on_message(message):
    if message.author == istemci.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Selam! Ben bir botum!')
    elif message.content.startswith('$smile'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('$coin'):
        await message.channel.send(yazi_tura())
    elif message.content.startswith('$pass'):
        await message.channel.send(sifre_olusturucu(10))
    else:
        await message.channel.send("Bu komutu anlayamadım :(")

istemci.run(ayarlar["TOKEN"])
