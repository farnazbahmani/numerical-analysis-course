import numpy as np


# define main function
def f(x):
    return x**3 + x**2 - 1.0

# define g(x) in fixed point theory
def g(x):
    return 1.0 / np.sqrt(1.0 + x)
    # return 1.0/x**2 - 1.0  # not converge !!!


x0 = 2.0
e = 0.000001


step = 1
flag = 1
Niter = 10
condition = True
while condition:
    x1 = g(x0)  # x1 = xi+1  and x0 = xi
    print('Iteration - %d, x1 = %0.8f and f(x1) = %0.8f'%(step, x1, f(x1)))

    # define functions for tolerance check
    f0 = f(x0)
    f1 = f(x1)

    # define next iteration run
    step += 1
    x0 = x1

    if step > Niter:
        flag = 0

    # print situation
    if flag == 1:
        print('\nRequired root is: %0.8f'%x1)
    else:
        print('This function can not be converge !!!')
        break

    condition = abs(f1-f0) > e
