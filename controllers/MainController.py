"""
Author: Juansedev2 - TODOS LOS DERECHOS RESERVADOS
This is the MainControler, here the GUI starts when the program starts
"""
from views.MainView import MainView

class MainController:

    def __init__(self):
        main_view = MainView("Calculadora de series de Taylor", "800x400")
        main_view.startWindowApp()