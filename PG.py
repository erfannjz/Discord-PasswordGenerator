from discord import Activity , ActivityType , Embed
from discord.ext import commands
from datetime import datetime
from random import shuffle , choice
from typing import Union

class CONFIG:
    PREFIX = 'g'
    TOKEN = ''
    COLORS = [0xFF0000 , 0xFF7F00 , 0xFFFF00 , 0x00FF00 , 0x0000FF , 0x2E2B5F , 0x8B00FF]
    ALPHABET = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    NUMBERS = list('1234567890')
    SYMBOLS = list('!@#$%^&*()_+~=[]}{:;/<>-')

bot = commands.Bot(command_prefix = CONFIG.PREFIX , help_command = None , case_insensitive = None)


@bot.event
async def on_ready():
    await bot.change_presence(activity = Activity(type = ActivityType.watching , name = 'ghelp command!'))
    print(datetime.today().replace(microsecond=0) ,'\n\nBot is online\nDeveloped by ErfanNJZ')

# @bot.event
# async def on_command_error(ctx , error):
#     pass

@bot.command(aliases = ['pass'])
async def password(ctx , type , length : Union[int]):
    if type == 'lvl1' and 5 <= length <= 16 :
        shuffle(CONFIG.ALPHABET)        
        await ctx.send(''.join(CONFIG.ALPHABET[:length]))

    elif type == 'lvl2' and 5 <= length <= 16 :
        spass = CONFIG.ALPHABET + CONFIG.NUMBERS
        shuffle(spass)
        await ctx.send(''.join(spass[:length]))

    elif type == 'lvl3' and 5 <= length <= 16 :
        spass = CONFIG.ALPHABET + CONFIG.NUMBERS + CONFIG.SYMBOLS
        shuffle(spass)
        await ctx.send(''.join(spass[:length]))
    else:
        await ctx.send(f'{ctx.author.mention}  \nNote that we have only three levels: `lvl1` , `lvl2` , `lvl3` , and length must be between `5` and `16`')
  
@bot.command()
async def help(ctx):
    embed = Embed(title = 'Help' , colour = choice(CONFIG.COLORS) , description = 
    """
    Send command with this formation:
        `Command Levels length`

    Command:
        `gpass` or `gpassword`

    Levels:
        lvl1 = `Alphabet`
        lvl2 = `Alphabet + Numbers`
        lvl3 = `Alphabet + Numbers + Symbols`

    length: 
        `Your password length in number between 5 and 16`
    """)
    await ctx.send(ctx.author.mention , embed = embed)


bot.run(CONFIG.TOKEN)