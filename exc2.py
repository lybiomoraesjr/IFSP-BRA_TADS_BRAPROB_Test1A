'''
Exercício 2 Prova P1 A

2º) Escreva um programa que preveja as vendas totais para cada produto em uma empresa.  O usuário deve digitar o nome do produto, as vendas do mês atual e a taxa de crescimento, e o programa deve calcular o valor das vendas previstas para o próximo mês.
Estruture seu programa da seguinte forma:
1. Crie um dicionário vazio para armazenar as previsões de vendas.
2. Crie um loop infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento.
3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
4. Se o usuário digitar 'sair', encerre o loop usando break.
5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular as vendas previstas e adicione-as ao dicionário.
6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar as previsões de vendas para cada produto.

Exemplo de saída:

Digite o nome do produto (ou 'sair' para sair): iphone
Digite as vendas do mês atual: 10000
Digite a taxa de crescimento (%): 10
Digite o nome do produto (ou 'sair' para sair): capinha para iphone
Digite as vendas do mês atual: 200
Digite a taxa de crescimento (%): 20
Digite o nome do produto (ou 'sair' para sair): sair
iphone: Previsão de vendas do próximo mês = R$ 11000.00
capinha para iphone: Previsão de vendas do próximo mês = R$ 240.00
'''

produtos = []

vendas = []

taxas_crescimento = []

while True:
    produto = input("Digite o nome do produto (ou 'sair' para sair): ")
    if produto == 'sair':
        break
    produtos.append(produto)

    venda = float(input("Digite as vendas do mês atual: "))
    vendas.append(venda)

    taxa_crescimento = float(input("Digite a taxa de crescimento(%): "))
    taxas_crescimento.append(taxa_crescimento)

tamanho_lista = len(produtos)

if tamanho_lista > 0:
    for i in range(tamanho_lista):
        print(f"{produtos[i]}: Previsão de vendas do próximo mês = R${vendas[i] * (taxas_crescimento[i] + 100) / 100} ")
