import discord
from random import choice

client = discord.Client()

insultos = [
        "introduce aqui los insultos que quieres añadir",
        ", insulto2",
        ", insulto3 ",  
    ]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('insulta a '): #10
                nombre = message.content[10:]  
                await message.channel.send(content =  nombre + choice(insultos), tts=True)


client.run('tokenbot')