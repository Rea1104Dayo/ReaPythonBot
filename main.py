import os
import platform
import discord
import os.path
import sys
import asyncio
import random, string

from discord import *
from discord.ext import commands
from discord.utils import get
from discord.ui import View,select,Button,Modal,TextInput
from discord_buttons_plugin import *
from datetime import datetime
from dotenv import load_dotenv
from colorama import Fore, init
init()
S = Fore.RESET
w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
lc = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
M = Fore.MAGENTA
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
W = Fore.WHITE
Y = Fore.YELLOW
C = Fore.CYAN
emojilist="๐","๐ฉ","โ","๐","๐","๐ฐ","๐"
now_time=datetime.now().__format__("%Y/%m/%d %H:%M:%S")
os.system("title BOT")
count=0
load_dotenv()
youtube=os.getenv("Youtube_bundle_name")
twitter=os.getenv("twitter_id")
admin=os.getenv("Admin")
prefix=os.getenv("prefix")
SupportServer=os.getenv("Support_server")
paths=os.path.dirname(os.path.realpath(__file__))
bot=commands.Bot(command_prefix="RPB!", help_command=None, intents=discord.Intents.all())
buttons=ButtonsClient(bot)
@bot.tree.command(name=f"slot",description=f"ใใใฒใผใ : slotใๅฎ่กใใพใ")
async def slot(ctx: discord.Interaction):
    ็ตๆ1=random.choice(emojilist)
    ็ตๆ2=random.choice(emojilist)
    ็ตๆ3=random.choice(emojilist)
    embed=Embed(title=f"็ตๆ",description=f"`{็ตๆ1}{็ตๆ2}{็ตๆ3}`",color=discord.Color.yellow())
    msg=await ctx.channel.send(embed=embed)
    if ็ตๆ1 + ็ตๆ2 + ็ตๆ3 == ็ตๆ1*3:
         embed=Embed(title=f"็ตๆ",description=f"`{็ตๆ1}{็ตๆ2}{็ตๆ3}`\n{ctx.author.name} ใใใๅฝใใใงใ๏ผ",color=discord.Color.green()) #ใใใใใฉใใชใใใใใ
    else:
         embed=Embed(title=f"็ตๆ",description=f"`{็ตๆ1}{็ตๆ2}{็ตๆ3}`\n{ctx.author.name} ใใใๅคใใงใ๏ผ",color=discord.Color.red())
    await msg.edit(embed=embed)
@bot.event
async def on_ready():
  os.system("cls")
  servers=bot.guilds
  print(f"{G}----------------------------------------")
  print(f"{R}Bot Info")
  print(f"{R}Bot Name : {bot.user.name}")
  print(f"{R}Bot id ๏ผ{bot.user.id}")
  print(f"{R}Bot Status : /help๏ฝCreated By @j9wx")
  print(f"{R}Joined Server : {servers} [{len(servers)}]")
  print(f"{G}----------------------------------------")
  print(f"{B}python Info")
  print(f"{B}discord Version ๏ผ{discord.__version__}")
  print(f"{B}Python Version ๏ผ{str(platform.python_version())}")
  print(f"{G}----------------------------------------")
  Synced=await bot.tree.sync()
  print(f"{C}{len(Synced)}ๅใฎใณใใณใใๅๆใใพใใ")
  print(f"{G}----------------------------------------"+ S + f"")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"/help๏ฝCreated By @j9wx"))
bot_startedtime=datetime.now().__format__("%Y/%m/%d %H:%M:%S")
@bot.command()
async def bot_run_time(ctx):
   await ctx.send(f"{bot_startedtime}ใใ่ตทๅไธญ") 
@bot.tree.command(name=f"nitrogen",description=f"nitroGen")
@app_commands.describe(counts="nitroใ็ๆใใๆฐ")
async def gen(ctx: discord.Interaction, counts:int):
  i=0
  if counts>101:
    counts=100
  while int(i)<int(counts):
    Nitro="https://discord.gift/"+random.choice(string.ascii_letters)+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(17))
    count=i
    count+=1
    i=count
    print(Fore.BLUE+f"\n{i}"+G+"/"+Fore.RED+f"{counts}\n\n"+Fore.LIGHTBLUE_EX+"ๅฎ่ก่ "+S+"> "+G+f"{ctx.user.name}")
    deleted=await ctx.channel.send(Nitro + f"\n{i}/{counts}\nๅฎ่ก่ > {ctx.user.name}")
    if i>counts-1:
      print(S+f"\nNitroGenใ็ตไบใใพใใ"+Fore.BLACK+"-"+Fore.BLUE+f"{i}"+G+"/"+Fore.RED+f"{counts}"+S+","+Fore.LIGHTBLUE_EX+"ๅฎ่ก่ "+S+"> "+G+f"{ctx.user.name}")
      deleted2=await ctx.channel.send(f"NitroGenใ็ตไบใใพใใ-{i}/{counts}, ๅฎ่ก่ > {ctx.user.name}")
      await asyncio.sleep(50)
      await deleted.delete
      await deleted2.delete()
      await ctx.response.send_message("ALL COMPLETED",ephemeral=True)

