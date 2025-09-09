import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("채팅 채널 알림 봇이 준비되었습니다!")

@bot.event
async def on_member_join(member):
    channel_id = 1414622920008925336
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f"🎉 **{member.display_name}**님이 서버에 입장했습니다! / 테토")

@bot.event
async def on_member_remove(member):
    channel_id = 1414622920008925336
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f"👋 **{member.display_name}**님이 서버에서 나갔습니다! / 에겐")

# 환경 변수에서 토큰 가져오기
bot.run(os.getenv('DISCORD_TOKEN'))