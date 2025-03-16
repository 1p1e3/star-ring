import logging

import requests

from log.logger import Logger

logger = Logger().get_logger()

def request_build(api_info: dict):
    try:
        res = requests.request(
            method=api_info.get("method"),
            url=api_info.get("url"),
            headers=api_info.get("headers") or None,
            params=api_info.get("params") or None,
            json=api_info.get("json") or None,
        )
        logger.info("请求构建成功")
        return res
    except requests.exceptions.RequestException as e:
        logger.info(f"请求构建失败{e}")
