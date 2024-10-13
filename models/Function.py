"""
Author: Juansedev2 - TODOS LOS DERECHOS RESERVADOS
Function class represent a math function model
"""
#import the modules that we need to define the function and other attributes
import sympy as sp

class Function:

    """
    A class that represent a math function
    """
    """
    Constructor of the class

        Parameters
        ----------
        function : str
            Is the math function that will be represented by a literal string.
        independient_variable: str
            Is the independient variable in the function to indicate what's the variable to make the respective derivate
    """
    def __init__(self, function_str, independient_variable = "x"):
        self.iv = sp.symbols(independient_variable) # The independient variable and get the simbolic expression
        self.function = self.tryParserFunction(function_str)
        self.derivatives = [] # A list ot save each derivates
        self.polinomies = [] # A list to save each n polinomy of the taylor series

    """
    evaluateInFunction method
        This method is to evaluate the function in an specific value throught his independient variable
        
        Parameters
        ----------
        value: is the number value to evaluate the function
        
        Returns
        -------
            numb_value : float | int
            Return the result to evalute the function in the indicated value.

    """

    def tryParserFunction(self,function_as_str):
        try:
            function_sympy = sp.sympify(function_as_str, locals={'e': sp.E, 'pi': sp.pi, 'sin': sp.sin, 'sen': sp.sin, 'cos': sp.cos, 'exp': sp.exp, 'sqrt': sp.sqrt})
            return function_sympy
        except (sp.SympifyError, TypeError):
            raise

    def evaluate_in_function(self, value):
        try:
            value = self.function.subs(self.iv, value)
            numb_value = value.evalf()
            return numb_value
        except (RuntimeError, TypeError, NameError):
            print(f"Ups, some errros in the program trying to evaluate in function by:")
            raise

    """
    This function is only to testing purposes, this will be print the currently values of the function and his derivate
    """
    def printData(self):
        print(f"La función es {self.function}")
        print(f"La derivada es {self.derivate}")

    def get_pretty_function_and_derivate_str(self):
        return "Función: " + str(self.function)+ " || Derivada: " + str(self.derivate)
    
    """
    This method is to get each and store the n derivates of the poliomies
    """
    def calculate_all_derivates(self, n):
        derivative_function = self.function # By starts, the first function to get the derivative, is the original function
        for i in range(n):
            derivative_function = sp.diff(derivative_function, self.iv)
            self.derivatives.append(derivative_function)

    def get_all_derivatives(self):
        print("Las derivadas son: ")
        for function in self.derivatives:
            print(function)

    """
    This method is to evalute an n derivate in a point(independiente variable value)
    """
    def evaluate_n_derivate(self, n_derivate, value):
        try:
            # First, get the derivate in the n position
            derivative = self.derivatives[n_derivate - 1] # By natural position on a list
            result = derivative.subs(self.iv, value)
            return result
        except (RuntimeError, TypeError, NameError):
            raise

    """
    This method get the taylor series of the function
    """
    def set_taylor_serie(self, n_order, a):

        for i in range(1, n_order + 2):
            try:
                serie_i = self.function.series(self.iv, a, i).removeO()
                self.polinomies.append(serie_i)
            except Exception as e:
                raise
            
        
    """
    This method return the list of the polinomies in pure state (simbolic expressions)
    """
    def get_polinomies(self):
        return self.polinomies
    
    """
    This method return the parsed function as str to graph later
    """
    def get_function_as_str(self):
        return self.function
    
    def get_pure_function(self):
        return self.function

    """
    This method return the independient variable simbol
    """
    def get_independient_variable_simbol(self):
        return self.iv 

    """
    This method is to return the polinomies that are simbolic expressions how an strings (used to later use matplotlib)
    """
    def get_polinomies_as_str(self):
        return [str(polinomio) for polinomio in self.polinomies]
    