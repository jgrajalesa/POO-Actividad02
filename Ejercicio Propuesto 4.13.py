VALCOMP = float(input("Ingrese el valor de la compra: "))
COLOR = input("Ingrese el color de la bolita: ").lower()

if COLOR == "blanca":
    PDES = 0
elif COLOR == "verde":
    PDES = 10
elif COLOR == "amarilla":
    PDES = 25
elif COLOR == "azul":
    PDES = 50
else:
    PDES = 100

VALPAG = VALCOMP - (VALCOMP * PDES / 100)

print(f"El valor a pagar es: {VALPAG:.2f}")