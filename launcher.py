# Be Aware, this is the launcher script for launching Galactic Space Reborn with Mods,
# only modify this file if you know what you are doing!

import os
import sys
import subprocess
from pathlib import Path

def main():
    print("=== Galactic Space Reborn Mod Launcher ===")
    
    # Track paths relative to this script
    root_dir = Path(__file__).resolve().parent
    mods_dir = root_dir / "mods"
    
    active_mod = None
    
    # 1. Intercept terminal arguments (e.g., python launcher.py --mod deep_space)
    if "--mod" in sys.argv:
        try:
            mod_idx = sys.argv.index("--mod")
            target_mod = sys.argv[mod_idx + 1]
            
            # Verify the mod folder actually exists
            if (mods_dir / target_mod).is_dir():
                active_mod = target_mod
                print(f"[Launcher] Mod found: '{active_mod}'. Initializing injection payload...")
            else:
                print(f"[Launcher] Error: Mod folder '{target_mod}' not found inside /mods/")
                sys.exit(1)
        except IndexError:
            print("[Launcher] Error: You must specify a mod folder name after the --mod flag!")
            sys.exit(1)
    else:
        target_mod = input("[Launcher] Enter a mod name, leave blank for vanilla\n\n>>> ")
        if (mods_dir / target_mod).is_dir():
            active_mod = target_mod
        elif not (mods_dir / target_mod).is_dir():
            print(f"[Launcher] Error: Mod folder '{target_mod}' not found inside /mods/")
            sys.exit(1)
        elif target_mod == "":
            print("Launching Vanilla Client")

    # 2. Pack the process environment data layer
    game_env = os.environ.copy()

    if active_mod:
        game_env["GSR_USE_MODS"] = "True"
        game_env["GSR_ACTIVE_MOD"] = active_mod
    else:
        game_env["GSR_USE_MODS"] = "False"

    py_executable = sys.executable

    # 3. Cleanly bootstrap main.py as a subprocess with our environment payload
    try:
        print("[Launcher] Executing core engine via main.py...\n")
        subprocess.run([py_executable, "main.py"], env=game_env, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[Launcher] Game exited with error code {e.returncode}.")
    except KeyboardInterrupt:
        print("\n[Launcher] Game execution terminated by user.")

if __name__ == "__main__":
    main()