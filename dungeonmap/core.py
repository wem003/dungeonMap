from __future__ import annotations
import random
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Config:
    width: int = 50
    height: int = 25
    coverage: float = 0.65
    seed: int | None = None
    border: bool = False

def _empty_grid(w: int, h: int) -> List[List[bool]]:
    return [[False for _ in range(w)] for _ in range(h)]

def _in_bounds(x: int, y: int, w: int, h: int) -> bool:
    return 0 <= x < w and 0 <= y < h

def _drunken_walk(grid: List[List[bool]], cfg: Config, rng: random.Random):
    H, W = len(grid), len(grid[0])
    x, y = rng.randrange(W), rng.randrange(H)
    grid[y][x] = True
    carved = 1
    target = int(cfg.coverage * W * H)
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while carved < target:
        dx, dy = rng.choice(dirs)
        nx, ny = x + dx, y + dy
        if _in_bounds(nx, ny, W, H):
            x, y = nx, ny
            if not grid[y][x]:
                grid[y][x] = True
                carved += 1
    return grid

def _to_ascii(grid: List[List[bool]]) -> str:
    return "\n".join("".join("." if c else "#" for c in row) for row in grid)

def _with_border(txt: str) -> str:
    lines = txt.splitlines()
    if not lines:
        return txt
    w = len(lines[0])
    top = "+" + "-"*w + "+"
    body = [f"|{ln}|" for ln in lines]
    return "\n".join([top, *body, top])

def generate(cfg: Config) -> str:
    rng = random.Random(cfg.seed)
    grid = _empty_grid(cfg.width, cfg.height)
    _drunken_walk(grid, cfg, rng)
    ascii_map = _to_ascii(grid)
    if cfg.border:
        ascii_map = _with_border(ascii_map)
    return ascii_map
