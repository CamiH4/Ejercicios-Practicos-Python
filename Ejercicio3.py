print("Ingresa el precio de un producto y le aplicaré el iva.")
precio = float(input("Ingrese el precio del producto C$: "))
precio_iva = precio * 0.15
total = precio + precio_iva
print("El total con iva es de C$: ", total)