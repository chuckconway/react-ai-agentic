import unittest

from src.llm.models.cohere_model import CohereModel
from src.react.agent import Message


class TestCohere(unittest.TestCase):
    def test_cohere(self):
        model = CohereModel()
        response = model.generate_content([Message(role="user", content="Write a title for a blog post about API design. Only output the title text.")])

        print(response.text)