'''
Enunciado del problema:
Una compañía eléctrica cobra el consumo mensual con tres tarifas:
$1.00 por kWh hasta 150 kWh, $1.50 por kWh de 151 a 280 kWh y
$3.00 por kWh arriba de 280 kWh. Se necesita calcular el importe
del recibo a partir del consumo del mes.
'''

# PROBLEMA
# Calcular el importe mensual de un recibo de luz a partir del
# consumo de energía eléctrica en kWh.

# ENTRADAS
# consumo : float, kWh, valor mayor o igual que 0.

# SALIDAS
# pago : float, pesos mexicanos, mostrado con dos decimales.
# El recibo debe mostrar el consumo y el importe calculado.

# REGLAS Y SUPUESTOS
# - Los primeros 150 kWh tienen un costo de $1.00 por kWh.
# - Los kWh del 151 al 280 tienen un costo de $1.50 por kWh.
# - Los kWh superiores a 280 tienen un costo de $3.00 por kWh.
# - La tarifa es escalonada: cada bloque se cobra con su tarifa
#   correspondiente.
# - Si el consumo es exactamente 150 kWh, todo se cobra a $1.00.
# - Si el consumo es exactamente 280 kWh, los primeros 150 kWh
#   se cobran a $1.00 y los siguientes 130 kWh a $1.50.
# - El resultado se muestra con dos decimales.
# - El consumo se considera un valor no negativo.

# ALGORITMO
# 1. Leer el consumo mensual en kWh.
# 2. Si consumo <= 150:
#       pago = consumo * 1.00
# 3. En caso contrario, si consumo <= 280:
#       pago = 150 * 1.00 + (consumo - 150) * 1.50
# 4. En caso contrario:
#       pago = 150 * 1.00 + 130 * 1.50 + (consumo - 280) * 3.00
# 5. Mostrar el consumo y el pago con dos decimales.

# CASOS DE PRUEBA
# 100 kWh -> $100.00
# 150 kWh -> $150.00
# 200 kWh -> $225.00
# 280 kWh -> $345.00
# 300 kWh -> $405.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerConsumo() -> float : lee y devuelve el consumo mensual en kWh.
# calcularPago(consumo) -> float : calcula y devuelve el importe del recibo.
# mostrarRecibo(consumo, pago) -> None : muestra el consumo y el importe del recibo.

# Implementa el algoritmo anterior utilizando las funciones del contrato.