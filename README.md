# 🅿️ Sistema de Estacionamento em Python

Este projeto é uma aplicação de terminal desenvolvida em Python que simula o funcionamento de um sistema de estacionamento. A aplicação permite o controle de tarifas, registro de entrada e saída de veículos, cálculo de valores com ou sem desconto, e geração de relatórios diários e estatísticos.

---

## 📌 Funcionalidades

1. **📊 Cadastro de Tarifas**
   - Permite ao usuário configurar os valores fixos para 3 horas de estadia e o valor por hora adicional.
   - Os valores são definidos com base no tipo do veículo:
     - Veículo Pequeno
     - Veículo Grande
     - Motos

2. **🛬 Registro de Entrada**
   - O usuário informa a **placa** e o **tipo de veículo**.
   - A hora de entrada é registrada automaticamente.

3. **🛫 Registro de Saída**
   - O usuário informa a **placa** e escolhe o método de pagamento (PIX ou outro).
   - O sistema calcula o valor total:
     - 5% de desconto se o pagamento for via **PIX**.
     - Se o tempo de permanência for maior que 3 horas, cobra-se o valor adicional por hora.
   - Ao final, são exibidos:
     - Placa
     - Tipo de veículo
     - Hora de saída
     - Tempo total de permanência
     - Valor final a pagar

4. **📅 Relatório Diário**
   - Mostra:
     - Quantidade de veículos atendidos no dia
     - Tempo médio de permanência
     - Lucro total do dia

5. **📈 Relatório por Tipo de Veículo**
   - Quantidade de veículos por categoria
   - Tipo de veículo mais frequente
   - Média de valor gasto por tipo de veículo

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Biblioteca `datetime`** para controle de tempo (hora de entrada e saída)

---

## 🚦 Como Funciona

O programa apresenta um **menu interativo** com 6 opções:
