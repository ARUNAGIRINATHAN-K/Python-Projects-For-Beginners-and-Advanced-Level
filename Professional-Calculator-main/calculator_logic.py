import math

def calculate(expression):
    try:
        return eval(expression, {"__builtins__": None}, math.__dict__)
    except Exception as e:
        return f"Error: {e}"
