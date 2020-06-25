# Component 4C: Expanding quadratic using alpha and beta values

alpha = -9
beta = -8

factorised_quadratic = "(x{})(x{})".format(alpha, beta)
print(factorised_quadratic)

a = 1
b = alpha + beta
c = alpha * beta

expanded_quadratic = "{}(x\u00b2)+({}x)+({})".format(a, b, c)
print(expanded_quadratic)
