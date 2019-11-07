
# Bryan the Bird

Discord bot with various features

## Beta branch 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements (listed in requirements.txt)

```bash
pip install -U -r requirements.txt
```

## Requirements
[Python 3.6 or higher](https://www.python.org/downloads/release/python-360/)

Then cd into the unzipped folder and run the pip command from above
Next create a config.py and copy the exact text from the text below[do not leave anything blank]
Then run bot.py how ever you want and you should be all set

If you plan on using the query function for Minecraft servers make sure you enable query and have it configured to the correct port in your server properties this feature only works on servers 1.7+. Status only needs the ip but can not provide as much information as query. 

## Config


```python
token = 'token'
server = 'server ip'

```
coords.txt is where your coords get written to, if this file is deleted the command will not function and the bot may crash, to solve this just create coords.txt again in the same directory as bot.py


## Resources 

[Discord Py GitHub Page](https://github.com/Rapptz/discord.py)

[Discord Embed Generator](https://cog-creators.github.io/discord-embed-sandbox/)

[Discord Py Documentation](https://discordpy.readthedocs.io/en/latest/index.html)

## Example command

```py
@bot.command()
async def Test (ctx):
    embed=discord.Embed(title="Addresses", description="All 5 of the gang members Addresses ", color=0xeee657)
    embed.add_field(name="test", value="embed 1", inline=False)
    embed.add_field(name="test", value="embed 2", inline=True)
    embed.add_field(name="test", value="embed 3", inline=True)
    embed.add_field(name="test" , value="embed 4", inline=True)
    embed.add_field(name="test", value="embed 5", inline=True)
    await ctx.send(embed=embed)
```

Here is an example list embed I created, it is incuded with the bot, you can create similar ones with the [embed creator](https://cog-creators.github.io/discord-embed-sandbox/).

To embed a link:
```py
 embed = discord.Embed(title="hyperlinked text", url="the link", description="description under or next to link" , color="yourcolor"
```

To set a thumbnail
```py
embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/f/f3/Erithacus_rubecula_with_cocked_head.jpg")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
