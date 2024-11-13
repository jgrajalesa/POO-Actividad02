tamaño_lado_triangulo = (input("Ingrese el tamaño de un lado del triangulo equilatero: "))
try:
  tamaño_lado_triangulo = float(tamaño_lado_triangulo)
  if tamaño_lado_triangulo >= 0:

    perimetro = 3 * tamaño_lado_triangulo
    valor_altura = tamaño_lado_triangulo * 3/2
    area = tamaño_lado_triangulo**2 * 1.73

    print(f"Perimetro: {perimetro:.2f}")
    print(f"Valor de la altura: {valor_altura:.2f}")
    print(f"Área: {area:.2f}")
  else: 
      print("El número debe ser positivo")
except ValueError:
    print("Por favor, ingrese un número válido.")
    print("En caso de que su número sea un decimal, utilice un punto.")