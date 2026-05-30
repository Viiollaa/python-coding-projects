# 4x4 Sudoku Solver (Backtracking Algorithm)

A Python-based application that solves a 4x4 Sudoku puzzle using the **backtracking algorithm**.

## How it works
The solver uses a recursive depth-first search approach:
1. **Empty Cell Identification:** It scans the grid for the first empty cell (represented by 0).
2. **Backtracking:** It attempts to fill the cell with a number (1-4).
3. **Validation:** It checks if the number violates Sudoku rules (row, column, and 2x2 sub-grid constraints).
4. **Recursion:** If valid, it proceeds to the next cell. If it hits a dead-end, it backtracks and resets the cell, trying the next possible number.

## Technical Skills
- **Algorithm Design:** Recursive backtracking.
- **Problem Solving:** Logical constraint satisfaction.
- **Data Structures:** 2D Array manipulation.

## How to run
1. Ensure you have Python installed.
2. Run the script: `python sudoku_solver.py`
3. Input the grid row by row (e.g., `1 0 0 2`).
