from __future__ import annotations
from .config import ApplicationConfig, get_config

from shiprts.core.application import Window


class ApplicationContext:

    def __init__(self) -> None:
        self.config: ApplicationConfig
        self.window: Window
