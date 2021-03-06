import numpy as np
import matplotlib.pylab as plt

# solve equation using the Newtonina Method
# y = x**2 - 2

xinit = 50.0
xn = xinit
for loop in range(10):
    # define the function
    fx = xn**2 - 2.0

    # define the derivative
    fpx = 2*xn

    # newton formula
    xn1 = xn - fx / fpx

    # define new xn
    xn = xn1

    # print results
    print('{:.16f}'.format(xn))
