# 🤖 Slack QA 테스트케이스 생성 봇

기능 명세서 엑셀을 Slack에 업로드하면,  
GPT를 통해 자동으로 QA 테스트케이스 엑셀로 변환하여 다시 업로드해주는 챗봇입니다.  
로컬 환경에서 실행할 수 있습니다.

---

## 📦 주요 기능

- 기능 명세서(.xlsx)를 기반으로 테스트케이스 자동 생성 (GPT-4 기반)
- 슬랙 파일 업로드 이벤트 감지 → 엑셀 파싱 → 테스트케이스 생성 → 결과 파일 다시 업로드

---

## 🛠️ 설치 및 실행 방법 (macOS 기준)

### 1. 레포 클론

```bash
git clone https://github.com/your-username/slack-qa-bot.git
cd slack-qa-bot
```

### 2. Python 가상환경 생성 및 활성화

```bash
python3 -m venv venv
source venv/bin/activate
```

> ⓘ `python3`가 설치되어 있어야 합니다. 설치되어 있지 않다면 [Homebrew](https://brew.sh/)로 설치할 수 있습니다:

```bash
brew install python
```

### 3. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

> `pip` 설치 중 오류가 날 경우, `pip` 버전 확인 또는 `wheel` 설치:

```bash
pip install --upgrade pip
pip install wheel
```

### 4. 환경변수 파일 설정

`.env.example` 파일을 복사하여 `.env` 파일을 만들고, Slack과 OpenAI 키를 입력하세요.

```bash
cp .env.example .env
```

`.env` 파일 예시:

```env
SLACK_BOT_TOKEN=xoxb-슬랙봇토큰
SLACK_APP_TOKEN=xapp-앱레벨토큰
OPENAI_API_KEY=sk-오픈ai키
```

> Slack 토큰은 [Slack API 페이지](https://api.slack.com/apps)에서 앱을 생성 후 `OAuth & Permissions`와 `Socket Mode` 설정을 통해 얻을 수 있습니다.

### 5. 앱 실행

```bash
python main.py
```

앱을 실행한 상태에서, Slack 채널에 **기능 명세서 엑셀 파일(.xlsx)** 을 업로드하면 챗봇이 자동으로 테스트케이스 엑셀 파일을 생성하여 업로드해줍니다.

---

## ✅ 예시 시나리오

1. Slack에서 `.xlsx` 명세서 파일 업로드
2. 챗봇이 자동으로 인식하고 GPT API를 호출하여 테스트케이스 생성
3. 생성된 테스트케이스 엑셀 파일이 Slack에 자동 업로드됨

---

## 🔐 환경 변수 (.env)

```env
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_APP_TOKEN=xapp-your-app-level-token
OPENAI_API_KEY=sk-your-openai-key
```

---

## 🧾 기능 명세서 엑셀 형식

| no. | 0depth | 1depth | 2depth | 3depth | 주 기능 | 레이아웃 요소 | 요구사항 | 텍스트 | 플랫폼 | 우선순위 | 비고 |

---

## 🧪 생성된 테스트케이스 엑셀 형식

| no. | 0depth | 1depth | 2depth | 3depth | objective | precondition | test step | expected result | 결과 | Bug 티켓 | 비고 |

---

## 🧠 GPT 모델

- OpenAI GPT-4 사용
- 테스트케이스 생성 프롬프트는 화면 위치 + 기능/요구사항을 기반으로 구성

---

## 👤 만든 사람

- [@silverbi](https://github.com/silverbi)
