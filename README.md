# Student Grade Calculator

A small, beginner-friendly Python command-line program that calculates a student's
total marks, percentage, and grade. Built for a Cloud and DevOps lab assignment to
practise Git branching and merge conflict resolution.

## Features

- Takes the student's name and marks for three subjects (Maths, Science, English)
- Validates input (only numbers from 0 to 100 are accepted)
- Calculates total marks and percentage
- Assigns a grade based on percentage:

  | Percentage | Grade |
  |------------|-------|
  | 85 and above | A |
  | 70 – 84.99 | B |
  | 40 – 69.99 | C |
  | Below 40 | D |

- No external libraries — uses only the Python standard library

## Requirements

- Python 3.6 or newer

Check your version with:

```bash
python --version
```

## Installation

1. Download or clone this project folder.
2. Open a terminal in the project folder.

No packages need to be installed.

## Usage

Run the program:

```bash
python main.py
```

(On some systems use `python3 main.py`.)

### Example

```
=== Student Grade Calculator ===
Enter student name: Riya
Enter marks for Maths (0-100): 92
Enter marks for Science (0-100): 85
Enter marks for English (0-100): 78

--- Result ---
Name       : Riya
Total      : 255 / 300
Percentage : 85.00%
Grade      : B
```

## Project Structure

```
Student Grade Calculator/
├── main.py      # Program logic: percentage and grade calculation
└── README.md    # Project documentation
```

## How the Code Works

- `calculate_percentage(marks)` – adds the marks and converts them to a percentage.
- `get_grade(percentage)` – returns `A`, `B`, `C`, or `D` based on the percentage.
- `read_marks(subject)` – asks for marks and keeps asking until a valid number is entered.
- `main()` – runs the program and prints the result.

## Merge Conflict Demonstration

This project is used to demonstrate a Git merge conflict. The `get_grade()`
function in `main.py` is the place to edit: change the **same line** (for example
the grade A threshold, `if percentage >= 85:`) to different values in two
branches, then merge them to produce a conflict and resolve it.
