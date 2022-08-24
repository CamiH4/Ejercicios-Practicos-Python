n = str(input("Ingrese su primer nombre: "))
sn = str(input("Ingrese su segundo nombre (en caso de no tenerlo presione enter): "))
ap = str(input("Ingrese su primer apellido: "))
sap = str(input("Ingrese su segundo apellido (en caso de no tenerlo presione enter): "))
c = (input("Carrera (Por ejemplo: Ingenieria en Sistemas): "))
p = float(input("Promedio: "))

if c == "Ingenieria en Sistemas" and p > 95:
    print("Usted puede optar a una beca.")
elif c != "Ingenieria en Sistemas" and p > 85:
    print("Usted puede optar a una beca.")
else:
    print("Usted no puede optar a una beca.")

