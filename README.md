# Find e to the Nth Digit

A Python project that calculates and displays **Euler's number (e)** to a user-defined number of decimal places. The project is implemented in three versions, progressing from Python's built-in `math.e` to a high-precision calculation using the `Decimal` module and the infinite series expansion of **e**.

## Features

- Display `e` to a user-defined number of decimal places.
- Validate user input with exception handling.
- Calculate `e` without using `math.e`.
- Support high-precision calculations up to **10,000 decimal places**.

## Project Versions

### Version 1 — Basic Implementation

Uses Python's built-in `math.e` and string formatting to display `e` with the requested number of decimal places.

### Version 2 — Input Validation

Improves the basic version by adding:

- Integer input validation.
- Range checking.
- `try/except` error handling.
- A loop that continues until valid input is entered.

### Version 3 — High-Precision Calculation

Calculates `e` from scratch using the infinite series:

> **e = Σ (1 / k!)**

This version uses:

- `Decimal` for arbitrary-precision arithmetic.
- Automatic precision based on the requested number of decimal places.
- A maximum supported precision of **10,000 decimal places**.

## Example

```text
Enter the number of decimal places for e (0-10000): 50

2.71828182845904523536028747135266249775724709369996
```

## Concepts Practiced

- User input and type conversion.
- `while` and `for` loops.
- Conditional statements.
- Exception handling with `try/except`.
- Factorials (`math.factorial`).
- Infinite mathematical series.
- High-precision arithmetic with `Decimal`.

## Project Structure

```text
find-e-to-the-nth-digit/
├── README.md
├── v1(basic).py
├── v2(input_validation).py
└── v3(high_precision).py
```

## Requirements

- Python 3.x
- Standard Library only (`math` and `decimal`)
- No external packages required.
