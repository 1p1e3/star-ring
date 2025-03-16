from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union, Any


class BaseClient(ABC):

    @abstractmethod
    def function_declaration(self) -> Any:
        pass

    @abstractmethod
    def generate_and_save_test_cases(self):
        pass

    @abstractmethod
    def generate_report(self):
        pass

