import discord
import requests
import json
import helpMenu
import tensorflow as tf
import cv2
import os
import numpy as np


js = open('config.json')
data = json.load(js)

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


# Carregar modelo
model = tf.keras.saving.load_model("model/model_covid.h5")


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
            with open(file_name, "wb") as f:
                f.write(d_url.content)
                f.close()
                
    pic_ext = ['.jpg','.png','.jpeg']
    
    
    if message.author == client.user:
        return
    cmds = message.content.split(" ")
    #restrcit commands to specific channel of specific server
    if server_id == data['piserver_id']: 
        if channel_id == data['pichannel_id']:
            if "!help" in message.content or "!h" in message.content:
                await message.channel.send(helpMenu.help())
                return
            if "!explain" in message.content or "!e" in message.content:
                await message.channel.send("Este bot classifica imagens de radiografias de pulmão saudáveis ou com covid.")
                return
        if "!classify" in message.content or "!c" in message.content:
            if message.attachments == []:
                await message.channel.send('Não há imagem anexada') 
            for msg in message.attachments:
                for ext in pic_ext:
                    if file_name.endswith(ext):
                        image_size = (256, 256)
                        imagem = cv2.imread(file_name)
                        imagem = cv2.resize(imagem, image_size)
                        imagem = imagem.reshape((1,256,256,3))
                        imagem = tf.cast(imagem/255. ,tf.float32)
                        label = model.predict(imagem)
                        os.remove(file_name)
                        await message.channel.send(label[0][0])
                        k = int(label[0][0])
                        classes = ["Covid", "Saudável"]
                        await message.channel.send("Esta imagem corresponde a " + classes[k])
                        
    else:
        if "!help" in message.content or "!h" in message.content:
            await message.channel.send(helpMenu.help())
            return
        if "!explain" in message.content or "!e" in message.content:
            await message.channel.send("Este bot classifica imagens de radiografias de pulmão saudáveis ou com covid.")
            return
        if "!classify" in message.content or "!c" in message.content:
            if message.attachments == []:
                await message.channel.send('Não há imagem anexada') 
            for msg in message.attachments:
                for ext in pic_ext:
                    if file_name.endswith(ext):
                        image_size = (256, 256)
                        imagem = cv2.imread(file_name)
                        imagem = cv2.resize(imagem, image_size)
                        imagem = imagem.reshape((1,256,256,3))
                        imagem = tf.cast(imagem/255. ,tf.float32)
                        label = model.predict(imagem)
                        os.remove(file_name)
                        await message.channel.send(label[0][0])
                        k = int(label[0][0])
                        classes = ["Covid", "Saudável"]
                        await message.channel.send("Esta imagem corresponde a " + classes[k])
            
            
client.run(data['token'])