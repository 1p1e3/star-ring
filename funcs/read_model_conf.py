import toml
from conf import MODEL_INFO_TOML_PATH


def read_model_conf(model_name: str) -> dict:
    model_info = toml.load(MODEL_INFO_TOML_PATH)
    return {
        "model": model_info[model_name]["model"],
        "api_key": model_info[model_name]["api_key"],
    }


