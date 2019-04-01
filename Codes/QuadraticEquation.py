# Quadratic equation is like ax**2 + bx + c = 0
"""
Quadratic Formula is like x = ((-b (+ or -) sqrt((b*b) - 4*a*c) / (2*a))
"""

import cmath

a, b, c = 2, 5, 4

# Calculate square root part
d = cmath.sqrt((b ** 2) - (4 * a * c))

# Find both the solutions with plus and minus
minusSolution = ((-b) - d) / (2*a)
plusSolution = ((-b) + d) / (2*a)

print("Solution of quadratic equation are: " + str(minusSolution) + " & " + str(plusSolution))