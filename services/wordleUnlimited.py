# Modules
from selenium import webdriver
from selenium import * 
from selenium.webdriver.common.by import By
import time
import json
import os
from selenium.webdriver.common.keys import Keys
from termcolor import *

def main(game_attempts, use_threading=False):

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("")
    print("")

    # Load the website
    base_url = "https://wordleunlimited.org/" 
    web = webdriver.Chrome()
    web.get(base_url + "?firstRun=1&puzzleNum=1") # ?firstRun=1 or ?attemptNum=1 not needed but helpful for debugging, has no impact on the website (i.e. the website doesn't use this URL Param for anything)

    total_start_time = time.time()

    for i in range(0, game_attempts): 

        start_time = time.time()

        cprint(f"[wordle-unlimited-service] Attempting Puzzle {i+1}...", color="blue", attrs=['bold']) 

        # Assmuing this launches a new game everytime
        web.delete_all_cookies() # This is done in case the website flags users based on the same cookies (doesn't look like it does)
        emptyGameState = {}
        # This solution will also clear the leaderboard as a result, currently is the best solution since the 'next game' button is not clickable 
        web.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", "gameState", json.dumps(emptyGameState)) # The website will auto fill in the missing keys and values
        web.get(base_url + f"?puzzleNum={i+1}") # ?attemptNum={num} not needed but helpful for debugging, has no impact on the website (i.e. the website doesn't use this URL Param for anything)
        time.sleep(1)
        
        # Click the dom on the inital 'instructions overlay', although this is not a very 'future proof' solution (i.e. if the website disables alert closing using the empty space)
        print("")
        cprint(f"[wordle-unlimited-service] Closing Instructions Alert...", color="blue", attrs=['bold'])

        dom = web.find_element(By.TAG_NAME, "body")
        dom.click()

        # Get gameState from LocalStorage
        gameState = web.execute_script("return window.localStorage.getItem(arguments[0]);", "gameState")

        gameStateParsed = json.loads(gameState)
        solution = gameStateParsed["solution"]
        first_upper_case = solution[0].upper()
        solution = first_upper_case + solution[1:]
        solutionIndex = 0

        print("")
        cprint(f"[wordle-unlimited-service] Solution: {solution}...", color="white", attrs=['bold'])

        while solutionIndex < 6:
            try:
                print("")
                letter = solution[solutionIndex]
                cprint(f"[wordle-unlimited-service] Typing Letter {letter}...", color="blue", attrs=['bold'])
                # print("")
                dom.send_keys(letter)
                solutionIndex += 1
            except Exception as e:
                # Assume that the game ended with the correct solution
                end_time = time.time()
                # print("")
                cprint(f"[wordle-unlimited-service] Solved...", color="green", attrs=['bold'])
                print("")
                cprint(f"[wordle-unlimited-service] Solved In: {round(end_time - start_time, 3)}s...", color="yellow", attrs=['bold'])
                print("")
                break


        dom.send_keys(Keys.ENTER)
        time.sleep(1.5) # This can be lowered?, although it is better for viewing the result


    total_end_time = time.time()
    cprint(f"[wordle-unlimited-service] Total Time Taken: {round(total_end_time - total_start_time, 3)}...", color="magenta", attrs=['bold'])
    print("")
    