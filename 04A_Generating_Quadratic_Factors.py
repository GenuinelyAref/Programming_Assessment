# Component 4A: Generating Quadratic factors/roots

import random

factor_one = ""
quadratic = ""

for i in range(0, 2):
    alpha = random.randint(-12, 12)
    if alpha == 0:
        factor_one = "x"
    elif alpha < 0:
        factor_one = "(x - {})".format(0-alpha)
    elif alpha > 0:
        factor_one = "(x + {})".format(alpha)
    quadratic += factor_one

print(quadratic)
