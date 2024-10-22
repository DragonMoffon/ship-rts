from __future__ import annotations

import arcade

from shiprts.core.application import View
from resources import load_png, load_toml

MAX_ZOOM = 5
MIN_ZOOM = 1

class AtlasView(View):

    def __init__(self):
        super().__init__()
        self.sheet_texture = load_png("atlas1", hash="atlas1")
        self.toml_data = load_toml("atlas1")
        self.cam = arcade.Camera2D(
            position=(self.sheet_texture.width / 2.0, self.sheet_texture.height / 2.0)
        )
        self.current_texture_idx = 0

        self.zoom = 1

    def on_update(self, delta_time: float) -> bool | None:
        self.cam.zoom = arcade.math.smerp(self.cam.zoom, self.zoom, delta_time, 0.25)
        fraction = (self.cam.zoom - 1) / (MAX_ZOOM - 1)
        target = self.toml_data['texture'][self.current_texture_idx]
        goal = arcade.math.lerp_2d(
            (self.sheet_texture.width/2, self.sheet_texture.height/2),
            (target['x'] + target['width'] / 2.0, self.sheet_texture.height - target['y'] - target['height']/2.0),
            fraction
        )
        self.cam.position = arcade.math.smerp_2d(self.cam.position, goal, delta_time, 0.1)

    def on_draw(self) -> None:
        self.clear()
        with self.cam.activate():
            arcade.draw_texture_rect(
                self.sheet_texture,
                arcade.LBWH(
                    0.0, 0.0, self.sheet_texture.width, self.sheet_texture.height
                ),
                pixelated=True,
            )
            for idx, text in enumerate(self.toml_data["texture"]):
                if not text['height'] or not text['width']:
                    continue
                texture = arcade.LBWH(text['x'], self.sheet_texture.height - text['y'], text['width'], -text['height'])
                padding = arcade.XYWH(texture.x, texture.y, texture.width + 2 * text['padding'], texture.height - 2 * text['padding'])
                arcade.draw_rect_outline(
                    texture, arcade.color.RADICAL_RED, 1
                )
                arcade.draw_rect_outline(
                    padding, arcade.color.SEA_GREEN
                )
                arcade.draw_text(f'{idx}', x=texture.left + 0.1, y=texture.bottom - 0.1, color=arcade.color.BLACK, font_size=13, anchor_y='top')
                arcade.draw_text(f'{idx}', x=texture.left + 0.1, y=texture.bottom - 0.1, anchor_y='top')
        target = self.toml_data['texture'][self.current_texture_idx]
        arcade.draw_rect_filled(
            arcade.LBWH(0.0, 0.0, self.width, 25),
            arcade.color.BLACK
        )
        arcade.draw_text(
            f'{self.current_texture_idx}:{target['name']}', x=4, y=4, font_size=16
        )

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

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int) -> bool | None:
        if scroll_y > 0:
            self.zoom = min(MAX_ZOOM, self.zoom + 1)
        elif scroll_y < 0:
            self.zoom = max(MIN_ZOOM, self.zoom - 1)