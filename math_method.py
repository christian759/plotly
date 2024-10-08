# -*- coding: utf-8 -*-

import re
import numpy as np
from pydantic import BaseModel
import matplotlib.pyplot as plt
from sympy import symbols, solve, Eq

class Method(BaseModel):
    def result(fig: int, equation: str, formatter) -> str:
        ans = formatter(equation=equation, fig=fig)
        return ans
    
    def formatter(equation: str, fig: int = 2) -> str:
        formatted = re.sub(r'(\d+)x', r'\1*x', equation)
        formatted = formatted.replace("^", "**")
        formatted = formatted.replace("x", str(fig))
        equals: str = eval(formatted)
        return equals
    
    
    def quadratic_plot(list_x: list, list_y: list, degree:int = 2):
        list_x = np.array(list_x)
        list_y = np.array(list_y)
        co_efficient = np.polyfit(list_x, list_y, deg = degree)
        polynomial = np.poly1d(co_efficient)
        x_points = np.linspace(min(list_x), max(list_y), 400)
        y_points = polynomial(x_points)
        return x_points, y_points

    def ploting(x_points, y_points, label:str = "Graph", color:str = "blue", color2:str = "red", zorder: int = 5, title: str = "GRAPH", grid:bool = False):
        plt.plot(x_points, y_points, label = label, color = color)
        plt.scatter(x_points, y_points, color = color2, zorder = zorder)
        plt.title(title)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(grid)
        plt.legend()
        plt.show()
        
    def quadratic_roots(equation:str) -> str:
        x = symbols('x')
        roots = solve(equation, x)
        answer = f"the roots of the equation are {roots[1]}"
        return answer
        
