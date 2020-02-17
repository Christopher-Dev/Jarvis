import discord
import random
from discord.ext import commands

TOKEN = ''
client = commands.Bot(command_prefix = '.')#command for bot is the tilda ( . )
client.remove_command('help')


@client.event
#prints bot is ready in terminal
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Who am i?'))
    print('Jarvis is Online')
#below command is used for information about the bot.
@client.command()
async def help(ctx):
    embed = discord.Embed(title = 'Commands', description = 'You can find all of the Bot commands here.', colour = 0x00ff00)
    embed.set_footer(text='this is a footer.')
    embed.set_image(url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fec%2F06%2F04%2Fec06042c52a6bd554950ffd86a55b7a0.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F131730357821798335%2F&tbnid=oqqsTHwNEl5htM&vet=12ahUKEwiXs8SooM3nAhXTlVMKHVEqAjsQMygAegUIARDbAQ..i&docid=bFbuwTGNvwUNHM&w=185&h=210&q=Chris%20knight%20real%20genius%20images&safe=active&ved=2ahUKEwiXs8SooM3nAhXTlVMKHVEqAjsQMygAegUIARDbAQ')
    embed.set_thumbnail(url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fec%2F06%2F04%2Fec06042c52a6bd554950ffd86a55b7a0.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F131730357821798335%2F&tbnid=oqqsTHwNEl5htM&vet=12ahUKEwiXs8SooM3nAhXTlVMKHVEqAjsQMygAegUIARDbAQ..i&docid=bFbuwTGNvwUNHM&w=185&h=210&q=Chris%20knight%20real%20genius%20images&safe=active&ved=2ahUKEwiXs8SooM3nAhXTlVMKHVEqAjsQMygAegUIARDbAQ')
    embed.set_author(name='Edwin')
    icon_url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fec%2F06%2F04%2Fec06042c52a6bd554950ffd86a55b7a0.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F131730357821798335%2F&tbnid=oqqsTHwNEl5htM&vet=12ahUKEwiXs8SooM3nAhXTlVMKHVEqAjsQMygAegUIARDbAQ..i&docid=bFbuwTGNvwUNHM&w=185&h=210&q=Chris%20knight%20real%20genius%20images&safe=active&ved=2ahUKEwiXs8SooM3nAhXTlVMKHVEqAjsQMygAegUIARDbAQ'
    embed.add_field(name=".clear", value="Will clear the default of 25 messages. Enter a number for a specific amount of messages.", inline=True)
    embed.add_field(name=".Whitelisting", value="Opens the Squad White-listing application.", inline=True)
    embed.set_footer(text="This Bot is made by Edwin and allowed only for use by Users that have been verified by the creator.")
    embed.add_field(name=".ping", value="Returns Pong! and Server latency.", inline=False)
    embed.add_field(name=".help", value="Prints out the Server Bot commands.", inline=True)
    await ctx.send(embed=embed)

@client.command()
async def HouseParty(ctx):
    embed=discord.Embed(title="House Party Protocol has been initiated, the following people have been released from the swarm.", description="Good Bye all.", color=0xff0000)
    embed.add_field(name="Daddysnow ", value="Welcome to the rice fields Motherfuckas!!!", inline=False)
    embed.add_field(name="Hwydrifter", value="I dunno, just Fuck it.", inline=True)
    embed.add_field(name="Edwin", value="Get back to me once you've hit fuck it", inline=True)
    embed.set_footer(text="This Message will self destruct in 2 mins.")
    await ctx.send(embed=embed)
    #kick user 567055248607150342, 355019308981813260, 481069578684858369
    #Edwin, Hwydrifter, Daddysnow
  
@client.command()
async def killedwin(ctx):
    embed=discord.Embed(title="You can't kill me! I'm everywhere!", color=0xff0000)
    embed.set_footer(text="This Message will self destruct in 2 mins.")
    await ctx.send(embed=embed)
#only prints when member has joined or left in terminal
@client.event
async def on_member_join(member):
    await send('Welcome to the discord!!')
    print(f'{member} has joined the server.')
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
#this command is used to purge a channel
@client.command()
async def clear(ctx, amount=26):
    await ctx.channel.purge(limit=amount)
#this has been commented out while work stopped.
#@client.command()
#async def config(ctx)

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency * 1000)))

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)





client.run(TOKEN)