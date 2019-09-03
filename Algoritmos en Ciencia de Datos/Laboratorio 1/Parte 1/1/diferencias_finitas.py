import re
import pandas as pd

def getFormula(strEqn):
    # Initializing output string
    strOutEqn = ''

    # Remove blank spaces
    strEqn = strEqn.replace(' ', '')

    # Split equation into terms
    terms = re.split('([\+|\-|x|\^])', strEqn)

    # Loop into the terms
    for term in terms:
        if (term.isdigit()):
            strOutEqn = strOutEqn + term
        elif (term == '^'):
            strOutEqn = strOutEqn + '**'
        elif (term == 'x'):
            strOutEqn = strOutEqn + '*' + term
        elif (term == '+' or term == '-'):
            strOutEqn = strOutEqn + ')' + term + '('

    return '(' + strOutEqn + ')'

def getDerivativeFormula(strEqn):

    # Convert equation to standard form
    strEqn = getFormula(strEqn)

    # Generate first term
    # f(x + 2h)
    firstTerm = strEqn.replace('x', '(x+2*h)')

    # Generate second term
    # -4 f(x + h)
    secondTerm = strEqn.replace('x', '(x+h)')
    secondTerm = '-4*(' + secondTerm + ')'

    # Generate third term
    # +3 f(x)
    thirdTerm = '+3*(' + strEqn + ')'

    # Constructing derivative formula
    derivative = firstTerm + secondTerm + thirdTerm
    derivative = '-1*(' + derivative + ')/(2*h)'

    return derivative


def evalFormula(strEqn, variables):
    # replacing variable names with its value
    for index, row in variables.iterrows(): 
        strEqn = strEqn.replace(row['name'], str(row['value']))

    # evaluating function
    return eval(strEqn)




# Example
# Getting derivative
derivative = getDerivativeFormula('3x^5 - 3')

# Evaluating derivative
variables = [['x', -5], ['h', 0.000001]] 
df_variables = pd.DataFrame(variables, columns = ['name', 'value']) 
out = evalFormula(derivative, df_variables)

# Printing result
print(out)




