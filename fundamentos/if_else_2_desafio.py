# Calculo de IMC
# Criar programa que faça o calculo de IMC, perguntar ao usuário:
# "Qual é sua Altura em cm?"
# "Qual o seu peso em kg?"

# Menor que 18.5: MAGREZA
# Entre 18.5 e 24.9: NORMAL
# Entre 25.0 e 29.9: SOBREPESO
# Entre 30.0 e 39.9: OBESIDADE
# 40.0 ou mais: OBESIDADE GRAVE

# Solicitar as informações ao usuário
altura = float(input("Qual a sua altuma em metros? "))
peso = float(input("Qual seu peso em kg? "))

# Calcula IMC
imc = peso / (altura * altura)

def calcula_imc(imc):
    if imc < 18.5:
        print(f"Seu IMC atual é {imc}, indica magresa.")
    elif imc >= 18.5 and imc < 25.0:
        print(f"Seu IMC atual é {imc}, é considerado normal.")
    elif imc >= 25.0 and imc < 30.0:
        print(f"Seu IMC atual é {imc}, indica sobrepeso.")
    elif imc >= 30.0 and imc < 40.0:
        print(f"Seu IMC atual é {imc}, indica obesidade.")
    else:
        print(f"Seu IMC atual é {imc:0.1f}, indica obesidade grave.")

calcula_imc(imc)