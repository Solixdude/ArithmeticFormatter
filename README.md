Arithmetic Arranger

This script is a Python function that formats and optionally solves simple arithmetic problems. It is particularly useful for presenting problems in a clean and readable format, such as for educational or illustrative purposes.

Features

Supports Basic Arithmetic: Handles addition (+) and subtraction (-).

Flexible Formatting: Right-aligns numbers for better readability.

Answer Display: Optionally shows the calculated answers.

Error Handling: Provides informative error messages for invalid inputs.

Usage

The main function arithmetic_arranger takes two parameters:

problems: A list of arithmetic problems as strings. Each problem should be in the format "number1 operator number2".

show_answers: A boolean flag (default: True) that determines whether answers should be displayed.

Input Constraints

The problems list can contain a maximum of 5 problems.

Each problem must:

Use + or - as the operator.

Contain only digits in the numbers.

Have numbers that are at most 4 digits long.

Functionality

Validation:

Checks the number of problems.

Ensures valid operators and numeric inputs.

Formatting:

Aligns numbers and operators.

Adds a dashed line below each problem.

Includes answers if show_answers=True.

Output:

Returns a string with the arranged problems.
