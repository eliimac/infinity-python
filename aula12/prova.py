class Material:
    def __init__(self,titulo,autor_editora):
        self.titulo = titulo
        self.autor_ou_editora =autor_editora
    def exibir_info(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor ou editora: {self.autor_ou_editora}')

class Livro(Material):
    def __init__(self,titulo,autor_editora,genero):
        super().__init__(titulo,autor_editora)
        self.genero = genero

    def exibir_info(self):
        super().exibir_info()
        print(f'Gênero: {self.genero}')

class Revista(Material):
    def __init__(self,titulo,autor_editora,edicao):
        super().__init__(titulo,autor_editora)
        self.edicao = edicao

    def exibir_info(self):
        super().exibir_info()
        print(f'Edição: {self.edicao}')

# ===============================


while True:
    print('''
____________
Livros
____________
1. Livro
2. Revista
3. Fechar
''')

    op = input('Digite:\n')
    if op not in ['1','2','3']:
        print('Caracter não identificado...')
    else:
        if op == '1':
            print('=====|Info Livro|=====')
            nome_livro = input('Digite o nome do livro:\n')
            aut_edi = input('Digite o nome do(a) autor(a) ou da editora:\n')
            genero = input('Digite o gênero do livro:\n')

            livro = Livro(nome_livro,aut_edi,genero)
            print('___________________')
            livro.exibir_info()
            
        elif op == '2':
            print('=====|Info Revista|=====')
            nome_revis = input('Digite o nome da revista:\n')
            aut_edi = input('Digite o nome do(a) autor(a) ou da editora:\n')
            edicao = input('Digite a edição da revista:\n')
            
            revista = Revista(nome_revis,aut_edi,edicao)
            print('___________________')
            revista.exibir_info()
        else:
            print('Até mais...')
            break