from clases.ejemplo.calculadora import Calculadora
from clases.ejercicios.ejercicio1_luzotro import ReciboLuz
from clases.ejercicios.ejercicio2_calificacionotro import Calificacion



class Menu(object):
    def __init__(self):
        self.opcion = 0
        
    def mostrarMenu(self):
        print()
        print("Ejemplo programación Orientada a objetos")
        print("1. Calculadora")
        print("2. Recibo de luz")
        print("3. Calificación final")    
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
            elif self.opcion == "2":
                recibo = ReciboLuz()
                recibo.leerConsumo()
                recibo.calcularPago()
                recibo.mostrarRecibo()
            elif self.opcion == "3":
                calificacion = Calificacion()
                calificacion.leerParciales()
                calificacion.calcularFinal()
                calificacion.determinarEstado()
                calificacion.mostrarResultado()
            else:
                print("Opción no válida, intente de nuevo.")    
                calculadora = Calculadora()
                calculadora.LeerNumeros()
                calculadora.CalcularSuma()
                calculadora.MostrarSuma()