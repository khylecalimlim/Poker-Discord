from discord.ext import commands
import random

bot = commands.Bot(command_prefix = '!')

# Idea function
@bot.command(name = "idea", help = " - Get a side project idea")
async def idea(ctx):
    await ctx.send("Ideas are hard")
    await ctx.send("Worry not, I think you should...")

    topics = ['chat bot', 'cli', 'game', 'web bot', 'browser extention', 'api', 'web interface']
    areas = ['note taking', 'social life', 'physical fitness', 'mental health', 'pet care']
    languages = ['Java', 'JavaScript', 'C', 'C#', 'Rust', 'C++', 'Python', 'Ruby', 'R']

    idea = f'Create a new {random.choice(topics)} that helps with {random.choice(areas)} using {random.choice(languages)}! :slight_smile:'
    await ctx.send(idea)

# Calculator function
@bot.command(name = "calc", help = " - Perform a calculation where fn is either +, -, *, / or **")
async def calc(ctx, x: float, fn: str, y: float):
    x = float(x)
    y = float(y)
    if fn == '+':
        await ctx.send(x + y)
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '/':
        await ctx.send(x / y)
    elif fn == '**':
        await ctx.send(x ** y)
    else:
        await ctx.send("We only support 4 function operations")

# make sure to create a token file (in real life use env variables)
with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)
