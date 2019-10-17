import discord
from discord.ext import commands
import json
import aiohttp
import random
import urllib.parse, urllib.request, re
from mcstatus import MinecraftServer
import config


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def brozart(ctx):
    await ctx.send(file=discord.File('brozart.jpg'))

@bot.command()
async def coord(ctx):
    with open('coords.txt') as f:
        await ctx.send(f.read())




# @bot.command()
# async def serverinvite(ctx):
#   await ctx.send('invite link: (your server invite)')



@bot.event
async def on_message(message):
    with open("users.json", "r") as f:
        users = json.load(f)

        if message.author.bot:
            return
        else:
            await update_data(users, message.author)
            number = random.randint(5,10)
            await add_experience(users, message.author, number)
            await level_up(users, message.author, message.channel)

        with open("users.json", "w") as f:
            json.dump(users, f)
    await bot.process_commands(message)

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]["experience"] = 0
        users[user.id]["level"] = 1

async def add_experience(users, user, exp):
    users[user.id]["experience"] += exp

async def level_up(users, user, channel):
    experience = users[user.id]["experience"]
    lvl_start = users[user.id]["level"]
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await ctx.send_message(channel, f":tada: Congrats {user.mention}, you levelled up to level {lvl_end}!")
        users[user.id]["level"] = lvl_end




@bot.command()
async def coords(ctx, xCoord: str, yCoord: str, zCoord: str, nameCoord: str = None):
    if not xCoord or not yCoord or not zCoord or not nameCoord:
        await ctx.send(ctx.message.author.mention + ' You are missing some information.\nFormat: ?coords x y z name')
        return
    try:      
        await ctx.send("You submitted {} located at {},{},{}".format(nameCoord, xCoord, yCoord, zCoord))
        with open('coords.txt','a') as f:
           f.write(f'{xCoord} {yCoord} {zCoord} {nameCoord}\n')
    except Exception as e:
        print(e)
        await ctx.send("Something went wrong.")




@bot.command()
async def Test (ctx):
    embed=discord.Embed(title="your title", description="your discription ", color=0xeee657)
    embed.add_field(name="test", value="embed 1", inline=False)
    embed.add_field(name="test", value="embed 2", inline=True)
    embed.add_field(name="test", value="embed 3", inline=True)
    embed.add_field(name="test" , value="embed 4", inline=True)
    embed.add_field(name="test", value="embed 5", inline=True)
    await ctx.send(embed=embed)

bot.remove_command('invite')

@bot.command()
async def invite(ctx):
    
    embed = discord.Embed(title="Invite Link", url="(put your discord bot link here)", description="Here you can invite me to your server", color=0xeee657)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/f/f3/Erithacus_rubecula_with_cocked_head.jpg")
    embed.add_field(name="Requirements", value="(put the requirements you want to allow your bot)", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def server(ctx):
        
    server = MinecraftServer.lookup('stankyleg.us.to')
    status = server.status()
    
    await ctx.send("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))


@bot.command()
async def reqcoord(ctx, *, search):
    with open('coords.txt') as f:
        for line in f:
            if line.endswith(f'{search}\n'):
                await ctx.send(line)
                break
            
        else:
                
                await ctx.send("No Coords Have Been Recorded Of That Location")


@bot.command()
async def giphy(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=API_KEY_GOES_HERE')
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=API_KEY_GOES_HERE&limit=10')
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    data = json.loads(await response.text())
    await session.close()

    await ctx.send_message(embed=embed)
   
@bot.command(pass_context=True)
async def youtube(ctx, *search):
    searchTerm = ' '.join(search)
    query_string = urllib.parse.urlencode({'search_query': searchTerm})
    htm_content = urllib.request.urlopen('https://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])


if __name__ == '__main__':
    import config
    bot.run(config.token)

