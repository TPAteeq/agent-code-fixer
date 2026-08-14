# calculator/pkg/calculator.py

class Calculator:
    """A small infix expression evaluator with operator precedence.

    Supports +, -, *, and / over space-separated tokens; see evaluate().
    """

    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "%": lambda a, b: a % b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "%": 2,
        }

    def evaluate(self, expression):
        """Evaluate a space-separated infix expression.

        Returns None for an empty or whitespace-only expression. Raises
        TypeError when ``expression`` is not a string, and ValueError on an
        invalid token, an unbalanced expression, or a division by zero.
        """
        if not isinstance(expression, str):
            raise TypeError("expression must be a string")
        if not expression or expression.isspace():
            return None
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens):
        """Evaluate the token list with a shunting-yard pass, honoring precedence."""
        values = []
        operators = []

        for token in tokens:
            if token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        while operators:
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        if operator in ("/", "%") and b == 0:
            raise ValueError("division by zero")
        values.append(self.operators[operator](a, b))