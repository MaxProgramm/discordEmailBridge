import discord
import tools
import json
import time

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

TOKEN = data["discord_bot"]["bot_token"]
channelName = data["discord_bot"]["bot_token"]

sender_mail = data["email"]["sender"]["address"]
sender_password = data["email"]["sender"]["password"]
receiver_mail = data["email"]["receiver"]["address"]

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message: discord.Message):
    if message.channel.name in channelName:
        pass
    tools.send_mail(sender_mail, sender_password, receiver_mail, message.channel.name, (f"{message.author}: {message.content}"))



client.run(TOKEN)
