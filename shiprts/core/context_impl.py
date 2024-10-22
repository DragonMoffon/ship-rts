from __future__ import annotations
from typing import Self

from .context import ApplicationContext as Base

from .config import ApplicationConfig, get_config
from .application import Window


class ApplicationContext(Base):

    def __init__(self, config: ApplicationConfig) -> None:
        self.config: ApplicationConfig = config
        self.window: Window = None

    @classmethod
    def parse(cls: Self, args: list[str]) -> Self:
        config_name = args[0]
        return cls(get_config(config_name))
    
    def initialise(self) -> None:
        self.window = Window()

    def launch(self) -> None:
        self.window.run()