@bot.tree.command(name=f"ping",description=f"pingใ่กจ็คบใใพใ")
async def ping(ctx: discord.Interaction):
  raw_ping=bot.latency
  ping=round(raw_ping * 1000)
  embed=Embed(title=f"Ping! {ping}ms", description=f"{bot.user.name}ใฎPingใฏ{ping}msใงใ๏ผ๏ผ", color=discord.Color.brand_green())
  await ctx.response.send_message(embed=embed,ephemeral=True)
  print(f"ๅฎ่ก่ | {ctx.user.name} | {prefix}pingใไฝฟ็จใใใพใใ"+G +f""+G +f"\n----------------------------------------"+ S + f""+ S + f"")


@bot.tree.command(name=f"botๆฆ่ฆ",description=f"botใฎๆฆ่ฆใ่กจ็คบใใพใ")
async def info(ctx: discord.Interaction):
    embed=Embed(title=f"{bot.user.name} : {bot.user.id}", description="pythonใงไฝๆใใใdiscord botใงใใ", color=0xeee657)
    embed.add_field(name=f"ๅฎ่ก่", value=f"{ctx.user.name}")
    embed.add_field(name=f"ไฝๆ่", value=f"{admin}")
    embed.add_field(name=f"ๅฐๅฅๆฐ", value=f"{len(bot.guilds)}")
    embed.add_field(name=f"botๆๅพ", value=f"ใชใณใฏใฏ[ใใกใ](https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot%20applications.commands)")
    embed.add_field(name=f"ใตใใผใใตใผใใผ", value=f"ๆๅพใชใณใฏใฏ[ใใกใ]({SupportServer})")
    dele_=await ctx.response.send_message(embed=embed)
    dele=await buttons.send(
      channel=ctx.channel.id,
            components=[
                ActionRow([
                    Button(
                        label="ๆๅพใฏใใกใ", 
                        style=ButtonType().Link, 
                        url=f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot%20applications.commands"
                    )
                ])
            ]
        )
    await asyncio.sleep(120)
    await dele.delete()
    await dele_.delete()
@bot.tree.command(name=f"setup",description=f"่จญๅฎใใฆใชใใฃใใไฝฟใฃใฆใใ ใใ")
@app_commands.default_permissions(administrator=True)
async def setup(ctx: discord.Interaction):
    for channel in ctx.guild.channels:
     await channel.delete()
    for role in ctx.guild.roles:
     if role.name != "@everyone":
      if role.name != "ReaPythonBot":
       await role.delete()
    # ๅฝน่ทใจๆจฉ้ใฎ่จญๅฎ
    role_settings = {
        "*": ("default", ["administrator"]),
        "**": ("default", ["administrator"]),
        "***": ("default", ["administrator"]),
        "****": ("default", ["administrator"]),
        "*****": ("default", ["administrator"]),
        "Owner": ("default", ["administrator"]),
        "Admin": ("gold", ["administrator"]),
        "Staffs": ("white", ["view_channel", "manage_webhooks", "manage_roles", 
                            "read_message_history", "send_messages", "embed_links", 
                            "attach_files", "use_external_emojis", "add_reactions", 
                            "mention_everyone", "manage_messages", "manage_threads"]),
        "Bot": ("purple", []),
        "่ช่จผ": ("green", [])
    }
    
    # ใใฃใณใใซใฎใซใใดใชใผ่จญๅฎ
    category_settings = {
        "้่ฆ": {"๐ข๏ฝใ็ฅใใ": "่ช่จผ", "โ ๏ฝใซใผใซ": "everyone"},
        "่ช่จผ": {"๐ญ๏ฝ้่ซ": "่ช่จผ", "โ๏ฝ่ณชๅ": "่ช่จผ"},
        "็ฎก็่": {"๐ญ๐๏ฝ็ฎก็่้่ซ": "็ฎก็่", "โ๐๏ฝ็ฎก็่่ณชๅ": "็ฎก็่"}
    }
    
    # ใซใใดใชใผไฝๆ
    for category_name in category_settings.keys():
        category_overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True, manage_channels=True)
        }
        category = await ctx.guild.create_category(category_name, overwrites=category_overwrites)
        
        # ใใฃใณใใซไฝๆ
        for channel_name, channel_roles in category_settings[category_name].items():
            channel_overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                ctx.guild.me: discord.PermissionOverwrite(read_messages=True, manage_channels=True)
            }
            for role_name in channel_roles.split(","):
                if role_name in role_settings:
                    role = discord.utils.get(ctx.guild.roles, name=role_name)
                    if role is not None:
                        for permission_name in role_settings[role_name][1]:
                            setattr(channel_overwrites, permission_name, True)
                
            channel = await ctx.guild.create_text_channel(channel_name, overwrites=channel_overwrites, category=category)
    for role_name in ["*", "**", "***", "****", "*****", "Owner", "Admin", "Staffs", "่ช่จผ"]:
     role = await ctx.guild.create_role(name=role_name, color=discord.Colour(role_settings[role_name][0]))
     if role_settings[role_name][1]:
        for permission_name in role_settings[role_name][1]:
            permission = getattr(discord.Permissions(), permission_name)
            await role.edit(permissions=permission, reason="Setting up roles and permissions")
            await ctx.user.add_roles(role, reason="Setting up roles and permissions")

