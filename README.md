# Galactic Space Reborn [Beta]

Be aware this is the beta branch, there will be bugs but this is the branch where I'll be testing out new features in the game, this is also the branch that should have bugs get reported in, that means if you see any bugs, you are encouraged to report them in this branch.

At this point the game is close to release, just needs a few more features

![Status Badge](https://img.shields.io/badge/Status-In_Development-orange?style=flat-square)

**Galactic Space Reborn** is a fast-paced space shooter where you blast enemies, collect power-ups, and dodge obstacles. Fight through increasingly difficult levels and take down bosses to prove who can achieve the highest score.

This repository archives game versions, showcases upcoming features, and serves as the home for `Project: Galaxy`.

> [!NOTE]
> NOTE ON PLATFORM COMPATIBILITY:
>
> The dedicated makey makey implementation is currently limited to the MakeCode Arcade version. Controller support for the pygame port is not in development but is planned for a future release
---

## Licenses

[![MIT](https://img.shields.io/badge/Code-MIT-green?style=for-the-badge)](https://github.com/Ghosted-Alex/Galactic_Space_Reborn/blob/main/LICENSE_MIT)\
[![CCO](https://img.shields.io/badge/Assets-CCO-blue?style=for-the-badge)](https://github.com/Ghosted-Alex/Galactic_Space_Reborn/blob/main/LICENSE_CCO)

---

## Requirements

|              | **Minimum** | **Recommended** |
|--------------|:-----------:|:---------------:|
| **Python**   |    3.10     |      3.13       |
| **Pygame**   |    2.1.3    |      2.5.7      |

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

> [!NOTE]
> Development Status:
>
> This game is currently undergoing active development.
> Please note that features are continuously being added and refined across multiple platforms.

---

> [!IMPORTANT]
> I will be using a structured format to track both stable release builds and public beta milestones:
>
> * Release Builds:
>   * `#.#-build.yyyymmdd`
>     * Example: `1.0-build.20260820` (Release 1.0 build that was published on Augest 20 2026)
>   * `#.#-beta.#`
>     * Example: `1.0-beta.1` (Release 1.0 on its first beta iteration)

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

![Version Badge](https://img.shields.io/badge/Version-1.0--beta.1-green?style=plastic)
![Update Badge](https://img.shields.io/badge/Update_Type-Beta-purple?style=plastic)

- **Added**: 
  - Added Animations
  - Added Cutscenes
  - Added Resource Packs
- **Changes**:
  - Updated Loading Screen Visuals
  - Updated Title Screen Visuals
- **Bug Fixes**
  - Fixed a Crash when Hitting a Game Over on High Score
  - Fixed a rendering bug of shooting a bullet


---

**Want to know the technical details?** For a comprehensive breakdown of all additions, changes, and removals, please refer to the full changelog below:

### [Full Changelog](./FULL_CHANGELOG.md)
