
class LLMResponse:
    def __init__(self, text: str, source_documents: list):
        self.text = text
        self.source_documents = source_documents