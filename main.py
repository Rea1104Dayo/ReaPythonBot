import discord
import os,os.path,sys
import asyncio,random,string
import platform
from discord import Permissions, app_commands, Embed
from discord.ext import commands
from discord.utils import get
from discord.ui import View,select,Button,Modal,TextInput
from datetime import datetime
from dotenv import load_dotenv
from colorama import Fore,init,Back,Style
from discord_buttons_plugin import *

now_time=datetime.now().__format__("%Y/%m/%d %H:%M:%S")
os.system("title BOT")
count=0
load_dotenv()
admin=os.getenv("Admin")
prefix=os.getenv("prefix")
SupportServer=os.getenv("Support_server")
paths=os.path.dirname(os.path.realpath(__file__))
bot=commands.Bot(command_prefix="/", help_command=None, intents=discord.Intents.all())
buttons=ButtonsClient(bot)
voice_client = None

async def status1():
  servers=len(bot.guilds)
  members=0
  for guild in bot.guilds:
    members +=guild.member_count - 1
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"{servers} サーバー | {members} メンバー"))
async def changestatus():
  while True:
    await asyncio.sleep(15)
    await status1()
slot=["1","2","3","4","5","6","7","8","9"]

@bot.event
async def on_ready():
  os.system("cls")
  servers=len(bot.guilds)
  members=0
  for guild in bot.guilds:
    members +=guild.member_count - 1
  print(Fore.GREEN + f"----------------------------------------")
  print(Fore.RED + f"Bot Info")
  print(Fore.RED + f"Bot Name : {bot.user.name}")
  print(Fore.RED + f"Bot id ：{bot.user.id}")
  print(Fore.RED + f"Bot Status : {servers} サーバー | {members} メンバー")
  print(Fore.RED + f"Server : {servers}")
  print(Fore.RED + f"All Server Member : {members}")
  print(Fore.GREEN + f"----------------------------------------")
  print(Fore.BLUE + f"python Info")
  print(Fore.BLUE + f"discord Version ：{discord.__version__}")
  print(Fore.BLUE + f"Python Version ：{str(platform.python_version())}")
  print(Fore.GREEN + f"----------------------------------------")
  Synced=await bot.tree.sync()
  print(Fore.CYAN + f"{len(Synced)}個のコマンドを同期しました")
  print(Fore.GREEN + f"----------------------------------------"+ Fore.RESET + f"")
  await changestatus()

@bot.tree.command(name=f"nitrogen",description=f"nitroGen")
@app_commands.describe(counts="nitroを生成する数")
async def gen(ctx: discord.Interaction, counts:int):
  i=0
  if counts>101:
    counts=100
  while int(i)<int(counts):
    Nitro="https://discord.gift/"+random.choice(string.ascii_letters)+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(17))
    count=i
    count+=1
    i=count
    print(Fore.BLUE+f"\n{i}"+Fore.GREEN+"/"+Fore.RED+f"{counts}\n\n"+Fore.LIGHTBLUE_EX+"実行者 "+Fore.RESET+"> "+Fore.GREEN+f"{ctx.user.name}")
    deleted=await ctx.channel.send(Nitro + f"\n{i}/{counts}\n実行者 > {ctx.user.name}")
    if i>counts-1:
      print(Fore.RESET+f"\nNitroGenが終了しました"+Fore.BLACK+"-"+Fore.BLUE+f"{i}"+Fore.GREEN+"/"+Fore.RED+f"{counts}"+Fore.RESET+","+Fore.LIGHTBLUE_EX+"実行者 "+Fore.RESET+"> "+Fore.GREEN+f"{ctx.user.name}")
      deleted2=await ctx.channel.send(f"NitroGenが終了しました-{i}/{counts}, 実行者 > {ctx.user.name}")
      await asyncio.sleep(50)
      await deleted.delete
      await deleted2.delete()
      await ctx.response.send_message("ALL COMPLETED",ephemeral=True)

@bot.tree.command(name=f"ping",description=f"pingを表示します")
async def ping(ctx: discord.Interaction):
  raw_ping=bot.latency
  ping=round(raw_ping * 1000)
  embed=Embed(title=f"Ping! {ping}ms", description=f"{bot.user.name}のPingは{ping}msです！！", color=discord.Color.brand_green())
  await ctx.response.send_message(embed=embed,ephemeral=True)
  print(f"実行者 | {ctx.user.name} | {prefix}pingが使用されました"+Fore.GREEN +f""+Fore.GREEN +f"\n----------------------------------------"+ Fore.RESET + f""+ Fore.RESET + f"")


