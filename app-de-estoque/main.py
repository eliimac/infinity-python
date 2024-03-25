import gerenciamento
# login: 111
# senha: 111


class Iniciar:
    def __init__(self) -> None:
        pass

    def iniciar(self):
        while True:
            print('''
    -----|Gerenciamento de estoque|-----
    1 = Banco de Dados
    2 = Produtos
    3 = Vendas
    0 = Parar
            ''')
            op = input('Digite:\n')
            if op not in ['1','2','3','0']:
                print('Caracter não identificado.')
            
            else:
                match op:
                    case '1':
                        print('''
-----|ADM|-----
1. Criar o BD e as tabelas
2. Deletar a tabela de produtos
3. Deletar a tabela de vendas''')
                        op1 = input('Digite:\n')
                        if op not in ['1','2','3']:
                            print('Caracter não identificado.')
                        else:
                            match op1:
                                case '1':
                                    self.login_db()
                                case '2':
                                    self.exc_tab_prod()
                                case '3':
                                    self.exc_tab_ven()

                    case '2':
                        print('''
    -----|Produtos|-----
    1. Incluir produto ao estoque
    2. Atualizar produto no estoque
    3. Excluir produto do estoque
    4. Consultar Produtos 
                        ''')
                        op2 = input('Digite:\n')
                        if op2 not in ['1','2','3','4']:
                            print('Caracter não identificado.')
                        else:
                            match op2:
                                case '1':
                                    self.adicionar_p()
                                case '2':
                                    self.consultar_nomes()
                                    self.atualizar_p()
                                case '3':
                                    self.consultar_nomes()
                                    self.excluir_p()
                                case '4':
                                    self.consultar_p()
                                    

                    case '3':
                        print('''
    -----|Vendas|-----
    1. Incluir venda
    2. Consultar Vendas 
                        ''')
                        op3 = input('Digite:\n')
                        if op3 not in ['1','2']:
                            print('Caracter não identificado')
                        
                        else:
                            match op3:
                                case '1':
                                    self.consultar_nomes()
                                    self.adicionar_venda()
                                case '2':
                                    self.consultar_v()


                    case '0':
                        print('Fechando...')
                        break

# ------------------- FUNÇÃO DE LOGIN AO BD

    def login_db(self):
        print('---|Login ADM|---')
        logTen = input('Digite o login:\n')
        senTen = input('Digite a senha:\n')
        if logTen == '111':
            if senTen == '111':
                    gerir = gerenciamento.Gerenciar_estoque()
                    gerir.criar_Bd()
                    print('Banco criado.')
        else:
            print('Login ou Senha inválido.')

    def exc_tab_prod(self):
        print('---|ADM|---')
        logTen = input('Digite o login:\n')
        senTen = input('Digite a senha:\n')
        if logTen == '111':
            if senTen == '111':
                op = input('Deseja excluir a tabela de produtos:\n').lower()
                if op == 'sim':
                        gerir = gerenciamento.Gerenciar_estoque()
                        gerir.excluir_tab_prod()
                        print('Tabela produtos deletada.')
                else:
                    pass
        else:
            print('Login ou Senha inválido.')
        
    def exc_tab_ven(self):
        print('---|ADM|---')
        logTen = input('Digite o login:\n')
        senTen = input('Digite a senha:\n')
        if logTen == '111':
            if senTen == '111':
                op = input('Deseja excluir a tabela de vendas:\n').lower()
                if op == 'sim':
                        gerir = gerenciamento.Gerenciar_estoque()
                        gerir.excluir_tab_ven()
                        print('Tabela vendas deletada.')
                else:
                    pass
        else:
            print('Login ou Senha inválido.')
        
# ------------------- FUNÇÕES DE ADICIONAR AO BD

    def adicionar_p(self):
        print('-----|Adição ao estoque|-----')
        nome_p = input('Digite o NOME do produto:\n').lower()
        desc_p = input('Digite a DESCRIÇÃO do p:\n').lower()
        qnt_p = int(input('Digite a QUANTIDADE do produto no estoque:\n'))
        preco_p = float(input('Digite o PREÇO do produto:\n'))
        
        gerir = gerenciamento.Gerenciar_estoque()
        retorno = gerir.incluir_produto(nome_p,desc_p,qnt_p,preco_p)
        print(retorno)

    def adicionar_venda(self):
        id_prod = int(input('Digite o ID do produto:\n'))
        nome = input('Digite o NOME do produto:\n').lower()
        qnt_comp = int(input('Digite a QUANTIDADE comprada:\n'))
        gerir = gerenciamento.Gerenciar_estoque()

        if qnt_comp > 0:
            retorno = gerir.incluir_venda(id_prod,nome,qnt_comp)
            print(retorno)
            if retorno == 'Adicionado as vendas':
                gerir.atualizar_prod_compra(id_prod,qnt_comp)
        else:
            print('A quantidade comprada não pode ser zero.')

#  ------------------------ FUNÇÃO DE ATUALIZAR O BD

    def atualizar_p(self):
        print('-----|Atualizar produto|-----')
        id_prod = int(input('Digite o ID do produto:\n'))
        qnt_nova = int(input('Digite a NOVA do produto:\n'))
        gerir = gerenciamento.Gerenciar_estoque()
        retorno = gerir.atualizar_produto(id_prod,qnt_nova)
        print(retorno)

# ------------------------ FUNÇÃO DE EXCLUIR PRODUTO

    def excluir_p(self):
        print('-----|Excluir produto|-----')
        id_prod = int(input('Digite o ID do produto que será REMOVIDO:\n'))
        nome = input('Digite o NOME do produto que será REMOVIDO:\n').lower()
        gerir = gerenciamento.Gerenciar_estoque()
        retorno = gerir.excluir_produto(id_prod,nome)
        print(retorno)


#---------------- FUNÇÕES DE CONSULTA 
    def consultar_p(self):
        print('-----|Consultar estoque|-----')
        gerir = gerenciamento.Gerenciar_estoque()
        retorno = gerir.consultar_produto()
        for prod in retorno:
            print(f''' 
ID: {prod[0]}
Nome: {prod[1]}
Descrição: {prod[2]}
Quantidade: {prod[3]}
Preço: {prod[4]}
-''')

    def consultar_v(self):
        print('-----|Consultar vendas|-----')
        gerir = gerenciamento.Gerenciar_estoque()
        retorno = gerir.consultar_venda()
        for venda in retorno:
            print(
                f"""
ID da Venda: {venda[0]}
ID do produto: {venda[1]}
Nome: {venda[2]}
Quantidade: {venda[3]}
Data: {venda[4]}    
        """
            )
        
    def consultar_nomes(self):
        print('-----|ID NOME QUANTIDADE|-----')
        gerir = gerenciamento.Gerenciar_estoque()
        retorno = gerir.consultar_produto()
        for prod in retorno:
            print(f''' 
ID: {prod[0]} - Nome: {prod[1]} - Quantidade: {prod[3]}
-''')

if __name__ == '__main__':
    estoque = Iniciar()
    estoque.iniciar()
else:
    print('este arquivo DEVE ser executado diretamente')