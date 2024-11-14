import math

class TrianguloEquilatero:
    def __init__(self, tamaño_lado):
        if tamaño_lado <= 0:
            raise ValueError("El tamaño del lado debe ser un número positivo.")
        self.tamaño_lado = tamaño_lado

    def calcular_perimetro(self):
        return 3 * self.tamaño_lado

    def calcular_altura(self):
        return (math.sqrt(3) / 2) * self.tamaño_lado

    def calcular_area(self):
        return (math.sqrt(3) / 4) * self.tamaño_lado ** 2

    def mostrar_informacion(self):
        print(f"El perímetro es: {self.calcular_perimetro():.2f}")
        print(f"El valor de la altura es: {self.calcular_altura():.2f}")
        print(f"El valor del área es: {self.calcular_area():.2f}")

tamaño_lado_triangulo = input("Ingrese el tamaño de un lado del triángulo equilátero: ")

try:
    tamaño_lado_triangulo = float(tamaño_lado_triangulo)
    triangulo = TrianguloEquilatero(tamaño_lado_triangulo)
    triangulo.mostrar_informacion()
except ValueError as e:
    print(e)
    print("Por favor, ingrese un número válido. En caso de que su número sea decimal, utilice un punto.")