from clases.ejemplo.calculadora import Calculadora


class Menu(object):
    def __init__(self):
        self.opcion = 0
        
    def mostrarMenu(self):
        print()
        print("Ejemplo programación Orientada a objetos")
        print("1. Calculadora")    
        print("0. Salir")


    def menu(self):
        self.opcion = ""
        while self.opcion != "0":
            self.mostrarMenu()
            self.opcion = input("Seleccione una opción: ")
            
            if self.opcion == "1":
                casio = Calculadora()
                casio.LeerNumeros()
                casio.CalcularSuma()
                casio.MostrarSuma()
            else:
                print("Opción no válida, intente de nuevo.")    
                calculadora = Calculadora()
                calculadora.LeerNumeros()
                calculadora.CalcularSuma()
                calculadora.MostrarSuma()