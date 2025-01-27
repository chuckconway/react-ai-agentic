import json
from typing import Optional

import wikipediaapi

from src.config.logging import logger
from src.tools.toolbase import ToolBase


class AskHuman(ToolBase):
    @property
    def name(self) -> str:
        return "Ask Human"

    def search(self, query: str) -> str | None:
        """
        Fetch Wikipedia information for a given search query using Wikipedia-API and return as JSON.

        Args:
            query (str): The search query string.

        Returns:
            Optional[str]: A JSON string containing the query, title, and summary, or None if no result is found.
        """

        try:
            logger.info(f"Asking Human for: {query}")
            user_input = input(query)
            return user_input

        except Exception as e:
            logger.exception(f"Human interaction failed: {e}")
            return None


if __name__ == '__main__':
    queries = ["Geoffrey Hinton", "Demis Hassabis"]

    wikipedia_search = WikipediaSearch()

    for q in queries:
        r = wikipedia_search.search(q)
        if r:
            print(f"JSON result for '{q}':\n{r}\n")
        else:
            print(f"No result found for '{q}'\n")