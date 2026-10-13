
'''
Un cine cobra $80 por boleto. Los niños de hasta 12 años y los adultos
de 60 años o más pagan la mitad. Se necesita mostrar el precio del
boleto según la edad.
'''

# PROBLEMA
# Calcular el precio de un boleto de cine según la edad del cliente.

# ENTRADAS
# edad : int, años cumplidos, número entero mayor o igual a 0.

# SALIDAS
# precio : float, pesos mexicanos, mostrado con dos decimales.
# edad : int, años cumplidos del cliente.

# REGLAS Y SUPUESTOS
# - El precio normal del boleto es de $80.00.
# - Los clientes de hasta 12 años inclusive pagan la mitad.
# - Los clientes de 60 años o más pagan la mitad.
# - Los clientes mayores de 12 y menores de 60 años pagan el precio normal.
# - El precio de mitad de tarifa es de $40.00.
# - La edad se expresa en años cumplidos.
# - El precio se muestra con dos decimales.

# ALGORITMO
# 1. Leer la edad del cliente.
# 2. Si edad <= 12:
#       precio = 80 / 2
# 3. En caso contrario, si edad >= 60:
#       precio = 80 / 2
# 4. En caso contrario:
#       precio = 80
# 5. Mostrar el precio del boleto con dos decimales.

# CASOS DE PRUEBA
# 8 años -> $40.00
# 12 años -> $40.00
# 13 años -> $80.00
# 59 años -> $80.00
# 60 años -> $40.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerEdad() -> int : lee y devuelve la edad del cliente.
# calcularPrecio(edad) -> float : calcula y devuelve el precio del boleto.
# mostrarPrecio(edad, precio) -> None : muestra la edad y el precio.

# Implementa el algoritmo anterior utilizando las funciones del contrato.


def leerEdad():
    return int(input())


def calcularPrecio(edad):
    if edad <= 12:
        precio = 80 / 2
    elif edad >= 60:
        precio = 80 / 2
    else:
        precio = 80

    return precio


def mostrarPrecio(edad, precio):
    print(f"Edad del cliente: {edad} años")
    print(f"Precio del boleto: ${precio:.2f}")
