"""
Author: Juansedev2 - TODOS LOS DERECHOS RESERVADOS
MainView is the main view to display when the program starts. An explanation of this view is that this view
is the form of the taylor series
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, scrolledtext
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
    def __init__(self, title, dimensions = "1200x200"):
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
            
            if ("e" in function or "E" in function or "exp" in function) and a_value == "1":
                messagebox.showwarning("Advertencia de cálculo", "Para la función exponencial, el valor de a debe ser mayor a 1")
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
            second_window.geometry("1600x1000")

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
            taylor_series_view.graph_polinomies(polinomies, n_order, independient_variable_simbol, x_vals, a_value)
            taylor_series_view.init_graph()
            taylor_series_view.graph_functions_table(polinomies)

            fig = taylor_series_view.get_fig()
            
            # Integrar la figura en Tkinter - integrate the figure of matplotlib with Tkinter
            canvas = FigureCanvasTkAgg(fig, master = second_window)
            canvas.draw()
            canvas.get_tk_widget().pack(pady = 20, padx = 20, fill = tk.BOTH, expand = True)

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
        instructions_window = tk.Toplevel()
        instructions_window.title("Instrucciones")
        instructions_window.geometry("800x500")
        title = tk.Label(instructions_window, text = "Instrucciones de Uso", font = ("Helvetica", 18, "bold"))
        title.pack(pady = 15)
        # Text box with scroll to show the instructions
        instructions_text = scrolledtext.ScrolledText(instructions_window, wrap = tk.WORD, width = 90, height=15, font = ("Helvetica", 16))
        instructions_text.pack(padx=10, pady=10)
        # Instrucciones as str
        instructions = (
            "1. Ingrese la función matemática en el campo correspondiente.\n\n"
            "PARA FUNCIONES TRIGONOMÉTRICAS escribir el equivalente: (sen = sin, cos = cos, tan = tan, sec = sec, csc = csc, etc.) y también admitimos el literal pi como el número pi, o E o e o exp(x) como euler-exponencial\n\n"
            "2. Especifique el valor de n para calcular el polinomio de Taylor de grado n.\n\n"
            "3. Ingrese el valor de 'a' en la serie de Taylor.\n\n"
            "4. Presione el botón 'Calcular' para obtener los polinomios y graficarlos.\n\n"
            "5. Las funciones racionales se pueden ingresar utilizando sqrt(x) para raíz cuadrada y x**(1/3) para raíz cúbica.\n\n"
            "6. Las funciones exponenciales pueden ser usadas también con el símbolo ^, pero por comodidad se sugiere usar la notación **(valor potencia) de manera literal.\n\n"
            "7. Asegúrese de que la función esté correctamente escrita para evitar errores en el cálculo.\n\n"
            "9. Para cerrar la aplicación, use el botón 'Cerrar' o cierre la ventana principal.\n\n"
            "10. Finalmente podrá notar que en toda serie calculada, habrá un polinomio cero, donde debe saber que este tan solo hace referencia a la función evaluada en el punto a, por lo que a partir del polinomio 1 es que obtiene los polinomios que usted quiere calcular\n\n"
            "FIN"
            
        )
        # Inser instructions in the text box and disable it to prevent edition
        instructions_text.insert(tk.END, instructions)
        instructions_text.config(state=tk.DISABLED)
        # Button to close the window
        close_button = tk.Button(instructions_window, text = "Cerrar", command = instructions_window.destroy, font=("Helvetica", 12))
        close_button.pack(pady=10)

    """
        show_credits is the method to display the messagebox that contains the credits of the program
    """
    def show_credits(self):
        credits_window = tk.Toplevel()
        credits_window.title("Créditos")
        credits_window.geometry("800x400")
        title = tk.Label(credits_window, text = "Desarrollado por", font = ("Helvetica", 16, "bold"))
        title.pack(pady = 15)

        # Texto de los créditos
        credits_text = (
            "Calculadora de Polinomios de Taylor\n\n"
            "Desarrollada por: Juan Sebastian Arias - Juansedev2\n\n"
            "TODOS LOS DERECHOS RESERVADOS\n\n"
            "PROHIDO reproducción para fines económicos y sin reconocimiento intelectual\n\n"
            "Contacto: https://github.com/juansedev2\n\n"
            "Año: 2024"
        )
        # Label to show the credits
        credits_label = tk.Label(credits_window, text = credits_text, font = ("Helvetica", 14), justify = "center")
        credits_label.pack(padx = 15, pady = 15)
        # BUtton to close the window
        close_button = tk.Button(credits_window, text = "Cerrar", command = credits_window.destroy, font = ("Helvetica", 12))
        close_button.pack(pady = 15)