@bot.tree.command(name=f"bot概要",description=f"botの概要を表示します")
async def info(ctx: discord.Interaction):
    embed=Embed(title=f"{bot.user.name} : {bot.user.id}", description="pythonで作成されたdiscord botです。", color=0xeee657)
    embed.add_field(name=f"実行者", value=f"{ctx.user.name}")
    embed.add_field(name=f"作成者", value=f"{admin}")
    embed.add_field(name=f"導入数", value=f"{len(bot.guilds)}")
    embed.add_field(name=f"bot招待", value=f"リンクは[こちら](https://discord.com/api/oauth2/authorize?bot_id={bot.user.id}&permissions=8&scope=bot%20applications.commands)")
    embed.add_field(name=f"サポートサーバー", value=f"招待リンクは[こちら]({SupportServer})")
    dele_=await ctx.response.send_message(embed=embed)
    dele=await buttons.send(
      channel=ctx.channel.id,
            components=[
                ActionRow([
                    Button(
                        label="招待はこちら", 
                        style=ButtonType().Link, 
                        url=f"https://discord.com/api/oauth2/authorize?bot_id={bot.user.id}&permissions=8&scope=bot"
                    )
                ])
            ]
        )
    await asyncio.sleep(120)
    await dele.delete()
    await dele_.delete()
@bot.tree.command(name=f"setup",description=f"設定してなかったら使ってください")
@app_commands.default_permissions(administrator=True)
async def setup(ctx: discord.Interaction):
  guild=ctx.guild
  channels=await guild.fetch_channels()
  for channel in channels:
      await channel.delete()
  #チャンネルとか
  c1=await guild.create_category("重要")
  await c1.create_text_channel("・👌｜参加者")
  rules=await c1.create_text_channel("・📚｜ルール")
  await c1.create_text_channel("・✅｜認証")
  await c1.create_text_channel("・📢｜お知らせ")
  c2=await guild.create_category("メイン-テキスト")
  await c2.create_text_channel("・👥｜雑談")
  await c2.create_text_channel("・🤖｜コマンド")
  await c2.create_text_channel("・✋｜要望")
  quest=await c2.create_text_channel("・❓｜質問")
  c3=await guild.create_category("メイン-ボイス")
  await c3.create_text_channel("・🎤｜雑談用聞き専-1")
  await c3.create_text_channel("・🎤｜雑談用聞き専-2")
  await c3.create_text_channel("・🎤｜雑談用聞き専-3")
  await c3.create_text_channel("・🎤｜雑談用聞き専-4")
  await c3.create_text_channel("━━━━━━━━━━━━━━━━")
  await c3.create_text_channel("・🎮｜ゲーム用聞き専-1")
  await c3.create_text_channel("・🎮｜ゲーム用聞き専-2")
  await c3.create_text_channel("・🎮｜ゲーム用聞き専-3")
  await c3.create_text_channel("・🎮｜ゲーム用聞き専-4")
  await c3.create_text_channel("━━━━━━━━━━━━━━━━")
  await c3.create_text_channel("・🎧｜音楽室用-1")
  await c3.create_text_channel("・🎧｜音楽室用-2")
  await c3.create_text_channel("・🎧｜音楽室用-3")
  await c3.create_text_channel("・🎧｜音楽室用-4")
  await c3.create_voice_channel("━━━━━━━━━━━━━━━━")
  await c3.create_voice_channel("・🎤｜雑談-1")
  await c3.create_voice_channel("・🎤｜雑談-2")
  await c3.create_voice_channel("・🎤｜雑談-3")
  await c3.create_voice_channel("・🎤｜雑談-4")
  await c3.create_voice_channel("━━━━━━━━━━━━━━━━")
  await c3.create_voice_channel("・🎮｜ゲーム-1")
  await c3.create_voice_channel("・🎮｜ゲーム-2")
  await c3.create_voice_channel("・🎮｜ゲーム-3")
  await c3.create_voice_channel("・🎮｜ゲーム-4")
  await c3.create_voice_channel("━━━━━━━━━━━━━━━━")
  await c3.create_voice_channel("・🎧｜音楽室-1")
  await c3.create_voice_channel("・🎧｜音楽室-2")
  await c3.create_voice_channel("・🎧｜音楽室-3")
  await c3.create_voice_channel("・🎧｜音楽室-4")
  await c3.create_voice_channel("━━━━━━━━━━━━━━━━")
  a=await guild.create_role(name=f"Admin", permissions=discord.Permissions.all(), color=discord.Color.gold(), reason="setup...")
  role=guild.get_role(a.id)
  member=guild.get_member(int(ctx.user.id))
  me=guild.get_member(int(bot.user.id))
  b=await guild.create_role(name=f"Bot", color=discord.Color.dark_purple(), reason="setup...")
  role2=guild.get_role(b.id)
  verify=await guild.create_role(name=f"Verify", color=discord.Color.green(), reason="setup...")
  role2=guild.get_role(b.id)
  await member.add_roles(verify, reason="setup...")
  await member.add_roles(role, reason="setup...")
  await me.add_roles(role2, reason="setup...")
  await me.add_roles(verify, reason="setup...")
  em=Embed(title=f"ルール",description=f"**重要：[利用規約](<https://discord.com/terms>)および[コミュニティガイドライン](<https://discord.com/guidelines>)、サーバールールを遵守してください。**\nこれらに違反した場合、タイムアウトやBAN等の処罰を受ける場合があります。\n`📜` サーバールール\n1. `😀` 発言には責任を持ち、攻撃的な口調を使わないこと。\n誹謗中傷や無責任な発言、他人の個人情報の投稿は固く禁止されています。\n2. `💥` スパムやサーバーへの荒らし行為を行わないこと。\nそれらを示唆したり称賛したりする発言・脅迫や、それらに関連する団体・ツールに関係する発言もしてはいけません。\n3. `🔞` R18コンテンツや、それに関する話題をしないこと。\n直接的な発言はもちろん、関連する話題を出したり、ニックネームやアバター画像、スレッド名等に含むことも禁止されています。\n4. `💖` 出会い、男女交際目的で利用しないこと。\n** **5. `🎭` ユーザー名の先頭に記号を付けないこと。\n** **6. `📡` 利己的な宣伝目的でSNSやコンテンツのURLを送信しないこと。\n** **7. `📢` これらに違反した行為に対して過剰に反応しないこと。\n** **\nその他、モデレーターが客観的に見て不適切と感じた場合は相応の処罰が課される場合があります。",color=discord.Color.red())
  em1=await bot.get_channel(rules.id).send(embed=em)
  em=Embed(title=f"ルール",description=f"`💬` テキストチャンネル ルール\n```テキストチャンネルを使用する際は、追加でルールが適用されます。```\n**1. `💬` チャンネルの趣旨にあった話をすること。**\n**2. `🔔` 意味もなく個人やロールをメンションしないこと。**\n**3. `❓` 質問がある場合は、可能な限り<#{quest.id}>を使用すること。** \n**4. `💥` 特定の分野に絞ったチャンネル内では、その分野を否定する発言を行わないこと。**",color=discord.Color.blue())
  em2=await bot.get_channel(rules.id).send(embed=em)
  em=Embed(title=f"ルール",description=f"`🔊` ボイスチャンネル ルール\n```ボイスチャンネルを使用する際は、追加でルールが適用されます。```\n**1. `🔊` 爆音や雑音を流す等、他人に迷惑をかけるような行為をしないこと。**\n**2. `🚫` 有料コンテンツ(映画)等の配信や、ゲームのルールやガイドラインに違反する企画の開催・配信をしないこと。**",color=discord.Color.green())
  em3=await bot.get_channel(rules.id).send(embed=em)
  em=Embed(title=f"目次",description=f"目次\n\n1. `📜` [サーバールール](https://ptb.discord.com/channels/{guild.id}/{rules.id}/{em1.id}) (必読)\n\n2. `💬` [`💬` テキストチャンネル ルール](https://ptb.discord.com/channels/{guild.id}/{rules.id}/{em2.id})\n\n3. `🔊` [🔊 ボイスチャンネル ルール](https://ptb.discord.com/channels/{guild.id}/{rules.id}/{em3.id})",color=discord.Color.purple())
  await bot.get_channel(rules.id).send(embed=em)
