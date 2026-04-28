# Desafio com 'Sets'
# Criar um programa que gera 3 listas de acordo com as necessidades logo abaixo:
# Lista1 = Funcionários que tem carro e trabalham a noite.
# Lista2 = Funcionários que tem carro e trabalham de dia.
# Lista3 = Funcionários que não tem carro.

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

# Gerar as listas utilizando 'Sets' (primeira resposta)
# funcionarios_set = set(funcionarios)
# turno_dia_set = set(turno_dia)
# turno_noite_set = set(turno_noite)
# tem_carro_set = set(tem_carro)
# lista1 = turno_noite_set.intersection(tem_carro_set)
# lista2 = turno_dia_set.intersection(tem_carro_set)
# lista3 = funcionarios_set.difference(tem_carro_set)

# Resposta corrigida utilizando 'Sets' (segunda resposta)
lista1 = set(tem_carro).intersection(turno_noite)
lista2 = set(tem_carro).intersection(turno_dia)
lista3 = set(funcionarios).difference(tem_carro)

# Exibir as listas
print("Funcionários que tem carro e trabalham a noite:", lista1)
print("Funcionários que tem carro e trabalham de dia:", lista2)
print("Funcionários que não tem carro:", lista3)

