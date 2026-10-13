
'''
En una avenida el límite es de 60 km/h. Si se excede hasta por
20 km/h, la multa es de $500. Si se excede por más de 20 km/h,
la multa es de $1,000. Se necesita mostrar la multa a partir de
la velocidad del vehículo.
'''

# PROBLEMA
# Determinar el importe de la multa según la velocidad del vehículo.

# ENTRADAS
# velocidad : float, kilómetros por hora (km/h), valor mayor o igual a 0.

# SALIDAS
# multa : float, pesos mexicanos, mostrada con dos decimales.
# velocidad : float, kilómetros por hora (km/h).

# REGLAS Y SUPUESTOS
# - El límite de velocidad es de 60 km/h.
# - Si la velocidad es menor o igual a 60 km/h, no hay multa.
# - Si la velocidad es mayor que 60 y menor o igual a 80 km/h,
#   la multa es de $500.00.
# - Si la velocidad es mayor que 80 km/h, la multa es de $1,000.00.
# - Exceder exactamente 20 km/h el límite corresponde a una multa de $500.00.
# - No se calculan multas acumuladas ni se agregan cargos adicionales.
# - El importe se muestra con dos decimales.

# ALGORITMO
# 1. Leer la velocidad del vehículo en km/h.
# 2. Si velocidad <= 60:
#       multa = 0
# 3. En caso contrario, si velocidad <= 80:
#       multa = 500
# 4. En caso contrario:
#       multa = 1000
# 5. Mostrar el importe de la multa con dos decimales.

# CASOS DE PRUEBA
# 50 km/h -> $0.00
# 60 km/h -> $0.00
# 61 km/h -> $500.00
# 80 km/h -> $500.00
# 81 km/h -> $1000.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerVelocidad() -> float : lee y devuelve la velocidad en km/h.
# calcularMulta(velocidad) -> float : determina y devuelve el importe de la multa.
# mostrarMulta(velocidad, multa) -> None : muestra la velocidad y la multa.

# Implementa el algoritmo anterior utilizando las funciones del contrato.


def leerVelocidad():
    return float(input())


def calcularMulta(velocidad):
    if velocidad <= 60:
        multa = 0
    elif velocidad <= 80:
        multa = 500
    else:
        multa = 1000

    return multa


def mostrarMulta(velocidad, multa):
    print(f"Velocidad del vehículo: {velocidad:.2f} km/h")
    print(f"Multa: ${multa:.2f}")
