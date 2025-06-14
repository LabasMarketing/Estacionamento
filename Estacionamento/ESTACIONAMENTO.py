#SISTEMA DE UM ESTACIONAMENTO

#Introdução ao usuário
print("Olá bem vindo ao estacionamento, este programa tem a funcionalidade de controlar tudo por aqui, entre seus recursos estão: a entrada e saída dos veículos e o pagamento")

#IMPORT'S
from datetime import datetime

#VISÃO GERAL
#OPCAO 1: Cadastro Tarífas
#OPCAO 2: Registrar entrada de veículo
#OPCAO 3: Registrar saída de veículo
#OPCAO 4: Gerar Relatório diário:
#OPCAO 5: Gerar Relatório por tipo de veículo
#OPCAO 6: Sair


#CONTA PARA CODIFICAR OPCÕES 4 e 5:
    #RELATORIO DIÁRIO
contagem_carros = 0
valor_total_dia = 0
tempo_medio = 0

#RELATÓRIO POR TIPO DE VEÍCULO
tipo_moto = 0
tipo_pequeno = 0
tipo_grande = 0

#MENU PRINCIPAL
while True:
    print("1. Cadastro Tarífas")
    print("2. Registrar entrada de veículo")
    print("3. Registrar saída de veículo")
    print("4. Gerar Relatório diário")
    print("5. Gerar Relatório por tipo de veículo")
    print("6. Sair")

    #DIGITE UMA OPCAO:
    opcao = int(input("Escolha uma opção: "))

    #Quando o usuário digitar 6, o aplicativo encerra
    if opcao == 6:
        print("Aplicativo Encerrado!")
        break  

    #Estrutura Repetição (While)
    while opcao > 6 or opcao < 1:
        print("Opção Inválida")
        print("Tente Novamente!")
        opcao = int(input("Escolha uma opção: "))

    #OPÇÃO REFERENTE AO CÓDIGO 1
    if opcao == 1:
        # Cadastro de tarífas
        print("\nAqui você poderá alterar o valor correspondente de cada veículo")

        # Tipo Veículo
        print("Escolha o tipo de veículo: ")
        print("1. Veículo Pequeno")
        print("2. Veículo Grande")
        print("3. Motos")
        tipo = int(input("Digite um número: "))
        while tipo < 1 or tipo > 3:
            tipo = int(input("Digite um número: "))
            break
        

        #CÓDIGO AUXILIAR OPÇÃO 5 
        if tipo == 1:
            tipo_pequeno+=1
        elif tipo == 2:
            tipo_grande+=1
        elif tipo == 3:
            tipo_moto+=1

        # PREÇO FIXO POR 3 HORAS UTILIZADAS NO ESTACIONAMENTO
        preco = float(input("\nDigite o valor referente a 3 horas de estádia no estacionamento: "))

        # PRECO POR CADA HORA ADICIONAL
        hora_adicional = float(input("Preço por cada hora adicional: "))

        # Final do Código 1
        print("\nPreços atualizados com sucesso!")
        print("Tipo do veículo: " + str(tipo) + ". Preço fixo por 3 horas: R$ " + str(preco) + " Preço por hora adicional: R$ " + str(hora_adicional) + "\n")

    #OPÇÃO REFERENTE AO CÓDIGO 2
    elif opcao == 2:
        # Controle HORA de ENTRADA e SAÍDA
        # Entrada e saída:
        entrada = datetime.now()
        entrada_hora = entrada.hour
        # Placa DO CARRO
        placa = input("\nDigite a placa do veículo: ")

        # Tipo Veículo
        print("\nEscolha o tipo de veículo: ")
        print("1. Veículo Pequeno")
        print("2. Veículo Grande")
        print("3. Motos")
        tipo = int(input("Digite um número: "))
        while tipo < 1 or tipo > 3:
            tipo = int(input("Digite um número: "))
            break

        # Registro de entrada
        print("\nPlaca: " + str(placa) + ". Tipo do veículo: " + str(tipo) + ". Hora de entrada: " + entrada.strftime('%H:%M:%S') + "\n")

    #OPÇÃO REFERENTE AO CODIGO 3
    elif opcao == 3:

        #CONTA ÚTIL PARA CODIGO 4  
        #VALOR TOTAL PAGAMENTO SOMA
        contagem_carros += 1

        placa = input("Digite a placa do veículo: ")
        print("\nO Pagamento será relizado por PIX? Caso seja você terá um desconto de 5%")
        print("1. Sim")
        print("2. Não")
        pix = int(input("Digite 1 para SIM ou 2 para NÃO: "))

        #CALCULO CASO PAGAMENTO SEJA POR PIX (HAVERÁ O DESCONTO DE 5%)
        # Registro da saída (PIX)
        saida = datetime.now()
        saida_hr=saida.hour
        tempo_estadia = (saida - entrada) .total_seconds()/ 3600  # Calcula o tempo de estadia em horas
        tempo_estadia_hr = (saida_hr - entrada_hora) / 3600
        if tempo_estadia_hr <= 3:
            if pix == 2:
               preco = preco
               print("\nO valor ficou em R$ " + str(preco))
               print("Tempo de estadia: ",round(tempo_estadia, 2),"horas. Pagamento por PIX? Não.")
        elif tempo_estadia_hora > 3:
            preco = preco + (tempo_estadia*tempo_estadia_hr)
            print("Preço a pagar: R$ ",preco)
        if pix == 1:
            desconto = preco * 0.05
            preco = preco - desconto
            print("\nO valor com o desconto ficou em " + "R$" + str(preco))
            print("Tempo de estadia:",round(tempo_estadia, 2),"horas. Pagamento por PIX? Sim.")
        print("Placa: ",placa,". Tipo do veículo:",tipo,". Hora de saída: ",saida.strftime('%H:%M:%S') + "\n")


        #CONTA ÚTIL PARA CODIGO 4
        #VALOR TOTAL PAGAMENTO SOMA
        valor_total_dia+=preco
        tempo_medio+=tempo_estadia


    elif opcao == 3:
    # Registro para a saída (Sem PIX)
        saida = datetime.now()
        saida_hora = saida.hour
        tempo_estadia = (saida - entrada).total_seconds() / 3600  # Calcula o tempo de estadia em horas
        tempo_estadia_hora = (saida_hora - entrada_hora) / 3600
        if tempo_estadia_hora <= 3:
            preco = preco
            print(str("Preço a pagar: R$ " + preco))
        elif tempo_estadia_hora > 3:
            preco = preco + (tempo_estadia * tempo_estadia_hora)
            print("Preço a pagar: R$ " + preco)
        print("Placa:" + str(placa) + ". Tipo do veículo:" + str(tipo) + ". Hora de saída:" + saida.strftime('%H:%M:%S') + "\n")
        print("Tempo de estadia:" + round(tempo_estadia, 2) + "horas. Pagamento por PIX? Não.")

    # OPÇÃO CODIGO 4
    elif opcao == 4:
        if contagem_carros > 0:
            tempo_medio = tempo_medio / contagem_carros
        print("\nQuantidade de clientes hoje: ", contagem_carros,". Tempo médio de permanência: ",round(tempo_medio,2),"horas", ". Lucro total do dia: R$ ", round(valor_total_dia,2))

    # OPÇÃO CODIGO 5
    elif opcao == 5:
        print("\nQuantidade de clientes de Veículos Pequenos: " + str(tipo_pequeno))
        print("Quantidade de clientes de Veículos Grandes: " + str(tipo_grande))
        print("Quantidade de clientes de Motos: " + str(tipo_moto))

    #QUAL O VEÍCULO MAIS REGISTRADO
        if tipo_pequeno > tipo_grande and tipo_pequeno > tipo_moto:
            print("\nOs veículos mais registrados foram os pequenos")
        elif tipo_grande > tipo_pequeno and tipo_grande > tipo_moto:
            print("\nOs veículos mais registrados foram os grandes")
        elif tipo_moto > tipo_pequeno and tipo_moto > tipo_grande:
            print("\nOs veículos mais registrados foram as motos")
        else:
            print("\nA quantidade de veículos registrados foram iguais")

    #MEDIA DE VALOR GASTO POR CADA UM:

        #PEQUENO:
        if tipo_pequeno > 0:
            media_pequeno = valor_total_dia/tipo_pequeno
            print("\nMedia do valor gasto por cada cliente com veículos pequenos foi: R$ " + str(media_pequeno))

        #GRANDE
        if tipo_grande > 0:
            media_grande = valor_total_dia/tipo_grande
            print("\nMedia do valor gasto por cada cliente com veículos grandes foi: R$ " + str(media_pequeno))

        #MOTOS
        if tipo_moto > 0:
            media_moto = valor_total_dia/tipo_moto
            print("\nMedia do valor gasto por cada cliente com motos foi: R$ " + str(media_moto))