@bot.tree.command(name=f"ๅ็ๆ",description=f"ใใฃใณใใซใๅ็ๆใใพใ")
async def nuke(ctx: discord.Interaction):
    channel=ctx.channel
    msg=Embed(title="ๅ็ๆใฎ้็ฅ", description="ใใฃใณใใซใฎๅ็ๆใๅฎไบใใพใใใ")
    msg.set_footer(text=f"ๅฎ่ก่ | {ctx.user.name}ใป{now_time}", icon_url=ctx.user.avatar.url)
    channel2=await channel.clone()
    await channel2.edit(position=channel.position)
    await channel.delete()
    delll=await channel2.send(embed=msg)
    await asyncio.sleep(120)
    await delll.delete()
    return
@bot.tree.command(name=f"test",description=f"test")
@app_commands.default_permissions(administrator=True)
async def TEST(ctx: discord.Interaction):
  await ctx.response.send_message(content="interaction!",embed=None,ephemeral=True)
  await ctx.followup.send(content="webhook!",embed=None,ephemeral=True)
@bot.tree.command(name=f"ใใฟใใ",description=f"ใใฟใใใใใพใ")
async def omikuji(ctx: discord.Interaction):
  result=["ๅคงๅ", "ไธญๅ", "ๅฐๅ", "ๅถ", "ๅฐๅถ"]
  msg1=await ctx.response.send_message(f"{ctx.user.mention}ใใใฎใใฟใใใฎ็ตๆใฏ...   ")
  for i in range(5):
    await msg1.edit(content=f"{ctx.user.mention}ใใใฎใใฟใใใฎ็ตๆใพใง ใใจ{5-i}็ง")
    await asyncio.sleep(1)
  await msg1.edit(content=f"{ctx.user.mention}ใใใฎใใฟใใใฎ็ตๆใฏ  **" + random.choice(result) + "**  ใงใใ")

