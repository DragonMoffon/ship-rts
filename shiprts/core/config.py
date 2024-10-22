from __future__ import annotations
from typing import TypedDict


class _ConfigDict(TypedDict):
    window_width: int
    window_height: int
    window_title: str
    update_rate: float
    fixed_rate: float


class ApplicationConfig:

    def __init__(self):
        pass

    @classmethod
    def deserialise(cls) -> ApplicationConfig:
        pass

    def serialise(self) -> _ConfigDict:
        pass
