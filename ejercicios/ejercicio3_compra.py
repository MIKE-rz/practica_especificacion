'''
Una tienda aplica 10% de descuento en compras de $1,000 o más y 20%
en compras de $5,000 o más. A la compra se le agrega el 16% de IVA.
Se necesita mostrar el ticket con subtotal, descuento, IVA y total.
'''

# PROBLEMA
# Calcular el descuento, IVA y total de una compra a partir del subtotal.

# ENTRADAS
# subtotal : float, pesos mexicanos, valor mayor o igual a 0.

# SALIDAS
# descuento : float, pesos mexicanos, mostrado con dos decimales.
# iva : float, pesos mexicanos, mostrado con dos decimales.
# total : float, pesos mexicanos, mostrado con dos decimales.

# REGLAS Y SUPUESTOS
# - Si el subtotal es menor a $1000, no hay descuento.
# - Si el subtotal es mayor o igual a $1000 y menor a $5000,
#   el descuento es del 10%.
# - Si el subtotal es mayor o igual a $5000, el descuento es del 20%.
# - El IVA es del 16%.
# - El IVA se calcula después de aplicar el descuento.
# - El total es subtotal - descuento + IVA.
# - Los valores monetarios se muestran con dos decimales.
# - Un subtotal exactamente de $1000 recibe 10% de descuento.
# - Un subtotal exactamente de $5000 recibe 20% de descuento.

# ALGORITMO
# 1. Leer el subtotal.
# 2. Si subtotal >= 5000:
#       descuento = subtotal * 0.20
# 3. En caso contrario, si subtotal >= 1000:
#       descuento = subtotal * 0.10
# 4. En caso contrario:
#       descuento = 0
# 5. Calcular subtotalConDescuento = subtotal - descuento.
# 6. Calcular iva = subtotalConDescuento * 0.16.
# 7. Calcular total = subtotalConDescuento + iva.
# 8. Mostrar subtotal, descuento, IVA y total.

# CASOS DE PRUEBA
# $500 -> Descuento $0.00, IVA $80.00, Total $580.00
# $900 -> Descuento $0.00, IVA $144.00, Total $1044.00
# $1000 -> Descuento $100.00, IVA $144.00, Total $1044.00
# $5000 -> Descuento $1000.00, IVA $640.00, Total $4640.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerSubtotal() -> float : lee y devuelve el subtotal de la compra.
# calcularDescuento(subtotal) -> float : calcula el descuento correspondiente.
# calcularIVA(subtotal, descuento) -> float : calcula el IVA después del descuento.
# calcularTotal(subtotal, descuento, iva) -> float : calcula el total de la compra.
# mostrarTicket(subtotal, descuento, iva, total) -> None : muestra el ticket.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerSubtotal():
    subtotal = float(input("Ingrese el subtotal de la compra: "))
    return subtotal

def calcularDescuento(subtotal):
    if subtotal >= 5000:
        descuento = subtotal * 0.20
    elif subtotal >= 1000:
        descuento = subtotal * 0.10
    else:
        descuento = 0
    return descuento

def calcularIVA(subtotal, descuento):
    subtotalConDescuento = subtotal - descuento
    iva = subtotalConDescuento * 0.16
    return iva

def calcularTotal(subtotal, descuento, iva):
    total = subtotal - descuento + iva
    return total

def mostrarTicket(subtotal, descuento, iva, total):
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"Total: ${total:.2f}")
