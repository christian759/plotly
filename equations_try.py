# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:51:37 2024

@author: chris
"""

from sympy import symbols, solve, Eq

# Define the variable
x = symbols('x')

# Define and solve the equation directly
equation = 3*x - 4 - 5
equation2 = Eq(23*x + 34, -3)
solution = solve(equation, x)
solution2 = solve(equation2, x)
print(f"The solution to the equation 3x - 4 = 5 is x = {solution[0]}")
print(f"The second solution is {solution2[0]}")

#%%
x, y = symbols('x y')
# Define the equations
eq1 = Eq(2*x + y, 8)
eq2 = Eq(x - y, 1)
# Solve the system of equations
solutions = solve((eq1, eq2), (x, y))
print(f"The solutions to the system are x = {solutions[x]} and y = {solutions[y]}")

#%%
quad = "x^2 - 4*x + 32"
roots = solve(quad, x)
print(roots) 
#%%
from math_method import Method
string = Method.quadratic_roots(quad)
print(string)
#%%

