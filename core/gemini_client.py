import json
import logging

from google import genai
from google.genai.types import GenerateContentConfig

from conf import PROMPT_FOR_GENERATE_TEST_CASE_PATH, API_DOC_PATH, TEST_REPORT_PATH
from core.client import BaseClient
from funcs.json_handler import read_prompt, read_api_doc_from_json, write_case_to_json
from funcs.read_model_conf import read_model_conf
from funcs.test_build import run_test
from log.logger import Logger

logger = Logger().get_logger()


class GeminiClient(BaseClient):
    def __init__(self):
        model_conf = read_model_conf("gemini")
        model_name = model_conf["model"]
        api_key = model_conf["api_key"]

        self.client = genai.Client(api_key=api_key)
        self.config = self.function_declaration()
        self.chat = self.client.chats.create(
            model=model_name,
            config=self.config
        )
        init_prompt = read_prompt(PROMPT_FOR_GENERATE_TEST_CASE_PATH)
        try:
            init_res = self.chat.send_message(init_prompt)
            logger.info(f"初始化 Gemini:{init_res.text}")
        except Exception as e:
            logger.error(f"Gemini 初始化失败:{e}")


    def function_declaration(self) -> GenerateContentConfig:
        config = GenerateContentConfig(tools=[
            write_case_to_json,
            run_test,
            self.generate_report
        ])
        return config

    def generate_and_save_test_cases(self):
        try:
            # 读取 api 文档并传给模型
            api_data = read_api_doc_from_json(API_DOC_PATH)
            res = self.chat.send_message(api_data)
            logger.info(f"解析 API 文档并生成用例: {res.text}")
        except Exception as e:
            logger.error(f"用例生成失败: {e}")


    def generate_report(self):
        with open(TEST_REPORT_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        res = self.chat.send_message("这是 json 格式的 pytest 框架的测试报告数据，请你总结归纳并返回结果: \n" + str(data) +
                                     "\n 你的总结要包含通过数、失败数、跳过数、通过率、失败率等信息，请换行输出这些信息")
        logger.info(f"测试结果统计: {res.text}")