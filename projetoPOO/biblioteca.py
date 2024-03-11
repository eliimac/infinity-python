from livro import *
from membro import *

class Biblioteca:
    def __init__(self,nome_b):
        self.nome = nome_b
        self.catalogo = []
        self.membros = []

    def incluir_L(self,id,titulo,autor):
        lv = Livros(titulo,autor,id)
        self.catalogo.append(lv)
        return f'Livro {lv.titulo} incluido no catálogo'
        
    def incluir_M(self,nome,id):
        membro = Membros(nome,id)
        self.membros.append(membro)
        return f'Membro {membro.nome} incluido no catálogo'

    def emprestimo(self,Id_liv,id_memb):
        resposta = ''
        for livro in self.catalogo:
            if livro.id == Id_liv:
                if livro.status == 'Disponível':
                    livro.status = 'emprestado'
                    for membro in self.membros:
                        if membro.id == id_memb:
                            membro.historico.append(livro.titulo)
                            resposta = f'Livro "{livro.titulo}" emprestado com sucesso.'
                        break
                else:
                    resposta = f'Livro "{livro.titulo}" está indisponível para emprestimo.'
            return resposta
    
    def devolver(self,id_liv):
        resposta = ''
        for livro in self.catalogo:
            if livro.id == id_liv:
                livro.status = 'Disponível'
                resposta = f'Livro "{livro.titulo}" devolvido com sucesso'
                break
            else:
                resposta = f'Livro "{livro.titulo}" não estava emprestado'
        return resposta
        



if __name__ == '__main__':
    print('Este arquivo não pode ser executado diretamente')