try:
    lado1 = float(input("Ingrese el tamaño del primer lado del triángulo: "))
    lado2 = float(input("Ingrese el tamaño del segundo lado del triángulo: "))
    lado3 = float(input("Ingrese el tamaño del tercer lado del triángulo: "))
    
    if lado1 > 0 and lado2 > 0 and lado3 > 0:
        if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
            perimetro = lado1 + lado2 + lado3
            semiperimetro = perimetro / 2
            area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5
            print(f"El perímetro del triángulo es: {perimetro}")
            print(f"El semiperímetro del triángulo es: {semiperimetro}")
            print(f"El área del triángulo es: {area}")
        else:
            print("Los lados ingresados no forman un triángulo válido.")
    else:
        print("Los lados ingresados no forman un triángulo válido")
except ValueError:
    print("Por favor, ingrese un número válido.")
    print("En caso de que su número sea decimal, utilice un punto.")