@bot.tree.command(name=f"help",description=f"helpใ่กจ็คบใใพใ")
@app_commands.describe(page="้ใใใผใธใ ็กใใ ใฃใใ1")
async def help(ctx: discord.Interaction, page: int=None):
    buttonlist=["โ","โฎ๏ธ","โช","โฌ๏ธ","โก๏ธ","โฉ","โญ","๐๏ธ"]
    if page==None:
      page=1
    if not page==None:
      page-=1
    counts=page
    page1=Embed(title=f"help - {bot.user.name}",description=f"ใใผใธ1 - ็ฎๆฌก",color=0x000000)
    page1.add_field(name=f"ใใผใธ1 - ็ฎๆฌก",value="ใใฎใกใใปใผใธใ่กจ็คบใใใ")
    page1.add_field(name=f"ใใผใธ2 - funใณใใณใ",value="ใฒใผใ ใณใใณใใ่กจ็คบใใใ")
    page1.add_field(name=f"ใใผใธ3 - Basicใณใใณใ",value="ๆจฉ้็กใใงใงใใใณใใณใใ่กจ็คบใใใ")
    page1.add_field(name=f"ใใผใธ4 - moderateใณใใณใ",value="ใขใใฌใผใฟใผๅฐ็จใฎใณใใณใใ่กจ็คบใใใ")
    page1.add_field(name=f"ใใผใธ5 - ๅฎฃไผ",value="ไฝๆ่ใฎๅฎฃไผ")
    page1.add_field(name=f"ใใผใธ6 - botใฎๆฆ่ฆ",value="botใฎ่ชฌๆ")
    page1.set_footer(text=f"ใใผใธ 1/6ใปๅฎ่ก่ | {ctx.user.name} : 5ๅ้ๆไฝใใชใใฃใใๅ้คใใใพใใป{now_time}",icon_url=ctx.user.avatar.url)
    page2=Embed(title=f"help - {bot.user.name}",description=f"ใใผใธ2 - Fun",color=0x000000)
    page2.add_field(name=f"{prefix}ใใฟใใ",value="ใใฟใใ")
    page2.add_field(name=f"{prefix}ในใญใใ", value="ในใญใใ")
    page2.set_footer(text=f"ใใผใธ 2/6ใปๅฎ่ก่ | {ctx.user.name} : 5ๅ้ๆไฝใใชใใฃใใๅ้คใใใพใใป{now_time}",icon_url=ctx.user.avatar.url)
    page3=Embed(title=f"help - {bot.user.name}",description=f"ใใผใธ3 - Basic",color=0x000000)
    page3.add_field(name=f"{prefix}help ",value="helpใ่กจ็คบใใ")
    page3.add_field(name=f"{prefix}serverinfo", value="ใตใผใใผใฎๆๅ ฑใ่กจ็คบใใ")
    page3.add_field(name=f"{prefix}userinfo", value="ใฆใผใถใผใฎๆๅ ฑใ่กจ็คบใใ")
    page3.add_field(name=f"{prefix}say",value="botใซใกใใปใผใธใ้ไฟกใใใ")
    page3.add_field(name=f"{prefix}ping",value="pingใ่กจ็คบ")
    page3.add_field(name=f"{prefix}ใชใขใฏใทใงใณใซใฆใณใฟใผ",value="ๆๅฎใใใใกใใปใผใธใฎใชใขใฏใทใงใณๆฐใๅๅพใใพใ")    
    page3.set_footer(text=f"ใใผใธ 3/6ใปๅฎ่ก่ | {ctx.user.name} : 5ๅ้ๆไฝใใชใใฃใใๅ้คใใใพใใป{now_time}",icon_url=ctx.user.avatar.url)
    page4=Embed(title=f"help - {bot.user.name}",description=f"ใใผใธ4 - Moderation")
    page4.add_field(name=f"{prefix}purge", value="ใกใใปใผใธใๅ้คใใ - ใกใใปใผใธใฎ็ฎก็")
    page4.add_field(name=f"{prefix}kick", value="ใฆใผใถใผใkick - ใฆใผใถใผใ็ฎก็(KICK)")
    page4.add_field(name=f"{prefix}ban", value="ใฆใผใถใผใban - ใฆใผใถใผใ็ฎก็(BAN)")
    page4.add_field(name=f"{prefix}unban", value="ใฆใผใถใผใฎbanใ่งฃ้ค - ใฆใผใถใผใ็ฎก็(BAN)")
    page4.set_footer(text=f"ใใผใธ 4/6ใปๅฎ่ก่ | {ctx.user.name} : 5ๅ้ๆไฝใใชใใฃใใๅ้คใใใพใใป{now_time}",icon_url=ctx.user.avatar.url)
    page5=Embed(title=f"ๅฎฃไผ - {bot.user.name}",description=f"ใใผใธ5 - ไฝๆ่")
    page5.add_field(name=f"youtube",value=f"youtubeใขใซใฆใณใใฏ[ใใกใ](https://www.youtube.com/@{youtube})",inline=False)
    page5.add_field(name=f"twiiter",value=f"ใใคใใฟใผใขใซใฆใณใใฏ[ใใกใ](https://twitter.com/{twitter})",inline=False)
    page5.add_field(name=f"bot github",value=f"botใฎใฌใใธใใชใฏ[ใใกใ](https://github.com/Rea1104Dayo/ReaPythonBot)",inline=False)
    page5.set_footer(text=f"ใใผใธ 5/6ใปๅฎ่ก่ | {ctx.user.name} : 5ๅ้ๆไฝใใชใใฃใใๅ้คใใใพใใป{now_time}",icon_url=ctx.user.avatar.url)
    page6=Embed(title=f"botใฎๆฆ่ฆ - {bot.user.name}",description=f"ใใผใธ6 - ๆฆ่ฆ")
    page6.add_field(name=f"่ฃฝไฝ่",value=f"{admin}")
    page6.add_field(name=f"botใฎๆฆ่ฆ",value="ไฝๆ่ใ่ถฃๅณใงไฝๆใใฆใใbotใงใใ")
    page6.set_footer(text=f"ใใผใธ 6/6ใปๅฎ่ก่ | {ctx.user.name} : 5ๅ้ๆไฝใใชใใฃใใๅ้คใใใพใใป{now_time}",icon_url=ctx.user.avatar.url)
    question=Embed(title=f"Question - {bot.user.name}",description=f"ใใผใธQuestion - Question")
    question.add_field(name=f"Question",value=f"""
โ: ใใฎใใผใธใซใใใ
โฎ๏ธ: ใใผใธใ3ๅๆปใใ
โช: ใใผใธใ2ๅๆปใใ
โฌ๏ธ: ใใผใธใ1ๅๆปใใ
โก๏ธ: ใใผใธใ1ๅ้ฒใใใ
โฉ: ใใผใธใ2ๅ้ฒใใใ
โญ: ใใผใธใ3ๅ้ฒใใใ
๐๏ธ: helpใๅ้คใใใ

helpใไฝฟใฃใฆใใใฆใใใใจใใใใใพใใ
""")
    question.set_footer(text=f"ใใผใธ Question/6ใปๅฎ่ก่ | {ctx.user.name} : 5ๅ้ๆไฝใใชใใฃใใๅ้คใใใพใใป{now_time}",icon_url=ctx.user.avatar.url) 
    embed_list=[page1,page2,page3,page4,page5,page6,question]
    embed=await ctx.channel.send(embed=embed_list[counts])
    embeds=Embed(title=f"helpใไฝๆใใพใใ!",description=f"ๅฟ็ญใ5ๅ้ใชใใฃใๅ ดๅใใใฎใกใใปใผใธใๅ้คใใพใ!",color=discord.Color.green()).set_footer(text=f"ๅฎ่ก่ | {ctx.user.name}",icon_url=ctx.user.avatar.url)
    await ctx.response.send_message(embed=embeds,ephemeral=True)
    for button in buttonlist:
      await embed.add_reaction(button)
    while True:
          try:
             reaction, user=await bot.wait_for("reaction_add",timeout=300,check=lambda reaction, user: user==ctx.user and reaction.emoji in buttonlist)
          except asyncio.TimeoutError:
             await embed.delete()
             await ctx.followup.send(embed=Embed(title=f"Deleted Help - {bot.user.name}, {ctx.user.name}",description=f"Helpใๅ้คใใใพใใ",color=discord.Color.red()).set_footer(text=f"ๅฎ่ก่ | {ctx.user.name}",icon_url=ctx.user.avatar.url), ephemeral=True)
             return
          else:
            preview_pages=counts
            if reaction.emoji=="โฌ๏ธ":
                counts -=1
            elif reaction.emoji=="โก๏ธ":
                counts +=1
            elif reaction.emoji=="โช":
                counts -=2
            elif reaction.emoji=="โฉ":
                counts +=2
            elif reaction.emoji=="โฎ๏ธ":
                counts -=3
            elif reaction.emoji=="โญ":
                counts +=3
            elif reaction.emoji=="๐๏ธ":
                await embed.delete()
                await ctx.followup.send(embed=Embed(title=f"Deleted Help - {bot.user.name}, {ctx.user.name}",description=f"Helpใๅ้คใใใพใใ",color=discord.Color.red()).set_footer(text=f"ๅฎ่ก่ | {ctx.user.name}",icon_url=ctx.user.avatar.url), ephemeral=True)
            elif reaction.emoji=="โ":
                counts = 6
            await embed.remove_reaction(reaction, user)
            if counts !=preview_pages:
              await embed.edit(embed=embed_list[counts])

