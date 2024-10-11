"""
Author: Juansedev2 - TODOS LOS DERECHOS RESERVADOS
This is the Function controller of the Function model to indicate make the calculates to taylor serie
"""
from models.Function import Function

class FunctionController:

    """
    constructor of FunctionController
    params:
        function_str: is the math function as a string to will be parsed
        independient_variable: is the independient variable symbol as a string to make derivation respecto the function
        n_order: is the order of the taylor polinomies to calculate it
        a: is the value of the a parameter to evalute in the taylor serie
    """
    def __init__(self, function_str, independient_variable, n_order, a):
        self.function = Function(function_str, independient_variable)
        self.function.set_taylor_serie(n_order, a)
        self.polinomies_as_str = self.function.get_polinomies_as_str()
    
    """
    get_polinomies_to_graph is the method to return the polinomies taylor of as a list of strings that represent the polinomies
    """
    def get_polinomies_to_graph(self):
        return self.polinomies_as_str
    
    """
    get_function_to_graph is the method to get the pure math function (symbolic expression)
    """
    def get_function_to_graph(self):
        return self.function.get_pure_function()
    
    """
    get_independient_variable_simbol is the method to get the indepdient variable symbol propertie of the function
    """
    def get_independient_variable_simbol(self):
        return self.function.get_independient_variable_simbol()
