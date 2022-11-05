
import discord, os, random, datetime
from discord import Color
from dotenv import load_dotenv
from discord.ext import commands
from showInfo import ShowInfo
from trivia import Database,Trivia,TriviaQuestion

# Load Token
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Setup Bot
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!',intents=intents)

# Load Our Info class for chosen show
officeInfo = ShowInfo('office')
RInfo = ShowInfo('R-IMPOSSIBLE')
data = Database('ranking.txt')
trivia_host = Trivia('general.txt')


# On Ready Test, tells us when online and server count
@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1

	print("Our Show Info Bot is in " + str(guild_count) + " guilds.")

# Message Sent Test
@bot.event
async def on_message(message):
    lowermessage = message.content.lower()
    if not message.author.bot and trivia_host.active_question:
        correct_answer_index = trivia_host.current_question.answer_index + 1
        if lowermessage == str(correct_answer_index):
            trivia_host.active_question = False
            data.increase_score(message.author.display_name)
            await message.channel.send(message.author.display_name + " is correct!\n" + trivia_host.current_question.get_correct_answer())
        else:
            await message.channel.send(message.author.display_name + " is wrong.")

    if "bad" in lowermessage:
        print("you said stuff")
        await message.delete()
    if "link" in lowermessage:
        embed = discord.Embed(title="[title]", url="https://www.google.com", 
        description="[description (optional)]", 
        color=Color.teal())
        await message.channel.send(embed=embed)
    await bot.process_commands(message)

# Command
@bot.command(name='office')
async def getOfficeInfo(ctx, *args):
    if len(args) >= 1:
        if args[0] == 'fact':
            fact = None
            if len(args) >= 2:
                fact = args[1]
            await ctx.send(officeInfo.getFact(fact))
        elif args[0] == 'quote':
            await ctx.send(officeInfo.getRandomQuote())
        elif args[0] == 'image':
            await ctx.send(file=discord.File(officeInfo.getRandomImage()))
        else:
            await ctx.send("Invalid Command Argument at [0]")
    else:
        await ctx.send("You need to add what you want 'quote', 'image', 'fact'")

# Command

@bot.command(name='rank')
async def getRank(ctx):
    response = "Current ranking: " + "\n"
    for record in data.records:
        response += str(record) + "\n"
    await ctx.send(response)

@bot.command(name='testrank')
async def getTestRank(ctx):
    author = ctx.author.display_name
    data.increase_score(author)
    await ctx.send(author + "Scored a point! ")


# Command
@bot.command(name='R-IMPOSSIBLE')
async def getRInfo(ctx, *args):
    if len(args) >= 1:
        if args[0] == 'fact':
            fact = None
            if len(args) >= 2:
                fact = args[1]
            await ctx.send(RInfo.getFact(fact))
        elif args[0] == 'quote':
            await ctx.send(RInfo.getRandomQuote())
        elif args[0] == 'image':
            await ctx.send(file=discord.File(RInfo.getRandomImage()))
        else:
            await ctx.send("Invalid Command Argument at [0]")
    else:
        await ctx.send("You need to add what you want 'quote', 'image', 'fact'")
@bot.command(name='time')
async def getTime(ctx): #greet user based on the curren time
    response = "Hello " + ctx.author.name + "Also known as " + ctx.author.display_name
    response += "Your account was created on " + str(ctx.author.created_at)
    response += "It is currently " + datetime.datetime.now().strftime("%H:%M:%S")
    await ctx.send(response)

# Spotify Test
@bot.command(name='track')
async def track(ctx, user: discord.Member = None):
    user = user or ctx.author
    print("Activites for", user.display_name,":")
    spotify_result = next((activity for activity in user.activities if isinstance(activity,discord.Spotify)),None)
    if spotify_result is None:
        await ctx.send(f'{user.name} is not listening to spotify.')
    else:
        await ctx.send(f'https://open.spotify.com/track/{spotify_result.track_id}')

# Trivia Test
@bot.command(name='trivia')
async def play_trivia(ctx):
    response = "Welcome to Trivia night! \n"
    trivia_host.random_question()
    response += trivia_host.current_question.get_question() + "\n"
    response += trivia_host.current_question.get_answers()
    await ctx.send(response)

bot.run(DISCORD_TOKEN)