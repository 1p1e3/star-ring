import json
import sys
from pathlib import Path
from typing import Union

from conf import TEST_CASE_PATH


def read_api_doc_from_json(file: Union[str, Path]) -> str:
    with open(file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return str(data)

def read_case_from_json(file: Union[str, Path]) -> dict:
    with open(file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return dict(data)


def write_case_to_json(data: str) -> str | None:
    try:
        final_data = json.loads(data)
        with open(TEST_CASE_PATH, "w", encoding="utf-8") as json_file:
            json.dump(final_data, json_file, ensure_ascii=False, indent=4)

        # 检查本地是否有该文件
        if TEST_CASE_PATH.exists():
            return f"用例成功写入文件: {TEST_CASE_PATH}"

    except Exception as e:
        print(f"用例写入文件失败: {e}")


def read_prompt(file: Union[str, Path]) -> str:
    with open(file, "r", encoding="utf-8") as prompt_file:
        prompt = prompt_file.read()
    return prompt


def write_test_report_to_json(data: list):
    json_data = {
        "report": data
    }
    with open(TEST_CASE_PATH, "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

