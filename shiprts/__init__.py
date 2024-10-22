from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .core.context import ApplicationContext

__all__ = ('set_context', 'get_context')

class CTX:
    context: ApplicationContext = None

def set_context(ctx: ApplicationContext):
    CTX.context = ctx

def get_context() -> ApplicationContext:
    return CTX.context