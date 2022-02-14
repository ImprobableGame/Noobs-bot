# bot.py
import discord

#connection to discord

client = discord.Client()

@client.event

#This is for when the bot is ready to be used

async def on_ready():
  print('We have logged in as {0.user}
  '.format(client))

# bot sensing message

@client.event
async def on_message(message):
  if message.author == client.user:
    return

#if the message sent is a command

  if message.content.startswith(''):
    await message.channel.send('Baap ko bolta hai bc') 
