from arquivo import *

while True:
    print('''======|Agenda de tarefas|======
            Opções:
            1- Adicionar tarefa
            2- Visualizar tarefas
            3- Concluir tarefa
            4- Fechar
    ''')
    opcao = input('Digite a opção:\n')
    match opcao:
        case '1':
            adicionar()
        case '2':
            print("""
            ======|Visualizar tarefas|======
            1- Visualizar todas as tarefas
            2- Visualizar feitas
            3- Visualizar por prioridade
            4- Visualizar titulos
            6- Visualizar incabadas
            """)
            opcao_tarefas = input('Digite a opção:\n')
            match opcao_tarefas:
                case '1':
                    listar()
                case '2':
                    listar_concluidas()
                case '3':
                    listar_prioridade()
                case '4':
                    listar_titulo()
                case '5':
                    listar_nao_concluidas()
                case _:
                    print('Caracter não identificado.')
        case '3':
            concluida()
        case '4':
            print('Até mais!')
            break
        case _:
            print('caracter não identificado.')
