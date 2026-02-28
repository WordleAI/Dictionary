import requests
import os
import datetime
from termcolor import *
import time

def main():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("")
    print("")

    cprint("[WordleSolver/NYTimes] Starting Timer...", color="blue", attrs=['bold'])
    print("")

    start_time = time.time()

    cprint("[WordleSolver/NYTimes] Getting Current Date...", color="blue", attrs=['bold'])

    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    if month != 12 or month != 11 or month != 10:
        month = f"0{month}"

    print("")
    cprint("[WordleSolver/NYTimes] Loading Wordle Data From NYTimes...", color="blue", attrs=['bold'])

    print("")
    url = f"https://www.nytimes.com/svc/wordle/v2/{year}-{month}-{day}.json"
    req = requests.get(url)
    json = req.json()

    cprint("[WordleSolver/NYTimes] Parsing & Displaying Results...", color="blue", attrs=['bold'])

    solution = json["solution"]
    solution = solution[0].upper() + solution[1:]
    print_date = json["print_date"]
    editor = json["editor"]
    id = json["id"]

    print("")

    cprint(f"[WordleSolver/NYTimes] ID: {id}", color="green", attrs=['bold'])

    print("")

    cprint(f"[WordleSolver/NYTimes] Print Date: {print_date}", color="green", attrs=['bold'])

    print("")

    cprint(f"[WordleSolver/NYTimes] Editor: {editor}", color="green", attrs=['bold'])

    print("")

    cprint(f"[WordleSolver/NYTimes] Answer: {solution}", color="white", attrs=['bold'])

    print("")

    cprint("[WordleSolver/NYTimes] Ending Timer...", color="blue", attrs=['bold'])

    end_time = time.time()

    print("")

    cprint(f"[WordleSolver/NYTimes] Found In: {round(end_time - start_time, 3)}s", color="yellow", attrs=['bold'])

    print("")
