import re

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

formula = getFormula('3x^5 - 3x + 12')
print(formula)


