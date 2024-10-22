from __future__ import annotations

import arcade

from shiprts.core.application import View
from resources import load_png, load_toml


class AtlasView(View):

    def __init__(self):
        super().__init__()
        self.sheet_texture = load_png("atlas1", hash="atlas1")
        self.toml_data = load_toml("atlas1")
        self.cam = arcade.Camera2D(
            position=(self.sheet_texture.width / 2.0, self.sheet_texture.height / 2.0)
        )
        self.current_texture_idx = 0

    def on_draw(self) -> None:
        self.clear()
        with self.cam.activate():
            arcade.draw_texture_rect(
                self.sheet_texture,
                arcade.LBWH(
                    0.0, 0.0, self.sheet_texture.width, self.sheet_texture.height
                ),
                pixelated=False,
            )
            for idx, text in enumerate(self.toml_data["texture"]):
                if idx == self.current_texture_idx:
                    arcade.draw_text(text["name"], 0.0, 0.0)

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        if symbol == arcade.key.R:
            self.toml_data = load_toml("atlas1")
        elif symbol == arcade.key.DOWN:
            self.current_texture_idx = (self.current_texture_idx + 1) % len(
                self.toml_data["texture"]
            )
        elif symbol == arcade.key.UP:
            self.current_texture_idx = (self.current_texture_idx - 1) % len(
                self.toml_data["texture"]
            )
