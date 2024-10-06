"""
Author: Juansedev2 - TODOS LOS DERECHOS RESERVADOS
MatlPlotParser is a class to make the parser operations to return graphic results
"""
import numpy as np
import sympy as sp

class MatPlotParser:

    """
    MatPlotParser constructor
    params:
        function: is the function as a sympi expression to will be parsed to integrate with matplotlib
        independient_variable_simbol: is the independient variable simbol that the function takes
        a_value: is the a value to will be evaluated to the taylor series
    """
    def __init__(self, function, independient_variable_simbol, a_value : int):
        try: 
            # Convert simbolic expression (function) to numeric function
            self.f_lambdified = sp.lambdify(independient_variable_simbol, function, 'numpy')
            # Define the range of the graph centered in the a_value to be adpataded
            self.range = 10  # Puedes ajustar este valor
            self.x_vals = np.linspace(a_value - self.range, a_value + self.range, 400)
            self.y_func = self.f_lambdified(self.x_vals)
            # Verificar y ajustar la forma de y_func
            if np.isscalar(self.y_func):
                self.y_func = np.full_like(self.x_vals, self.y_func)
            elif self.y_func.shape != self.x_vals.shape:
                self.y_func = np.array(self.y_func).flatten()
        except:
            raise

    """
    get_function_expression is the method to return the function lamdified expression
    """
    def get_function_expression(self):
        return self.f_lambdified
    
    """
    get_x_vals is the method to return the get_x_vals property 
    """
    def get_x_vals(self):
        return self.x_vals
    
    """
    get_y_func is the method to return the get_y_func property 
    """
    def get_y_func(self):
        return self.y_func
