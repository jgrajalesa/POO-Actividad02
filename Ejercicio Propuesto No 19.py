import math

tamaño_lado_triangulo = input("Ingrese el tamaño de un lado del triángulo equilátero: ")

try:
    tamaño_lado_triangulo = float(tamaño_lado_triangulo)
    
    if tamaño_lado_triangulo > 0:
        perimetro = 3 * tamaño_lado_triangulo
        valor_altura = (math.sqrt(3) / 2) * tamaño_lado_triangulo
        area = (math.sqrt(3) / 4) * tamaño_lado_triangulo ** 2

        print(f"El perímetro es: {perimetro:.2f}")
        print(f"El valor de la altura es: {valor_altura:.2f}")
        print(f"El valor del área es: {area:.2f}")
    else: 
        print("El número debe ser positivo.")
except ValueError:
    print("Por favor, ingrese un número válido.")
    print("En caso de que su número sea decimal, utilice un punto.")