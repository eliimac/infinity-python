from biblioteca import *

class Rodar:
    def __init__(self,nome_bib):
        self.bib = Biblioteca(nome_bib)
        while True:
            print(f'''
-----|Biblioteca {self.bib.nome}|-----
1. Incluir um livro
2. Incluir um membro
3. Listar livro
4. Listar membros
5. Emprestar livro
6. Devolver Livro
0. Encerrar
            ''')
            op = input('Digite a opção:\n')
            if op not in ['0','1','2','3','4','5','6']:
                print('Caracter não identificado')
            else:
                match op:
                    case '0':
                        print('Até a próxima.')
                        break
                    case '1':

                        self.inc_livro()
                    case '2':
                        self.inc_membro()
                    case '3':
                        self.lista_livros()
                    
                    case '4':
                        self.lista_membros()
                    
                    case '5':
                        self.fun_emprestimo()
                    
                    case '6':
                        self.fun_devolucao()
                        

    def inc_livro(self):
        print('-----|inclusão de Livros|-----')
        id_livro = int(input('Digite o ID do Livro:\n'))
        titulo_liv = input('Digite o titulo do livro:\n')
        nome_autor = input('Digite o nome do autor:\n')
        retorno = self.bib.incluir_L(id_livro,titulo_liv,nome_autor)
        print(retorno)

    def inc_membro(self):
        print('-----|inclusão de membros|-----')
        id_mem = int(input('Digite o ID do membro:\n'))
        nome_mem = input('Digite o nome membro:\n')
        retorno = self.bib.incluir_M(nome_mem,id_mem)
        print(retorno)

    def lista_livros(self):
        print('-----|Lista de livros|-----')
        for livro in self.bib.catalogo:
            print(f'''
Titulo: {livro.titulo}
-
Autor: {livro.autor}
Id: {livro.id}
Status: {livro.status}
_____________________
            ''')

    def lista_membros(self):
        print('-----|Lista de membros|-----')
        for membro in self.bib.membros:
            print(f'''
Nome: {membro.nome}
Id: {membro.id}
___________________
            ''')

    def fun_emprestimo(self):
        self.lista_livros()
        self.lista_membros()
        print('-----|Emprestimo livro|-----')
        liv_id = int(input('Digite o ID do Livro:\n'))
        id_mem = int(input('Digite o ID do membro:\n'))
        retorno = self.bib.emprestimo(liv_id,id_mem)
        print(retorno)

    def fun_devolucao(self):
        self.lista_livros
        print('-----|Devolução livro|-----')
        liv_id = int(input('Informe o Id do livro:\n'))
        retorno = self.bib.devolver(liv_id)
        print(retorno)

if __name__ == '__main__':
    biblioteca = Rodar('Salcity')
else:
    print('este arquivo DEVE ser executado diretamente')
