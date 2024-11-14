nombre = input("Ingrese el nombre del empleado: ")
salario_por_hora = float(input("Ingrese el salario básico por hora: "))
horas_trabajadas = float(input("Ingrese el número de horas trabajadas en el mes: "))

salario_mensual = salario_por_hora * horas_trabajadas

if salario_mensual > 450000:
    print(f"Nombre: {nombre}, Salario Mensual: ${salario_mensual:.2f}")
else:
    print(f"Nombre: {nombre}")