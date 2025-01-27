import abc

from src.llm.llm_response import LLMResponse


class GenerativeModel(abc.ABC):

    @abc.abstractmethod
    def generate_content(self, contents) -> LLMResponse:
        pass