import classeBd
import classProduto
import classVenda
from datetime import datetime



class Gerenciar_estoque:
    def __init__(self) -> None:
        pass

    def criar_Bd(self):
        banco = classeBd.Bd_estoque()
        banco.criar_tab()
        banco.fechar()
        return f"Banco criado"
    
    def excluir_tab_prod(self):
        banco = classeBd.Bd_estoque()
        banco.excluir_tabela_p()
        banco.fechar()
        return f'A tabela produtos foi excluida.'

    def excluir_tab_ven(self):
        banco = classeBd.Bd_estoque()
        banco.excluir_tabela_v()
        banco.fechar()
        return f'A tabela vendas foi excluida.'

    def incluir_produto(self, nome, desc, qnt, preco):
        banco = classeBd.Bd_estoque()
        produtos = banco.consultar_p()
        resposta = ""

        if qnt > 0:
            if preco > 0:
                banco.incluir_p(nome, desc, qnt, preco)
                resposta = f"{nome} adicionado ao estoque"

            else:
                resposta = "O valor não pode ser menor que zero"
        else:
            resposta = "A quantidade não pode ser menor que zero"

        return resposta

        banco.fechar()

    def incluir_venda(self, id_prod, nome, qnt):
        banco = classeBd.Bd_estoque()
        data_venda = datetime.now().strftime("%d-%m-%Y %H:%M")
        produto = banco.consultar_p_id(id_prod)
        resposta = ""

        for linha in produto:
            nome_p = linha[1]
            qnt_prod = linha[3]

        if produto:
            if nome == nome_p:
                if qnt <= qnt_prod:
                    banco.incluir_v(id_prod, nome, qnt, data_venda)
                    resposta = f"Adicionado as vendas"
                else:
                    resposta = "A quantidade não pode ser maior do que a quantia do estoque."
            else:
                resposta = 'O nome do produto não está cadastrado no estoque.'
        else:
            resposta = 'O ID do produto não está cadastrado no estoque.'


        banco.fechar()
        return resposta

    def atualizar_produto(self, id_prod, qnt_nova):
        banco = classeBd.Bd_estoque()
        resposta = ""
        produto = banco.consultar_p_id(id_prod)

        if produto:
            if qnt_nova > 0:
                banco.atualizar_p(id_prod, qnt_nova)
                resposta = "Produto Atualizado no estoque"
            else:
                resposta = "A Quantidade não pode ser menor que zero"
        else:
            resposta = 'O ID não está cadastrado'

        banco.fechar()
        return resposta

    def atualizar_prod_compra(self, id_prod, qnt_comp):
        banco = classeBd.Bd_estoque()
        produto = banco.consultar_p_id(id_prod)
        resposta = ""

        if produto:
            for linha in produto:
                qnt_prod = linha[3]
                break
            atual_qnt = qnt_prod - qnt_comp

            if atual_qnt >= 0:
                banco.atualizar_p(id_prod, atual_qnt)
            else:
                pass
        
        banco.fechar()

    def consultar_produto(self):
        banco = classeBd.Bd_estoque()
        produtos = banco.consultar_p()
        banco.fechar()
        return produtos


    def consultar_venda(self):
        banco = classeBd.Bd_estoque()
        vendas = banco.consultar_v()
        banco.fechar()
        return vendas


    def excluir_produto(self, id_prod, nome):
        banco = classeBd.Bd_estoque()
        produtos = banco.consultar_p_id(id_prod)
        resposta = ""

        for prod in produtos:
            nome_exc = prod[1]
            break

        if nome == nome_exc:
            banco.excluir_p(nome)
            resposta = f"{nome} foi removido do estoque de produtos."

        else:
            resposta = "Produto não cadastrado."
        return resposta


if __name__ == "__main__":
    print("Este arquivo não pode ser executado diretamente")