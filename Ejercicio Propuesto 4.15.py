def encontrar_esfera_diferente(pesoA, pesoB, pesoC, pesoD):
    if pesoA == pesoB and pesoA == pesoC:
        diferente = "D"
        if pesoD > pesoA:
            mensaje = "La esfera D es de mayor peso."
        else:
            mensaje = "La esfera D es de menor peso."
    elif pesoA == pesoB and pesoA == pesoD:
        diferente = "C"
        if pesoC > pesoA:
            mensaje = "La esfera C es de mayor peso."
        else:
            mensaje = "La esfera C es de menor peso."
    elif pesoA == pesoC and pesoA == pesoD:
        diferente = "B"
        if pesoB > pesoA:
            mensaje = "La esfera B es de mayor peso."
        else:
            mensaje = "La esfera B es de menor peso."
    else:
        diferente = "A"
        if pesoA > pesoB:
            mensaje = "La esfera A es de mayor peso."
        else:
            mensaje = "La esfera A es de menor peso."
    return diferente, mensaje

# Solicitar pesos al usuario
pesoA = float(input("Ingrese el peso de la esfera A: "))
pesoB = float(input("Ingrese el peso de la esfera B: "))
pesoC = float(input("Ingrese el peso de la esfera C: "))
pesoD = float(input("Ingrese el peso de la esfera D: "))

# Encontrar la esfera diferente
diferente, mensaje = encontrar_esfera_diferente(pesoA, pesoB, pesoC, pesoD)

# Salida del resultado
print(f"La esfera diferente es la {diferente}. {mensaje}")