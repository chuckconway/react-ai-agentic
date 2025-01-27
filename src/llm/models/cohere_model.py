import os

import cohere

from src.llm.llm_config import LLMConfig
from src.llm.llm_response import LLMResponse
from src.llm.models.generative_model import GenerativeModel
from src.react.message import Message

api_key =  os.getenv('COHERE_API_KEY')

class CohereModel(GenerativeModel):
    def __init__(self):
        self.config = LLMConfig(
            temperature=0.0,
            top_p=1.0,
            candidate_count=1,
            max_output_tokens=8192,
            seed=12345)

    def generate_content(self, contents: list[Message]) -> LLMResponse:
        co = cohere.ClientV2(api_key=api_key)
        res = co.chat(
            model="command-r-plus-08-2024",
            messages=contents,
        )

        return LLMResponse(res.message.content[0].text, [])
