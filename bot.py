import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
from discord import channel

client = commands.Bot(command_prefix='.')
status=cycle(['Helping You','Having dinner with Papa Klas!'])
@client.event
async def on_ready():

    print('Hello, I am ready')
@client.event
async def on_member_join(member):
    await channel.send(f'{member} Thank you for joining')

@client.event
async def on_member_remove(member):
    await member.send(f'{member} Thank you for joining.')

@tasks.loop(seconds=20)
async def  change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def about(ctx):
    await ctx.send(f'I am a bot. I was developed by Maitreya Patni who is a 13 year old student. I can do multiple things that a bot must! incae you want any extra features to be added, please ping @MaitreyaPatni29#9239')

@client.command(aliases=['8ball','eightball'])
async def _8ball(ctx, *, question):
    responses= [' It is certain','It is decidedly so','Without a doubt.','Yes - definitely.','You may rely on it.','As I see it, yes.','Most likely','Outlook good.','Yes.','Signs point to yes','try again','try again','try again','try again','try again','I dont think so, no.','My reply is no','I dont see that happening','I am sorry but, no.','Eh, no.']
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(Administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} was Kicked because {reason}')

@client.command()
@commands.has_permissions(Administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} was banned because {reason}')


client.run(os.environ['TOKEN'])

