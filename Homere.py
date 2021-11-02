import discord
import os
import FonctionDB as FDB

client = discord.Client()


#Connection to Discord
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#When someone send a message 
@client.event
async def on_message(message):
    #Varaible to not have to tip every time message.content
    msg = message.content
    #If the message is frome himself
    if message.author == client.user:
        return

    #If the message start with a a special word
    if msg.startswith('$hi'):
        #Send a message to the channel 
        await message.channel.send('Hello')

    if msg.startswith('$add'):
        print (len(msg.split())-1)
        encouraging_message = msg.split("$add ",1)[1]
        #call the fonction update_encouragements
        rep = FDB.addHomeWork(encouraging_message)
        await message.channel.send(rep)





#No env
client.run("OTA0NDIwOTE5MzQ1MjkxMjk1.YX7Rng._xy7t7M2vNwWFzdl3i8DgLMd1IQ")
#nev
#client.run(os.getenv('TOKEN'))