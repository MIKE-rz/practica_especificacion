'''
Un estacionamiento cobra $20 la primera hora y $15 por cada hora
adicional o fracción. El cobro máximo es de $150. El sistema recibe
el tiempo de estancia en minutos y muestra el importe a cobrar.
'''

# PROBLEMA
# Calcular el importe a pagar por el tiempo de estancia de un vehículo
# en un estacionamiento.

# ENTRADAS
# minutos : int, minutos de estancia, valor entero mayor o igual a 1.

# SALIDAS
# cobro : int, pesos mexicanos, mostrado con dos decimales.

# REGLAS Y SUPUESTOS
# - La primera hora tiene un costo de $20.
# - Cada hora adicional o fracción tiene un costo de $15.
# - Cualquier fracción de hora se redondea hacia arriba a una hora completa.
# - El cobro máximo es de $150.
# - No se permite importar ni utilizar módulos de la biblioteca estándar.
# - Se utilizará división entera para determinar las horas cobrables.
# - 1 a 60 minutos corresponden a una hora cobrable.
# - 61 a 120 minutos corresponden a dos horas cobrables.
# - El resultado nunca puede ser mayor a $150.

# ALGORITMO
# 1. Leer el tiempo de estancia en minutos.
# 2. Calcular horas = (minutos + 59) // 60.
# 3. Si horas <= 1:
#       cobro = 20
# 4. En caso contrario:
#       cobro = 20 + (horas - 1) * 15
# 5. Si cobro > 150:
#       cobro = 150
# 6. Mostrar el importe a cobrar con dos decimales.

# CASOS DE PRUEBA
# 45 minutos -> $20.00
# 60 minutos -> $20.00
# 61 minutos -> $35.00
# 150 minutos -> $50.00
# 600 minutos -> $150.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No uses módulos de la biblioteca estándar.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerMinutos() -> int : lee y devuelve el tiempo de estancia en minutos.
# calcularCobro(minutos) -> float : calcula y devuelve el importe a cobrar.
# mostrarCobro(cobro) -> None : muestra el importe a cobrar.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

