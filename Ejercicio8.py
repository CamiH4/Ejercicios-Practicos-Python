precios = []

cant = int(input("Digite la cantidad de precios: "))

for x in range(cant):
    precio = float(input("Digite el precio C$: "))
    precios.append(precio)

mayor = precios[x]
menor = precios[x]
for precio in precios:
    if precio > mayor:
        mayor = precio

    if precio < menor:
        menor = precio

print("El precio mas alto es C$: ", mayor)
print("El precio mas bajo es C$: ", menor)