@bot.tree.command(name=f"再生成",description=f"チャンネルを再生成します")
async def nuke(ctx: discord.Interaction):
    channel=ctx.channel
    msg=Embed(title="再生成の通知", description="チャンネルの再生成が完了しました。")
    msg.set_footer(text=f"実行者 | {ctx.user.name}・{now_time}", icon_url=ctx.user.avatar.url)
    channel2=await channel.clone()
    await channel2.edit(position=channel.position)
    await channel.delete()
    delll=await channel2.send(embed=msg)
    await asyncio.sleep(120)
    await delll.delete()
    return
@bot.tree.command(name=f"test",description=f"test")
@commands.is_owner()
async def TEST(ctx: discord.Interaction):
  await ctx.response.send_message(content="interaction!",embed=None,ephemeral=True)
  await ctx.followup.send(content="webhook!",embed=None,ephemeral=True)
@bot.tree.command(name=f"おみくじ",description=f"おみくじをします")
async def omikuji(ctx: discord.Interaction):
  result=["大吉", "中吉", "小吉", "凶", "小凶"]
  msg1=await ctx.response.send_message(f"{ctx.user.mention}さんのおみくじの結果は...   ")
  for i in range(5):
    await msg1.edit(content=f"{ctx.user.mention}さんのおみくじの結果まで あと{5-i}秒")
    await asyncio.sleep(1)
  await msg1.edit(content=f"{ctx.user.mention}さんのおみくじの結果は  **" + random.choice(result) + "**  でした")

