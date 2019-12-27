import discord
from discord.ext import commands
import random
import os
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Hello, I am ready')
@client.event
async def on_member_join(member):
    print(f'{member} has joined')
@client.event
async def on_member_remove(member):
    print(f'{member} has left')
@client.command()
async def about(ctx):
    await ctx.send(f'I am a bot. {round(client.latency *1000)} ms is the latency')
@client.command(aliases=['8ball','eightball'])
async def _8ball(ctx, *, question):
    responses= [' It is certain','It is decidedly so','Without a doubt.','Yes - definitely.','You may rely on it.','As I see it, yes.','Most likely','Outlook good.','Yes.','Signs point to yes','try again','try again','try again','try again','try again','I dont think so, no.','My reply is no','I dont see that happening','I am sorry but, no.','Eh, no.']
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')
client.run(os.environ[TOKEN])

