class Empleado:
    def __init__(self, codigo_empleado, nombres, horas_trabajadas_mes, valor_hora_trabajada, porcentaje_retencion):
        self.codigo_empleado = codigo_empleado
        self.nombres = nombres
        self.horas_trabajadas_mes = horas_trabajadas_mes
        self.valor_hora_trabajada = valor_hora_trabajada
        self.porcentaje_retencion = porcentaje_retencion

    def calcular_salario_bruto(self):
        return self.horas_trabajadas_mes * self.valor_hora_trabajada

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto - (salario_bruto * self.porcentaje_retencion / 100)

    def mostrar_informacion(self):
        print(f"Código de empleado: {self.codigo_empleado}")
        print(f"Nombres: {self.nombres}")
        print(f"Salario bruto: {self.calcular_salario_bruto()}")
        print(f"Salario neto: {self.calcular_salario_neto()}")

empleado = Empleado(418524, "David Alexander", 70, 42000, 12.5)

empleado.mostrar_informacion()