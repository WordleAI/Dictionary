# WordleSolver

This project currently has two implementations: a Python version and a c++ port. While they share a common goal, their feature sets are a bit different.

#### C++ Version: https://github.com/gs109111/WordleSolver/tree/cpp
#### Python Version:  https://github.com/gs109111/WordleSolver/

---

> [!WARNING]
> This project uses an **undocumented NYTimes Wordle endpoint** to fetch the latest puzzle answers. 
> It is intended **for educational purposes only**. 
> Please do **not use this for mass scraping, automated attacks, or commercial purposes**. 
> The endpoint may change or be removed by NYTimes at any time, which could break this tool.
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

| Feature                          | Status |
|----------------------------------| -------|
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
| AI Solver                         | ??? |
