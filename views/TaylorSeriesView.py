"""
Author: Juansedev2 - TODOS LOS DERECHOS RESERVADOS
TaylorSeriesView is the view model of the taylor series
"""
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import sympy as sp
from matplotlib.table import Table

class TaylorSeriesView:

    def __init__(self):
        # Create the matplotlib figure
        self.fig, self.ax = plt.subplots(figsize = (8, 6))

    """
        get_fig is the method to return the matplotlib figure
    """
    def get_fig(self):
        return self.fig

    """
        graph_original_function is the method to graph the original math function in matplotlib
        params:
            function: is the math function (in math expression) to will be graphic
            x_vals: is the vals in the x dimension
            y_func: is the y_function correlation with the x dimension
    """
    def graph_original_function(self, function, x_vals, y_func):
        # Grapth the original function
        self.ax.plot(x_vals, y_func, label=f'Función: {function}', color = 'black', linewidth = 2)

    """
        graph_polinomies is the method to graph the polinomies of taylor
        params:
            polinomies_list: must be a list of the taylor polinomies of taylor, this can be an list of string
            n_order: is the n_order to graph the polinomies
            independient_variable_simbol: is the symbol of the independient variable to get and graph as original
            x_vals: therea are the vals in the x dimension
    """
    def graph_polinomies(self, polinomies_list, n_order, independient_variable_simbol, x_vals, a_value):
        colors = cm.viridis(np.linspace(0, 1, n_order))
        colores = ['yellow', 'blue', 'red', 'green', 'orange', 'purple', 'brwon', 'gray', 'aqua', '']
        i = 0
        # Graph each taylor polinomie
        for idx, polinomie in enumerate(polinomies_list, start = 0):
            
            y_polinomie = sp.lambdify(independient_variable_simbol, polinomie, 'numpy')(x_vals)
            # Verify and fix the form for the y_polinomie
            if np.isscalar(y_polinomie):
                y_polinomie = np.full_like(x_vals, y_polinomie)
            elif y_polinomie.shape != x_vals.shape:
                y_polinomie = np.array(y_polinomie).flatten()
            
            self.ax.plot(x_vals, y_polinomie, label = f'Taylor n = {idx}', linestyle = "-", color = colores[i % len(colores)])
            i = i +1
        
        plt.axvline(x = a_value, color='black', linestyle='--', label=f'Línea en a={a_value}', linewidth = 2)

    """
        init_graph initis the matplotlib graf window
    """
    def init_graph(self):
        self.ax.set_title('Función y su Serie de Taylor')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.legend()
        self.ax.grid(True)

    """
        graph_functions_table is the method to graph a table by each polinomies list;
        params:
            polinomies: must be a list of the taylor polinomies of taylor, this can be an list of string
    """
    def graph_functions_table(self, polinomies):
        # Prepare the data to the table
        data_table = [['n', 'Polinomio de Taylor']]
        for idx, polinomie in enumerate(polinomies, start = 1):
            data_table.append([str(idx), polinomie])

        # Add the data to the main graph
        table = self.ax.table(cellText = data_table,
                colLabels=None,
                cellLoc='left',
                loc='upper right',
                bbox=[1.05, 0.5, 0.4, 0.4]
        )  # [x0, y0, width, height]

        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1, 1.5)

        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1, 1.5)
        # Adjunts layout to prevent curts
        plt.tight_layout()