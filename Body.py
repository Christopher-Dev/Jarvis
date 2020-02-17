import discord
import random
from discord.ext import commands
import Commands
import discord.utils 

TOKEN = ''
client = commands.Bot(command_prefix = '.')#command for bot is the tilda ( . )
client.remove_command('help')

@client.event
#prints bot is ready in terminal
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('How can i help you Sir?'))
    print('Jarvis is Online')
#below command is used for information about the bot.
@client.command()
async def help(ctx):
    embed = discord.Embed(title = 'Commands', description = 'You can find all of the Bot commands here.', colour = 0x00ff00)
    embed.set_footer(text='this is a footer.')
    embed.set_image(url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fec%2F06%2F04%2Fec06042c52a6bd554950ffd86a55b7a0.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F131730357821798335%2F&tbnid=oqqsTHwNEl5htM&vet=12ahUKEwiXs8SooM3nAhXTlVMKHVEqAjsQMygAegUIARDbAQ..i&docid=bFbuwTGNvwUNHM&w=185&h=210&q=Chris%20knight%20real%20genius%20images&safe=active&ved=2ahUKEwiXs8SooM3nAhXTlVMKHVEqAjsQMygAegUIARDbAQ')
    embed.set_thumbnail(url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fec%2F06%2F04%2Fec06042c52a6bd554950ffd86a55b7a0.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F131730357821798335%2F&tbnid=oqqsTHwNEl5htM&vet=12ahUKEwiXs8SooM3nAhXTlVMKHVEqAjsQMygAegUIARDbAQ..i&docid=bFbuwTGNvwUNHM&w=185&h=210&q=Chris%20knight%20real%20genius%20images&safe=active&ved=2ahUKEwiXs8SooM3nAhXTlVMKHVEqAjsQMygAegUIARDbAQ')
    embed.set_author(name='Jarvis')
    icon_url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fec%2F06%2F04%2Fec06042c52a6bd554950ffd86a55b7a0.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F131730357821798335%2F&tbnid=oqqsTHwNEl5htM&vet=12ahUKEwiXs8SooM3nAhXTlVMKHVEqAjsQMygAegUIARDbAQ..i&docid=bFbuwTGNvwUNHM&w=185&h=210&q=Chris%20knight%20real%20genius%20images&safe=active&ved=2ahUKEwiXs8SooM3nAhXTlVMKHVEqAjsQMygAegUIARDbAQ'
    embed.add_field(name="@clear", value="Will clear the default of 25 messages. Enter a number for a specific amount of messages.", inline=True)
    embed.add_field(name="@Whitelisting", value="Opens the Squad White-listing application.", inline=True)
    embed.set_footer(text="This Bot is made by Edwin and allowed only for use by Users that have been verified by the creator.")
    embed.add_field(name="@ping", value="Returns Pong! and Server latency.", inline=False)
    embed.add_field(name="@help", value="Prints out the Server Bot commands.", inline=True)
    await ctx.send(embed=embed)

@client.command()
async def HouseParty(ctx):
    embed=discord.Embed(title="House Party Protocol has been initiated, the following people have been released from the swarm.", description="Good Bye all.", color=0xff0000)
    embed.add_field(name="Daddysnow ", value="Welcome to the rice fields Motherfuckas!!!", inline=False)
    embed.add_field(name="Hwydrifter", value="I dunno, just Fuck it.", inline=True)
    embed.add_field(name="Edwin", value="Get back to me once you've hit fuck it", inline=True)
    embed.set_footer(text="This Message will self destruct in 2 mins.")
    await ctx.send(embed=embed)
    #Edwin#4323, Hwydrifter#8173, Daddysnow#7904
  
@client.command()
async def killedwin(ctx, amount=2):
    embed=discord.Embed(title="You can't kill me! I'm everywhere!", color=0xff0000)
    embed.set_footer(text="This Message will self destruct in 2 mins.")
    await ctx.channel.purge(limit=amount)
    await ctx.send(embed=embed)
#only prints when member has joined or left in terminal
@client.event
async def on_member_join(ctx):
    embed=discord.Embed(title="Welcome to the Jarvis Dev Server", description="Enter .help in the Jarvis channel for info on the commands.", color=0x00ff00)
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSEg1KbS2iNOL_jYT5XHZ8161fx5AeAzgah-eHmkCNnhGuJYDVi")
    await ctx.send(embed=embed)
    
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
#this command is used to purge a channel
@client.command()
async def clear(ctx, amount=26):
    await ctx.channel.purge(limit=amount)
    embed=discord.Embed(title="I have cleared up to the last 25 messages for you sir", color=0x00ff00)
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSEg1KbS2iNOL_jYT5XHZ8161fx5AeAzgah-eHmkCNnhGuJYDVi")
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency * 1000)))

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
#This command is used for asking for help  
@client.command()
async def welcome(ctx, member: discord.Member, *, content):
    embed=discord.Embed(title="Welcome to the Jarvis Dev Server", description="Enter $help in the Jarvis channel for info on the commands.", color=0x00ff00)
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSEg1KbS2iNOL_jYT5XHZ8161fx5AeAzgah-eHmkCNnhGuJYDVi")
    await ctx.send(embed=embed)
    channel = await member.create_dm()
    await channel.send(content)


@client.command(pass_context=True)
async def add(ctx, user: discord.Member, role: discord.Role):#adds the role, format of .add Edwin#0000 <ROLE>
    await user.add_roles(role)  
async def remove(ctx, user: discord.Member, role: discord.Role):#adds the role, format of .add Edwin#0000 <ROLE>
    await user.remove_roles(role)



@client.command()
async def commandlist(ctx):
    embed=discord.Embed(title="Welcome to Jarvis Dev Command", description="All commands are Prefixed by a period  . ", color=0x00ff00)
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSEg1KbS2iNOL_jYT5XHZ8161fx5AeAzgah-eHmkCNnhGuJYDVi")
    embed.add_field(name="Adding a Role", value=".add jarvis#0000 role", inline=True)
    embed.add_field(name="Removing a Role", value=".remove jarvis#0000 role", inline=True)
    embed.add_field(name="Ping", value=".ping", inline=True)
    embed.add_field(name="Help", value=".help", inline=True)
    embed.add_field(name="Welcome", value=".welcome", inline=True)
    embed.add_field(name="Purge", value=".clear 25", inline=True)
    await ctx.send(embed=embed)










client.run(TOKEN)