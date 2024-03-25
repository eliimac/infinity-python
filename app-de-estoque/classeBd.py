import sqlite3


class Bd_estoque:
    def __init__(self)-> None:
        self.conexao = sqlite3.connect('bd_estoque.sqlite')
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()
    
    def criar_tab(self):
        cmdSQL = '''
        CREATE TABLE IF NOT EXISTS produtos(
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR (30) NOT NULL,
            descricao VARCHAR (50),
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
        '''
        self.cursor.execute(cmdSQL)

        cmdSQL = '''
        CREATE TABLE IF NOT EXISTS vendas(
            id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
            id_produto INTEGER,
            nome VARCHAR (30) NOT NULL,
            quantidade INTEGER NOT NULL,
            data_venda DATE,
            FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
        )
        '''
        self.cursor.execute(cmdSQL)
    
    def excluir_tabela_p(self):
        cmdSQL = '''
        DELETE FROM produtos
        '''
        self.cursor.execute(cmdSQL)
        self.conexao.commit()
    
    def excluir_tabela_v(self):
        cmdSQL = '''
        DELETE FROM vendas
        '''
        self.cursor.execute(cmdSQL)
        self.conexao.commit()

    def incluir_p(self,nome,desc,qnt,preco):
        cmdSQL = '''
        INSERT INTO produtos(
            nome,descricao,quantidade,preco
        )
        VALUES (?,?,?,?)
        '''
        self.cursor.execute(cmdSQL,(nome,desc,qnt,preco))
        self.conexao.commit()


    def incluir_v(self,id_prod,nome,qnt,data):
        cmdSQL = '''
        INSERT INTO vendas(
            id_produto,nome,quantidade,data_venda
        )
        VALUES (?,?,?,?)
        '''
        self.cursor.execute(cmdSQL,(id_prod,nome,qnt,data))
        self.conexao.commit()

    def atualizar_p(self,id_prod,qnt):
        cmdSQL = '''
        UPDATE produtos 
        SET quantidade = ?
        where id_produto = ?
        '''
        self.cursor.execute(cmdSQL,(qnt,id_prod))
        self.conexao.commit()
    
    def consultar_p(self):
        cmdSQL ='''
        SELECT * FROM produtos
        '''
        self.cursor.execute(cmdSQL)
        resposta = self.cursor.fetchall()
        return resposta


    def consultar_p_id(self,id_prod):
        cmdSQL ='''
        SELECT * FROM produtos
        WHERE id_produto = ?
        '''
        self.cursor.execute(cmdSQL,(id_prod,))
        resposta = self.cursor.fetchall()
        return resposta


    def consultar_v(self):
        cmdSQL ='''
        SELECT * FROM vendas
        '''
        self.cursor.execute(cmdSQL)
        resposta = self.cursor.fetchall()
        return resposta

    def excluir_p(self,nome):
        cmdSQL = '''
                DELETE FROM produtos
                WHERE nome = ?   
        '''
        self.cursor.execute(cmdSQL,(nome,))
        self.conexao.commit()

if __name__ == '__main__':
    print('Este arquivo não pode ser executado diretamente')