'''
Exercício1 Prova P1 A

Instruções:
	A prova é individual e sem consulta.
	Não utilize de meios eletrônicos como internet, pen drive ou rede para efetuar transferência de arquivos sem a anuência do professor.
	Ao Terminar, faça a compactação dos arquivos da sua prova em um único arquivo que deverá ter seu nome completo e o seu prontuário, conforme o seguinte modelo: P1A_Nome_do_Aluno_12345
	Atenção: O aluno é responsável pela compactação dos arquivos de sua prova. Não deixe nenhum arquivo da prova de fora do arquivo compactado.
1º) Escreva um programa que permita que um usuário crie um dicionário de compras.  O usuário deve ser capaz de adicionar itens, remover itens e visualizar o dicionário. O dicionário deve armazenar o nome do item e a quantidade desejada pelo usuário. Por exemplo, se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como chave e 2 como valor. A estrutura do dicionário ficaria assim: ‘{"banana": 2}’.
O programa deve permitir que o usuário adicione, remova e visualize o dicionário de compras.
Além disso, o programa deve mostrar uma mensagem de erro se o usuário tentar usar uma opção inválida do menu. Por exemplo, se o usuário digitar 5, o programa deve mostrar a mensagem "Opção inválida. Por favor, escolha uma opção válida." e mostrar o menu novamente. Além disso, o programa deve ser *case insensitive*, ou seja, "Maçã" e "maçã" devem ser considerados o mesmo item.
Estruture seu programa da seguinte forma:
1. Crie um dicionário vazio para armazenar os itens da lista de compras.
2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e sua quantidade e adicione-o ao dicionário.
5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o do dicionário.
6. Se o usuário escolher ver o dicionário, mostre cada item dele em sua própria linha.
7. Se o usuário escolher sair, encerre o loop usando break.

Exemplos de saída:
1 Adicionar item
2 Remover item
3 Ver lista
4 Sair
Escolha uma opção: 1
Digite um item: banana
Digite a quantidade: 2
-------------------------------
1 Adicionar item
2 Remover item
3 Ver lista
4 Sair
Escolha uma opção: 1
Digite um item: maçã
Digite a quantidade: 3
-------------------------------
1 Adicionar item
2 Remover item
3 Ver lista
4 Sair
Escolha uma opção: 2
Digite um item: banana
Digite a quantidade: 1
-------------------------------
1 Adicionar item
2 Remover item
3 Ver lista
4 Sair
Escolha uma opção: 3
{'banana': 1, 'maçã': 3}
-------------------------------
1 Adicionar item
2 Remover item
3 Ver lista
4 Sair
Escolha uma opção: 4
'''

itens = []
quantidades = []

while True:
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Sair")

    tamanho_lista = len(itens)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        item = input("Digite um item: ")

        if item in itens:
            for i, valor in enumerate(itens):
                if valor == item:
                    quantidade = int(input("Digite a quantidade: "))
                    quantidades[i] = quantidades[i] + quantidade
        else:
            itens.append(item)
            quantidade = int(input("Digite a quantidade: "))
            quantidades.append(quantidade)

    if opcao == 2:
        item_remover = input("Digite o item: ")
        quantidade_remover = int(input("Digite a quantidade: "))

        if item_remover in itens:
            for i, valor in enumerate(itens):
                if valor == item_remover:
                    if quantidades[i] - quantidade_remover > 0:
                        quantidades[i] = quantidades[i] - quantidade_remover
                    elif quantidades[i] - quantidade_remover < 0:
                        print(f"Você não pode remover mais que {quantidades[i]} do produto: {item_remover}")
                    else:
                        del(quantidades[i])
                        del(itens[i])
        else:
            print("O item digitado não está na lista")

    if opcao == 3:
        if tamanho_lista > 0:
            for i in range(tamanho_lista):
                print(f"{itens[i]}:{quantidades[i]}")
        else:
            print("Sua lista está vazia.")

    if opcao == 4:
        break