@bot.tree.command(name=f"poll",description=f"ใขใณใฑใผใใใใ")
@app_commands.describe(message=f"ใกใใปใผใธ",ๅ็ญ=f"1็ช็ฎใฎ้ธๆ่ข",ๅ็ญ2=f"2็ช็ฎใฎ้ธๆ่ข")
async def poll(ctx: discord.Interaction, message:str, ๅ็ญ:str,ๅ็ญ2:str):
  Number="1","2","3","4","5","6","7","8","9"
  Answer1=0
  Answer2=0
  poll_id=random.choice(Number)+"".join(random.choice(Number) for _ in range(14))
  embed=Embed(title=f"{message}", description=f"1๏ธโฃ : {ๅ็ญ}\n2๏ธโฃ : {ๅ็ญ2}",color=0x000000)  
  embed.set_footer(text=f"ๅฎ่ก่ | {ctx.user.name}ใปPOLL id : {poll_id}", icon_url=ctx.user.avatar.url)
  msg=await ctx.channel.send(embed=embed)
  created=Embed(title=f"ไฝๆใใพใใ๏ผ", description="ใขใณใฑใผใใไฝๆใใพใใ๏ผ", color=discord.Color.blue())
  created.add_field(name=f"ใกใใปใผใธ",value=f"{message}")
  created.add_field(name=f"ๅ็ญ1",value=f"{ๅ็ญ}")
  created.add_field(name=f"ๅ็ญ2",value=f"{ๅ็ญ2}")
  await ctx.response.send_message(embed=created, ephemeral=True)
  reactionlist=["1๏ธโฃ","2๏ธโฃ"]
  await msg.add_reaction("1๏ธโฃ")
  await msg.add_reaction("2๏ธโฃ")

@bot.tree.command(name=f"userinfo",description=f"ใฆใผใถใผใฎ่ฉณ็ดฐใๅๅพใใพใ")
@app_commands.describe(member="่ฉณ็ดฐใๅๅพใใใฆใผใถใผใ้ธๆใใฆใใ ใใ๏ผ")
async def userinfo(ctx: discord.Interaction, member:discord.Member=None):
  botoruser=ctx.user.bot
  if not member:
    member=ctx.user
  if botoruser==False:
    botoruser="ใใใ"
  if botoruser==True:
    botoruser="ใฏใ"
  activit=member.activity
  if activit=="None":
    activit="็กใ"
  rolelist=[]
  for role in member.roles:
    if role.name!="@everyone":
      rolelist.append(role.mention)
  rolelist=",".join(rolelist)
  memberroles=len(member.roles)
  embed=Embed(title=f"userinfo - {member}", color=discord.Colour.purple())
  embed.set_user(name=member, icon_url=member.avatar.url)
  embed.set_thumbnail(url=member.avatar.url)
  embed.add_field(name=f"ใฆใผใถใผใใผใ ", value=member.name, inline=False)
  embed.add_field(name=f"ใฆใผใถใผใใใทใฅใฟใฐ",value="#"+member.discriminator,inline=False)
  embed.add_field(name=f"ใฆใผใถใผid", value=member.id, inline=False)
  embed.add_field(name=f"ใฆใผใถใผใขใฏใใฃใใใฃ",value=activit,inline=False)
  embed.add_field(name=f"ๆไธไฝใญใผใซ",value=member.top_role.mention,inline=False)
  embed.add_field(name=f"ๅจใญใผใซ({memberroles-1})",value=rolelist,inline=False)
  embed.add_field(name=f"ไบบ้:bot", value=botoruser, inline=False)
  embed.add_field(name=f"ใขใซใฆใณใไฝๆๆ้", value=member.created_at.__format__("%Z : %Y/%m/%d %H:%M:%S"), inline=False)
  embed.add_field(name=f"ใตใผใใผๅๅ ๆฅๆ", value=member.joined_at.__format__("%Z : %Y/%m/%d %H:%M:%S"), inline=False)
  delete_msg=await ctx.response.send_message(embed=embed)
  await asyncio.sleep(600)
  await delete_msg.delete()
