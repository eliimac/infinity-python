# Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. O programa deve permitir adicionar, remover, atualizar e listar os alunos.



# Para isso, você deve implementar um módulo que contém as seguintes funções:



# AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.



# RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.



# AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .



# VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.

alunos = {}

def adicionar_aluno():
    print('_'*60)
    cont = 1
    nome = input('Digite o nome do aluno:\n')
    matricula = int(input('Digite a matrícula do aluno:\n'))
    print('_'*60)
    if matricula in alunos:
        while True:
            print(f'Esse número de matrícula já existe em nosso sitema, tentativa n° {cont}')
            matricula = int(input('Digite a matrícula do aluno:\n'))
            cont +=1
            print('_'*60)
            if matricula not in alunos:
                alunos[matricula] = nome
                break
            elif cont == 4:
                print('Limite de tentativas ultrapassado.')
                break

            else:
                continue

        print('_'*60)
    else:
        alunos[matricula] = nome
 
def remover_aluno():
    cont =1
    matricula = int(input('Digite a matrícula do aluno:\n'))
    if matricula in alunos:
        del alunos[matricula]
        print('_'*60)

    else: 
        # print('Número de matricula não encontrado')
        while True:
            print(f'Esse número de matrícula não foi encontrado em nosso sistema, tentativa n° {cont}')
            matricula = int(input('Digite a matrícula do aluno:\n'))
            cont +=1
            print('_'*60)
            if matricula in alunos:
                del alunos[matricula]
                break
            elif cont == 4:
                print('Limite de tentativas ultrapassado.') 
                break   

            else:
                continue

        print('_'*60)

def atualizar():
    cont = 1
    matricula = int(input('Digite a matrícula do aluno:\n'))
    if matricula in alunos:
        nome_atualizado = input('Atualize o nome:\n')
        alunos[matricula] = nome_atualizado
        print('_'*60)
    else:
        # print('Número de matrícula não encontrado.')    
        while True:
            print(f'Esse número não foi encotrado em nosso sistema, tentativa n° {cont}')
            matricula = int(input('Digite a matrícula do aluno:\n'))
            cont +=1
            print('_'*60)
            if matricula in alunos:
                nome_atualizado = input('Atualize o nome:\n')
                alunos[matricula] = nome_atualizado
                break

            elif cont == 4:
                print('Limite de tentativas ultrapassado.')
            else:
                continue

        print('_'*60)

def ver_alunos():
    print('_'*60)
    for matricula, nome in alunos.items():
        print(f'N° de matrícula: {matricula}; nome: {nome}')