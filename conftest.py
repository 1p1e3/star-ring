import pytest

from funcs.json_handler import write_test_report_to_json

test_descriptions = {}
test_results = []


def pytest_runtest_protocol(item, nextitem):
    # 保存节点的描述信息（如果存在）
    if hasattr(item, 'description'):
        test_descriptions[item.nodeid] = item.description

def pytest_runtest_logreport(report):

    # 只关心执行阶段的结果
    if report.when == "call":
        test_results.append({
            # 测试用例名称
            "name": report.nodeid,
            # 用例描述
            "description": test_descriptions.get(report.nodeid, ""),
            # 结果: "passed", "failed", "skipped"
            "outcome": report.outcome,
            # 执行时间
            "duration": report.duration,
            # 日志 (如果有)
            "log": report.caplog if hasattr(report, "caplog") else "",
            # 失败时的错误信息
            "error": str(report.longrepr) if report.failed else None
        })

def pytest_sessionfinish(session):
    write_test_report_to_json(test_results)


