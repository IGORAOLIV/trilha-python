# Desafio com If, Elif e Else
# Criar um programa que dependendo da temperatura (em celsius) do Steak retorne o ponto de cozimento em português. O usuário deve informar a temperatura. 

# Temperaturas:
# -  < 48°C: Cru (exibir mensagem de "Crua - Cozinhar por mais alguns minutos" )
# - 48°C a 53°C: Selada (exibir mensagem de "Selada" )
# - 54°C a 60°C: Ao ponto para mal passado (exibir mensagem de "Ao ponto para mal passado" )
# - 61°C a 65°C: Ao ponto (exibir mensagem de "Ao ponto" )
# - 66°C a 71°C: Bem passado (exibir mensagem de "Bem passado" )
# - > 71°C: Queimada (exibir mensagem de "Queimada - Finalizar o cozimento" )

# Solicitar a temperatura do Steak ao usuário
temperatura = int(input("Informe a temperatura do Steak em Celsius: "))

# Verificar o ponto de cozimento com base na temperatura (primeira resposta)
# def verifica_temperatura(temperatura):
#     if temperatura < 48:
#         print("Crua - Cozinhar por mais alguns minutos")
#     elif 48 <= temperatura <= 53:
#         print("Selada")
#     elif 54 <= temperatura <= 60:
#         print("Ao ponto para mal passado")
#     elif 61 <= temperatura <= 65:
#         print("Ao ponto")
#     elif 66 <= temperatura <= 71:
#         print("Bem passado")
#     else:
#         print("Queimada - Finalizar o cozimento")

# verifica_temperatura(temperatura) 

# Segunda resposta após correção utilizando "in range"
def verifica_temperatura(temperatura):
    if temperatura < 48:
        print("Crua - Cozinhar por mais alguns minutos")
    elif temperatura in range(48, 53):
        print("Selada")
    elif temperatura in range(54, 59):
        print("Ao ponto para mal passado")
    elif temperatura in range(60, 64):
        print("Ao ponto")
    elif temperatura in range(65, 70):
        print("Bem passado")
    else:
        print("Queimada - Finalizar o cozimento")

verifica_temperatura(temperatura)