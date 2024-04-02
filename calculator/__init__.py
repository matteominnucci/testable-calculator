Number = int | float
#the number could be an integer or a float
class Calculator:

    def __init__(self):
        self.expression = ""

    def _ensure_is_digit(self, value: int | str):
        if isinstance(value, str):
            value = int(value)
        if value not in range(10):
            raise ValueError("Value must a digit in [0, 9]: " + str(value))
        return value

    def _append(self, value):
        self.expression += str(value)
    
    def digit(self, value: int | str):
        value = self._ensure_is_digit(value)
        self._append(value)
    
    def open_parentheses(self):
        self._append("(")
    
    def close_parentheses(self):
        self._append(")")
        
    def square_root(self):
        self._append("sqrt")
    
    def power(self):
        self._append("**")
    
    def plus(self):
        self._append("+")

    def minus(self):
        self._append("-")
    
    def multiply(self):
        self._append("*")
    
    def divide(self):
        self._append("/")

    def dot(self):
        self._append(".")

    def clear(self):
        self.expression = ""
    
    def compute_result(self) -> Number:
        try:
            from math import sqrt
            result = eval(self.expression)
            if isinstance(result, int) or isinstance(result, float):
                #more precise result, previous version won't work with previous versions of Python
                self.expression = str(result)
                return result
            else:
                raise ValueError("Result is not a number: " + str(result))
        except Exception as e:
            expression = self.expression
            self.expression = ""
            raise ValueError("Invalid expression: " + expression) from e
