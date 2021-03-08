import asyncio
import discord
import random

f = open("token.txt", "r")
TOKEN = f.read()
client = discord.Client()

key = "Hello"

@client.event
async def on_message(message):  # bulk of command handling
    if message.content.startswith('!hello') :
        #key = 'Hello {0.author.mention}'
        msg = ('-' * len(key)).format(message)
        sent_message = await message.channel.send(msg)
        for i in range(len(key) + 1) :
            new_message = (key[:i] + '-' * (len(key) - i)).format(message)
            await sent_message.edit(content=new_message)
            await asyncio.sleep(0.5)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    msg = "!hello"
    await client.change_presence(activity=discord.Activity(name=msg,type=discord.ActivityType.playing))

client.run(TOKEN)
