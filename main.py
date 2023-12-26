import os
import discord
from dotenv import load_dotenv
from twitter import verificar_twitter_periodico, mensaje_de_prueba # Importar la función desde twitter.py
from discord.ext import commands 

# Load variables from .env
load_dotenv()

# Get variables from .env
whitelist = list(map(int, os.getenv('WHITELIST').split(',')))
twitter_channel = int(os.getenv('TWITTER_CHANNEL'))
bot_token = os.getenv('BOT_TOKEN')
ultimo_tweet = os.getenv('ULTIMO_TWEET')  
USER_TWITTER = os.getenv('USER_TWITTER')  
ROLE = os.getenv('ROLE')  
ALLOWED_GUILD_ID = int(os.getenv('ALLOWED_GUILD_ID'))

Variables = [ultimo_tweet, USER_TWITTER, ROLE, twitter_channel]


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "!", intents=intents)


@bot.command()
async def set_twitter_account(ctx, new_user):
    if ctx.author.guild_permissions.administrator and bot.get_guild(ALLOWED_GUILD_ID):
        Variables[1] = new_user
        Variables[0] = ""
        await ctx.send(f'Updated Twitter account to: {Variables[1]}')
    else:
        await ctx.send("You don't have permission to use this command.")

@bot.command()
async def set_role(ctx, new_role):
    if ctx.author.guild_permissions.administrator and bot.get_guild(ALLOWED_GUILD_ID):
        try:
            role = await commands.RoleConverter().convert(ctx, new_role)
        except commands.BadArgument:
            # If it's not a mention or a valid role name, treat it as a string
            role = new_role
        
        Variables[2] = str(role)
        await ctx.send(f'Updated Role to: {Variables[2]}')
    else:
        await ctx.send("You don't have permission to use this command.")

@bot.command()
async def set_channel(ctx, channel: discord.TextChannel):
    # 'channel' is a discord.TextChannel object, and you can access its ID
    channel_id = channel.id
    Variables[3] = channel_id
    await ctx.send(f"The new channel where the tweets will be sent is ({channel.mention}), ID: {channel_id}")


@bot.command()
async def test_command(ctx):
    if ctx.author.guild_permissions.administrator and bot.get_guild(ALLOWED_GUILD_ID):
        await mensaje_de_prueba(ctx, bot, Variables)
    else:
        await ctx.send("You don't have permission to use this command.")


@bot.event
async def on_ready():
    global Variables
    allowed_guild = bot.get_guild(ALLOWED_GUILD_ID)
    if allowed_guild:
        bot.loop.create_task(verificar_twitter_periodico(bot, Variables))
    else:
        print(f'Bot is not in the allowed guild. Exiting...')
        await bot.close()



bot.run(bot_token) # Change <bot-token> with the bot token
