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

def evalFormula(strEqn, variables):
    # replacing variable names with its value
    for index, row in variables.iterrows(): 
        strEqn = strEqn.replace(row['name'], str(row['value']))

    # evaluating function
    return eval(strEqn)


def bisection(strEqn, a, b, i):
    # Setting equation to the required syntax
    strEqn = getFormula(strEqn)

    # Setting variables
    variable_a = [['x', a]]
    df_variable_a = pd.DataFrame(variable_a, columns = ['name', 'value'])

    variable_b = [['x', b]]
    df_variable_b = pd.DataFrame(variable_b, columns = ['name', 'value'])
    
    # Evaluating F(a)
    fa = evalFormula(strEqn, df_variable_a)

    # Evaluating F(b)
    fb = evalFormula(strEqn, df_variable_b)

    # Evaluating if the range is valid
    if (fa * fb > 0):
        print('Bisecion method does not work on range [' + str(a) + ',' + str(b) + '] - f(a) = ' + str(fa) + ' - f(b) = ' + str(fb))
        return None

    # Setting variables for iteration
    a_n = a
    b_n = b
    m_n = 0
    results = pd.DataFrame(columns=['iteration', 'a', 'b', 'm', 'fa', 'fb', 'fm'])

    for n in range (1, i + 1):

        # Calculating mid value
        m_n = (a_n + b_n)/2

        # Setting variables
        variable_a_n = [['x', a_n]]
        df_variable_a_n = pd.DataFrame(variable_a_n, columns = ['name', 'value'])

        variable_b_n = [['x', b_n]]
        df_variable_b_n = pd.DataFrame(variable_b_n, columns = ['name', 'value'])

        variable_m_n = [['x', m_n]]
        df_variable_m_n = pd.DataFrame(variable_m_n, columns = ['name', 'value'])

        # Evaluating
        fa_n = evalFormula(strEqn, df_variable_a_n)
        fb_n = evalFormula(strEqn, df_variable_b_n)
        fm_n = evalFormula(strEqn, df_variable_m_n)

        # Setting iteration results
        results = results.append({'iteration': n, 'a': a_n, 'b': b_n, 'm': m_n, 'fa': fa_n, 'fb': fb_n, 'fm': fm_n}, ignore_index=True)

        if fm_n == 0:
            return results
        elif (fa_n * fm_n) < 0:
            b_n = m_n
        elif (fb_n * fm_n) < 0:
            a_n = m_n
        else:
            print('Bisection method failed.')
            return results

    print ('No solution found')
    return results


# Example
strEqn = '4x^4 - 4x + 1'
a = 5
b = -5
i = 100

results = bisection(strEqn, a, b, i)

# Printing result
print(results)



    
