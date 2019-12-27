import discord
from discord.ext import commands
import random
import os
from discord import channel

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Hello, I am ready')
@client.event
async def on_member_join(member):
    await channel.send(f'{member} Thank you for joining')

@client.event
async def on_member_remove(member):
    await member.send(f'{member} Thank you for joining.')

@client.command()
async def about(ctx):
    await ctx.send(f'I am a bot. {round(client.latency *1000)} ms is the latency')

@client.command(aliases=['8ball','eightball'])
async def _8ball(ctx, *, question):
    responses= [' It is certain','It is decidedly so','Without a doubt.','Yes - definitely.','You may rely on it.','As I see it, yes.','Most likely','Outlook good.','Yes.','Signs point to yes','try again','try again','try again','try again','try again','I dont think so, no.','My reply is no','I dont see that happening','I am sorry but, no.','Eh, no.']
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount):
    await ctx.channel.purge(limit=amount)

client.run(os.environ['TOKEN'])

