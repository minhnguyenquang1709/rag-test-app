from pydantic import BaseModel
from typing import Literal, Any, Dict, List, Optional


class ParamSpec(BaseModel):
    name: str
    label: str
    type: Literal["int", "float", "bool", "string", "select"]
    default: Any
    min: Optional[float] = None
    max: Optional[float] = None
    step: Optional[float] = None
    options: Optional[List[Any]] = None  # for select


class StrategyDescriptor(BaseModel):
    key: str
    display_name: str
    params: List[ParamSpec]

# each strategy provides a descriptor -> backend is the source of truth for available strategies