@bot.tree.command(name=f"help",description=f"helpを表示します")
@app_commands.describe(page="開くページ。 無しだったら1")
async def help(ctx: discord.Interaction, page: int=None):
    buttonlist=["❓","⏮️","⏪","⬅️","➡️","⏩","⏭","🗑️"]
    if page==None:
      page=1
    if page==1:
      page=0
    if page==2:
      page=1
    if page==3:
      page=2
    if page==4:
      page=3
    if page==5:
      page=4
    if page==6:
      page=5
    if page==7:
      page=6
    counts=page
    page1=Embed(title=f"help - {bot.user.name}",description=f"ページ1 - 目次",color=0x000000)
    page1.add_field(name=f"ページ1 - 目次",value="このメッセージを表示させる")
    page1.add_field(name=f"ページ2 - funコマンド",value="ゲームコマンドを表示させる")
    page1.add_field(name=f"ページ3 - Basicコマンド",value="権限無しでできるコマンドを表示させる")
    page1.add_field(name=f"ページ4 - moderateコマンド",value="モデレーター専用のコマンドを表示させる")
    page1.add_field(name=f"ページ5 - 宣伝",value="作成者の宣伝")
    page1.add_field(name=f"ページ6 - botの概要",value="botの説明")
    page1.set_footer(text=f"ページ 1/6・実行者 | {ctx.user.name} : 5分間操作がなかったら削除されます・{now_time}",icon_url=ctx.user.avatar.url)
    page2=Embed(title=f"help - {bot.user.name}",description=f"ページ2 - Fun",color=0x000000)
    page2.add_field(name=f"{prefix}おみくじ",value="おみくじ")
    page2.add_field(name=f"{prefix}スロット", value="スロット")
    page2.set_footer(text=f"ページ 2/6・実行者 | {ctx.user.name} : 5分間操作がなかったら削除されます・{now_time}",icon_url=ctx.user.avatar.url)
    page3=Embed(title=f"help - {bot.user.name}",description=f"ページ3 - Basic",color=0x000000)
    page3.add_field(name=f"{prefix}help ",value="helpを表示する")
    page3.add_field(name=f"{prefix}serverinfo", value="サーバーの情報を表示する")
    page3.add_field(name=f"{prefix}userinfo", value="ユーザーの情報を表示する")
    page3.add_field(name=f"{prefix}say",value="botにメッセージを送信させる")
    page3.add_field(name=f"{prefix}ping",value="pingを表示")
    page3.add_field(name=f"{prefix}リアクションカウンター",value="指定されたメッセージのリアクション数を取得します")    
    page3.add_field(name=f"{prefix}招待回数取得リンク", value="招待リンクの使用数を取得する。 : 因数 /招待回数取得リンク url")
    page3.add_field(name=f"{prefix}招待回数取得全部", value="指定したメンバーの招待リンクの使用数を取得する。 : 因数 /招待回数取得全部 @メンバー (@メンバーなしだと自分になる)")
    page3.set_footer(text=f"ページ 3/6・実行者 | {ctx.user.name} : 5分間操作がなかったら削除されます・{now_time}",icon_url=ctx.user.avatar.url)
    page4=Embed(title=f"help - {bot.user.name}",description=f"ページ4 - Moderation")
    page4.add_field(name=f"{prefix}purge", value="メッセージを削除する - メッセージの管理")
    page4.add_field(name=f"{prefix}kick", value="ユーザーをkick - ユーザーを管理(KICK)")
    page4.add_field(name=f"{prefix}ban", value="ユーザーをban - ユーザーを管理(BAN)")
    page4.add_field(name=f"{prefix}unban", value="ユーザーのbanを解除 - ユーザーを管理(BAN)")
    page4.set_footer(text=f"ページ 4/6・実行者 | {ctx.user.name} : 5分間操作がなかったら削除されます・{now_time}",icon_url=ctx.user.avatar.url)
    page5=Embed(title=f"宣伝 - {bot.user.name}",description=f"ページ5 - 作成者")
    page5.add_field(name=f"youtube",value=f"youtubeアカウントは[こちら](https://www.youtube.com/@Rea1104)",inline=False)
    page5.add_field(name=f"twiiter",value=f"ツイッターアカウントは[こちら](https://twitter.com/Rea1104__)",inline=False)
    page5.add_field(name=f"bot github",value=f"botのレポジトリは[こちら](https://github.com/Rea1104Dayo/ReaPythonBot)",inline=False)
    page5.set_footer(text=f"ページ 5/6・実行者 | {ctx.user.name} : 5分間操作がなかったら削除されます・{now_time}",icon_url=ctx.user.avatar.url)
    page6=Embed(title=f"botの概要 - {bot.user.name}",description=f"ページ6 - 概要")
    page6.add_field(name=f"製作者",value=f"Rea#1234")
    page6.add_field(name=f"botの概要",value="作成者が趣味で作成しているbotです。")
    page6.set_footer(text=f"ページ 6/6・実行者 | {ctx.user.name} : 5分間操作がなかったら削除されます・{now_time}",icon_url=ctx.user.avatar.url)
    question=Embed(title=f"Question - {bot.user.name}",description=f"ページQuestion - Question")
    question.add_field(name=f"Question",value=f"""
❓: このページにする。
⏮️: ページを3個戻す。
⏪: ページを2個戻す。
⬅️: ページを1個戻す。
➡️: ページを1個進める。
⏩: ページを2個進める。
⏭: ページを3個進める。
🗑️: helpを削除する。

helpを使ってくれてありがとうございます。
""")
    question.set_footer(text=f"ページ Question/6・実行者 | {ctx.user.name} : 5分間操作がなかったら削除されます・{now_time}",icon_url=ctx.user.avatar.url) 
    embed_list=[page1,page2,page3,page4,page5,page6,question]
    embed=await ctx.channel.send(embed=embed_list[counts])
    embeds=Embed(title=f"helpを作成しました!",description=f"応答が5分間なかった場合、このメッセージを削除します!",color=discord.Color.green()).set_footer(text=f"実行者 | {ctx.user.name}",icon_url=ctx.user.avatar.url)
    await ctx.response.send_message(embed=embeds,ephemeral=True)
    for button in buttonlist:
      await embed.add_reaction(button)
    while True:
          try:
             reaction, user=await bot.wait_for("reaction_add",timeout=300,check=lambda reaction, user: user==ctx.user and reaction.emoji in buttonlist)
          except asyncio.TimeoutError:
             await embed.delete()
             await ctx.followup.send(embed=Embed(title=f"Deleted Help - {bot.user.name}, {ctx.user.name}",description=f"Helpが削除されました",color=discord.Color.red()).set_footer(text=f"実行者 | {ctx.user.name}",icon_url=ctx.user.avatar.url), ephemeral=True)
             return
          else:
            preview_pages=counts
            if reaction.emoji=="⬅️":
                counts -=1
            elif reaction.emoji=="➡️":
                counts +=1
            elif reaction.emoji=="⏪":
                counts -=2
            elif reaction.emoji=="⏩":
                counts +=2
            elif reaction.emoji=="⏮️":
                counts -=3
            elif reaction.emoji=="⏭":
                counts +=3
            elif reaction.emoji=="🗑️":
                await embed.delete()
                await ctx.followup.send(embed=Embed(title=f"Deleted Help - {bot.user.name}, {ctx.user.name}",description=f"Helpが削除されました",color=discord.Color.red()).set_footer(text=f"実行者 | {ctx.user.name}",icon_url=ctx.user.avatar.url), ephemeral=True)
            elif reaction.emoji=="❓":
                counts = 6
            await embed.remove_reaction(reaction, user)
            if counts !=preview_pages:
              await embed.edit(embed=embed_list[counts])

