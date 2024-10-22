"""
A custom implimentation of `arcade.TextureAtlasBase` with spritesheet loading methods
"""

from pathlib import Path
import tomllib

from arcade import ArcadeContext, Texture
from arcade.texture_atlas import TextureAtlasBase

from PIL import Image


class SpriteSheet:

    def __init__(self, img_path: Path, data_path: Path) -> None:
        with open(img_path, "rb") as img_fp:
            self.img = Image.open(img_fp)


class TextureAtlas(TextureAtlasBase):

    def __init__(self, ctx: ArcadeContext, img_path: Path, data_path: Path):
        self._ctx = ctx
        self._max_size = self._ctx.info.MAX_VIEWPORT_DIMS
        self._source_sheet: SpriteSheet = SpriteSheet(img_path, data_path)
