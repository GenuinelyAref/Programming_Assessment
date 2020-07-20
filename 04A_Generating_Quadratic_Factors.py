# Component 4A: Generating Quadratic factors/roots

import random

factor_one = ""
quadratic = ""

alpha = -3
if alpha == 0:
    factor_one = "x"
elif alpha < 0:
    factor_one = "(x - {})".format(0-alpha)
elif alpha > 0:
    factor_one = "(x + {})".format(alpha)
quadratic += factor_one

beta = 3
if beta == 0:
    factor_one = "x"
elif beta < 0:
    factor_one = "(x - {})".format(0-beta)
elif beta > 0:
    factor_one = "(x + {})".format(beta)
quadratic += factor_one

a = 1
b = alpha + beta
c = alpha * beta

expanded_quadratic = "{}(x\u00b2)+({}x)+({})".format(a, b, c)
print(expanded_quadratic)


print(quadratic)
