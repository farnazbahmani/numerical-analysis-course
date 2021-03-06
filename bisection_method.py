import numpy as np
import matplotlib.pylab as plt
import sys


# root-finding algorithm using bisection method
def f(x):
    return x**3 - 5*x - 9

a = 2
b = 3
e = 0.00001

# tolerance condition: |f(pn) - f(pn1)|/|f(pn)| < e


# check reliabillity
if f(a) * f(b) >= 0:
    print(' *** This function do not have any root in this bound ***')
    sys.exit()
else:
    step = 1
    print('\n\n *** BISECTION METHOD ***')
    condition = True
    while condition:

        # bosection algorithm
        x2 = (a + b) / 2.0
        if f(a) * f(x2) < 0:
            b = x2
        else:
            a = x2

        # condition check
        if step > 1:
            pn1 = x2
            condition = np.abs(pn1 - pn0) / np.abs(pn1) > e
            print('Iteration - %d, x2 = %0.6f and tolerance = %0.6f' %(step, x2, np.abs(pn1 - pn0) / np.abs(pn1)))

        pn0 = x2
        step += 1
