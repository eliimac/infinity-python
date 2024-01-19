dic = {}

nomeAluno = input('Digite o nome do aluno: \n').lower()
matriculaAluno = int(input('Digite a matrícula aluno: \n'))
dic[matriculaAluno] = nomeAluno
print('-'*60)
while True:
    print(f"""
        A = adicionar;
        R = remover;
        V = visualizar;
        P = parar.
    """)
    conf = input('Deseja adicionar, remover, visualizar ou parar? \n').lower()
    match conf:
        case 'a':
                nomeAluno = input('Digite o nome do aluno: \n').lower()
                matriculaAluno = int(input('Digite a matrícula aluno: \n'))
                if matriculaAluno in dic:
                    for i in range(3):
                        print('Matrícula já cadastrada, digite novamente.')
                        nomeAluno = input('Digite o nome do aluno: \n').lower()
                        matriculaAluno = int(input('Digite a matrícula aluno: \n'))
                        print('-'*60)
                        if matriculaAluno not in dic:
                            dic[matriculaAluno] = nomeAluno
                            break


                else:
                    dic[matriculaAluno] = nomeAluno
                print('-'*60)
                # continue
        case 'r':
                print(list(dic))
                matriculaAluno = int(input('Digite a matricula: \n'))
                if matriculaAluno in dic:
                    rem = dic.pop(matriculaAluno)
                    print(f'{rem} foi removid(a) ')
                else:
                    for i in range(3):
                        print('Caracter não encontrado.')
                        print(list(dic))
                        matriculaAluno = int(input('Digite a matricula: \n'))
                        if matriculaAluno in dic:
                            rem = dic.pop(matriculaAluno)
                            print(f'{rem} foi removid(a)')
                            print('-'*60)

                print('_'*60)


        case 'p':
            print('-'*60)
            break     
        
        case 'v':
            print(dic)  
            print('-'*60)

        case _: 
            print('-'*60)
            print('Caracter não identificado, digite novamente.')
