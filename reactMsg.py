import discord
import requests
import json

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

    for msg in message.attachments:
        for ext in pic_ext:
            if file_name.endswith(ext):
                await message.channel.send('Imagem: ' + file_name)    

"""     if message.content.startswith('hi'):
        await message.channel.send('Hello!')
 
    if message.content.startswith('image'):
        await message.channel.send(file=discord.File('download.jpg'))
 
    if message.content.startswith('video'):
        await message.channel.send(file=discord.File('sample-mp4-file-small.mp4'))
 
    if message.content.startswith('audio'):
        await message.channel.send(file=discord.File('file_example_MP3_700KB.mp3'))
 
    if message.content.startswith('file'):
        await message.channel.send(file=discord.File('sample.pdf')) """
 
        
client.run(data['token'])