# Please follow me!!
# https://twitter.com/k_electory
import k_token, k_probably, k_help
import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="k_")

@bot.event
async def on_ready():
  print("Successfully logged in.\n")
  print("[Information]")
  print("Name: " + bot.user.name)
  print("Id: " + str(bot.user.id) + "\n")
  print("[System]")
  print("I'm Ready")

@bot.command()
async def electory(ctx):
  await ctx.send("Please follow me!!\nhttps://twitter.com/k_electory")

@bot.command()
async def probably(ctx):
  await ctx.send(k_probably.create(\
    random.randint(1,8), random.randint(1,8),\
    random.randint(1,8), random.randint(1,8)))

@bot.command()
async def faithfully(ctx):
  await ctx.send("ワン！！")

@bot.command()
async def emotionally(ctx, alias, id):
  await ctx.send("<:"+alias+":"+id+">")

@bot.command()
async def mimicry(ctx, *, words):
  await ctx.message.delete()
  await ctx.send(words)

@bot.command()
async def helpfully(ctx):
  await ctx.send(k_help.helpText())

@bot.command()
async def usefully(ctx):
  await ctx.send(k_help.helpText())

bot.run(k_token.login())

