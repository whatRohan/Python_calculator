"""Basic arithmetic calculator operations."""


def calculator(operation, num1, num2):
    """Apply an arithmetic operation to two numbers.

    Supported operations are add, subtract, multiply, and divide.
    """
    if operation == "add":
        return num1 + num2
    if operation == "subtract":
        return num1 - num2
    if operation == "multiply":
        return num1 * num2
    if operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    raise ValueError(f"Unsupported operation: {operation}")