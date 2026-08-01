"""Extends from main.py"""

from . import animation, assets, bullet, controls, entity, events, powerup, ui, update, starfield, stats, clock, states

try:
    from . import mod
except ImportError:
    mod = None

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

if mod is not None:
    __all__.append(mod)