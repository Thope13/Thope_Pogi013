from scipy.misc import derivative
import sympy as sp


x = sp.Symbol('x')
def f(x):
    return 25/x
t = sp.diff(f(x))
print(t)
