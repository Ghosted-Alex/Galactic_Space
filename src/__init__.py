"""Extends from main.py"""

from . import (animation,
               assets,
               bullet,
               controls,
               entity,
               events,
               powerup,
               ui,
               update,
               starfield,
               stats,
               clock,
               states)

try:
    from . import pack
except ImportError:
    pack = None

__all__ = [
    animation,
    assets,
    bullet,
    controls,
    entity,
    events,
    powerup,
    ui,
    update,
    starfield,
    stats,
    clock,
    states
]

if pack is not None:
    __all__.append(pack)