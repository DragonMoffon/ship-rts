"""
The abstract base class for the ApplicationContext for typing. Think of this as `context.h`.
Saves me from writing `from typing import TypeChecking` absolutely everywhere
"""
# noqa
# fmt: off
from __future__ import annotations
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from .config import ApplicationConfig
    from .application import Window

class ApplicationContext:

    def __init__(self) -> None:
        self.config: ApplicationConfig = None
        self.window: Window = None
        raise NotImplementedError

    @classmethod
    def parse(cls: Self, args: list[str]) -> Self: raise NotImplementedError

    def initialise(self) -> None: raise NotImplementedError

    def launch(self) -> None: raise NotImplementedError
# fmt: on