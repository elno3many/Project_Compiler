import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Define the token rules
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# A regular expression rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define the grammar rules
def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | term
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]

def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
         | factor
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]

def p_factor(p):
    '''
    factor : NUMBER
           | LPAREN expression RPAREN
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error")

# Build the parser
parser = yacc.yacc()

# Get user input
expression = input("Enter an arithmetic expression: ")

# Parse the input
result = parser.parse(expression)

# Display the result
print(f"Result: {result}")

