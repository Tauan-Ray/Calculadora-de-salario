salario_anual = 192000
horas_por_dia = 8
dias_por_semana = 5
semanas_por_ano = 52

horas_trabalhadas_por_ano = horas_por_dia * dias_por_semana * semanas_por_ano
salario_por_hora = salario_anual / horas_trabalhadas_por_ano

print(f"Seu salário por hora é: {salario_por_hora:.2f}")