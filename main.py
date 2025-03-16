from core.gemini_client import GeminiClient
from funcs.test_build import run_test


def main():
    gemini = GeminiClient()
    gemini.generate_and_save_test_cases()
    run_test()
    gemini.generate_report()

if __name__ == '__main__':
    main()