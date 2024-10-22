from __future__ import annotations

from arcade import View as ArcadeView, Window as ArcadeWindow

from shiprts import get_context

__all__ = (
    'Window',
    'View',
    'ArcadeWindow',
    'ArcadeView'
)

class Window(ArcadeWindow):

    def __init__(self):
        ctx = get_context()
        super().__init__(
            ctx.config.window.width,
            ctx.config.window.height,
            ctx.config.window.title,
            update_rate=ctx.config.window.update_rate,
            fixed_rate=ctx.config.window.fixed_rate,
            draw_rate=ctx.config.window.draw_rate
        )
        self.show_view(View())

    @property
    def current_view(self) -> View:
        """
        The currently active view.

        To set a different view, call :py:meth:`~arcade.Window.show_view`.
        """
        return self._current_view

class View(ArcadeView):

    def __init__(self, window: Window | None = None) -> None:
        super().__init__(window)
