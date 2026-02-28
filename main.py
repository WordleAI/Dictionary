import sys
import os
from termcolor import *

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

def help():
    print("")
    print("")
    cprint("Select a Wordle Service: Wordle Unlimited (--unlimited, solver) or NYTimes (--nytimes, latest answer only)", color="yellow", attrs=['bold'])
    cprint("Help: (--help)", color="yellow", attrs=['bold'])
    print("")

try:
    args = sys.argv[1]
    if args.lower() == "--nytimes":
        from services.nyTimes import *
        main()
    elif args.lower() == "--unlimited":
        from services.wordleUnlimited import *
        print("")
        print("")
        game_attempts = input("Number Of Puzzles: ")
        print("")
        main(game_attempts=int(game_attempts))
    elif args.lower == "--help":
        help()
    else:
     help()
except Exception as e:
    print("")
    print("")
    cprint(f"Error: {repr(e)}", color="red", attrs=['bold'])
    print("")