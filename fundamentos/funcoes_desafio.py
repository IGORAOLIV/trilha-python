# Desafio com funções
# Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário deve informar as segintes iinformações:
# - Largura da parede (em metros) 
# - Altura da parede (em metros)
# - Rendimento da tinta (em metros quadrados por litro)
# O programa deve mostrar na tela a mensagem "Você necessita de X latas de tinta"

# Solicitar as informações ao usuário
rendimento = float(input("Informe o rendimento da tinta em metros quadrados por litro: "))
altura = float(input("Informe a altura da parede em metros: "))
largura = float(input("Informe a largura da parede em metros: "))

# Calcular a área da parede
area = largura * altura

# Função para calcular a quantidade de tinta necessária com base na área e rendimento da tinta
def calcula_tinta(area, rendimento):
    quantidade_tinta = area / rendimento
    print(f"Você necessita de {quantidade_tinta:.1f} latas de tinta")

calcula_tinta(area, rendimento)