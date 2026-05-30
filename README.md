# Galactic Space Reborn

![Status Badge](https://img.shields.io/badge/Status-In_Development-orange)
![Version Badge](https://img.shields.io/badge/Version-Dev_Build_7.4.1-green)

**Galactic Space Reborn** is a fast-paced space shooter where you blast enemies, collect power-ups, and dodge obstacles. Fight through increasingly difficult levels and take down bosses to prove who can achieve the highest score.

This repository archives game versions, showcases upcoming features, and serves as the home for `Project: Galaxy`.

> [!NOTE]
> The Makey Makey is currently only available in the MakeCode Arcade Version, no plans in the Pygame version
>
> There are plans however for adding Controller support in pygame

---

## Licenses

[![MIT](https://img.shields.io/badge/Code-MIT-green)](https://github.com/Ghosted-Alex/Galactic_Space_Reborn/blob/main/LICENSE_MIT)\
[![CCO](https://img.shields.io/badge/Assets-CCO-blue)](https://github.com/Ghosted-Alex/Galactic_Space_Reborn/blob/main/LICENSE_CCO)

---

## Requirements

|              | Minimum          | Recommended        |
|--------------|:----------------:|:------------------:|
| **Python**   | 3.10             | 3.13               |
| **Pygame**   | 2.1.3            | 2.5.7              |
| **Json5**    | 0.10.0           | 0.14.0             |

## Download & How to Play

### Download

You can download the assets and source code of the game

There are 2 ways to download/play the game currently:

- You can Git Clone the Repo by using

    ```bash
    git clone https://github.com/Ghosted-Alex/Galactic_Space_Reborn
    ```

- Or you can go to the [releases](https://github.com/Ghosted-Alex/Galactic_Space_Reborn/releases) and click one of the releases and click/tap `Galactic Space Beta #.# Here`

> [!NOTE]
> The game is still in development which means not all features are in from the MakeCode Arcade version with the fact that there is no relaease, yet.

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

### Game Updates

![Version Badge](https://img.shields.io/badge/Version-Dev_Build_8-green)
![Update Badge](https://img.shields.io/badge/Update_Type-Major-red)

#### Major Engine Overhaul

- Seperated UI and Updates to `ui.py` and `update.py` respectively
- Added `ui.py`
- Added `update.py`
- Moved `animation.py`, `assets.py`, `bullet.py`, `entity.py`, `powerup.py` into `src` folder
- Added `src` and `assets` folders

### [Full Changelog](./FULL_CHANGELOG.md)

---

#### REPO UPDATES

- Added `FULL_CHANGELOG.md`

> [!NOTE]
> Repo Updates are only included if major updates to the repo take place,
> please note that the new `FULL_CHANGELOG.md` file will NOT
> include repo updates and the `Game Updates` section will be maxed out at 5 bulletpoints,
> the rest will be put into `FULL_CHANGELOG.md` file.
