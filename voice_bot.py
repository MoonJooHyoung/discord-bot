import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # 서버 멤버 이벤트를 위해 추가

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("채팅 채널 알림 봇이 준비되었습니다!")

# 서버 입장 알림
@bot.event
async def on_member_join(member):
    channel_id = 1414622920008925336
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f"🎉 **{member.display_name}**님이 서버에 쳐들어왔습니다! / 테토")

# 서버 퇴장 알림
@bot.event
async def on_member_remove(member):
    channel_id = 1414622920008925336
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f"👋 **{member.display_name}**님이 서버에서 도망쳤습니다! / 에겐")

bot.run("MTQxNDc4Nzc0MzAxNTM3NDkxMA.Gh3Ttv.FcHCRCp2Ez-U9vYxoYByFeztnY_XZuC_KwlIGU")