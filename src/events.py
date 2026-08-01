"""Events Module — Overridable game loop functions exposed to the Modding API.

Every function here is a named hook that mods can target with:
  api.mixin.overwrite(api.events, 'function_name', replacement)
  api.mixin.inject(api.events, 'function_name', at='HEAD')
  api.mixin.inject(api.events, 'function_name', at='TAIL')
"""

import random
import pygame
import config

from . import entity
from . import bullet
from . import powerup
from . import assets
from . import stats
from . import states
from . import animation


# =============================================================================
# SPAWNING events
# =============================================================================

def spawn_enemy(enemies: list) -> None:
    """Spawns a new enemy and appends it to the active enemies list.

    Override this to change enemy types, spawn positions, spawn rates,
    formations, or turn the game into something like Space Invaders entirely.

    Args:
        enemies: The live enemies list from the game loop.
    """
    enemy_chance = random.randint(0, 2)
    shield = (enemy_chance == 2)
    new_enemy = entity.Enemy(1000, random.randint(48, 816), enemy_chance, shield=shield)
    enemies.append(new_enemy)


def spawn_powerup(chance: int, player, powerups: list) -> None:
    """Evaluates a chance roll and conditionally spawns a powerup.

    Override this to change drop rates, add new powerup types, or make
    drops context-sensitive in completely different ways.

    Args:
        chance: A random integer (1-100) rolled by the game loop.
        player: The live Player instance.
        powerups: The live powerups list from the game loop.
    """
    # Health Wrench -- 15% base chance when player isn't full health
    if player.health <= 95 and 1 <= chance <= 15:
        print("Wrench Powerup Summoned!")
        new_powerup = powerup.Spawn(1000, random.randint(48, 816), 0)
        powerups.append(new_powerup)

    # Energy Cell -- 10% base chance when player isn't full energy
    elif player.energy <= 95 and 16 <= chance <= 25:
        print("Energy Powerup Summoned!")
        new_powerup = powerup.Spawn(1000, random.randint(48, 816), 2)
        powerups.append(new_powerup)

    # Power Wrench (Invincibility) -- 5% flat chance, only if no powerup is active
    elif not states.powerup_active and 50 <= chance <= 55:
        print("Power Wrench Powerup Summoned!")
        new_powerup = powerup.Spawn(1000, random.randint(48, 816), 1)
        powerups.append(new_powerup)


# =============================================================================
# PLAYER ACTION events
# =============================================================================

def on_shoot(player, effects: list, bullets: list) -> bool:
    """Called when the player attempts to fire a bullet.

    Override this to change bullet type, cost, count, spread, cooldown,
    or any other shoot behavior.

    Args:
        player: The live Player instance.
        bullets: The live bullets list from the game loop.
        effects: The live shooting animation

    Returns:
        True if a bullet was successfully fired, False if energy was too low.
    """
    if player.energy > 0:
        # Create bullet
        new_bullet = bullet.Normal(player.rect.centerx, player.rect.centery)
        bullets.append(new_bullet)
        
        # Create and add effect slightly in front of the player
        # Adjust '+ 20' to match your player width
        new_effect = animation.ShootEffect(player.rect.right, player.rect.centery - 16)
        effects.append(new_effect)
        
        assets.Sounds.player_shoot.play()
        player.energy -= 5
        return True
    else:
        pygame.mixer.Sound.play(assets.Sounds.fail)
        states.blink_timer = 0
        return False


# =============================================================================
# SCORING events
# =============================================================================

def on_score_increment(amount: int = 1) -> None:
    """Called every time the score should increase.

    Override this to multiply scores, add combo bonuses, clamp differently,
    or route score changes to an external system.

    Args:
        amount: How much to add to the score (default: 1).
    """
    stats.score += amount


# =============================================================================
# HIGH SCORE I/O events
# =============================================================================

def save_high_score(score: int, path) -> None:
    """Saves the high score to disk.

    Override this to change the save location, file format (e.g. JSON),
    or add a remote leaderboard write.

    Args:
        score: The score value to persist.
        path:  The target file path (pathlib.Path or str).
    """
    with open(path, "w") as file:
        file.write(str(score))
    print(f"[events] High score saved: {score} -> {path}")


def load_high_score(path) -> int:
    """Loads the high score from disk.

    Override this to change the load source, file format, or pull from
    a remote leaderboard instead.

    Args:
        path: The source file path (pathlib.Path or str).

    Returns:
        The loaded high score as an integer.
    """
    with open(path, "r") as file:
        return int(file.read().strip())


# =============================================================================
# GAME STATE events
# =============================================================================

def on_game_over() -> None:
    """Called when the player's health reaches zero.

    Override this to change death behavior -- play a different sound,
    trigger a cutscene, delay the game-over screen, add a revival mechanic,
    or anything else.
    """
    print("Game Over!")
    assets.Sounds.player_death.play()
    states.game_over = True
