# WordleSolver

This project currently has two implementations: a Python version and a c++ port. While they share a common goal, their feature sets are a bit different.

---

## Python Version

The Python implementation provides expanded functionality and automation features:

### NYTimes Wordle *(Latest Answer Only)*

- Fetches and displays the **latest official answer**
- Designed for quick retrieval and reference
- No automation or solver functionality for NYTimes


### Wordle Unlimited *(Auto Solver)*

- Fully supports **Wordle Unlimited**
- Includes an **automatic solver**
- Can solve multiple puzzles in sequence
- Number of puzzles solved depends on the user-selected amount

### External Dependencies
##### NYTimes
- Requests (https://pypi.org/project/requests/)
##### Wordle Unlimited
- Selenium (https://github.com/SeleniumHQ/selenium)
- Chromedriver (https://developer.chrome.com/docs/chromedriver/downloads)
- Google Chrome (https://www.google.com/intl/en_ca/chrome/)
##### Common
- Termcolor (https://pypi.org/project/termcolor/)

---

## Current Features

| Feature                          | 
|----------------------------------|
| NYTimes          | Yes        |
| Wordle Unlimited          | Yes        
| Automatic Solver (NYTimes)       | No         |
| Automatic Solver (Wordle Unlimited)     | Yes |
| Colored & Formatted Logs    | Yes |
| Performance Stats  | Yes            |
---
## Todo

| Feature                          | Notes |
|----------------------------------|-------|
| Add Support For Other Browsers (Selenium) | Currently only supports Chrome |
| Threading                         | Stability? |
| Integration with Other Services   | Not yet implemented |
| AI Solver                         | |