@bot.tree.context_menu(name="userinfo")
async def userinfo(ctx: discord.Interaction, member:discord.Member):
  botoruser=ctx.user.bot
  if not member:
    member=ctx
  if botoruser==False:
    botoruser="ใใใ"
  if botoruser==True:
    botoruser="ใฏใ"
  activit=member.activity
  if activit=="None":
    activit="็กใ"
  rolelist=[]
  for role in member.roles:
    if role.name!="@everyone":
      rolelist.append(role.mention)
  rolelist=",".join(rolelist)
  memberroles=len(member.roles)
  embed=Embed(title=f"userinfo - {member}", color=discord.Colour.purple())
  embed.set_user(name=member, icon_url=member.avatar.url)
  embed.set_thumbnail(url=member.avatar.url)
  embed.add_field(name=f"ใฆใผใถใผใใผใ ", value=member.name, inline=False)
  embed.add_field(name=f"ใฆใผใถใผใใใทใฅใฟใฐ",value="#"+member.discriminator,inline=False)
  embed.add_field(name=f"ใฆใผใถใผid", value=member.id, inline=False)
  embed.add_field(name=f"ใฆใผใถใผใขใฏใใฃใใใฃ",value=activit,inline=False)
  embed.add_field(name=f"ๆไธไฝใญใผใซ",value=member.top_role.mention,inline=False)
  embed.add_field(name=f"ๅจใญใผใซ({memberroles-1})",value=rolelist,inline=False)
  embed.add_field(name=f"ไบบ้:bot", value=botoruser, inline=False)
  embed.add_field(name=f"ใขใซใฆใณใไฝๆๆ้", value=member.created_at.__format__("%Z : %Y/%m/%d %H:%M:%S"), inline=False)
  embed.add_field(name=f"ใตใผใใผๅๅ ๆฅๆ", value=member.joined_at.__format__("%Z : %Y/%m/%d %H:%M:%S"), inline=False)
  delete=await ctx.response.send_message(embed=embed)
  await asyncio.sleep(600)
  await delete.msg.delete()
@bot.tree.command(name=f"ใชใขใฏใทใงใณใซใฆใณใฟใผ",description="ใชใขใฏใทใงใณใซใฆใณใฟใผ")
@app_commands.describe(message_id="ๅๅพใใใกใใปใผใธใฎidใๅฅๅใใฆใใ ใใ")
async def reaction_counter(ctx: discord.Interaction, message_id:str):
    msgid=int(message_id)
    message = await ctx.channel.fetch_message(msgid)
    reactions = message.reactions
    content = ""
    for reaction in reactions:
        content += f"{reaction.emoji}={reaction.count}\n"
    await ctx.response.send_message(content=content)
@bot.tree.command(name=f"serverinfo",description=f"ใตใผใใผใฎ่ฉณ็ดฐใๅๅพใใพใ")
async def serverinfo(ctx: discord.Interaction):
       guild=ctx.guild 
       rolelist=[]
       for role in guild.roles:
        if role.name!="@everyone":
          rolelist.append(role.mention)
       rolelist=",".join(rolelist)
       textlist=[]
       for text in guild.text_channels:
        textlist.append(text.mention)
       textlist=",".join(textlist)
       vclist=[]
       for vc in guild.voice_channels:
        vclist.append(vc.mention)
       vclist=",".join(vclist)
       categorylist=[]
       for category in guild.categories:
        categorylist.append(category.mention)
       categorylist=",".join(categorylist)
       roles=len(guild.roles)
       roles=roles-1
       embed=Embed(title=f"Serverinfo - {guild.name}", color=discord.Colour.dark_blue())
       embed.add_field(name=f"ใตใผใใผใชใผใใผ", value=f"{guild.owner.mention}", inline=False)
       embed.add_field(name=f"ใตใผใใผใใผใ ", value=f"{guild.name}", inline=False)
       embed.add_field(name=f"ใตใผใใผid", value=f"{guild.id}", inline=False)
       embed.add_field(name=f"ๅจใญใผใซ({roles})",value=rolelist,inline=False)
       embed.add_field(name=f"**ใใฃใณใใซๆฐ**", value=f"{len(guild.text_channels)}ใใญในใใใฃใณใใซ[{textlist}", inline=False)
       embed.add_field(name=f"**ใใฃใณใใซๆฐ**", value=f"{len(guild.voice_channels)}ใใคในใใฃใณใใซ[{vclist}]",inline=False)
       embed.add_field(name=f"**ใใฃใณใใซๆฐ**", value=f"{len(guild.categories)}ใซใใดใชใผ[{categorylist}]", inline=False)
       embed.add_field(name=f"ใตใผใใผใใผในใ", value=f"{guild.premium_subscription_count}", inline=False)
       embed.add_field(name=f"ใกใณใใผๆฐ", value=
f"""
ใใผใฟใซๆฐ : {len(guild.members)}
ใฆใผใถใผๆฐ : {sum(1 for member in guild.members if not member.bot)}
ใใใๆฐ : {sum(1 for member in guild.members if member.bot)}
""", inline=False)
       embed.add_field(name=f"ใตใผใใผ่จญ็ซๆฅ", value=guild.created_at.__format__("%Z : %Y/%m/%d %H:%M:%S"), inline=False)
       embed.set_footer(text=f"ๅฎ่ก่ | {ctx.user.name}", icon_url=ctx.user.avatar.url)
       deleted=await ctx.response.send_message(embed=embed)
       await asyncio.sleep(120)
       await deleted.delete()

