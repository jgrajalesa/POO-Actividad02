codigo_empleado = 418524
nombres = "David Alexander"
horas_trabajadas_mes = 70
valor_hora_trabajada = 42000
porcentaje_retencion = 12.5

salario_bruto = horas_trabajadas_mes * valor_hora_trabajada
salario_neto = salario_bruto - (salario_bruto * porcentaje_retencion / 100)

print(f"Codigo de empleado: {codigo_empleado}")
print(f"Nombres: {nombres}")
print(f"Salario bruto: {salario_bruto}")
print(f"Salario neto: {salario_neto}")