ct = int(input("Ingrese su numero de cuenta: "))
saldo = 5790
print("Su saldo actual es de $", saldo)
ret = float(input("Digite el monto a retirar $: "))
saldorest = saldo - ret
if saldorest == 100:
    print("Ha llegado al minimo de su cuenta.")
    print("Su saldo actual es de $", saldorest)
elif saldorest < 100:
    print("Su saldo es insuficiente para realizar el retiro. ")
else:
    print("Su saldo actual es de $", saldorest)