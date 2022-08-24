precios = []

cant = int(input("Cuantos productos?: "))
for i in range(cant):
    precio = float(input("Digite el precio C$: "))
    precios.append(precio)

suma = 0
for precio in precios:
    suma += precio

print("El total es C$: ", suma)
