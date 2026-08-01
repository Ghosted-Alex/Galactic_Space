# Galactic Space Reborn

![Status Badge](https://img.shields.io/badge/Status-In_Development-orange?style=flat-square)

**Galactic Space Reborn** is a fast-paced space shooter where you blast enemies, collect power-ups, and dodge obstacles. Fight through increasingly difficult levels and take down bosses to prove who can achieve the highest score.

This repository archives game versions, showcases upcoming features, and serves as the home for `Project: Galaxy`.

> [!NOTE] Platform Compatibility
> The dedicated Makey Makey implementation is currently limited to the MakeCode Arcade version. However, controller support for the Pygame port is actively planned and under development.

---

## Licenses

[![MIT](https://img.shields.io/badge/Code-MIT-green?style=for-the-badge)](https://github.com/Ghosted-Alex/Galactic_Space_Reborn/blob/main/LICENSE_MIT)\
[![CCO](https://img.shields.io/badge/Assets-CCO-blue?style=for-the-badge)](https://github.com/Ghosted-Alex/Galactic_Space_Reborn/blob/main/LICENSE_CCO)

---

## Requirements

|              | Minimum          | Recommended        |
|--------------|:----------------:|:------------------:|
| **Python**   | 3.10             | 3.13               |
| **Pygame**   | 2.1.3            | 2.5.7              |

## Download & How to Play

### Download

You can download the assets and source code of the game
There are 2 ways to download the game currently:

- You can Git Clone the Repo by using

    ```bash
    git clone https://github.com/Ghosted-Alex/Galactic_Space_Reborn
    ```

    or

    ```bash
    git clone https://gitlab.com/ghostedalex/Galactic_Space_Reborn
    ```

There are 2 ways to play the Legacy MakeCode Arcade version

You can go to the [releases on Github](https://github.com/Ghosted-Alex/Galactic_Space_Reborn/releases) or [Releases on GitLab](https://gitlab.com/ghostedalex/Galactic_Space_Reborn/-/releases) and click one of the releases and click `Galactic Space Beta #.#`

> [!NOTE] Development Status
> This game is currently undergoing active development.
> Please note that features are continuously being added and refined across multiple platforms.
> I plan for a formal Beta release phase before moving to final public release.

---

#### How to Play

1. Clone the repository:

   ```bash
   git clone https://github.com/Ghosted-Alex/Galactic_Space_Reborn
   cd Galactic_Space_Reborn
   ```

2. Install Dependancies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Game:

    ```bash
    python main.py
    ```

---

---

### Game Updates

![Version Badge](https://img.shields.io/badge/Version-Dev_Build_8-green?style=plastic)
![Update Badge](https://img.shields.io/badge/Update_Type-Major-red?style=plastic)

#### Major Gameplay Overhaul and Visual Refresh and Menus

- **Pre-Game Experience**: Added a dedicated splash screen sequence before game loading for better player onboarding and immersion.
- **Enhanced Scale**: Expanded the game window size to provide significantly more room for maneuvering and spectacular battles.
- **Horizontal Playfield**: Pivoted the entire gameplay experience from vertical to a sprawling horizontal layout, allowing for complex arena combat.
- **Visual Polish**: Complete sprite redesigns were implemented to seamlessly accommodate the new horizontal orientation and enhanced visual effects.
- **Improved Loading**: Major overhaul of asset parsing and loading routines, resulting in dramatically faster startup times and smoother transitions.
- **More Screens**: Added more menus such as the title menu, options menu, and play menu.

---

**Want to know the technical details?** For a comprehensive breakdown of all additions, changes, and removals, please refer to the full changelog below:

### [Full Changelog](./FULL_CHANGELOG.md)

<!-- ---

#### REPO UPDATES

- Added `FULL_CHANGELOG.md`

> [!NOTE]
> Repo Updates are only included if major updates to the repo take place,
> please note that the new `FULL_CHANGELOG.md` file will NOT
> include repo updates and the `Game Updates` section will be maxed out at 5 bulletpoints,
> the rest will be put into `FULL_CHANGELOG.md` file. -->
