tarefas =[]

def adicionar():
    tarefa = {}
    titulo = input('Digite o titulo:\n')
    descricao = input('Descreva a tarefa:\n')
    prioridade = int(input('De 1 à 5, qual a prioridade:\n'))
    categoria = input('Digite a categoria:\n')
    concluida = False
    tarefa = {
        'titulo':titulo,
        'descricao':descricao,
        'prioridade':prioridade,
        'categoria':categoria,
        'concluida':concluida
    }
    tarefas.append(tarefa)

    print('Tarefa adicionada com sucesso!')

def listar():
    print('======|Tarefas|=====')
    for tarefa in tarefas:
        print(f"""
        Tarefa:{tarefa['titulo']} 
        Descrição:{tarefa['descricao']}
        Prioridade:{tarefa['prioridade']}
        Categoria:{tarefa['categoria']}
        Concuida:{tarefa['concluida']}
        """)
        print("-"*60)

def concluida():
    for tarefa in tarefas:
        print(f'Titulo: {tarefa["titulo"]}')
    print('-'*60)
    tarefa_conc = input('Digite o nome da tarefa que foi concluida:\n')
    for tarefa in tarefas:
        if tarefa['titulo'] == tarefa_conc:
            tarefa['concluida'] = True
            return f'Tarefa concluida' 


def listar_prioridade():
    opcao = input('Digite a prioridade:\n')
    match opcao:
        case "1":
            for tarefa in tarefas:
                if tarefa['prioridade'] == 1:
                    print('======|Prioridade 1|======')
                    print(f"""
            Tarefa:{tarefa['titulo']} 
            Descrição:{tarefa['descricao']}
            Prioridade:{tarefa['prioridade']}
            Categoria:{tarefa['categoria']}
            Concuida:{tarefa['concluida']}
            """)
                    print('-'*60)
        case '2':
            for tarefa in tarefas:
                if tarefa['prioridade'] == 2:
                    print('======|Prioridade 2|======')
                    print(f"""
            Tarefa:{tarefa['titulo']} 
            Descrição:{tarefa['descricao']}
            Prioridade:{tarefa['prioridade']}
            Categoria:{tarefa['categoria']}
            Concuida:{tarefa['concluida']}
            """)
                    print('-'*60)
        case '3':
            for tarefa in tarefas:
                if tarefa['prioridade'] == 3:
                    print('======|Prioridade 3|======')
                    print(f"""
            Tarefa:{tarefa['titulo']} 
            Descrição:{tarefa['descricao']}
            Prioridade:{tarefa['prioridade']}
            Categoria:{tarefa['categoria']}
            Concuida:{tarefa['concluida']}
            """)
                    print('-'*60)
        case '4':
            for tarefa in tarefas:
                if tarefa['prioridade'] == 4:
                    print('======|Prioridade 4|======')
                    print(f"""
            Tarefa:{tarefa['titulo']} 
            Descrição:{tarefa['descricao']}
            Prioridade:{tarefa['prioridade']}
            Categoria:{tarefa['categoria']}
            Concuida:{tarefa['concluida']}
            """)
                    print('-'*60)
        case '5':
            for tarefa in tarefas:
                if tarefa['prioridade'] == 5:
                    print('======|Prioridade 5|======')
                    print(f"""
            Tarefa:{tarefa['titulo']} 
            Descrição:{tarefa['descricao']}
            Prioridade:{tarefa['prioridade']}
            Categoria:{tarefa['categoria']}
            Concuida:{tarefa['concluida']}
            """)
                    print('-'*60)
        case _:
            print('Caracter não identificado.')            

def listar_concluidas():
    for tarefa in tarefas:
        if tarefa['concluida'] == True:
            print(f"""
            Tarefa:{tarefa['titulo']} 
            Descrição:{tarefa['descricao']}
            Prioridade:{tarefa['prioridade']}
            Categoria:{tarefa['categoria']}
            Concuida:{tarefa['concluida']}
            """)

def listar_nao_concluidas():
    for tarefa in tarefas:
        if tarefa['concluida'] == False:
            print(f"""
            Tarefa:{tarefa['titulo']} 
            Descrição:{tarefa['descricao']}
            Prioridade:{tarefa['prioridade']}
            Categoria:{tarefa['categoria']}
            Concuida:{tarefa['concluida']}
            """)

def listar_titulo():
    for tarefa in tarefas:
        print(f"Titulo: {tarefa['titulo']}")
    print('-'*60)

