"""
NOM: Nombre del trabajador.
NHT: Número de horas trabajadas.
VHN: Valor hora normal trabajada.
HET: Horas extras trabajadas.
HEE8: Horas extras que exceden de 8.
SALARIO: Pago total que recibe el trabajador.
"""


def calcular_salario(nombres, nht, vhn):
    # Definición de variables
    het = 0
    hee8 = 0
    salario = 0

    # Proceso
    if nht > 40:
        het = nht - 40
        if het > 8:
            hee8 = het - 8
            pago_horas_extras = vhn * 2 * 8 + vhn * 3 * hee8
        else:
            pago_horas_extras = vhn * 2 * het
        salario = vhn * 40 + pago_horas_extras
    else:
        salario = nht * vhn

    # Datos de salida
    return nombres, salario

# Ejemplo de uso
nombres = "Juan Perez"
nht = 50  # Número de horas trabajadas en la semana
vhn = 10  # Valor recibido por una hora normal de trabajo

nombre_trabajador, salario_devengado = calcular_salario(nombres, nht, vhn)
print(f"Nombre del trabajador: {nombre_trabajador}")
print(f"Salario devengado: {salario_devengado}")