import discord
from discord.ext import commands
from itertools import cycle
import random
import os
from discord import channel
import asyncio
import youtube_dl


client = commands.Bot(command_prefix='.')
censored=['Indian Kebab','IndianKebab','Indian kebab','indiankebab']

players = {}
 
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Dinner with Papa Klas"))
    print('Hello, I am ready')
@client.event
async def on_member_join(member):
    await member.send(f'{member} Thank you for joining')

@client.event
async def on_member_remove(member):
    await member.send(f'{member} Sad to see you go.')


@client.command()
async def about(ctx):
    await ctx.send(f'I am a bot. I was developed by Maitreya Patni who is a 13 year old student. I can do multiple things that a bot must! incae you want any extra features to be added, please ping @MaitreyaPatni29#9239')

@client.command(aliases=['8Ball','eightball'])
async def _8ball(ctx, *, question):
    responses= [' It is certain','It is decidedly so','Without a doubt.','Yes - definitely.','You may rely on it.','As I see it, yes.','Most likely','Outlook good.','Yes.','Signs point to yes','I dont think so, no.','My reply is no','I dont see that happening','I am sorry but, no.','Eh, no.']
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=6):

    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(manage_messages=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'@{member} was Kicked because {reason}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'@{member} was banned because {reason}')

@client.command(aliases=['bmm','Bmm'])
async def BMM(ctx):
    await ctx.author.send('BMM - https://dbree.org/v/39ec8b')
    await ctx.send('Check DM, link to Beat My Meat sent!')

@client.command(aliases=['leak','leakedsongs'])
async def Leaks(ctx):
    await ctx.author.send('https://mega.nz/#F!liIRUaSR!TjZVna3mHZWk6CRT3kiP2Q')
    await ctx.send('Checks DM, Link to all leaked songs sent to DMs.')

client.run(os.environ['TOKEN'])

