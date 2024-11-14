numero_inscripcion = 192
nombres = 'Juan Pablo'
patrimonio = 2000001
estrato_social = 3

# Valor constante de matrícula
valor_matricula = 50000

# Verificar si se aplica incremento
if patrimonio > 2000000 and estrato_social > 3:
    incremento = patrimonio * 0.03
    valor_matricula += incremento

# Mostrar resultados
print(f"Número de inscripción: {numero_inscripcion}")
print(f"Nombres: {nombres}")
print(f"Pago por matrícula: ${valor_matricula:.2f}")