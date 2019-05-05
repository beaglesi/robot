import time
import discord
client = discord.Client()
@client.event
async def on_ready():
    print('{0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!'):
        time.sleep(2)
        await message.channel.send(message.content[1:])
    if message.content.startswith('hello'):
        time.sleep(2)
        await message.channel.send('hi '+str(message.author)[:-5])
    if message.content.startswith('be excellent'):
        await message.channel.send('party on dudes!')
    if message.content.startswith('Be excellent'):
        await message.channel.send('party on dudes!')
    elif message.content.startswith('stop'):
        await message.channel.send('grugger')
client.run('NTcwNjIzOTk2MTY1NjE5NzEz.XMB75w._2AD2nfVicR1bTcxfrM4JieHAkM')