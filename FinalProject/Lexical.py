import re

def lexer(input_string):
    # Define regular expressions for tokens
    token_patterns = [
        ('NUMBER', r'\d+'),
        ('PLUS', r'\+'),
        ('MINUS', r'-'),
        ('TIMES', r'\*'),
        ('DIVIDE', r'/'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
    ]

    # Combine regular expressions into a single pattern
    combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)
    token_regex = re.compile(combined_pattern)

    # Tokenize the input string
    tokens = []
    for match in token_regex.finditer(input_string):
        for name, value in match.groupdict().items():
            if value is not None:
                tokens.append((name, value))

    return tokens

# Get user input
input_expr = input("Enter an arithmetic expression: ")
tokens = lexer(input_expr)
print("Tokens:", tokens)


