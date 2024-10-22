from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

import tomllib
import tomli_w

from resources.filefactory import make_path_finder
import resources.config as config


@dataclass(slots=True)
class WindowConfig:
    width: int = 1280
    height: int = 720
    title: str = "Ships!"
    update_rate: float = 1/60.0
    fixed_rate: float = 1/20.0
    draw_rate: float = 1/60.0


@dataclass(slots=True)
class ApplicationConfig:
    name: str
    window: WindowConfig


get_config_path = make_path_finder(config, 'toml')

def get_config(name: str) -> ApplicationConfig:
    path = get_config_path(name)
    with open(path) as config_fp:
        data = tomllib.load(config_fp)
    print(data)
    return ApplicationConfig(
        data['name'],
        WindowConfig(**data.get('window', {}))
    )

def put_config(config: ApplicationConfig) -> dict[str, Any]:
    app = asdict(config)
    path = get_config_path(config.name)
    with open(path, 'wb') as config_fp:
        tomli_w.dump(app, config_fp)
    return app