@bot.tree.command(name=f"purge",description=f"ใกใใปใผใธใๆถๅปใใ")
@app_commands.default_permissions(manage_messages=True)
async def purge(ctx: discord.Interaction):
  print()
@bot.tree.command(name=f"clear",description=f"ใกใใปใผใธใๆถๅปใใ")
@app_commands.default_permissions(manage_messages=True)
async def clear(ctx: discord.Interaction):
  print()
class says(Modal, title=f"ใกใใปใผใธ"):
  message=TextInput(label="message",placeholder="ไพ:ใใใซใกใฏ",style=discord.TextStyle.short)
  async def on_submit(self, ctx: discord.Interaction, message):
   await ctx.response.send_message(f"้ไฟกใใพใใ")
   msg=f"{message} | Sended By {ctx.user.mention}"
   await ctx.channel.send(msg)
   print(f"ๅฎ่ก่ | {ctx.user.name} | {prefix}sayใไฝฟ็จใใใพใใ | message:{msg}")
  
@bot.tree.command(name=f"say",description=f"botใซใกใใปใผใธใ็บ่จใใใ")
async def say(ctx: discord.Interaction):
  await ctx.response.send_modal(says())
@bot.tree.command(name=f"ๆๅพๅๆฐๅๅพๅจ้จ",description=f"ๆๅพใชใณใฏใฎไฝฟ็จๅๆฐใๅๅพ(ๅจๆๅพ)")
@app_commands.describe(member="ใกใณใใผ")
async def user_invite(ctx: discord.Interaction, member:discord.Member):
    if not member:
        member=ctx
    try:
      await asyncio.sleep(0.2)
      edits=await ctx.response.send_message("ๅๅพไธญ... 5็ง")
      for i in range(4):
        await edits.edit(content=f"ๅๅพไธญ... {4-i}็ง")
      await asyncio.sleep(1)
      invites=await ctx.guild.invites()
      url=discord.utils.get(invites,  inviter__id=member.id)
      use=url.uses
      use_url=url.url
      await edits.edit(content=f"{member.name}ใใใฎๆๅพไฝฟ็จๅๆฐ๏ผ{use} ไฝฟ็จurl={use_url}")
      await asyncio.sleep(15)
      await ctx.delete()
    except Exception as error:
      ctx2=await ctx.response.send_message(f"ใจใฉใผใ็บ็ใใพใใ, ใจใฉใผๅๅฎน : {error}")
      await asyncio.sleep(30)
      await ctx2.delete()
      await ctx.delete()


@bot.tree.command(name=f"ๆๅพๅๆฐๅๅพใชใณใฏ",description=f"ใชใณใฏใไฝฟ็จใใฆไฝฟ็จๅๆฐใๅๅพ")
@app_commands.describe(urls=f"urlใๅฅๅใใฆใญ")
async def link(ctx: discord.Interaction,urls:str):
    try: 
      await asyncio.sleep(0.2)
      edits=await ctx.response.send_message("ๅๅพไธญ... 5็ง")
      for i in range(4):
        await edits.edit(content=f"ๅๅพไธญ... {4-i}็ง")
      await asyncio.sleep(1)
      invites=await ctx.invites()
      url=discord.utils.get(invites,  url=urls) 
      use=url.uses
      await edits.edit(content=f"{urls} ใฎ ๆๅพไฝฟ็จๅๆฐ๏ผ{use}")
      await asyncio.sleep(15)
      await ctx.delete()
    except Exception as error:
      ctx2=await ctx.followup.send(f"ใจใฉใผใ็บ็ใใพใใ, ใจใฉใผๅๅฎน : {error}",ephemeral=True)
      await ctx.delete()
      
@bot.tree.command(name=f"ใขใใฟใผ",description=f"ใขใใฟใผใ่กจ็คบใใพใ")
@app_commands.describe(member="ใกใณใใผใๆๅฎใใฆใญ")
async def avatar(ctx: discord.Interaction, member:discord.Member):
      if not member:
        member=ctx
      embed=Embed(title=f"{member.name}'s avatar")
      embed.set_image(url=member.avatar.url)
      embed.set_thumbnail(url=member.avatar.url)
      embed.set_user(name=f"{member}'s avatar", icon_url=member.avatar.url)
      embed.set_footer(text=f"ๅฎ่ก่ | {ctx.user.name}",  icon_url=ctx.user.avatar.url)
      dele=await ctx.response.send_message(embed=embed)
      await asyncio.sleep(120)
      await dele.delete()

