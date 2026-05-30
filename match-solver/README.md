# Guess & Match Solver

A logic-based engine designed to solve word/password guessing puzzles (inspired by the Bulls and Cows game logic). This program identifies potential candidates by applying strict constraints and backtracking algorithms.



## Core Features
* **Constraint-Based Filtering:** Automatically filters out invalid candidates based on feedback (`A` for exact matches, `B` for partial matches).
* **Recursive Search:** Uses a depth-first search approach to generate all possible combinations efficiently.
* **Optimization:** Implements early pruning of the search tree by identifying "impossible" characters early in the process.

## Technical Implementation
The system relies on three main components:
1. **Validation (`t` function):** Enforces strict password requirements (length, specific character sets, and uniqueness).
2. **Scoring (`s` function):** Calculates the exact match (`A`) and partial match (`B`) scores for a given guess against a target.
3. **Generation (`generate` function):** A backtracking engine that traverses the character space to find solutions that satisfy all given user guesses.

## Complexity & Logic
- **Time Complexity:** The use of `set()` for lookups and a pruned search space ensures that the solver remains performant.
- **Data Structures:** Uses `dictionary` for frequency mapping and `set` for constraint tracking, ensuring $O(1)$ average time complexity for character lookups.

## How to Run
1. Ensure you have Python installed.
2. Run the script: `python guess_solver.py`
3. Input the required mode (`T`, `S`, or `G`) followed by the test cases as defined in the system input.
