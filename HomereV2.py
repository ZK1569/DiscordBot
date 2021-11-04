from discord.ext import commands, tasks
import os
import FonctionDB as FDB
import FonctionBot as FB
import datetime

nameClasses = ["francais", "anglais", "dev"]
nameOptionClasses = ["all", "slam", "sisr"]

# The signe for the command
client = commands.Bot(command_prefix="$")

@tasks.loop(seconds=60) # Do some thing every X seconde
async def change_status():
  channel = client.get_channel(904425955399958619)
  now = datetime.datetime.now()
  current_time = now.strftime("%H:%M")

  if current_time == '16:22':
    await channel.send('il est lheure')
    print("now")

#When the bot is connect to discord 
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  change_status.start()# Start the tasks loop

# If command hi is detected
@client.command()
async def hi(ctx):
    await ctx.send("hi")

# If command add is detected it add homework
@client.command()
async def add(ctx, subject, date_end, groupe, *,work): # , *,word : take every word not juste the first 
    reply = FB.botAdd(subject, date_end, groupe, work)
    await ctx.send(reply)

@client.command()
async def get(ctx, element):
  if element.lower() in nameClasses:
    info = FB.botGetWithSubject(element.lower())
  else:
    info = FB.botGetWithDate(element.lower())
    
  await ctx.send(info)

#*****



#******
#No env
client.run("OTA0NDIwOTE5MzQ1MjkxMjk1.YX7Rng._xy7t7M2vNwWFzdl3i8DgLMd1IQ")
#env
#client.run(os.getenv('TOKEN'))