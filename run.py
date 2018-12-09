import os
from dotenv import load_dotenv,find_dotenv
import discord

load_dotenv(find_dotenv())

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("<:okokokay:"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            m = "https://drive.google.com/uc?authuser=0&id=1zwQ2pkqlgMk4nQGEdLKX6LG8p5n8cfWH&export=download"
            await client.send_message(message.channel, m)

    if message.content.startswith("<:dx_kowai:"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            m = "https://drive.google.com/uc?authuser=0&id=1dTd6iInoBTNeljiseanCBeephKkiRQJ3&export=download"
            await client.send_message(message.channel, m)

    if message.content.startswith("<:aikatsu_tbcss:"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            m = "https://drive.google.com/uc?authuser=0&id=1wky3TXWVrD3SzNOU6u4aUlLtoeX-fzA7&export=download"
            await client.send_message(message.channel, m)

    if message.content.startswith("<:aikatsu_not_odayaka:"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            m = "https://drive.google.com/uc?authuser=0&id=1i3yRK5pYG5KW7o2IA9kWTOHUNOi4SxxQ&export=download"
            await client.send_message(message.channel, m)

    if message.content.startswith("<:aikatsu_aasouiukotoka:"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            m = "https://drive.google.com/uc?authuser=0&id=1PZJYW2voXxKvRMhQWyEChJpno6IXQ5op&export=download"
            await client.send_message(message.channel, m)

    if message.content.startswith("<:noja_yaranakereba:"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            m = "https://drive.google.com/uc?authuser=0&id=1ANCTItSnqAzKCP8cxfZEAaB-0xxNzGjb&export=download"
            await client.send_message(message.channel, m)

API_KEY= os.environ.get("API_KEY")
client.run(API_KEY)
