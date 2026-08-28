# Galactic Space Reborn

## Full Changelog

![Version Badge](https://img.shields.io/badge/Version-1.0--beta.1-green)
![Update Badge](https://img.shields.io/badge/Update_Type-Beta-purple)

### 1.0-Beta.1 — Update Visuals & Fixed Bugs

> This beta for Release 1.0 includes some updates to some visuals and adds
> several quality-of-life improvements, also fixes a game breaking bug!

### NEW FEATURES
* Added Animations System
* Added the beginning part to the Invincibility Theme
* Added the Resource Pack API
* Added the Resource Pack Selection Screen
* Added a Pause Menu in game

#### Invincibility Theme
* Updated the Invincibility Theme to sound more filled and to add the beginning part

#### Animations
* Added the new Animations System
> **Developer's Note**: The animations stuff was added but the API is not clean
> to use, it will be cleaned up as the game develops but for now it is very
> messy to use and there is no clean way to use it.
* The Invincibility Power Up now shows a proper cutscene when interacted with

#### Resource Pack API
* Added the Resource Pack Selection Screen
* Added the Resource Pack API

> **Developer's Note**: I've added the Resource Pack API and currently in the
> process of making the wiki for it as well as for the rest of the game. Be
> aware that it will take a while to add everything necessary as not only
> this is a new API, but I am also the solo developer making this whole thing.
> I have added the Resource Pack Selection Screen, currently the game
> restarts when you are applying a resource pack, that is due to the fact
> that how I did the assets loading system doesn't allow for hot swapping
> assets.

### CHANGES
#### UI
* Loading Screen now shows what asset is loading at that time below the loading bar
* Main Menu now has a `Resource Packs` button
* Overhauled the Play screen to now have a `difficulty` button and a `Start Game` button
* The `gameplay` scene now has a pause menu overlay and will now pause the game when `ESC` is pressed
* Overhauled the Options Menu and now there is `Video` and `Music & Sounds` settings
* Options menu now modifies a new `settings.json` file
* Updated the title logo on the main menu and is now more detailed and uses a sprite now instead of text

#### Sprites
* Main Menu now uses a sprite for the title logo instead of text
* Updated 4th ship sprite to Teal, repurposing yellow for invincibility

#### Technical Changes
* There is a `@option_def` decorator for defining settings
  * It is defined like this: `@option_def(<key>, <name>, <values>, <order>, <description>)`
    * Example:
      * ```python
        @option_def("master_volume", "MASTER VOLUME", (0.0, 0.25, 0.5, 0.75, 1.0), order=0, description="Controls all game audio.")
        ```
* Resource Packs are now available in Beta, they are defined by a `manifest.json` file in the pack's directory, `assets/` folder is for overriding assets
* Made the difficulty mechanic functional, and now it serves as a multiplier
> **Developer's Note**: The Difficulty mechanic unlike in the original Microsoft
> zMakeCode Arcade version does not go up expanentially but should go up 
> linearly, also speed shouldn't be affected by difficulty anymore.
### BUG FIXES
* Fixed a crash bug where if you game over and get a high score, the game tries to call for a variable called `HIGH_SCORE_FILE` in the `src/stats.py` file where it actually is located in the `config.py` file
* Fixed a bug where the shoot animation was not appearing at the correct part of the ship

### RESOURCE PACK DOCUMENTATION

Resource Pack Documentation will be coming soon.
> **Developer's Note**: I am currently in the process of building the
> documentation, thank you for your patience.