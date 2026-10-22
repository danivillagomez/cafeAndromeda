# Andromeda Digital - Nombre de Algoritmo

# Variables iniciales
total_cuenta = 0.0      # Total a pagar
detalle_ticket = ""     # Se junta la data del subtotal

# Precio simulado
precio_producto = 25.00

# Loop para agregar mas productos
while True:

    # Filtro anti campos vacios
    while True:
        producto_o_id = input("Escriba el nombre del producto o ID: ")
        if producto_o_id == "":
            print("Error! Escriba un producto")
        else:
            break

    # Validacion de cantidad
    cantidad = int(input("Escriba la cantidad de su producto: "))
    while cantidad <= 0:
        print("Error! Escriba al menos uno")
        cantidad = int(input("Escriba la cantidad de su producto: "))

    # Operaciones de cuenta
    costo_individual = precio_producto * cantidad
    total_cuenta += costo_individual

    # Subtotal
    detalle_ticket += f"{cantidad}x {producto_o_id} (${precio_producto} c/u) = ${costo_individual}\n"

    # Solicitud de nuevo producto
    if input("¿Desea agregar otro producto? (s/n): ") != "s":
        break

# Ticket final a imprimir
print("====================================")
print("         CAFE ANDROMEDA          ")
print("====================================")
print(detalle_ticket)
print("====================================")
print(f"TOTAL A PAGAR:            ${total_cuenta}")
print("====================================")
print("     ¡Gracias por su compra!       ")
print("====================================")
