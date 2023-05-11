import discord
import requests
import json
import urllib.request
import tarfile
import helpMenu


js = open('config.json')
data = json.load(js)

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    
    print("message-->", message)
    print("message content-->", message.content)
    print("message attachments-->", message.attachments)
    print("message id", message.author.id)
    print("channel id", message.channel.id)
    print("server id", message.guild.id)
    
    server_id = int(message.guild.id)
    channel_id = int(message.channel.id)
    a_id = message.author.id
    if a_id != data['token']:
        for x in message.attachments:
            print("attachment-->",x.url)
            d_url = requests.get(x.url)
            file_name = x.url.split('/')[-1]
            #code to save the file locally
            #with open(file_name, "wb") as f:
                #f.write(d_url.content)
    pic_ext = ['.jpg','.png','.jpeg']
    
    
    if message.author == client.user:
        return
    
    cmds = message.content.split(" ")
    if "!help" in message.content or "!h" in message.content:
        await message.channel.send(helpMenu.help())
        return
    if "!classify" in message.content or "!c" in message.content:
        if server_id == data['piserver_id']:
            if channel_id == data['pichannel_id']:
                if message.attachments == []:
                    await message.channel.send('Não há imagem anexada')
                for msg in message.attachments:
                    for ext in pic_ext:
                        if file_name.endswith(ext):
                            await message.channel.send('Imagem: ' + file_name)
        else:
            if message.attachments == []:
                await message.channel.send('Não há imagem anexada')    
            for msg in message.attachments:
                for ext in pic_ext:
                    if file_name.endswith(ext):
                        await message.channel.send('Imagem: ' + file_name)  

                          
      
client.run(data['token'])