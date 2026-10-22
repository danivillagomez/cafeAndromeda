# Andromeda Digital - Registro de pedidos

# Variables iniciales
total_cuenta = 0.0      # Acumula el total de toda la venta
detalle_ticket = ""     # Guarda una línea por cada producto para imprimirlas al final

# Precio simulado: en una fase posterior vendrá de la base de datos
precio_producto = 25.00

# Ciclo principal: se repite hasta que el usuario decida no agregar más productos
while True:

    # Valida que el nombre del producto no esté vacío
    while True:
        producto_o_id = input("Escriba el nombre del producto o ID: ")
        if producto_o_id == "":
            print("Error! Escriba un producto")
        else:
            break

    # Pide la cantidad y la repite hasta que sea al menos uno
    cantidad = int(input("Escriba la cantidad de su producto: "))
    while cantidad <= 0:
        print("Error! Escriba al menos uno")
        cantidad = int(input("Escriba la cantidad de su producto: "))

    # Calcula el subtotal de este producto y lo suma al total de la venta
    costo_individual = precio_producto * cantidad
    total_cuenta += costo_individual

    # Guarda la línea de este producto para mostrarla en el ticket final
    detalle_ticket += f"{cantidad}x {producto_o_id} (${precio_producto} c/u) = ${costo_individual}\n"

    # Pregunta si se desea registrar otro producto; con cualquier respuesta distinta de "s" termina el ciclo
    if input("¿Desea agregar otro producto? (s/n): ") != "s":
        break

# Ticket final con todos los productos y el total acumulado
print("====================================")
print("         CAFE ANDROMEDA          ")
print("====================================")
print(detalle_ticket)
print("====================================")
print(f"TOTAL A PAGAR:            ${total_cuenta}")
print("====================================")
print("     ¡Gracias por su compra!       ")
print("====================================")
