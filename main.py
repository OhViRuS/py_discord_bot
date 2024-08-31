import discord

intents = discord.Intents.default()
intents.message_content = True

#token =
client = discord.client(intents=intents)

@client.event
async def on_ready():
    print(f"labas as esu online")


#client.run(token)

