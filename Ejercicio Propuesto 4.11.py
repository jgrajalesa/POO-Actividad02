
N1 = int(input("Ingrese el primer número: "))
N2 = int(input("Ingrese el segundo número: "))
N3 = int(input("Ingrese el tercer número: "))

# Proceso para encontrar el mayor número
if (N1 > N2) and (N1 > N3):
    MAYOR = N1
elif (N2 > N1) and (N2 > N3):
    MAYOR = N2
else:
    MAYOR = N3

# Datos de salida
print("El número mayor es:", MAYOR)