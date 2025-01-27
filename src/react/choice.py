from pydantic import BaseModel, Field

from src.react.name import Name


class Choice(BaseModel):
    """
    Represents a choice of tool with a reason for selection.
    """
    name: Name = Field(..., description="The name of the tool chosen.")
    reason: str = Field(..., description="The reason for choosing this tool.")