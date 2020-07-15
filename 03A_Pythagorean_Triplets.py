# Component 3A: Generate a pythagorean triplet

import random

''' RESEARCH NOTES:
    Any pythagorean triplet can be found by applying a^2 + b ^2 = c^2 in a different way
    a = 2m
    b = m^2 - 1
    c = m^2 + 1
    where m > 1
    
    This leads to the equation ==> (2m)^2 + (m^2 - 1)^2 = (m^2 + 1)^2 ---- substituting from the original equation
    This equation will be used to determine all pythagorean triplets for this section of the quiz '''


def pythagorean_triplet(m):
    a = 2*m
    b = m**2 - 1
    c = m**2 + 1
    print("This is a pythagoras triplet where m = {}\n".format(m_value))
    print("a\u00b2 + b\u00b2 = c\u00b2")
    print("a = {}, b = {}, c = {}".format(a, b, c))


# Main routine
m_value = random.randint(2, 20)
pythagorean_triplet(m_value)
