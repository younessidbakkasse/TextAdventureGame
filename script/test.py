def arithmetic_arranger(problems, solution = False):
    """
    receives a list of strings that are arithmetic problems and 
    returns the problems arranged vertically and side-by-side.
    """
    # checks maximum operations
    if len(problems) > 5: 
        return "Error: Too many problems."

    # constructing lines
    lines = ["" for line in range(4)]
    
    # main loop
    for i, problem in enumerate(problems):
        operand_up, operator, operand_down = problem.split()

        # check operation 
        if operator != "+" and operator != "-": 
            return "Error: Operator must be '+' or '-'."

        # checks if user iput is only digits
        if not operand_up.isdigit() or not operand_down.isdigit():
            return "Error: Numbers must only contain digits."

        # checks operand length 
        if len(operand_up) > 4 or len(operand_down) > 4: 
            return "Error: Numbers cannot be more than four digits."

        # calculating the solution
        if operator == "+":
            operation_solution = int(operand_up) + int(operand_down)  
        else:
            operation_solution = int(operand_up) - int(operand_down)

        # calculating space lenght required for right alignement
        space = len(max([operand_up,operand_down], key = len))

        # creating every line
        lines[0] += operand_up.rjust(space + 2)
        lines[1] += operator + operand_down.rjust(space + 1)
        lines[2] += "-" * (space + 2)
        lines[3] += str(operation_solution).rjust(space + 2)

        # adding 4 bllocks of space between each vertical problem
        if i < len(problems) - 1:
            lines[0] += 4 * " "
            lines[1] += 4 * " "
            lines[2] += 4 * " "
            lines[3] += 4 * " "

    # checking ether to display solution or not 
    vertical_problems = lines[0] + "\n" + lines[1] + "\n" + lines[2]
    if solution:
        vertical_problems += "\n" + lines[3]

    return vertical_problems

print(arithmetic_arranger(["11 + 4", "3801 - 2999", "123 + 49", "1 - 9380"], True))



