import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            raise ValueError("Los lados deben ser números positivos.")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def es_valido(self):
        return (
            self.lado1 + self.lado2 > self.lado3 and
            self.lado1 + self.lado3 > self.lado2 and
            self.lado2 + self.lado3 > self.lado1
        )

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def calcular_semiperimetro(self):
        return self.calcular_perimetro() / 2

    def calcular_area(self):
        if not self.es_valido():
            raise ValueError("Los lados ingresados no forman un triángulo válido.")
        s = self.calcular_semiperimetro()
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def mostrar_informacion(self):
        if self.es_valido():
            print(f"El perímetro del triángulo es: {self.calcular_perimetro()}")
            print(f"El semiperímetro del triángulo es: {self.calcular_semiperimetro()}")
            print(f"El área del triángulo es: {self.calcular_area():.2f}")
        else:
            print("Los lados ingresados no forman un triángulo válido.")

try:
    lado1 = float(input("Ingrese el tamaño del primer lado del triángulo: "))
    lado2 = float(input("Ingrese el tamaño del segundo lado del triángulo: "))
    lado3 = float(input("Ingrese el tamaño del tercer lado del triángulo: "))
    
    triangulo = Triangulo(lado1, lado2, lado3)
    triangulo.mostrar_informacion()
except ValueError as e:
    print(e)
    print("Por favor, ingrese un número válido. En caso de que su número sea decimal, utilice un punto.")