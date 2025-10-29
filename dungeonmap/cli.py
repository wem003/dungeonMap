# Allow running both "python -m dungeonmap.cli" and "python dungeonmap/cli.py"
try:
    from .core import Config, generate
except Exception:
    import sys, os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from core import Config, generate

import argparse
from pathlib import Path
import secrets  # for strong random seed
from typing import Optional

# Project root = parent of this file's directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
LATEST = DATA_DIR / "latest_map.txt"


def _normalize_coverage(cov: float) -> float:
    """
    Keep coverage in a sane range. Typical sweet spot is ~0.25..0.55.
    We'll clamp to [0.05, 0.90] to avoid degenerate outputs.
    """
    if cov < 0.05:
        print(f"[note] coverage {cov} too low; clamping to 0.05")
        return 0.05
    if cov > 0.90:
        print(f"[note] coverage {cov} too high; clamping to 0.90")
        return 0.90
    return cov


def _pick_seed(user_seed: Optional[int]) -> int:
    """
    If the user supplied a seed, use it. Otherwise, pick a strong random
    32-bit seed and print it so runs are reproducible later.
    """
    if user_seed is not None:
        return user_seed
    seed = secrets.randbits(32)
    print(f"[seed] {seed}")
    return seed


def main():
    p = argparse.ArgumentParser(description="ASCII dungeon generator")
    p.add_argument("--width", type=int, default=50, help="grid width (columns)")
    p.add_argument("--height", type=int, default=25, help="grid height (rows)")
    p.add_argument("--coverage", type=float, default=0.35,
                   help="0..1 fraction of tiles carved as floor (try 0.25–0.55)")
    p.add_argument("--seed", type=int, default=None,
                   help="reproducible RNG seed (omit to auto-generate & print one)")
    p.add_argument("--border", action="store_true",
                   help="draw a border box around the map")
    p.add_argument("--view", action="store_true",
                   help="print the last generated map without overwriting it")
    args = p.parse_args()

    if args.view:
        print(LATEST.read_text() if LATEST.exists() else "(no map yet)")
        return

    cov = _normalize_coverage(args.coverage)
    used_seed = _pick_seed(args.seed)

    cfg = Config(
        width=args.width,
        height=args.height,
        coverage=cov,
        seed=used_seed,
        border=args.border,
    )

    # Header for quick context
    print(f"[gen] {cfg.width}x{cfg.height} coverage={cfg.coverage:.2f} seed={used_seed} border={'on' if cfg.border else 'off'}")

    ascii_map = generate(cfg)
    print(ascii_map)
    LATEST.write_text(ascii_map)


if __name__ == "__main__":
    main()