@bot.tree.command(name=f"poll",description=f"アンケートをする")
@app_commands.describe(message=f"メッセージ",回答=f"1番目の選択肢",回答2=f"2番目の選択肢")
async def poll(ctx: discord.Interaction, message:str, 回答:str,回答2:str):
  Number="1","2","3","4","5","6","7","8","9"
  Answer1=0
  Answer2=0
  poll_id=random.choice(Number)+"".join(random.choice(Number) for _ in range(14))
  embed=Embed(title=f"{message}", description=f"1️⃣ : {回答}\n2️⃣ : {回答2}",color=0x000000)  
  embed.set_footer(text=f"実行者 | {ctx.user.name}・POLL id : {poll_id}", icon_url=ctx.user.avatar.url)
  msg=await ctx.channel.send(embed=embed)
  created=Embed(title=f"作成しました！", description="アンケートを作成しました！", color=discord.Color.blue())
  created.add_field(name=f"メッセージ",value=f"{message}")
  created.add_field(name=f"回答1",value=f"{回答}")
  created.add_field(name=f"回答2",value=f"{回答2}")
  await ctx.response.send_message(embed=created, ephemeral=True)
  reactionlist=["1️⃣","2️⃣"]
  await msg.add_reaction("1️⃣")
  await msg.add_reaction("2️⃣")

@bot.tree.command(name=f"userinfo",description=f"ユーザーの詳細を取得します")
@app_commands.describe(member="詳細を取得するユーザーを選択してください！")
async def userinfo(ctx: discord.Interaction, member:discord.Member=None):
  botoruser=ctx.user.bot
  if not member:
    member=ctx
  if botoruser==False:
    botoruser="いいえ"
  if botoruser==True:
    botoruser="はい"
  activit=member.activity
  if activit=="None":
    activit="無し"
  rolelist=[]
  for role in member.roles:
    if role.name!="@everyone":
      rolelist.append(role.mention)
  rolelist=",".join(rolelist)
  memberroles=len(member.roles)
  embed=Embed(title=f"userinfo - {member}", color=discord.Colour.purple())
  embed.set_author(name=member, icon_url=member.avatar.url)
  embed.set_thumbnail(url=member.avatar.url)
  embed.add_field(name=f"ユーザーネーム", value=member.name, inline=False)
  embed.add_field(name=f"ユーザーハッシュタグ",value="#"+member.discriminator,inline=False)
  embed.add_field(name=f"ユーザーid", value=member.id, inline=False)
  embed.add_field(name=f"ユーザーアクティビティ",value=activit,inline=False)
  embed.add_field(name=f"最上位ロール",value=member.top_role.mention,inline=False)
  embed.add_field(name=f"全ロール({memberroles-1})",value=rolelist,inline=False)
  embed.add_field(name=f"人間:bot", value=botoruser, inline=False)
  embed.add_field(name=f"アカウント作成時間", value=member.created_at.__format__("%Z : %Y/%m/%d %H:%M:%S"), inline=False)
  embed.add_field(name=f"サーバー参加日時", value=member.joined_at.__format__("%Z : %Y/%m/%d %H:%M:%S"), inline=False)
  delete_msg=await ctx.response.send_message(embed=embed)
  await asyncio.sleep(600)
  await delete_msg.delete()
