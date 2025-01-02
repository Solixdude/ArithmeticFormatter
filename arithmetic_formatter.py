def arithmetic_arranger(problems, show_answers=True):
    # Validate the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize the lines
    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    # Process each problem
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        # Check for valid operators
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check for numeric values and digit limits
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the width and perform calculation
        width = max(len(num1), len(num2)) + 2
        result = str(int(num1) + int(num2)) if operator == '+' else str(int(num1) - int(num2))

        # Format lines
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        dash_line.append('-' * width)
        answer_line.append(result.rjust(width))

    # Assemble the arranged problems
    arranged_problems = (
            '    '.join(first_line) + '\n' +
            '    '.join(second_line) + '\n' +
            '    '.join(dash_line)
    )
    if show_answers:
        arranged_problems += '\n' + '    '.join(answer_line)

    return arranged_problems


print(arithmetic_arranger(["212 + 12"]))