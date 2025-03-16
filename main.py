from core.client import BaseClient
from core.deepseek_client import DeepSeekClient
from core.gemini_client import GeminiClient
from core.gpt_client import GPTClient
from funcs.test_build import run_test


def main(model: BaseClient):
    model.generate_and_save_test_cases()
    run_test()
    model.generate_report()

if __name__ == '__main__':
    gemini = GeminiClient()
    main(gemini)

    """
    or: 
    
    gpt = GPTClient()
    main(gpt)
    
    deepseek = DeepSeekClient()
    main(deepseek)
    
    ... ...
    
    """

