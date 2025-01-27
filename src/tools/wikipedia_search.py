import json
from typing import Optional

import wikipediaapi

from src.config.logging import logger
from src.tools.toolbase import ToolBase


class WikipediaSearch(ToolBase):
    @property
    def name(self) -> str:
        return "Wikipedia"

    def search(self, query: str) -> str | None:
        """
        Fetch Wikipedia information for a given search query using Wikipedia-API and return as JSON.

        Args:
            query (str): The search query string.

        Returns:
            Optional[str]: A JSON string containing the query, title, and summary, or None if no result is found.
        """
        # Initialize Wikipedia API with a user agent
        wiki = wikipediaapi.Wikipedia(user_agent='Chuck Conway (charles.conway@mailme.com)',
                                      language='en')

        try:
            logger.info(f"Searching Wikipedia for: {query}")
            page = wiki.page(query)

            if page.exists():
                # Create a dictionary with query, title, and summary
                result = {
                    "query": query,
                    "title": page.title,
                    "summary": page.summary
                }
                logger.info(f"Successfully retrieved summary for: {query}")
                return json.dumps(result, ensure_ascii=False, indent=2)
            else:
                logger.info(f"No results found for query: {query}")
                return None

        except Exception as e:
            logger.exception(f"An error occurred while processing the Wikipedia query: {e}")
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