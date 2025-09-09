# Discord Bot

Discord 서버에서 멤버 입장/퇴장 알림을 보내는 봇입니다.

## 설정 방법

1. Discord Developer Portal에서 봇을 생성하고 토큰을 복사합니다.
2. Railway에서 환경 변수를 설정합니다:
   - `DISCORD_TOKEN`: Discord 봇 토큰

## 로컬 실행

1. 필요한 패키지 설치:
   ```bash
   pip install -r requirements.txt
   ```

2. 환경 변수 설정:
   - `.env` 파일을 생성하고 `DISCORD_TOKEN=your_token_here` 추가

3. 봇 실행:
   ```bash
   python main.py
   ```

## Railway 배포

1. GitHub에 코드를 푸시합니다.
2. Railway에서 새 프로젝트를 생성합니다.
3. GitHub 저장소를 연결합니다.
4. 환경 변수 `DISCORD_TOKEN`을 설정합니다.
5. 빌드 명령어: `pip install -r requirements.txt`
6. 시작 명령어: `python main.py`
