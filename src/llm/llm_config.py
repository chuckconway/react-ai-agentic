
class LLMConfig:
    def __init__(self, temperature: float, max_output_tokens: int, top_p: float, candidate_count: int, seed: int):
        self.temperature = temperature,
        self.top_p = top_p,
        self.candidate_count = candidate_count,
        self.max_output_tokens = max_output_tokens,
        self.seed = seed