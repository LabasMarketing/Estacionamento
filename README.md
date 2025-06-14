# 🅿️ Sistema de Estacionamento em Python

Este projeto é uma aplicação de terminal desenvolvida em Python que simula o funcionamento de um sistema de estacionamento. A aplicação permite o controle de tarifas, registro de entrada e saída de veículos, cálculo de valores com ou sem desconto, e geração de relatórios diários e estatísticos.

---

## 📌 Funcionalidades

### 📊 Cadastro de Tarifas  
Permite configurar os valores cobrados para cada tipo de veículo (pequeno, grande ou moto). O sistema registra o valor fixo para até 3 horas e também o valor cobrado por cada hora adicional de permanência no estacionamento.
```python
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
```
### 🛬 Registro de Entrada  
Nesta etapa, o usuário informa a placa e o tipo do veículo. A hora de entrada é registrada automaticamente pelo sistema usando a hora atual, garantindo o controle de tempo desde a chegada do cliente.
```python
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
```
### 🛫 Registro de Saída  
Ao informar a placa novamente, o sistema calcula o tempo de permanência e o valor a ser pago. Caso o pagamento seja via PIX, o cliente recebe um desconto de 5%. O sistema exibe a placa, o valor final e a hora de saída.
```python
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
```
### 📅 Relatório Diário  
Gera um resumo das operações do dia, incluindo a quantidade de veículos que utilizaram o estacionamento, o tempo médio de permanência dos clientes e o lucro total obtido no período.
```python
# OPÇÃO CODIGO 4
    elif opcao == 4:
        if contagem_carros > 0:
            tempo_medio = tempo_medio / contagem_carros
        print("\nQuantidade de clientes hoje: ", contagem_carros,". Tempo médio de permanência: ",round(tempo_medio,2),"horas", ". Lucro total do dia: R$ ", round(valor_total_dia,2))
```
### 📈 Relatório por Tipo de Veículo  
Apresenta estatísticas sobre o tipo de veículos mais registrados no dia (pequeno, grande ou moto), além da média de valor gasto por cada categoria. Informa também qual tipo foi o mais frequente entre os clientes.
```python
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
```
---

## 🚦 Como Funciona

### 1. Menu
![image](https://github.com/user-attachments/assets/66b1d172-63a1-4c3b-9b5b-becec7b6a4bc)


### 2. Opção 1
![image](https://github.com/user-attachments/assets/476d94f5-03d5-4359-8701-a17910bf6672)


### 3. Opção 2
![image](https://github.com/user-attachments/assets/7d2d9eaa-82d6-4cdd-85bb-b899a2b3a734)


### 4. Opção 3
![image](https://github.com/user-attachments/assets/a008e0ce-498c-4ee6-a69a-b07068446b95)


### 5. Opção 4
![image](https://github.com/user-attachments/assets/90a06ce5-1422-416f-9cd2-409ff86ac2db)


### 6. Opção 5
![image](https://github.com/user-attachments/assets/3082853d-daf5-4a53-b5f5-280cec2fc311)


### 7. Opção 6
![image](https://github.com/user-attachments/assets/c5821799-87d2-48dd-a9d5-367f94aae1ca)

---
---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Biblioteca `datetime`** para controle de tempo (hora de entrada e saída)

---

