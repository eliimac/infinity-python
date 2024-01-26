
def calcular_total(produto):
    return produto['quantidade'] * produto['valor_unitario']


lista_de_produtos = []


total_produtos = 0


def adicionar_produto():
    global total_produtos
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor_unitario = float(input("Digite o valor unitário do produto: "))
    
    total = calcular_total({'quantidade': quantidade, 'valor_unitario': valor_unitario})
    
    produto = {
        'nome': nome,
        'quantidade': quantidade,
        'valor_unitario': valor_unitario,
        'total': total
    }

    lista_de_produtos.append(produto)
    total_produtos += total
    print("Produto adicionado com sucesso!")


def visualizar_lista():
    print("\nLista de Produtos:")
    for produto in lista_de_produtos:
        print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Valor Unitário: {produto['valor_unitario']}, Total: {produto['total']}")
    
    print(f"\nValor Total de Todos os Produtos: {total_produtos}")


def atualizar_produto():
    global total_produtos
    nome_atualizar = input("Digite o nome do produto que deseja atualizar: ")
    
    for produto in lista_de_produtos:
        if produto['nome'] == nome_atualizar:
            quantidade = int(input("Digite a nova quantidade do produto: "))
            valor_unitario = float(input("Digite o novo valor unitário do produto: "))
            
            total_produtos -= produto['total']
            
            produto['quantidade'] = quantidade
            produto['valor_unitario'] = valor_unitario
            produto['total'] = calcular_total({'quantidade': quantidade, 'valor_unitario': valor_unitario})
            
            total_produtos += produto['total']
            
            print("Produto atualizado com sucesso!")
            return
    
    print("Produto não encontrado.")


def remover_produto():
    global total_produtos
    nome_remover = input("Digite o nome do produto que deseja remover: ")
    
    for produto in lista_de_produtos:
        if produto['nome'] == nome_remover:
            total_produtos -= produto['total']
            lista_de_produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
    
    print("Produto não encontrado.")


while True:
    print("\nOpções:")
    print("1. Adicionar Produto")
    print("2. Visualizar Lista de Produtos")
    print("3. Atualizar Produto Existente")
    print("4. Remover Produto")
    print("5. Encerrar Programa")

    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        visualizar_lista()
    elif opcao == '3':
        atualizar_produto()
    elif opcao == '4':
        remover_produto()
    elif opcao == '5':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
