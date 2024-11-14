
peso_A = float(input("Ingrese el peso de la esfera A: "))
peso_B = float(input("Ingrese el peso de la esfera B: "))
peso_C = float(input("Ingrese el peso de la esfera C: "))

if peso_A > peso_B and peso_A > peso_C:
    print("La esfera de mayor peso es la esfera A.")
elif peso_B > peso_A and peso_B > peso_C:
    print("La esfera de mayor peso es la esfera B.")
else:
    print("La esfera de mayor peso es la esfera C.")