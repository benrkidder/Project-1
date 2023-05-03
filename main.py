# Import Formulas by Method Names
import sys
from formulas import add, subtract, multiply, divide


# Run Program
def main():
    # Retrieve Argument List at Program Init
    term_input = sys.argv

    # Exit with Invalid Argument Length
    if len(term_input) <= 1:
        sys.exit("Need to provide the operator name")
    elif len(term_input) <= 3:
        sys.exit("Need to provide at least two values")

    # Define Portions of Argument List
    operator = term_input[1]
    values = [float(val) for val in term_input[2:]]
    # Init Final Answer
    answer = 0

    # Operator Check and Execution
    if operator not in ["add", "subtract", "multiply", "divide"]:
        sys.exit("Valid operator names (add, subtract, multiply, divide)")
    elif operator == "add":
        answer = add(values)
    elif operator == "subtract":
        answer = subtract(values)
    elif operator == "multiply":
        answer = multiply(values)
    elif operator == "divide":
        answer = divide(values)

    # Print Final Answer
    print(f'Answer = {answer:.2f}')


# Init Program
if __name__ == "__main__":
    main()
