import discord
from discord.ext import commands
import os
import keep_alive
import json
from discord.ext.commands import has_permissions, MissingPermissions


client = commands.Bot(command_prefix = ['/'], case_insensitive = True, intents = discord.Intents.all())


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_member_join(member):
  channel = client.get_channel(805221709854670898)
  embed = discord.Embed(title = "Welcome", description = f"Welcome ***{member.name}*** to {member.guild.name} , also visit our bot panel https://vzuniversesmm.com/ . Hope you have a great stay!", colour = 0x00c8ff)
  await channel.send(embed = embed)


@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
   client.load_extension(f'cogs.{extension}')
   await ctx.send('Succesfully loaded module')
   
@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
   client.unload_extension(f'cogs.{extension}')
   await ctx.send('Succesfully unloaded module')
  
@client.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
   client.reload_extension(f'cogs.{extension}')
   await ctx.send('Succesfully reloaded module')



keep_alive.keep_alive()
client.run(os.getenv("token"))