@bot.tree.context_menu(name="userinfo")
async def userinfo(ctx: discord.Interaction, member:discord.Member):
  botoruser=ctx.user.bot
  if not member:
    member=ctx
  if botoruser==False:
    botoruser="いいえ"
  if botoruser==True:
    botoruser="はい"
  activit=member.activity
  if activit=="None":
    activit="無し"
  rolelist=[]
  for role in member.roles:
    if role.name!="@everyone":
      rolelist.append(role.mention)
  rolelist=",".join(rolelist)
  memberroles=len(member.roles)
  embed=Embed(title=f"userinfo - {member}", color=discord.Colour.purple())
  embed.set_author(name=member, icon_url=member.avatar.url)
  embed.set_thumbnail(url=member.avatar.url)
  embed.add_field(name=f"ユーザーネーム", value=member.name, inline=False)
  embed.add_field(name=f"ユーザーハッシュタグ",value="#"+member.discriminator,inline=False)
  embed.add_field(name=f"ユーザーid", value=member.id, inline=False)
  embed.add_field(name=f"ユーザーアクティビティ",value=activit,inline=False)
  embed.add_field(name=f"最上位ロール",value=member.top_role.mention,inline=False)
  embed.add_field(name=f"全ロール({memberroles-1})",value=rolelist,inline=False)
  embed.add_field(name=f"人間:bot", value=botoruser, inline=False)
  embed.add_field(name=f"アカウント作成時間", value=member.created_at.__format__("%Z : %Y/%m/%d %H:%M:%S"), inline=False)
  embed.add_field(name=f"サーバー参加日時", value=member.joined_at.__format__("%Z : %Y/%m/%d %H:%M:%S"), inline=False)
  delete=await ctx.response.send_message(embed=embed)
  await asyncio.sleep(600)
  await delete.msg.delete()
@bot.tree.command(name=f"リアクションカウンター",description="リアクションカウンター")
@app_commands.describe(message_id="取得するメッセージのidを入力してください")
async def reaction_counter(ctx: discord.Interaction, message_id:str):
    msgid=int(message_id)
    message = await ctx.channel.fetch_message(msgid)
    reactions = message.reactions
    content = ""
    for reaction in reactions:
        content += f"{reaction.emoji}={reaction.count}\n"
    await ctx.response.send_message(content=content)
@bot.tree.command(name=f"serverinfo",description=f"サーバーの詳細を取得します")
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
       embed.add_field(name=f"サーバーオーナー", value=f"{guild.owner.mention}", inline=False)
       embed.add_field(name=f"サーバーネーム", value=f"{guild.name}", inline=False)
       embed.add_field(name=f"サーバーid", value=f"{guild.id}", inline=False)
       embed.add_field(name=f"全ロール({roles})",value=rolelist,inline=False)
       embed.add_field(name=f"**チャンネル数**", value=f"{len(guild.text_channels)}テキストチャンネル[{textlist}", inline=False)
       embed.add_field(name=f"**チャンネル数**", value=f"{len(guild.voice_channels)}ボイスチャンネル[{vclist}]",inline=False)
       embed.add_field(name=f"**チャンネル数**", value=f"{len(guild.categories)}カテゴリー[{categorylist}]", inline=False)
       embed.add_field(name=f"サーバーブースト", value=f"{guild.premium_subscription_count}", inline=False)
       embed.add_field(name=f"メンバー数", value=
f"""
トータル数 : {len(guild.members)}
ユーザー数 : {sum(1 for member in guild.members if not member.bot)}
ボット数 : {sum(1 for member in guild.members if member.bot)}
""", inline=False)
       embed.add_field(name=f"サーバー設立日", value=guild.created_at.__format__("%Z : %Y/%m/%d %H:%M:%S"), inline=False)
       embed.set_footer(text=f"実行者 | {ctx.user.name}", icon_url=ctx.user.avatar.url)
       deleted=await ctx.response.send_message(embed=embed)
       await asyncio.sleep(120)
       await deleted.delete()

