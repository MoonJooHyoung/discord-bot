# Discord Voice Bot

디스코드 서버에서 멤버 입장/퇴장 알림을 보내는 봇입니다.

## 기능

- 멤버 입장 시 환영 메시지 전송
- 멤버 퇴장 시 퇴장 메시지 전송
- 커스텀 메시지 설정 가능

## 설치 및 실행

### 1. 의존성 설치
```bash
pip install discord.py python-dotenv
```

### 2. 환경 변수 설정
`.env` 파일을 생성하고 다음 내용을 추가하세요:
```
DISCORD_TOKEN=your_bot_token_here
```

### 3. 봇 실행
```bash
python voice_bot.py
```

## 설정

- `channel_id`: 메시지를 보낼 채널 ID
- `on_member_join`: 입장 메시지 내용
- `on_member_remove`: 퇴장 메시지 내용

## 주의사항

- 봇 토큰은 절대 공개하지 마세요
- `.env` 파일은 `.gitignore`에 포함되어 있습니다
