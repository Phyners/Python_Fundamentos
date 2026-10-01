nombre_cliente = input("¿Cuál es el nombre del cliente? ")
print(f"Hola {nombre_cliente}, bienvenido a la tienda.")
precio_producto1 = float(input("¿Cuál es el precio del producto 1? "))
precio_producto2 = float(input("¿Cuál es el precio del producto 2? "))
precio_total = precio_producto1 + precio_producto2
print(f"{nombre_cliente}, El precio total de los productos es: {precio_total}")