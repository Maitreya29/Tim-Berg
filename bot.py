import discord
from discord.ext import commands
from itertools import cycle
import random
import os



client = commands.Bot(command_prefix='.')

players = {}
 
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Avicii | By MaitreyaPatni29"))
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

@client.command(aliases=['8Ball','eightball','8ball'])
async def _8ball(ctx, *, question):
    responses= [' It is certain','It is decidedly so','Without a doubt.','Yes - definitely.','You may rely on it.','As I see it, yes.','Most likely','Outlook good.','Yes.','Signs point to yes','I dont think so, no.','My reply is no','I dont see that happening','I am sorry but, no.','Eh, no.']
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions()
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

@client.command(aliases=['leak','leakedsongs','leaks','Leak'])
async def Leaks(ctx):
    await ctx.author.send('https://mega.nz/#F!liIRUaSR!TjZVna3mHZWk6CRT3kiP2Q')
    await ctx.send('Check DMs, Link to all leaked songs sent to DMs. \n  This is the new set of leaks : https://media.discordapp.net/attachments/617859698875432968/666275268150820884/unknown.png?width=799&height=666 \n old leaks are also included in link.')

@client.command(aliases=['CurretBuys','currentBuys','Currentbuys','songBuys','SongBuys','Songbuys','songbuys'])
async def currentbuys(ctx):
    await ctx.send('Name: Avicii Public Buy◢◤ \n Currently buying: Nothing \n Invite link:https://discord.gg/tkXCnNA \n \n Name: Public Avicii Buy \n Currently buying: Avicii - I Want You feat. Aloe Blacc \n Invite link: https://discord.gg/KgHDcDq \n \n Name: Kygo Groupbuy \n Currently buying: Nothing \n Invite link: https://discord.gg/Vy2FBwx')

client.run(os.environ['TOKEN'])

