
'''
Un parque renta bicicletas a $30 por hora. Si se rentan 3 horas o más,
se aplica un 15% de descuento. Se necesita mostrar el importe a pagar
según las horas de renta.
'''

# PROBLEMA
# Calcular el importe a pagar por la renta de una bicicleta según
# el número de horas contratadas.

# ENTRADAS
# horas : int, horas de renta, número entero mayor o igual a 1.

# SALIDAS
# importe : float, pesos mexicanos, mostrado con dos decimales.
# horas : int, horas de renta.

# REGLAS Y SUPUESTOS
# - El precio de renta es de $30.00 por hora.
# - El importe sin descuento se calcula multiplicando las horas por 30.
# - Si las horas son mayores o iguales a 3, se aplica un descuento del 15%.
# - Si las horas son menores a 3, no se aplica descuento.
# - El descuento se calcula sobre el importe total sin descuento.
# - El importe final es el importe sin descuento menos el descuento.
# - El resultado se muestra con dos decimales.
# - Se considera que las horas de renta son números enteros positivos.

# ALGORITMO
# 1. Leer las horas de renta.
# 2. Calcular importe = horas * 30.
# 3. Si horas >= 3:
#       importe = importe - importe * 0.15
# 4. Mostrar las horas y el importe final con dos decimales.

# CASOS DE PRUEBA
# 1 hora -> $30.00
# 2 horas -> $60.00
# 3 horas -> $76.50
# 4 horas -> $102.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerHoras() -> int : lee y devuelve las horas de renta.
# calcularRenta(horas) -> float : calcula y devuelve el importe final.
# mostrarRenta(horas, importe) -> None : muestra las horas y el importe.

# Implementa el algoritmo anterior utilizando las funciones del contrato.


def leerHoras():
    return int(input())


def calcularRenta(horas):
    importe = horas * 30

    if horas >= 3:
        importe = importe - importe * 0.15

    return importe


def mostrarRenta(horas, importe):
    print(f"Horas de renta: {horas}")
    print(f"Importe a pagar: ${importe:.2f}")
