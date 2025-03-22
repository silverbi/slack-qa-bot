import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_test_cases_from_row(row):
    prompt = f"""
다음은 앱의 기능 명세입니다.

- 화면 위치: {row['0depth']} > {row['1depth']} > {row['2depth']} > {row['3depth']}
- 주 기능: {row['주 기능']}
- 레이아웃 요소: {row['레이아웃 요소']}
- 요구사항: {row['요구사항']}
- 플랫폼: {row['플랫폼']}

이 기능을 테스트하기 위한 QA 테스트 케이스를 가능한 자세히 생성해주세요.
각 테스트케이스는 다음 항목을 포함해야 하며, 가능한 세분화해주세요:

1. objective
2. precondition
3. test step
4. expected result

결과는 JSON 배열 형식으로 반환해주세요.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return json.loads(response['choices'][0]['message']['content'])
