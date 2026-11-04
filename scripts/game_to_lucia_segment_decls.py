# a helper script to connect with a different project whose current codename is "lucia-wm"

#!/usr/bin/env python3
import argparse
from pathlib import Path

ROOTDIR = (Path(__file__).parents[1] / "data" / "games").resolve()
PATHPREFIX = ROOTDIR
PATHSUFFIX = "orientazioniReduxOutput/merged.csv"

def main():
    parser = argparse.ArgumentParser(description="mario2lucia generator")
    parser.add_argument('-g', '--games', nargs='+', help="List of game names")
    parser.add_argument('--glob', default=None, help="Search game names wia a glob expression rather than providing a list of names")
    args = parser.parse_args()

    # mutual exclusivity of game list selection
    game_names = None
    if args.games:
        game_names = args.games
    if args.glob:
        if game_names is not None:
            raise RuntimeError("Exactly one definition of games (--games, --glob)")
        game_names = sorted(gdir.name for gdir in ROOTDIR.glob(args.glob))
    if game_names is None:
        raise RuntimeError("Exactly one definition of games (--games, --glob)")

    for gname in game_names:
        game_path = ROOTDIR / gname
            
        for item in sorted(game_path.iterdir()):
            if item.is_dir() and item.name.startswith("gc_section_"):
                print(f"{gname}/{item.name}: {PATHPREFIX}/{gname}/{item.name}/{PATHSUFFIX}")

if __name__ == "__main__":
    main()