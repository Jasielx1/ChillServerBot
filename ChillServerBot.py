#import needed libraries
import discord
import os
import requests
import json

client = discord.Client()

#define quote for zenquote api
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']
  return(quote)

@client.event
async def on_ready():
  print('Hola, esto funciona, soy: {0.user}!'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  #messages for users (spanish)
  if message.content.startswith('$klk'):
    await message.channel.send('Klk manito 🤪')

  if message.content.startswith('$minecraft'):
    await message.channel.send('⛏ El server de minecraft es **"chillserverdiscord.aternos.me"**')

  if message.content.startswith('$guia'):
    await message.channel.send('https://chillserver.rf.gd/Guia.html')

  if message.content.startswith('$logo'):
    await message.channel.send(file=discord.File('ChillServer.png'))

  if message.content.startswith('$cita'):
    quote = get_quote
    await message.channel.send(quote)

  if message.content.startswith('$web'):
    await message.channel.send('https://chillserver.rf.gd/')

  if message.content.startswith('$reglas'):
    await message.channel.send(file=discord.File('Reglas.jpg'))

  if message.content.startswith('$ayuda'):
    await message.channel.send('🔹 En `#comandos-del-bot` puedes ver cuales son mis comandos')

  if message.content.startswith('$help'):
    await message.channel.send('🔹 En `#comandos-del-bot` puedes ver cuales son mis comandos')
#get bot token
client.run(os.getenv('TOKEN'))
