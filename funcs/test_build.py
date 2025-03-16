import logging
import subprocess

import pytest

from conf import TEST_CASE_PATH
from funcs.json_handler import read_case_from_json
from funcs.request_build import request_build
import subprocess


cases = read_case_from_json(TEST_CASE_PATH)

from log.logger import Logger
logger = Logger().get_logger()

@pytest.mark.parametrize("case", cases, ids=[case_id for case_id in cases.keys()])
def test_build(case, request):
    logger.info(f"执行测试用例:{cases[case]}")
    request.node.description = cases[case].get("desc")

    res = request_build(cases.get(case))

    # 断言
    assert res.status_code == cases.get(case).get("expectedStatusCode")
    expectedFields = cases.get(case).get("expectedFields")
    if res.json().get("token") is not None:
        assert expectedFields.get("token") is not None
    else:
        assert res.json() == cases[case].get("expectedFields")


def run_test():
    subprocess.run(["pytest", "-s", ""])