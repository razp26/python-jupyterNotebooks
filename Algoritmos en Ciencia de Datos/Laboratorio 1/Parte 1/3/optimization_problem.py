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


def newtonRaphson(strEqn, x, epsilon, h):
    # Initializing variables 
    strFx = getFormula(strEqn)
    strDx = getDerivativeFormula(strEqn)
    error = epsilon + 1
    xn = x
    xn1 = 0
    i = 1
    results = pd.DataFrame(columns=['iteration', 'xn', 'error', 'fx', 'dx'])


    while (error > epsilon):

        # Setting variables
        variables = [['x', xn], ['h', h]]
        df_variables = pd.DataFrame(variables, columns = ['name', 'value'])

        # Evaluating f
        fx = evalFormula(strFx, df_variables)

        # Evaluating derivative
        dx = evalFormula(strDx, df_variables)

        # Calculating xn1
        xn1 = xn - (fx/dx)

        # Calculamos error
        # error = abs(xn1 - xn)
        error = abs(xn1 - xn)

        # solution
        results = results.append({'iteration': i, 'xn': xn, 'error': error, 'fx': fx, 'dx': dx}, ignore_index=True)
        
        # Keep iterating
        i = i + 1
        xn = xn1

    return results


# Example
strEqn = '4x^4 - 4x + 1'
x = 1
epsilon = 0.000001
h = 0.000001
results = newtonRaphson(strEqn, x, epsilon, h)

# Printing result
print(results)
