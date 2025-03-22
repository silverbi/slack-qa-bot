import os
import pandas as pd
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from gpt_utils import generate_test_cases_from_row
from excel_utils import read_function_spec_from_excel, convert_to_testcase_df
import requests
from io import BytesIO

load_dotenv()

app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.event("file_shared")
def handle_file_shared_events(event, client, logger):
    try:
        file_id = event["file_id"]
        file_info = client.files_info(file=file_id)["file"]
        download_url = file_info["url_private_download"]
        channel_id = file_info["channels"][0]

        headers = {"Authorization": f"Bearer {os.environ['SLACK_BOT_TOKEN']}"}
        response = requests.get(download_url, headers=headers)
        spec_df = read_function_spec_from_excel(BytesIO(response.content))

        all_testcases = []
        for _, row in spec_df.iterrows():
            gpt_cases = generate_test_cases_from_row(row)
            for case in gpt_cases:
                case.update({
                    "0depth": row["0depth"],
                    "1depth": row["1depth"],
                    "2depth": row["2depth"],
                    "3depth": row["3depth"]
                })
                all_testcases.append(case)

        result_df = convert_to_testcase_df(all_testcases)
        output_path = "/tmp/testcases.xlsx"
        result_df.to_excel(output_path, index=False)

        client.files_upload(
            channels=channel_id,
            file=output_path,
            title="🧪 테스트케이스 자동 생성 결과",
            initial_comment="기능 명세서를 기반으로 생성된 QA 테스트케이스입니다 😊"
        )

    except Exception as e:
        logger.error(f"파일 처리 중 오류 발생: {e}")

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
