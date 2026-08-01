# Galactic Space Reborn

## Full Changelog

![Version Badge](https://img.shields.io/badge/Version-Dev_Build_8-green)
![Update Badge](https://img.shields.io/badge/Update_Type-Major-red)

### Dev Build 8 — Major Engine & Architecture Overhaul

*This build includes a complete rewrite of core systems and substantial graphical overhauls.*

#### 🎮 Graphics, Audio & User Interface (UI/UX)

- **Pre-Roll Splash Screen**: Implemented pre-roll splash presentation (`show_pre_roll()`) configured dynamically via `manifest.json`. Supports press-any-key or click skipping for improved onboarding.
- **Screen Resolution & Scaling**: Upgraded native screen resolution to **1072 × 861** px, updating the global `SPRITE_SCALING` constant to `3`.
- **Asset Manifest Schema Overhaul**: The core manifest structure was upgraded to support greater flexibility and detail:
  - **Texture Support**: Now accepts custom scaling factors (e.g., `"scale": float`).
  - **Audio/Sound Support**: Entries now allow for custom volume levels (e.g., `"volume": float`).
  - **New Asset Registrations**: Added manifest entries to support multiple player ship variants (`player0`–`3`), laser bolt types (`bullet0`–`3`), shooting effect (`effect_shoot`), and the UI pre-roll splash (`pre_roll`).
- **Screens/Scenes**: Added the ability to add more menus/scenes and added a scene system, a few included are:
  - **title**: A title scene.
  - **options**: A scene to change options... more options will be included soon.
  - **play/difficulty**: The scene that shows when Play Game button is pressed.
  - **gameplay**: The scene where the actual game takes place.

#### ⚡ Event & Game Loop Refactoring

*The core game loop logic was modularized by extracting key functions into an observable Event Bus.*

- **Modular Event Bus (`src/events.py`)**: Extracted inline main loop logic into overridable event functions, centralizing control and improving testability:
  - `events.spawn_enemy()` — Handles enemy spawning, formation logic, and type rolls.
  - `events.spawn_powerup()` — Manages powerup drop chance evaluation.
  - `events.on_shoot()` — Controls bullet creation, sound effects triggers, and energy deduction.
  - `events.on_score_increment()` — Centralized score calculation logic and capping mechanism.
  - `events.save_high_score()` / `events.load_high_score()` — Handles high score persistence across sessions.
  - `events.on_game_over()` — Triggers death sound sequences and manages the game over state transition.

#### 🔒 Security & Architecture Improvements

- **Vulnerability Remediation**: Completely removed all instances of `custom_executables` (pre/post/wrapper script subprocess execution) from launcher and validator to eliminate critical security vulnerabilities.
- **Standalone Vanilla Execution**: Decoupled asset loading and core engine loops, allowing the game to run 100% standalone without dependency on `src/mod.py`.
- **Advanced Mixin Features**: Expanded `MixinHelper` with explicit `RETURN` injection points and formalized the `@api.mixin.redirect()` decorator usage.
- **Priority-Ordered Mixins**: Added support for priority dictionary entries in manifest mixin declarations (`{"file": "name", "priority": 10}`).

---

### Previous Structural Updates (Historical Changelog)

#### Major File & Directory Restructure (Pre-DevBuild_8)

- Separated UI and Update logic into dedicated modules: `src/ui.py` and `src/update.py`.
- Consolidated various source files (`animation.py`, `assets.py`, `bullet.py`, `entity.py`, `powerup.py`) into the central `src/` directory for better namespace management.
- Structured the entire asset tree under a dedicated, organized `assets/` folder.
