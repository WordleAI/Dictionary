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

## C++ Port/Version

**The C++ port supports:**

- Fetching and displaying the **latest answer** from **NYTimes Wordle**
- Lightweight JSON parsing
- Fast, minimal-dependency execution

### External Dependencies
##### NYTimes
- CPR (https://github.com/libcpr/cpr)
- RapidJSON (https://github.com/Tencent/rapidjson)

### Limitations

- Currently only supports **NYTimes Wordle**
- Retrieves **latest answer only**
- No auto solver functionality
- Currently no support for alternative Wordle variants
- No formatting or coloring of logs



---

## Current Features

| Feature                          | C++ Version | Python Version |
|----------------------------------|------------|----------------|
| NYTimes          | Yes        | Yes            |
| Wordle Unlimited          | No         | Yes            |
| Automatic Solver (NYTimes)       | No         | No             |
| Automatic Solver (Wordle Unlimited)     | No         | Yes            |
| Colored & Formatted Logs    | No         | Yes            |
| Performance Stats    | No         | Yes            |
---

## Design Philosophy

- This project started from the **Python version**


- **Python version** → Feature-rich and includes automation for Wordle Unlimited.
- **C++ version** → Minimal and fast port of the Python version

Future updates may expand the C++ and Python feature set

---

## Todo

| Features                          | Version | Notes 
|----------------------------------|----------------| ---|
| Add Support For Other Browsers (Selenium)          | Python        |   Currently only supports Chrome          | 
| Threading              | Python            | Reliability? 
| Automatic Solver (Wordle Unlimited)                | C++             | https://github.com/digination/cpp-webdriver or better https://github.com/sekogan/webdriverxx
| Wordle Unlimited    | C++                   |
| Formatting & Coloring Of Logs    | C++                   |
| Performance Stats    | C++                   |
| Create Header Files?   | C++                   | Are they needed?
| Other Services   | Python/C++                   | 
| AI Solver? | Python |
