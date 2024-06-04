# Spreadsheet

![Hard](https://img.shields.io/badge/Difficulty-Hard-red)

Make a Spreadsheet module that takes as input a matrix of inputs, and allows evaluation of a coordinate cell.

The columns are identified by `A`, `B`, `C`, etc. The rows are `1`, `2`, `3` etc. Therefore the top-left cell coordinate is `A1`. And you're implementing an `evaluate_cell(coordinate: str) -> int` function.

Make it work for:
- Part 1: basic numbers.
- Part 2: basic formula cells, where addition (`+`) is the main operator (e.g. `1 + 2`)
- Part 3: cells referencing each other, plainly or in formulae.

Instead of extending it for other operators, under time constraint can you avoid corner cases?

What's the complexity and can it be optimized?

Note:
The difficulty level is decided based on the need to solve a combination of several types of problems under a fixed amount of time.
