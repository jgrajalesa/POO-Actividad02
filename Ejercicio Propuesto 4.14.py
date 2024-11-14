VD1 = float(input("Ingrese las ventas del departamento 1: "))
VD2 = float(input("Ingrese las ventas del departamento 2: "))
VD3 = float(input("Ingrese las ventas del departamento 3: "))
SALAR = float(input("Ingrese el salario de los vendedores: "))

TOTVEN = VD1 + VD2 + VD3
PORVEN = TOTVEN * 0.33

if VD1 > PORVEN:
    SALAR1 = SALAR + SALAR * 0.2
else:
    SALAR1 = SALAR

if VD2 > PORVEN:
    SALAR2 = SALAR + SALAR * 0.2
else:
    SALAR2 = SALAR

if VD3 > PORVEN:
    SALAR3 = SALAR + SALAR * 0.2
else:
    SALAR3 = SALAR

print(f"Salario recibido por los vendedores del departamento 1: {SALAR1}")
print(f"Salario recibido por los vendedores del departamento 2: {SALAR2}")
print(f"Salario recibido por los vendedores del departamento 3: {SALAR3}")