"""
Author: Juansedev2 - TODOS LOS DERECHOS RESERVADOS
MainView is the main view to display when the program starts. An explanation of this view is that this view
is the form of the taylor series
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controllers.FunctionController import FunctionController
from models.MatPlotParser import MatPlotParser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from views.TaylorSeriesView import TaylorSeriesView
import sys


class MainView:

    """
        Constructor of the MainView
        title : str is the ttile of the main window
        dimensions: is the dimensions of the main window, by default is 1200 width x 200 height (pixelds)
    """
    def __init__(self, title : str, dimensions = "1200x200"):
        # Create the main window
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(dimensions)
        self.create_taylor_form()
        # Assign the hanler to the WM_DELETE_WINDOW protocol and close all program/process
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # Create a menu var
        menu_bar = tk.Menu(self.root)
        help_menu_var = tk.Menu(menu_bar, tearoff = 0)
        help_menu_var.add_command(label = "Instrucciones", command = self.show_instructions)
        help_menu_var.add_command(label = "Créditos", command = self.show_credits)
        menu_bar.add_cascade(label = "Ayuda", menu = help_menu_var)
        self.root.config(menu = menu_bar)

    """
        create_taylor_form method is to define the taylor series form on the window
    """
    def create_taylor_form(self):
        # label and field to the math function
        font_labels = ('Helvetica', 14)  # Cambiar a una fuente más grande
        font_entries = ('Helvetica', 12)
        func_label = ttk.Label(self.root, text = "Ingresa la función a evaluar:", font = font_labels)
        func_label.pack(pady = 10, padx = 20)
        func_entry = ttk.Entry(self.root, width = 50, font = font_entries)
        func_entry.pack(pady = 10, padx = 40)
        # Label and field to n order of taylor series
        n_label = ttk.Label(self.root, text = "Orden n de la Serie a calcular:", font = font_labels)
        n_label.pack(pady = 10, padx = 40)
        n_entry = ttk.Entry(self.root, width = 50, font=font_entries)
        n_entry.pack(pady = 10, padx = 40)
        # Label and field to the a value on the serie
        a_label = ttk.Label(self.root, text = "Valor de a:", font = font_labels)
        a_label.pack(pady = 10, padx = 40)
        a_entry = ttk.Entry(self.root, width = 50, font = font_entries)
        a_entry.pack(pady = 10, padx = 40)

        """
        display_taylor_results function display a window of the results of process to get the Taylor series by the form
        parameteres:
            func_entry: input of the math function provided to the user in the input
            n_entry: input of the number of the n serie of taylor to get
            a_entry: input of the number of the a value in the taylor serie
        """
        def display_taylor_results():
            # Get the values
            function = func_entry.get()
            n_order = n_entry.get()
            a_value = a_entry.get()

            if not function or not n_order or not a_value:
                messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")
                return
    
            try:
                n_order = int(n_order)
                if(n_order <= 0):
                    messagebox.showerror("Entrada Inválida", "El valor del orden debe ser un entero positivo mayor a cero")
                    return
            except ValueError:
                messagebox.showerror("Entrada Inválida", "El orden n debe ser un número entero.")
                return
            
            try:
                a_value = int(a_value)
            except ValueError:
                messagebox.showerror("Entrada Inválida", "El valor de a debe ser numérico")
                return
            
            try:
                function_controller = FunctionController(function, "x", n_order, a_value)
                original_function = function_controller.get_function_to_graph()
                polinomies = function_controller.get_polinomies_to_graph()
                independient_variable_simbol = function_controller.get_independient_variable_simbol()
                polinomies = function_controller.get_polinomies_to_graph()

            except (TypeError):
                messagebox.showerror("Función Inválida", "La función ingresada no es válida, verifique que se digite de acuerdo a las reglas definidas.")
                raise

            # Create a new window to display the results
            second_window = tk.Toplevel(self.root)
            second_window.title("Valores Recibidos")
            second_window.geometry("1500x1000")

            #Show the values
            mensaje = f"Función: {function}\nOrden n: {n_order}\nValor a: {a_value}"
            label = ttk.Label(second_window, text=mensaje, justify="left")
            label.pack(pady = 20, padx = 20)

            # Now start with the process of calculate and display the taylor serie

            # First process the original function to parse
            mat_plot_parser = MatPlotParser(original_function, independient_variable_simbol, a_value)
            x_vals = mat_plot_parser.get_x_vals()
            y_func = mat_plot_parser.get_y_func()

            taylor_series_view = TaylorSeriesView()
            taylor_series_view.graph_original_function(original_function, x_vals, y_func)
            taylor_series_view.graph_polinomies(polinomies, n_order, independient_variable_simbol, x_vals)
            taylor_series_view.init_graph()
            taylor_series_view.graph_functions_table(polinomies)

            fig = taylor_series_view.get_fig()
            
            # Integrar la figura en Tkinter - integrate the figure of matplotlib with Tkinter
            canvas = FigureCanvasTkAgg(fig, master = second_window)
            canvas.draw()
            canvas.get_tk_widget().pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Button to send the form
        submit_button = ttk.Button(self.root, text = "Enviar", command = display_taylor_results)
        submit_button.pack(pady = 20)

    """
        startWindowApp method inits the loop of Tkinter to init the window
    """
    def startWindowApp(self):
        # Execute the maindow
        self.root.mainloop()

    """
        on_closing is the method to destroy the tkinter main process to close the program and the process in OS
    """
    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Quieres salir de la aplicación?"):
            self.root.destroy()
            sys.exit()

    """
        show_instructions is the method to display the messagebox that contains the instructions of the program
    """
    def show_instructions(self):
        header_str = "Esta calculadora es un primera versión puede graficar las n series de taylor de una función, esto a través del formulario que verá en su pantalla,\n"
        body1_str = "Para poder graficar funciones, debe serguir la nomenclatura siguiente:\n"
        body2_str = "Funciones con potencias: x**n donde n es un número | functiones como euler usar E literal.\n"
        body3_str = "Funciones racionales como raiz cuadrada en adelante, usar: x**(1/3), donde la conversión de la raiz debe ir en fraccionario y delimitado entre paréntesis.\n"
        body4_str = "Todo escalar que multiplique a una variable, se debe escribir como: numero*variable -> 5*x por ejemplo.\n"
        body5_str = "Para funciones trigonométricas: seno = sin, coseno = cos, tangente = tan, cosecante = cosc, etc.\n"
        body5_str = "\nAnte cualquier novedad | pregunta | inquietud | reporte por favor contactarse con el administrador.\n"
        final_str = header_str + body1_str + body2_str + body3_str + body4_str + body5_str + "\n"
        messagebox.showinfo("Instrucciones", final_str)

    """
        show_credits is the method to display the messagebox that contains the credits of the program
    """
    def show_credits(self):
        messagebox.showinfo("Créditos", "Desarrollado por Juansedev2\nTODOS LOS DERECHOS RESERVADOS\nSe puede consultar y probar el programa pero no disponible para generar recursos económicos ni suplantación de autoría.\nAnte cualquier duda|reporte|sugerencia comunicarse con el administrador en el perfil de Github")