class Clears(Modal, title=f"削除する数"):
  count=TextInput(label="Counts",placeholder="例:1",style=discord.TextStyle.short)
  async def on_submit(self, ctx: discord.Interaction):
    c=ctx.channel
    d=await c.purge(limit=count+1)
    await ctx.response.send_message(embed=Embed(title=f"Clear - {bot.user.name} : {ctx.user.name}",description=f"{len(d)}メッセージを削除しました", color=discord.Color.green()),ephemeral=True)
    print(f"実行者 | {ctx.user.name} | {prefix}purgeが使用されました- | {len(d)}メッセージが削除されました"+Fore.GREEN +f"\n----------------------------------------"+ Fore.RESET + f"")

@bot.tree.command(name=f"purge",description=f"メッセージを消去する")
@app_commands.default_permissions(manage_messages=True)
async def purge(ctx: discord.Interaction):
  await ctx.response.send_modal(Clears())

@bot.tree.command(name=f"clear",description=f"メッセージを消去する")
@app_commands.default_permissions(manage_messages=True)
async def clear(ctx: discord.Interaction):
  await ctx.response.send_modal(Clears())
class says(Modal, title=f"メッセージ"):
  message=TextInput(label="message",placeholder="例:こんにちは",style=discord.TextStyle.short)
  async def on_submit(self, ctx: discord.Interaction, message):
   await ctx.response.send_message(f"送信しました")
   msg=f"{message} | Sended By {ctx.user.mention}"
   await ctx.channel.send(msg)
   print(f"実行者 | {ctx.user.name} | {prefix}sayが使用されました | message:{msg}")

@bot.tree.command(name=f"say",description=f"botにメッセージを発言させる")
async def say(ctx: discord.Interaction):
  await ctx.response.send_modal(says())
@bot.tree.command(name=f"招待回数取得全部",description=f"招待リンクの使用回数を取得(全招待)")
@app_commands.describe(member="メンバー")
async def user_invite(ctx: discord.Interaction, member:discord.Member):
    if not member:
        member=ctx
    try:
      await asyncio.sleep(0.2)
      edits=await ctx.response.send_message("取得中... 5秒")
      for i in range(4):
        await edits.edit(content=f"取得中... {4-i}秒")
      await asyncio.sleep(1)
      invites=await ctx.guild.invites()
      url=discord.utils.get(invites,  inviter__id=member.id)
      use=url.uses
      use_url=url.url
      await edits.edit(content=f"{member.name}さんの招待使用回数：{use} 使用url={use_url}")
      await asyncio.sleep(15)
      await ctx.delete()
    except Exception as error:
      ctx2=await ctx.response.send_message(f"エラーが発生しました, エラー内容 : {error}")
      await asyncio.sleep(30)
      await ctx2.delete()
      await ctx.delete()


@bot.tree.command(name=f"招待回数取得リンク",description=f"リンクを使用して使用回数を取得")
@app_commands.describe(urls=f"urlを入力してね")
async def link(ctx: discord.Interaction,urls:str):
    try: 
      await asyncio.sleep(0.2)
      edits=await ctx.response.send_message("取得中... 5秒")
      for i in range(4):
        await edits.edit(content=f"取得中... {4-i}秒")
      await asyncio.sleep(1)
      invites=await ctx.invites()
      url=discord.utils.get(invites,  url=urls) 
      use=url.uses
      await edits.edit(content=f"{urls} の 招待使用回数：{use}")
      await asyncio.sleep(15)
      await ctx.delete()
    except Exception as error:
      ctx2=await ctx.followup.send(f"エラーが発生しました, エラー内容 : {error}",ephemeral=True)
      await ctx.delete()


slot1_2=random.choice(slot)
slot2_2=random.choice(slot)
slot3_2=random.choice(slot)

@bot.tree.command(name=f"スロット",description=f"スロットをします")
async def slot(ctx: discord.Interaction):
    msg=await ctx.response.send_message(f"{ctx.user.name}さんのスロット結果は...")
    await msg.add_reaction("1️⃣")
    def check(reaction, user):
        return user==ctx and str(reaction.emoji) in ["1️⃣", "2️⃣", "3️⃣"]
    while True:
        try:
            reaction, user=await bot.wait_for("reaction_add", timeout=60, check=check)
            if str(reaction.emoji)=="1️⃣":
              await msg.remove_reaction(reaction)
              await msg.edit(content=f"{slot1_2}")
              await msg.add_reaction("2️⃣")
            elif str(reaction.emoji)=="2️⃣":
              await msg.remove_reaction(reaction)
              await msg.edit(content=f"{slot1_2}{slot2_2}")
              await msg.add_reaction("3️⃣")
            elif str(reaction.emoji)=="3️⃣":
              await asyncio.sleep(0.2)
              await msg.remove_reaction(reaction)
              await msg.edit(content=f"結果を読み込み中...")
              await asyncio.sleep(0.6)
              await msg.edit(cotent=f"{slot1_2}{slot2_2}{slot3_2}")
              await asyncio.sleep(2)
              await msg.edit(content=f"{ctx.user.name}さんのスロット結果は{slot1_2}{slot2_2}{slot3_2}でした")
            else:
              await msg.remove_reaction(reaction)
        except asyncio.TimeoutError:
              await msg.delete()
              break
      
