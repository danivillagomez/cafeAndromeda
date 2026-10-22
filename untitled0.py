# Andromeda Digital

#Declaramos variables

total_cuenta = 0.0
costo_individual = 0.0
precio_producto = 0.0
cantidad = 0
producto_o_id = ""

while True:
  producto_o_id = str(input("Escriba el nombre del producto o ID: "))
  if producto_o_id == "" :
    print("Error! Escriba un producto")
  else :
    break
precio_producto = 25.00

cantidad = int(input("Escriba la cantidad de su producto: "))

while cantidad <= 0 :
  print("Error! Escriba al menos uno")
  cantidad = int(input("Escriba la cantidad de su producto: "))

costo_individual = precio_producto * cantidad
total_cuenta = costo_individual

# Formato de ticket de compra profesional corregido
print("====================================")
print("         CAFE ANDROMEDA          ")
print("====================================")
print(f"{cantidad}x {producto_o_id} ($ {precio_producto} c/u)")
print(f"SUBTOTAL:                 ${costo_individual}")
print("====================================")
print(f"TOTAL A PAGAR:            ${total_cuenta}")
print("====================================")
print("     ¡Gracias por su compra!       ")
print("====================================")
