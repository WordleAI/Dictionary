# WordleSolver

This project includes two implementations: a Python version and a C++ port. While both share the same core goal, their features differ slightly. The long-term objective is to move away from reliance on the NYTimes endpoint and other services, focusing on a universal, independent Wordle-solving solution.

#### C++ Version: https://github.com/gs109111/WordleSolver/tree/cpp
#### Python Version:  https://github.com/gs109111/WordleSolver/tree/python

---

> [!WARNING]
> This project currently uses an **undocumented NYTimes Wordle endpoint** to fetch the latest puzzle answers. 
> It is intended **for educational purposes only**. 
> Please do **not use this for mass scraping, automated attacks, or commercial purposes**. 
> The endpoint may change or be removed by NYTimes at any time, which could break this tool.
---

### Goals Of This Branch

- Host word lists
- Usage of the word lists in a system capable of intelligently guessing wordle answers
- Reduce external dependencies (i.e. NYTimes) over time

---

## Word List Sources
 
- https://github.com/dwyl/english-words