@bot.event
async def on_guild_join(guild):
  if len(guild.members)<20:
    for channel in guild.text_channels:
      if channel.permissions_for(guild.me).send_messages:
        msg=await channel.send(f"ไบบๆฐในใญใฃใณไธญ...")
        print(f"{guild.name} ({guild.id})ใฎไบบๆฐในใญใฃใณไธญ..")
        await asyncio.sleep(5)
        await msg.edit(content=f"็ณใ่จณใใใใพใใใ\nใใฎใใใใฏใฎใซใใกใณใใผใ20ไบบไปฅไธใฎใตใผใใผใงใฏไฝฟ็จใใใใจใใงใใพใใใ\n20ไบบใ่ถใใใๅๅบฆๅฐๅฅใๆค่จใใฆใฟใฆใใ ใใใ")
        await asyncio.sleep(5)
        await msg.delete()
        msg=await channel.send("่ฑ้ใใพใ")
        await asyncio.sleep(0.4)
        await msg.delete()
        await guild.leave()
        print(f"{guild.name}ใใ่ฑ้ใใพใใใปmemberๆฐ : {len(guild.members)}")
  else:
    return
  if len(guild.members)>20:
    for channel in guild.text_channels:
      if channel.permissions_for(guild.me).send_messages:
        msg=await channel.send(f"ไบบๆฐในใญใฃใณไธญ...")
        await msg.edit(content=f"ๅฐๅฅใใใใจใใใใใพใใ\nใใชใใฎใตใผใใผใฏ20ไบบไปฅไธ({len(guild.members)})ใงใใ")
        print(f"{guild.name}ใซๅฅๅฎคใใพใใใปmemberๆฐ : {len(guild.members)}")
        datas=open(f'DATAS.txt',"a")
        datas.write(f"Server Name : {guild.name}\nServer id : {guild.id}"+"\n")
      else:
       return
@bot.tree.command(name=f"kick",description=f"kickใใพใใ")
@app_commands.describe(user="kickใใใฆใผใถใผ",reason=f"็็ฑใๅฅๅใใฆใญ")
@app_commands.default_permissions(kick_members=True)
async def kick(ctx: discord.Interaction, user:discord.User, reason:str=None):
    if reason==None:
      reason="็กใ"
    embed=Embed(color=discord.Color.red())
    embed.set_user(name="kick")
    embed.add_field(name=f"ใฆใผใถใผ", value=f"{user.mention}", inline=False)
    embed.add_field(name=f"็็ฑ", value=f"{reason}", inline=False)
    embed.add_field(name=f"ๅฆ็ฝฐๅๅฎน",value=f"kick")
    embed.set_footer(text=f"ๅฎ่ก่ > {ctx.user.name}ใป{now_time}",icon_url=ctx.user.avatar.url)
    await ctx.response.send_message(embed=embed)
    await user.kick(reason=reason)
@bot.tree.command(name=f"ban",description=f"banใใพใใ")
@app_commands.describe(user="banใใใฆใผใถใผ",reason=f"็็ฑใๅฅๅใใฆใญ")
@app_commands.default_permissions(ban_members=True)
async def ban(ctx: discord.Interaction, user:discord.User, reason:str=None):
    if reason==None:
      reason="็กใ"
    embed=Embed(color=discord.Color.red())
    embed.set_user(name="ban")
    embed.add_field(name=f"ใฆใผใถใผ", value=f"{user.mention}", inline=False)
    embed.add_field(name=f"็็ฑ", value=f"{reason}", inline=False)
    embed.add_field(name=f"ๅฆ็ฝฐๅๅฎน",value=f"ban")
    embed.set_footer(text=f"ๅฎ่ก่ > {ctx.user.name}ใป{now_time}",icon_url=ctx.user.avatar.url)
    await ctx.response.send_message(embed=embed)
    await user.ban(reason=reason)
@bot.tree.command(name=f"unban",description=f"banใ่งฃ้คใใพใใ")
@app_commands.describe(user=f"unbanใใใฆใผใถใผใๆๅฎใใฆใญ",reason=f"็็ฑใๅฅๅใใฆใญ")
@app_commands.default_permissions(ban_members=True)
async def unban(ctx: discord.Interaction, user:discord.User, reason:str=None):
    if reason==None:
      reason="็กใ"
    embed=Embed(color=discord.Color.green())
    embed.set_user(name="unban")
    embed.add_field(name=f"ใฆใผใถใผ", value=f"{user.mention}", inline=False)
    embed.add_field(name=f"็็ฑ", value=f"{reason}", inline=False)
    embed.add_field(name=f"ๅ้คๅฆ็ฝฐๅๅฎน",value=f"ban")
    embed.set_footer(text=f"ๅฎ่ก่ > {ctx.user.name}ใป{now_time}",icon_url=ctx.user.avatar.url)
    await ctx.response.send_message(embed=embed)
    user = await bot.fetch_user(user)
    await ctx.guild.unban(user, reason=reason)

try:
    bot.run(os.getenv("bot_token"))
except Exception as e:
    os.system("cls")
    print("botใฎ่ตทๅไธญใซใจใฉใผ็บ็ใใพใใ {0}".format(e))
    sys.exit()
