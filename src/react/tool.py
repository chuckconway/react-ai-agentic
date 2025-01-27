from typing import Callable

from src.config.logging import logger

from src.react.name import Name
from src.react.observation import Observation


class Tool:
    """
    A wrapper class for tools used by the agent, executing a function based on tool type.
    """

    def __init__(self, name: str, func: Callable[[str], str]):
        """
        Initializes a Tool with a name and an associated function.

        Args:
            name (Name): The name of the tool.
            func (Callable[[str], str]): The function associated with the tool.
        """
        self.name = name
        self.func = func

    def use(self, query: str) -> Observation:
        """
        Executes the tool's function with the provided query.

        Args:
            query (str): The input query for the tool.

        Returns:
            Observation: Result of the tool's function or an error message if an exception occurs.
        """
        try:
            return self.func(query)
        except Exception as e:
            logger.error(f"Error executing tool {self.name}: {e}")
            return str(e)