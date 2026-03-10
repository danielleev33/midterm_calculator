# Advanced Calculator

## Project Overview
This project is an advanced command-line calculator application built in Python. It supports both standard and advanced arithmetic operations, includes undo/redo functionality, maintains calculation history, saves and loads history from CSV files, logs calculation activity, and uses a REPL-based interface for user interaction.

The project was designed using object-oriented programming principles and several software design patterns, including the Factory, Memento, and Observer patterns.

---

## Features

### Arithmetic Operations
The calculator supports the following operations:
- add
- subtract
- multiply
- divide
- power
- root
- modulus
- int_divide
- percent
- abs_diff

### History Management
- Stores completed calculations in memory
- Displays calculation history
- Clears history
- Saves history to CSV
- Loads history from CSV

### Undo / Redo
- Undo the most recent calculation
- Redo a previously undone calculation

### Logging and Auto-Save
- Logs calculations to a file
- Automatically saves calculation history to CSV using the Observer pattern

### Configuration
- Uses a `.env` file for application settings
- Supports configurable log paths, history paths, precision, max input size, and encoding

### REPL Command-Line Interface
- Interactive calculator session
- Command-based input and output
- Graceful error handling
- Help menu
- Exit command

### Optional Feature
- Color-coded terminal output using `colorama`

---

## Design Patterns Used

### Factory Pattern
Used to create operation objects dynamically based on the user’s command.

### Memento Pattern
Used to implement undo and redo by saving snapshots of calculator history.

### Observer Pattern
Used so that logging and auto-save respond automatically whenever a new calculation is performed.

---

## Project Structure

```text
project_root/
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── logger.py
│   └── operations.py
├── tests/
│   ├── __init__.py
│   ├── test_calculation.py
│   ├── test_calculator.py
│   ├── test_calculator_memento.py
│   ├── test_history.py
│   ├── test_logger.py
│   ├── test_operations.py
│   └── test_repl.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── .github/
    └── workflows/
        └── python-app.yml