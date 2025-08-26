# Runtime-enforced contracts: abc.ABC

- abc.ABC: enforce that subclasses implement certain methods **at runtime**.
  - use when want to guarantee a class implements specific behaviors before it can be instantiated.
  - heavier than typing.Protocol, as it involves runtime checks.

# static type-checking only: typing.Protocol

- typing.Protocol: define a shape of a class
  - use in business logic contracts (lightweight, TS-style, no runtime check).

# data shapes (like TS type aliases for objects): pydantic.BaseModel

# TypeScript -> Python equivalents

- TS interface (object shape) -> Python dataclasses.dataclass or pydantic.BaseModel

```python
# type hints only
from dataclasses import dataclass
from typing import Optional, Callable, Awaitable

@dataclass
class GameplayPopupProps:
    popup_type: str
    time_remaining: int
    distance: float
    level_id: str
    progress: float
    config: "IGameConfig"
    on_quit: Optional[Callable[["IGameData"], Awaitable[None]]] = None
    on_close: Optional[Callable[[], None]] = None
    restart_game: Optional[Callable[[], None]] = None


# with runtime check
from pydantic import BaseModel
from typing import Optional, Callable, Awaitable

class GameplayPopupProps(BaseModel):
    popup_type: str
    time_remaining: int
    distance: float
    level_id: str
    progress: float
    config: "IGameConfig"
    on_quit: Optional[Callable[["IGameData"], Awaitable[None]]] = None
    on_close: Optional[Callable[[], None]] = None
    restart_game: Optional[Callable[[], None]] = None
```

- TS enum -> Python enum.Enum

```python
from enum import Enum

class EGameState(str, Enum):
    READY = "ready"
    WAITING = "waiting"
    REACH_DESTINATION = "reach_destination"
    ACCELERATE = "accelerate"
    DECELERATE = "decelerate"
    RUNNING = "running"
    BOOST = "boost"
    END = "end"
    STOPPED = "stopped"

# remember to use EGameState.READY.value to get the actual value
```

- TS Optional property (?) -> Python Optional[type] (from 'typing' module)
- TS function type in interface -> Python method signature with type hints
- TS class with properties -> Python with attribute type hints

# Suggestions

- use pydantic.BaseModel for data models related to API
- use enum.Enum for static values -> easier to serialize to JSON
- use type hints + typing.Optional + typing.Callable for function props
- use dataclass for type hints only
