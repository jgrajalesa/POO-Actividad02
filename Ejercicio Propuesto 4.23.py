import cmath

def cuadratico(a, b, c):
    discriminant = b**2 - 4*a*c
    
    sol1 = (-b - cmath.sqrt(discriminant)) / (2*a)
    sol2 = (-b + cmath.sqrt(discriminant)) / (2*a)
    
    return sol1, sol2

# Example usage
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))

solution1, solution2 = cuadratico(A, B, C)
print(f"Las soluciones de la ecuación son: {solution1} y {solution2}")