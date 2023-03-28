

# Há duas telas de abertura no inicio do programa, edite e escolha da forma que desejar rickdevcod exercicios # 

print("**********************************************")
print("Bem vindo ao programa de bonus para assinatura")
print("**********************************************")
continuar = True

while continuar:
    tipo_assinatura = input("Digite o tipo de assinatura (Basic/Silver/Gold/Platinum): ")
    print("Bem-vindo ao programa de bônus para assinatura " + tipo_assinatura + "!")


    faturamento_anual_str = input("Digite o faturamento anual:")
    faturamento_anual = float(faturamento_anual_str.replace(".",""))
    print(faturamento_anual)

    if tipo_assinatura == "Basic":
        bonus = faturamento_anual * 0.3
        print("O valor da anuidade é:",bonus)
    elif tipo_assinatura == "Silver":
        bonus = faturamento_anual * 0.2
    elif tipo_assinatura == "Gold":
        bonus = faturamento_anual * 0.1
        print("O valor da anuidade é:", bonus)
    elif tipo_assinatura == "Platinum":
        bonus = faturamento_anual * 0.05
        print("O valor da anuidade é",bonus)
    else:
        print("Tipo de assinatura invalida: Digite Basic, Silver, Gold,Platinum")

    opcao = input("Deseja fazer uma nova consulta? (S/N)")
    if opcao.upper() == "N":
        continuar = False
