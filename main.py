"""
Student Grade Calculator
------------------------
A simple program that takes a student's marks in a few subjects,
calculates the total and percentage, and assigns a grade.
"""

# Number of subjects and the maximum marks for each subject
SUBJECTS = ["Maths", "Science", "English"]
MAX_MARKS_PER_SUBJECT = 100


def calculate_percentage(marks):
    """Return the percentage scored, given a list of marks."""
    total = sum(marks)
    max_total = len(marks) * MAX_MARKS_PER_SUBJECT
    return (total / max_total) * 100


def get_grade(percentage):
    """Return a grade (A, B, C or D) based on the percentage."""
    if percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "D"


def read_marks(subject):
    """Ask the user for marks in one subject and validate the input."""
    while True:
        try:
            value = float(input(f"Enter marks for {subject} (0-{MAX_MARKS_PER_SUBJECT}): "))
            if 0 <= value <= MAX_MARKS_PER_SUBJECT:
                return value
            print(f"Please enter a number between 0 and {MAX_MARKS_PER_SUBJECT}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=== Student Grade Calculator ===")
    name = input("Enter student name: ").strip() or "Student"

    # Collect marks for every subject
    marks = [read_marks(subject) for subject in SUBJECTS]

    # Calculate results
    total = sum(marks)
    percentage = calculate_percentage(marks)
    grade = get_grade(percentage)

    # Display the report
    print("\n--- Result ---")
    print(f"Name       : {name}")
    print(f"Total      : {total:.0f} / {len(SUBJECTS) * MAX_MARKS_PER_SUBJECT}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")


if __name__ == "__main__":
    main()
