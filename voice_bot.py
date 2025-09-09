import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("채팅 채널 알림 🤖이 준비되었습니다!")

@bot.event
async def on_member_join(member):
    channel_id = 1414622920008925336
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f"🎉 **{member.display_name}**님이 서버에 쳐들어왔습니다! / 테토")

@bot.event
async def on_member_remove(member):
    channel_id = 1414622920008925336
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f"👋 **{member.display_name}**님이 서버에서 도망쳤습니다! / 에겐")

# 봇 토큰 설정 (환경변수에서 가져오기)
TOKEN = os.getenv('DISCORD_TOKEN')

try:
    print("🤖 봇을 시작하는 중...")
    bot.run(TOKEN)