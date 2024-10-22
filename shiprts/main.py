from sys import argv

from .core.context_impl import ApplicationContext
from shiprts import set_context


def main() -> None:
    args = argv[1:] or [
        "default",
    ]
    ctx = ApplicationContext.parse(args)
    set_context(ctx)

    ctx.initialise()
    ctx.launch()
