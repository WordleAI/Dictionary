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

    cprint("[nytimes-wordle-service] Starting Timer...", color="blue", attrs=['bold'])
    print("")

    start_time = time.time()

    cprint("[nytimes-wordle-service] Getting Current Date...", color="blue", attrs=['bold'])

    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    if month != 12 or month != 11 or month != 10:
        month = f"0{month}"

    print("")
    cprint("[nytimes-wordle-service] Loading Wordle Data From NYTimes...", color="blue", attrs=['bold'])

    print("")
    url = f"https://www.nytimes.com/svc/wordle/v2/{year}-{month}-{day}.json"
    req = requests.get(url)
    json = req.json()

    cprint("[nytimes-wordle-service] Parsing & Displaying Results...", color="blue", attrs=['bold'])

    solution = json["solution"]
    solution = solution[0].upper() + solution[1:]
    print_date = json["print_date"]
    editor = json["editor"]
    id = json["id"]

    print("")

    cprint(f"[nytimes-wordle-service] ID: {id}", color="green", attrs=['bold'])

    print("")

    cprint(f"[nytimes-wordle-service] Print Date: {print_date}", color="green", attrs=['bold'])

    print("")

    cprint(f"[nytimes-wordle-service] Editor: {editor}", color="green", attrs=['bold'])

    print("")

    cprint(f"[nytimes-wordle-service] Answer: {solution}", color="white", attrs=['bold'])

    print("")

    cprint("[nytimes-wordle-service] Ending Timer...", color="blue", attrs=['bold'])

    end_time = time.time()

    print("")

    cprint(f"[nytimes-wordle-service] Found In: {round(end_time - start_time, 3)}s", color="yellow", attrs=['bold'])

    print("")