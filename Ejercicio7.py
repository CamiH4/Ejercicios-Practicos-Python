edades = []

cant = int(input("Cuantas edades?: "))

for i in range(cant):
    edad = int(input("Digite la edad: "))
    edades.append(edad)

suma = 0 
for i in edades:
    suma += edad

prom = suma / len(edades)
print("El promedio es: ", prom)