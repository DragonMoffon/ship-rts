from __future__ import annotations

from shiprts.core.application import View


class TEMPLATEView(View):

    def __init__(self) -> None:
        super().__init__()

    def on_draw(self) -> None:
        self.clear()
