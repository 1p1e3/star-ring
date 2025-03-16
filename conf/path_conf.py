from pathlib import Path


# 根目录
ROOT_PATH = Path(__file__).absolute().parent.parent

# conf
CONF_PATH = ROOT_PATH.joinpath("conf")

# 模型信息配置文件
MODEL_INFO_TOML_PATH = CONF_PATH.joinpath('model_info.toml')

#  核心包
CORE_PATH = ROOT_PATH.joinpath('core')

# 提示词文件
PROMPTS_PATH = ROOT_PATH.joinpath('prompts')

PROMPT_FOR_GENERATE_TEST_CASE_PATH = PROMPTS_PATH.joinpath('prompt_for_generate_test_case.md')

# 函数工具包
FUNCS_PATH = ROOT_PATH.joinpath('funcs')

# 接口文档、用例、测试结果文件
FILES_PATH = ROOT_PATH.joinpath('files')

## api doc
API_DOC_PATH = FILES_PATH.joinpath("openapi.json")

# 测试用例
TEST_CASES_PATH = FILES_PATH.joinpath('test_cases.json')

# 测试报告
TEST_REPORT_PATH = FILES_PATH.joinpath('test_report.json')