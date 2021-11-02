import discord
from discord.ext import commands
import os
import FonctionDB as FDB

# The signe for the command
client = commands.Bot(command_prefix="$")

#When the bot is connect to discord 
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#if command $hello is detected
@client.command()
async def hello (ctx, arg):
    await ctx.send(arg)

# If command hi is detected
@client.command()
async def hi(ctx):
    await ctx.send("hi")

# If command add is detected
@client.command()
async def add(ctx, subject, date_end, *,work): # , *,word : take every word not juste the first 
    
    
    #Verifier le bon nombre de commande pour pas qu'il plante 
    #et que donc les gens complaitent le bon nombre d'options


    # List of all the subject autorised by the bot
    lsSubjects = ["francais", "anglais", "dev"]

    # If the command send by the user is correct 
    if subject.lower() in lsSubjects:
        # Add to database and send a message
        success = FDB.addHomeWork(subject, date_end, work)
        if success:
            await ctx.send("Devoir de {} ajouté pour le {}".format(subject, date_end))
        else:
            await ctx.send("ERREUR : La date incorrect.")
    else:
        await ctx.send("ERREUR : La matiere n'est pas reconnu.")


#No env
client.run("OTA0NDIwOTE5MzQ1MjkxMjk1.YX7Rng._xy7t7M2vNwWFzdl3i8DgLMd1IQ")
#env
#client.run(os.getenv('TOKEN'))