from discord.ext import commands, tasks
import os
import FonctionDB as FDB
import FonctionBot as FB

nameClasses = ["francais", "anglais", "dev"]
nameOptionClasses = ["all", "slam", "sisr"]

# The signe for the command
client = commands.Bot(command_prefix="$")

#Loop every minute
@tasks.loop(minutes=1) 
async def change_status():
  rep = FB.everyTime()
  if rep != None:
    channel = client.get_channel(904425955399958619)
    await channel.send(rep)

#When the bot is connect to discord and ready
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  change_status.start()# Start the tasks loop

#--------------------------------------------------------------------

# If command hi is detected
@client.command()
async def hi(ctx):
    await ctx.send("hi")

#--------------------------------------------------------------------

# If command add is detected it add the homework
@client.command()
async def add(ctx, subject, date_end, groupe, *,work): # , *,word : take every word not juste the first 
    reply = FB.botAdd(subject, date_end, groupe, work)
    await ctx.send(reply)

#--------------------------------------------------------------------

#if command get is detected
@client.command()
async def get(ctx, element):
    if element.lower() in nameClasses:
        info = FB.botGetWithSubject(element.lower())
    else:
        info = FB.botGetWithDate(element.lower())

    await ctx.send(info)

#--------------------------------------------------------------------

#No env
client.run("OTA0NDIwOTE5MzQ1MjkxMjk1.YX7Rng._xy7t7M2vNwWFzdl3i8DgLMd1IQ")
#env
#client.run(os.getenv('TOKEN'))