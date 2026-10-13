'''
La calificación final de una materia se obtiene de tres parciales que
valen 30%, 30% y 40%. La materia se aprueba con 70. Un parcial menor
a 50 reprueba la materia. Se necesita mostrar la calificación final
y si el alumno aprobó.
'''

# PROBLEMA
# Calcular la calificación final de una materia a partir de tres
# calificaciones parciales y determinar si el alumno aprobó.

# ENTRADAS
# parcial1 : float, puntos de 0 a 100.
# parcial2 : float, puntos de 0 a 100.
# parcial3 : float, puntos de 0 a 100.

# SALIDAS
# final : float, puntos de 0 a 100, mostrado con dos decimales.
# estado : texto, "Aprobado" o "Reprobado".

# REGLAS Y SUPUESTOS
# - El parcial 1 representa el 30% de la calificación final.
# - El parcial 2 representa el 30% de la calificación final.
# - El parcial 3 representa el 40% de la calificación final.
# - La calificación mínima para aprobar es 70.
# - Si cualquier parcial es menor que 50, el alumno reprueba.
# - Un parcial exactamente igual a 50 no provoca reprobación automática.
# - La calificación final se muestra con dos decimales.
# - Para aprobar se deben cumplir ambas condiciones:
#   calificación final mayor o igual a 70 y ningún parcial menor a 50.

# ALGORITMO
# 1. Leer las tres calificaciones parciales.
# 2. Calcular final = parcial1 * 0.30 + parcial2 * 0.30 + parcial3 * 0.40.
# 3. Si final >= 70 y parcial1 >= 50 y parcial2 >= 50 y parcial3 >= 50:
#       estado = "Aprobado"
# 4. En caso contrario:
#       estado = "Reprobado"
# 5. Mostrar la calificación final y el estado.

# CASOS DE PRUEBA
# (80, 70, 90) -> Final 81.00, Aprobado
# (70, 70, 70) -> Final 70.00, Aprobado
# (100, 100, 40) -> Final 76.00, Reprobado
# (69, 70, 70) -> Final 69.70, Reprobado

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerParciales() -> tuple : lee y devuelve las tres calificaciones.
# calcularFinal(parcial1, parcial2, parcial3) -> float : calcula la calificación final.
# determinarEstado(final, parcial1, parcial2, parcial3) -> str : determina si el alumno aprobó.
# mostrarResultado(final, estado) -> None : muestra la calificación final y el estado.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerParciales():
    # Leer las tres calificaciones parciales
    parcial1 = float(input("Ingrese la calificación del primer parcial (0-100): "))
    parcial2 = float(input("Ingrese la calificación del segundo parcial (0-100): "))
    parcial3 = float(input("Ingrese la calificación del tercer parcial (0-100): "))
    return parcial1, parcial2, parcial3

def calcularFinal(parcial1, parcial2, parcial3):
    # Calcular la calificación final
    final = parcial1 * 0.30 + parcial2 * 0.30 + parcial3 * 0.40
    return final

def determinarEstado(final, parcial1, parcial2, parcial3):
    # Determinar si el alumno aprobó
    if final >= 70 and parcial1 >= 50 and parcial2 >= 50 and parcial3 >= 50:
        return "Aprobado"
    else:
        return "Reprobado"

def mostrarResultado(final, estado):
    # Mostrar la calificación final y el estado
    print(f"Calificación final: {final:.2f}")
    print(f"Estado: {estado}")
