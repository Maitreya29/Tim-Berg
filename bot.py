import discord
from discord.ext import commands
from itertools import cycle
import random
import os
from discord import channel
import asyncio
import youtube_dl


client = commands.Bot(command_prefix='.')
censored=['PAB']

players = {}
 
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Dinner with Papa Klas"))
    print('Hello, I am ready')
@client.event
async def on_member_join(member):
    await channel.send(f'{member} Thank you for joining')

@client.event
async def on_member_remove(member):
    await member.send(f'{member} Thank you for joining.')


@client.command()
async def about(ctx):
    await ctx.send(f'I am a bot. I was developed by Maitreya Patni who is a 13 year old student. I can do multiple things that a bot must! incae you want any extra features to be added, please ping @MaitreyaPatni29#9239')

@client.command(aliases=['8ball','eightball'])
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

@client.command()
async def helpme(ctx):
    await ctx.send("Here is a list of commands currently Available \nyou can use .8ball (question) to use the 8 ball command.\nsample: .8ball am I gay?\nOutput: 8Ball replies with a random message\nyou can use .clear  to delete the last 6 messages.\nsample: .clear \noutput: last 6 messages are deleted \n(optional: you can add a value after .clear to delete a certain number of messages.\nsample: .clear 20 \noutput: This deletes last 20 messages\nyou can use .kick to kick a user.\nsample: .kick @xyz#6976 I don't like you \noutput: User is kicked, Bot prints '@xyz#6967 was kicked because I don't like you' \nyou can use .ban to ban a user. \nsample: .ban @xyz#6976 I don't like you \noutput: User is banned, Bot prints '@xyz#6967 was banned because I don't like you')")

@client.command(aliases=['bmm','Bmm'])
async def BMM(ctx):
    await ctx.author.send('BMM - https://dbree.org/v/39ec8b')
    await ctx.send('Check DM, link to Beat My Meat sent!')

#connect command
@client.command(pass_context=True)
async def connect(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    await client.say("Connected!")

#disconnect command
@client.command(pass_context=True)
async def disconnect(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    await client.say("Disconnected, Thanks for using me!")

#play command
@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()
    await client.say("Now Playing: " +(url))

#pause command
@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()
    await client.say("Audio output has been paused! :pause_button:")

#resume commands
@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()
    await client.say("Audio output has been resumed! :play_pause:")

#stop command
@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()
    await client.say("Audio output has been stopped! :stop_button:")

client.run(os.environ['TOKEN'])