@bot.tree.command(name=f"アバター",description=f"アバターを表示します")
@app_commands.describe(member="メンバーを指定してね")
async def avatar(ctx: discord.Interaction, member:discord.Member):
      if not member:
        member=ctx
      embed=Embed(title=f"{member.name}'s avatar")
      embed.set_image(url=member.avatar.url)
      embed.set_thumbnail(url=member.avatar.url)
      embed.set_author(name=f"{member}'s avatar", icon_url=member.avatar.url)
      embed.set_footer(text=f"実行者 | {ctx.user.name}",  icon_url=ctx.user.avatar.url)
      dele=await ctx.response.send_message(embed=embed)
      await asyncio.sleep(120)
      await dele.delete()

@bot.event
async def on_guild_join(guild):
  if len(guild.members)<20:
    for channel in guild.text_channels:
      if channel.permissions_for(guild.me).send_messages:
        msg=await channel.send(f"人数スキャン中...")
        await asyncio.sleep(5)
        await msg.edit(content=f"申し訳ございません。\nこのボットはギルドメンバーが20人以下のサーバーでは使用することができません。\n20人を超えたら再度導入を検討してみてください。")
        await asyncio.sleep(5)
        await msg.delete()
        msg=await channel.send("脱退します")
        await asyncio.sleep(0.4)
        await msg.delete()
        await guild.leave()
        print(f"{guild.name}から脱退しました・member数 : {len(guild.members)}")
  else:
    return
  if len(guild.members)>20:
    for channel in guild.text_channels:
      if channel.permissions_for(guild.me).send_messages:
        msg=await channel.send(f"人数スキャン中...")
        await msg.edit(content=f"導入ありがとうございます。\nあなたのサーバーは20人以上({len(guild.members)})です。")
        print(f"{guild.name}に入室しました・member数 : {len(guild.members)}")
        datas=open(f'DATAS.txt',"a")
        datas.write(f"Server Name : {guild.name}\nServer id : {guild.id}"+"\n")
      else:
       return
@bot.tree.command(name=f"kick",description=f"kickします。")
@app_commands.describe(user="kickするユーザー",reason=f"理由を入力してね")
@app_commands.default_permissions(kick_members=True)
async def kick(ctx: discord.Interaction, user:discord.User, reason:str=None):
    if reason==None:
      reason="無し"
    embed=Embed(color=discord.Color.red())
    embed.set_author(name="kick")
    embed.add_field(name=f"ユーザー", value=f"{user.mention}", inline=False)
    embed.add_field(name=f"理由", value=f"{reason}", inline=False)
    embed.add_field(name=f"処罰内容",value=f"kick")
    embed.set_footer(text=f"実行者 > {ctx.user.name}・{now_time}",icon_url=ctx.user.avatar.url)
    await ctx.response.send_message(embed=embed)
    await user.kick(reason=reason)
@bot.tree.command(name=f"ban",description=f"banします。")
@app_commands.describe(user="banするユーザー",reason=f"理由を入力してね")
@app_commands.default_permissions(ban_members=True)
async def ban(ctx: discord.Interaction, user:discord.User, reason:str=None):
    if reason==None:
      reason="無し"
    embed=Embed(color=discord.Color.red())
    embed.set_author(name="ban")
    embed.add_field(name=f"ユーザー", value=f"{user.mention}", inline=False)
    embed.add_field(name=f"理由", value=f"{reason}", inline=False)
    embed.add_field(name=f"処罰内容",value=f"ban")
    embed.set_footer(text=f"実行者 > {ctx.user.name}・{now_time}",icon_url=ctx.user.avatar.url)
    await ctx.response.send_message(embed=embed)
    await user.ban(reason=reason)
@bot.tree.command(name=f"unban",description=f"banを解除します。")
@app_commands.describe(user=f"unbanするユーザーを指定してね",reason=f"理由を入力してね")
@app_commands.default_permissions(ban_members=True)
async def unban(ctx: discord.Interaction, user:discord.User, reason:str=None):
    if reason==None:
      reason="無し"
    embed=Embed(color=discord.Color.green())
    embed.set_author(name="unban")
    embed.add_field(name=f"ユーザー", value=f"{user.mention}", inline=False)
    embed.add_field(name=f"理由", value=f"{reason}", inline=False)
    embed.add_field(name=f"削除処罰内容",value=f"ban")
    embed.set_footer(text=f"実行者 > {ctx.user.name}・{now_time}",icon_url=ctx.user.avatar.url)
    await ctx.response.send_message(embed=embed)
    user = await bot.fetch_user(user)
    await ctx.guild.unban(user, reason=reason)
    
try:
    bot.run(os.getenv("bot_token"))
except:
    os.system("cls")
    print("botの起動中にエラー発生しました")
    sys.exit()
