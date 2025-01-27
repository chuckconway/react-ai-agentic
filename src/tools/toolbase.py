import abc

class ToolBase(abc.ABC):

    @abc.abstractmethod
    def search(self, query: str) -> str | None:
        pass

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass