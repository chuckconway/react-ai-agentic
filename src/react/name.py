from enum import Enum, auto


class Name(Enum):
    """
    Enumeration for tool names available to the agent.
    """
    WIKIPEDIA = auto()
    GOOGLE = auto()
    NONE = auto()

    def __str__(self) -> str:
        """
        String representation of the tool name.
        """
        return self.name.lower()